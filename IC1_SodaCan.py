# Davis Arita
# 11/14/22
# CS 131 Lecture 12A lab 1
# implmenting classes
import math


class SodaCan:
    def __init__(self, height=0.0, radius=0.0):
        self._radius = radius
        self._height = height

    def getSurfaceArea(self):
        return (2*math.pi*self._height*self._radius) +\
               (2*math.pi*(math.pow(self._radius,2)))

    def getVolume(self):
        return self._radius * math.pi * self._height

    def getRadius(self):
        return self._radius

    def getHeight(self):
        return self._height

    def setRadius(self, newRadius):
        self._radius = newRadius

    def setHeight(self, newHeight):
        self._height = newHeight


