class String:

    s = ""

    def __init__(self,p1=""):
        self.s = p1

    def __str__(self):
        return "Ez egy string, amely ezt írja: {}".format(self.s)

    def setString(self,p1):
        self.s = p1

    def toUpper(self):
        return self.s.upper()

    def toLower(self):
        return self.s.lower()

    def bigCapital(self):
        return self.s.title()

#main
str = String("This is a monkey")
print(str)
str = String()
print(str)
str.setString("Ez egy majom")
print(str)
print(str.toUpper())
print(str.toLower())
print(str.bigCapital())