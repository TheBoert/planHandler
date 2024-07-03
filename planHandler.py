from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
import pathlib, os
from qgis.core import Qgis

from .layutils.layerHandler import LayerHandler
from .error.planHandlerErrors import *

class PlanHandler:
  
    def __init__(self, iface):
        self.iface = iface
        self.layerHandler : LayerHandler

    def initGui(self):
        icon = 'planhandler.svg'
        iconPath = os.path.join(pathlib.Path(__file__).parent.resolve(), icon)  
        self.action = QAction('Planhandler', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.action.setIcon(QIcon(iconPath))
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        try:
            layer = self.iface.activeLayer()
            self.layerHandler = LayerHandler(layer)
        except InvalidLayerError as error:
            self.pushMessageCritical(str(error))
        else:
            self.pushMessageSucess(
                f"planHandler überwacht den Layer \"{layer.name()}\" " +
                "auf Attributänderungen und passt bei Bedarf die Geometrie an.")
        
    def pushMessageCritical(self, message):
        self.iface.messageBar().pushMessage("planHandler", 
                                            message, 
                                            Qgis.Critical)

    def pushMessageSucess(self, message):
        self.iface.messageBar().pushMessage("planHandler", 
                                            message, 
                                            Qgis.Success)