class Complex_Numbers:
    def __init__(self,re=0,Im=0):
        self.real=re
        self.imaginary=Im

    def add(self,other):
        sum=Complex_Numbers()
        sum.real=self.real + other.real
        sum.imaginary=self.imaginary + other.imaginary
        return sum
        
    def sub(self,other):
        subm=Complex_Numbers()
        subm.real=self.real - other.real
        subm.imaginary=self.imaginary - other.imaginary
        return subm
        
    def mul(self,other):
        mult=Complex_Numbers()
        mult.self=(self.real * other.real) - (self.imaginary * other.imaginary)
        mult.imaginary=(self.real * other.imaginary)+(self.imaginary * other.real)
        return mult

    def show(self):
        if self.imaginary>0:
            print(self.real, "+", self.imaginary, "i")
        else:
            print(self.real, self.imaginary,"i")


#tabe vared kardan real
def get_real():
    print("Enter the real part:")
    input_re=int(input("real:"))

    return input_re

#tabe vared kardn Im
def get_imaginary():
    print("Enter the imaginary part:")
    input_Im=int(input("imaginary:"))

    return input_Im


############

print("Enter one option:\n1.Sum\n2.Sub\n3.Mul")
choose=int(input("-->"))


#jam
if choose==1:
    #sakht shei aval
    obj1=Complex_Numbers(get_real(),get_imaginary())

    #sakht shei dovom
    obj2=Complex_Numbers(get_real(),get_imaginary())

    #hasel
    result = obj1.add(obj2)

    #namayesh hasel
    result.show()

#tafriq
if choose==2:
    #sakht shei aval
    obj1=Complex_Numbers(get_real(),get_imaginary())

    #sakht shei dovom
    obj2=Complex_Numbers(get_real(),get_imaginary())

    
    #hasel
    result = obj1.sub(obj2)

    #namayesh hasel
    result.show()

#zarb
if choose==3:
    #sakht shei aval
    obj1=Complex_Numbers(get_real(),get_imaginary())

    #sakht shei dovom
    obj2=Complex_Numbers(get_real(),get_imaginary())

    
    #hasel
    result = obj1.mul(obj2)

    #namayesh hasel
    result.show()