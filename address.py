# Davis Arita
# 11/21/22
# CS 131 Exercise 11 Part B

class Address:
    def __init__(self, houseNum, streetName, cityName,
                 StateName, pCode, aptNum=None):
        self._houseNumber = houseNum
        self._streetName = streetName
        self._aptNum = aptNum
        self._cityName = cityName
        self._stateName = StateName
        self._pCode = int(pCode)

    def print(self):
        print(self._houseNumber, self._streetName, end="\n")
        print(self._cityName, end=", ")
        print(self._stateName, self._pCode)

    def getPostal(self):
        return self._pCode

    def comesBefore(self, other):
        print("a comes before b is", end=" ")
        if self._pCode < other._pCode:
            print(True)
        else:
            print(False)
