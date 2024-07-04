from qgis.core import QgsMapLayer, QgsWkbTypes

from ..error.planHandlerErrors import *
from .featureHandling import *

def validateLayer(layer: QgsMapLayer):
    if not layer:
        raise NoLayerSelectedError()
    if not layer.type() == QgsMapLayer.VectorLayer:
        raise NonVectorLayerSelectedError(layer.name())
    if not layer.wkbType() == QgsWkbTypes.Polygon:
        raise NonPolygonLayerSelectedError(layer.name())
    if missingOrInvalidFields := __missingOrInvalidFieldsInLayer(layer):
        raise MissingLayerFieldsError(layer.name(), 
                                        missingOrInvalidFields)
    
def __missingOrInvalidFieldsInLayer(layer):
    missingFields = []
    for expectedFieldName in geometryFieldnames:
        field = __getLayerFieldByName(layer, expectedFieldName)
        # All fields should be of Type double (field.type() == 6)
        if field is None or field.type() != 6:
            missingFields.append(expectedFieldName)
    return missingFields

def __getLayerFieldByName(layer, expectedFieldName):
    for field in layer.fields():
        if field.name() == expectedFieldName:
            return field
    return None