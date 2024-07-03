#-----------------------------------------------------------
# PlanHandler QGIS Python Plugin
# Copyright (C) 2024 Robert Schlich
#-----------------------------------------------------------
#
# 
#-----------------------------------------------------------

def classFactory(iface):
    from .planHandler import PlanHandler
    return PlanHandler(iface)
