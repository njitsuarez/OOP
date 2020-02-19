'''
classes Square & Triangle have the function calculate_area() w/ the same name, but due to different
objects its call get resolved correctly, that is when the function is called using the object sqre then the function
of class Square is called and when it is called using the object tri then the function of class Triangle is called.

by doing this developers don't have have remember the name of every function
'''
class Square(aLenght):
    sideLen = aLength
    def calculate_area (self):
        return (self.sideLen * self.sideLen)

class Triangle(aBase, aHeight):
    base = aBase
    height = aHeight
    def calculate_area(self):
        return (self.base * self.height)

sqre = Square(3)
tri = Triangle(4, 2)
