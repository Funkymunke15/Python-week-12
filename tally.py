# Davis Arita

class Counter:
    def __init__(self):
        self._value = 10

    def getValue(self):
        return self._value

    def click(self):
        self._value = self._value + 1

    def reset(self):
        self._value = 0


