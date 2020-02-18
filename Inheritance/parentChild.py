'''
example of single inheritance where it involves one child class and one parent class
the child class inherits the properties of the parent class
'''

class Parent:
    def funct1(self):
        print ("this is a parent function")

class Child (Parent):
    def funct2(self):
        print("this is a child function")


ob = Child()
ob.funct1()
ob.funct2()



