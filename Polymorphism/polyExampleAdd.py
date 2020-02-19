# Polymorphism with the adding operation

def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
# output 5 because z = 0
print(add(2, 3, 4))
# output 9 because z is 4 but z is defacto 0 when no value is placed for z