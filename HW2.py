import math

class Vector:

    def __init__(self,p1,p2):
        self.X = p1
        self.Y = p2

    def __str__(self):
        return '<{},{}>'.format(self.X,self.Y)

    def __abs__(self):
        return (self.X**2+self.Y**2)**0.5

    def getHossz(self):
        return Vector.__abs__(self)

    def __round__(self, n=None):
        return self.__class__(round(self.X), round(self.Y))

    def __add__(self, other):
        if isinstance(other,Vector):
            x = self.X + other.X
            y = self.Y + other.Y

        if isinstance(other,int) or isinstance(other,float):
            x = self.X + other
            y = self.Y + other

        return self.__class__(x,y)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other,Vector):
            x = self.X - other.X
            y = self.Y - other.Y

        if isinstance(other,int) or isinstance(other,float):
            x = self.X - other
            y = self.Y - other

        return self.__class__(x,y)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other,Vector):
            return self.X*other.X+self.Y*other.Y

        if isinstance(other,int) or isinstance(other,float):
            x = self.X * other
            y = self.Y * other
            return self.__class__(x,y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other,Vector):
            return self.X/other.X+self.Y*other.Y
        if isinstance(other,int) or isinstance(other,float):
            x = self.X / other
            y = self.Y / other
            return self.__class__(x,y)

    def __gt__(self, other):
        return self.getHossz() > other.getHossz()

    def __le__(self, other):
        return self.getHossz() <= other.getHossz()

    def __eq__(self, other):
        return self.getHossz() == other.getHossz()

    def __ne__(self, other):
        return self.getHossz() != other.getHossz()

class ComplexNumber:
    def __init__(self, val, kepz):
        self.val= val
        self.kepz = kepz

    def __str__(self):
        if self.kepz < 0:
            return "({}{}i)".format(self.val,self.kepz)
        return "({}+{}i)".format(self.val,self.kepz)

    def __round__(self, n=None):
        return self.__class__(round(self.val), round(self.kepz))

    def conjugate(self):
        return self.__class__(self.val, -self.kepz)

    def argz(self):
        return math.atan(self.kepz / self.val)

    def __abs__(self):
        return (self.val**2 + self.kepz**2)**0.5

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            val_part = self.val + other
            kepz_part = self.kepz

        if isinstance(other, ComplexNumber):
            val_part = self.val + other.val
            kepz_part = self.kepz + other.kepz

        return self.__class__(val_part, kepz_part)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            val_part = (self.val - other)
            kepz_part = self.kepz

        if isinstance(other, ComplexNumber):
            val_part = (self.val - other.val)
            kepz_part = (self.kepz - other.kepz)

        return self.__class__(val_part, kepz_part)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            val_part = self.val* other
            kepz_part = self.kepz * other

        if isinstance(other, ComplexNumber):
            val_part = (self.val * other.val) - (self.kepz * other.kepz)
            kepz_part = (self.val * other.kepz) + (self.kepz * other.val)

        return self.__class__(val_part, kepz_part)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __gt__(self, other):
        return 'hiba'

    def __eq__(self, other):
        return (self.val == other.val) and (self.kepz == other.kepz)

    def __ne__(self, other):
        return (self.val != other.val) or (self.kepz != other.kepz)

#main
v1 = Vector(4,20)
v2 = Vector(6,9)
print(v1-v2)
print(v1)
print(abs(v1))
v1+=5
print(v1)
v1+=7
print(v2-v1)
print(v2*v1)
print(v2*14)
print(v1.__abs__())
print(v1.getHossz())
print(v1+v2)
print(v2+v1)
print(v2*2)
print(v2/2)
print(round(v2/2))
print(v1<v2)
print(v1>v2)

print()

c1 = ComplexNumber(3,-5)
c2 = ComplexNumber(2,6)
c3 = ComplexNumber(3,7)
print(c1)
print(c2)
print(c1+c2)
print(round(c1-c2))
print(c1-c2, "orig")
print(c2-c1,"ellentét")
print(c1*c2)
print(c1*c2*c3)
print(c1 == c2)
print(ComplexNumber.__abs__(c1))
c1 += 5
print(c1)
c1 -= 5
print(c1)
print(ComplexNumber.argz(c1))
print(c1>c2)

