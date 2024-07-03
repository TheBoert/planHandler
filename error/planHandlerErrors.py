class InvalidLayerError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NoLayerSelectedError(InvalidLayerError):
    def __init__(self):
        message = "Es wurde kein Layer ausgewählt, den PlanHandler " + \
            "überwachen könnte."
        super().__init__(message)

class NonVectorLayerSelectedError(InvalidLayerError):
    def __init__(self, layername):
        message = f"Layer \"{layername}\" ist kein Vektorlayer und daher " + \
                "nicht für die Bearbeitung durch Planhandler geeignet."
        super().__init__(message)

class NonPolygonLayerSelectedError(InvalidLayerError):
    def __init__(self, layername):
        message = f"Layer \"{layername}\" ist kein Polygonlayer und daher " + \
                "nicht für die Bearbeitung durch Planhandler geeignet."
        super().__init__(message)

class MissingLayerFieldsError(InvalidLayerError):
    def __init__(self, layername, missingFields):
        message = f"Layer \"{layername}\" ist ungültig. Folgende Felder " + \
         " fehlen, oder sind vom falschen Datentyp: "
        for missingField in missingFields:
            message += "\"" + missingField + "\", "
        # remove last comma
        message = message[:-2]
        message += "."
        super().__init__(message)
