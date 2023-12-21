class Calculator:

    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return float(self.number) + float(other.number)

    def __sub__(self, other):
        return float(self.number) - float(other.number)

    def __mul__(self, other):
        return float(self.number) * float(other.number)

    def __truediv__(self, other):
        return float(self.number) / float(other.number)


calculator = Calculator(5)
calculator2 = Calculator(6)
print(calculator+calculator2)
print(calculator - calculator2)
print(calculator * calculator2)
print(calculator / calculator2)
