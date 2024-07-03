import math
from qgis.core import *

from .layerValidator import validateLayer

class LayerHandler:
    
    def __init__(self, layer, ):
        self.layer = layer
        validateLayer(layer)
        self.layer.attributeValueChanged.connect(self.update)

    # Durch das attributeValueChanged Signal werden standardmäßig die fid des 
    # geänderten Features, die idx des geänderten Attributes und der neue Wert 
    # (value) des Attributes für das geänderte Feature übergeben.
    def update(self, fid, idx, value):
        attributeName = self.layer.attributeDisplayName(idx)
        if not attributeName in["ansicht_breite_welt", 
                                "ansicht_hoehe_welt"]:
            print(f"Änderung: {fid=},{attributeName=},{value=}")
            self.updateGeometry(fid)

    def addHeight(self, fromPoint, newHeight, angle):
        newX = fromPoint.x() - math.sin(math.radians(angle)) * newHeight 
        newY = fromPoint.y() + math.cos(math.radians(angle)) * newHeight 
        return QgsPointXY(newX,newY)

    def addWidth(self, fromPoint, newWidth, angle):
        newX = fromPoint.x() + math.cos(math.radians(angle)) * newWidth 
        newY = fromPoint.y() + math.sin(math.radians(angle)) * newWidth 
        return QgsPointXY(newX,newY)

    def newViewWidth(self, feature):
        newViewWidth = \
            (float(feature["seite_breite"]) \
            - feature["seitenrand_links"] \
            - feature["seitenrand_rechts"] \
            - feature["breite_schriftfeld"]) \
            * feature["massstab"] / 1000.0
        return newViewWidth
    
    def newViewHeight(self, feature):
        newViewHeight = \
            (float(feature["seite_hoehe"]) \
            - feature["seitenrand_oben"] \
            - feature["seitenrand_unten"]) \
            * feature["massstab"] / 1000.0
        return newViewHeight

    def createNewRectangle(self, feature, lowerLeft):
        newWidth = self.newViewWidth(feature)
        newHeight = self.newViewHeight(feature)
        angle = feature["winkel"]
 
        lowerRight = self.addWidth(lowerLeft, newWidth, angle)
        uperRight = self.addHeight(lowerRight, newHeight, angle)
        upperLeft = self.addHeight(lowerLeft, newHeight, angle)
        newPolygon =  [lowerLeft, lowerRight, uperRight, upperLeft]

        for i in range(len(newPolygon)):
            print(f"newPolygon[{i}]= {newPolygon[i]}")
        return newPolygon
    
    def updateGeometry(self, fid):
        feature = self.layer.getFeature(fid)
        oldGeometry = feature.geometry()
        oldPolygon = oldGeometry.asPolygon()
        newPolygon = self.createNewRectangle(feature, oldPolygon[0][0])
        newGeometry = QgsGeometry.fromPolygonXY([newPolygon])
        self.layer.changeGeometry(fid, newGeometry)
