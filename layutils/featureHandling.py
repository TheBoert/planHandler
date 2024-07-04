from qgis.core import QgsFeature, QgsPointXY, QgsGeometry

from .point import phPoint
from .plan import *

geometryFieldnames = [\
    "seite_hoehe", 
    "seite_breite", 
    "seitenrand_oben",
    "seitenrand_unten",
    "seitenrand_links",
    "seitenrand_rechts",
    "breite_schriftfeld",
    "massstab",
    "winkel"]   

def phPointToQgsPointXY(point: phPoint) -> QgsPointXY:
    returnpoint = QgsPointXY(point.x, point.y)
    return returnpoint

class featureHandling:

    @classmethod
    def createNewWorldViewGeometry(self, feature) -> QgsGeometry:
        plan = featureHandling.createNewPlan(feature)

        lowerLeft = phPointToQgsPointXY(plan.worldViewLowerLeft)
        lowerRight = phPointToQgsPointXY(plan.worldViewLowerRight)
        upperRight = phPointToQgsPointXY(plan.worldViewUpperRight)
        upperLeft = phPointToQgsPointXY(plan.worldViewUpperLeft)

        newPolygon =  [lowerLeft, lowerRight, upperRight, upperLeft]
        for i in range(len(newPolygon)):
            print(f"newPolygon[{i}]= {newPolygon[i]}")
        return QgsGeometry.fromPolygonXY([newPolygon])

    @classmethod
    def createNewPlan(self, feature: QgsFeature) ->phPlanLayout:
        return phPlanLayout(featureHandling.extractPageLayout(feature), 
                            float(feature["massstab"]),
                            float(feature["winkel"]),
                            featureHandling.extractFirstVertexAsPhPoint(feature))

    @classmethod
    def extractPageLayout(self, feature: QgsFeature) -> phPageLayout:
        return phPageLayout(float(feature["seite_breite"]), 
                            float(feature["seite_hoehe"]), 
                            featureHandling.extractMargins(feature), 
                            float(feature["breite_schriftfeld"]))

    @classmethod
    def extractMargins(self, feature: QgsFeature) -> phPageMargins:
        return phPageMargins(float(feature["seitenrand_oben"]), 
                             float(feature["seitenrand_links"]),
                             float(feature["seitenrand_rechts"]),
                             float(feature["seitenrand_unten"]))

    @classmethod
    def extractFirstVertexAsPhPoint(self, feature: QgsFeature) -> phPoint:
        oldGeometry = feature.geometry()
        oldPolygon = oldGeometry.asPolygon()
        firstVertex = oldPolygon[0][0]
        return phPoint(firstVertex.x(), firstVertex.y())