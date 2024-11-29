from qgis.core import *

from .layerValidation import validateLayer
from .featureHandling import featureHandling, mandatoryGeometryFieldnames, optionalGeometryFieldnames

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
        geometryFieldnames = mandatoryGeometryFieldnames + \
                             optionalGeometryFieldnames

        changedAttributeName = self.layer.fields().field(idx).name();

        if changedAttributeName in geometryFieldnames:
            self.printGeometryChangedMessage(fid, changedAttributeName, newValue)
            feature = self.layer.getFeature(fid)
            newGeometry = featureHandling.createNewWorldViewGeometry(feature)
            self.layer.changeGeometry(fid, newGeometry)