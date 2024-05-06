# Davis Arita
# 11/14/22
# CS 131 Exercise 11 part A
# implmenting the car class

class Car:
    def __init__(self, fuel):
        self._fuelE = fuel
        self._gasLevel = 0

    def addGasLevel(self, newGas):
        self._gasLevel = newGas

    def drive(self, milesToDrive):
        self._gasLevel=  (self._gasLevel * self._fuelE - milesToDrive) / self._fuelE

    def getGasLevel(self):
        return self._gasLevel
