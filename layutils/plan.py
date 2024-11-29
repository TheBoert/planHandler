from .point import phPoint

class phPageMargins:
    """
    Defines page margins

    Args:
    top -- Page margin at the top in mm
    left -- Page margin at the left in mm
    right -- Page margin at the right in mm
    bottom -- Page margin at the bottom in mm
    """

    top: float
    left: float
    right: float
    bottom: float 

    def __init__(self, top: float, left:float, right: float, bottom: float):
        if top < 0 or left < 0 or right < 0 or bottom < 0:
            raise ValueError("Seitenränder können nicht negativ sein!")
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom

class phPageLayout:
    """
    Defines a page-layout.
    
    Args:
    width -- the page width in mm
    height -- the page height in mm
    xxxMargin -- the page margins (top, left, right, bottom) in mm
    mapborder -- the width of the mapborder in mm (optional, default = 0)
    titleblockwidth -- the width of the titleblock in mm (optional, default = 0)
    """
    width: float
    height: float
    margins: phPageMargins
    mapborder: float
    titleblockwidth: float

    def __init__(self, width: float , height:float, pageMargins: phPageMargins, \
                 mapborder: float = 0, titleblockwidth: float = 0):
        self.margins = pageMargins
        if width < 0 or height < 0:
            raise ValueError("Seite kann keine negativen Abmessungen haben!")
        if mapborder < 0:
            raise ValueError("Kartenrahmen kann keine negative Breite haben!")
        if titleblockwidth < 0:
            raise ValueError("Schriftfeld kann keine negative Breite haben!")
        if self.margins.left + titleblockwidth + self.margins.right > width:
            raise ValueError("Die Seitenränder links und rechts + Breite des \
                             Schriftfelds können zusammen nicht größer als die \
                             Breite der Seite sein.")
        if self.margins.top + self.margins.bottom > height:
            raise ValueError("Die Seitenränder oben und unten können zusammen \
                             nicht größer als die Höhe der Seite sein.")
        self.width = width
        self.height = height
        self.mapborder = mapborder
        self.titleblockwidth = titleblockwidth
        print(self.mapborder)

    @property
    def pageViewWidth(self):
        """
        The width of the resulting view of the page layout in mm.
        """
        return self.width - self.margins.left - self.margins.right - \
            self.mapborder * 2 - self.titleblockwidth
    
    @property
    def pageViewHeight(self):
        """
        The height of the resulting view of the page layout in mm.
        """
        return self.height - self.margins.top - self.margins.bottom - \
            self.mapborder * 2 
    
class phPlanLayout:
    """
    Defines a plan Layout
    """

    def __init__(self, pageLayout: phPageLayout, scale: float, angle: float, 
                 worldViewLowerLeft: phPoint):
        if scale < 0:
            raise ValueError("Maßstab kann nicht negativ sein.")
        self.pageLayout = pageLayout
        self.scale = scale
        self.angle = angle
        self.worldViewLowerLeft = worldViewLowerLeft
    
    @property
    def pageViewWidth(self) -> float:
        return self.pageLayout.pageViewWidth
    
    @property
    def pageViewHeight(self) -> float:
        return self.pageLayout.pageViewHeight

    @property
    def worldViewWidth(self) -> float:
        """The width of the View on the world in m"""
        return self.pageViewWidth * self.scale / 1000

    @property
    def worldViewHeight(self) -> float:
        """The height of the View on the world in m"""
        return self.pageViewHeight * self.scale / 1000
    
    @property
    def worldViewLowerRight(self) -> phPoint:
        return \
            self.worldViewLowerLeft \
                .newPointAtDistanceAndAngle(self.worldViewWidth, self.angle)
    
    @property
    def worldViewUpperLeft(self) -> phPoint:
        return \
            self.worldViewLowerLeft \
                .newPointAtDistanceAndAngle(self.worldViewHeight, \
                                            self.angle + 90)

    @property
    def worldViewUpperRight(self) -> phPoint:
        return \
            self.worldViewLowerRight \
                .newPointAtDistanceAndAngle(self.worldViewHeight, \
                                            self.angle + 90)

    



    


