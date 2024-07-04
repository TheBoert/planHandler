from qgis.core import *

from .layerValidation import validateLayer
from .featureHandling import featureHandling, geometryFieldnames

class LayerHandler:

    def printGeometryChangedMessage(self, fid, attributeName, newValue):
        print(f"Geometrieänderung bei Feature {fid=}:\n\
            {attributeName=} {newValue=}")

    def __init__(self, layer):
        self.layer = layer
        validateLayer(layer)
        self.layer.attributeValueChanged.connect(self.handleAttributeChange)

    # Durch das attributeValueChanged Signal werden standardmäßig die fid des 
    # geänderten Features, die idx des geänderten Attributes und der neue Wert 
    # (value) des Attributes für das geänderte Feature übergeben.
    def handleAttributeChange(self, fid, idx, newValue):
        attributeName = self.layer.fields().field(idx).name();
        if attributeName in geometryFieldnames:
            self.printGeometryChangedMessage(fid, attributeName, newValue)
            feature = self.layer.getFeature(fid)
            newGeometry = featureHandling.createNewWorldViewGeometry(feature)
            self.layer.changeGeometry(fid, newGeometry)