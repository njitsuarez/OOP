'''
created a class and adds and subtracts methods are defined and __init__ initializes values a b
'''
class addSub():
    def __init__(self, a, b):
        init.a = a
        init.b = b

    def add (self):
        self.c = self.a + self.b
        return self.c

    def sub (self):
        self.c = self.a + self.b
        return self.c
'''
created a class called fullCal that inherits the addSub class (parent class) and creates the multiplication method
'''
class fullCal(addSub):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mult(self):
        self.c = self.a * self.b
        return self.c

clcltr = fullCal()
clcltr.add()
clcltr.mult()
clcltr.sub()