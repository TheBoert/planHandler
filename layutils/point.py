import math

class phPoint:
    """
    A Point coordinate.
    
    Args:
    x -- The world x-Coordinate in m
    y -- The world y-Coordinate in m
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.digits = 5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"phPoint - x:{self.x}, y:{self.y}"

    def newPointAtDistanceAndAngle(self, distance: float, angle: float):
        """
        Returns a new point at given distance and angle.
        """
        newX = self.x + round(math.cos(math.radians(angle)), self.digits) * distance
        newY = self.y + round(math.sin(math.radians(angle)), self.digits) * distance
        return self.__class__(newX, newY)