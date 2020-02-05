from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.root import Root


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Multiplication(self, a, b):
        self.Result = Multiplication.multiplication(a, b)
        return self.Result

    def Division(self, a, b):
        self.Result = Division.division(a, b)
        return self.Result

    def Exponentiation(self, a, b):
        self.Result = Exponentiation.exponentiation(a, b)
        return self.Result

    def Root(self, a, b):
        self.Result = Root.root(a, b)
        return self.Result