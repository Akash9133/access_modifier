class Employee:
    firstName: str = "Rock"
    lastName: str = "star"

emp=Employee()
print(emp.firstName)
print(emp.lastName)


# partially private
class Employee:
    _firstName: str = "naveen"
    _lastName: str = "akash"
emp = Employee()
print(emp._firstName)
print(emp._lastName)

# strictly private
class Employee:
    _firstName: str = "rocksrar"
    _lastName: str = "akash"
emp = Employee()
print(emp._firstName)

#global variable
def fullName():
    global fName
    global lName
    fName = "naveen"
    lName = "alisheety"
fullName()
print(fName)
print(lName)

# functional scope
def fullName():
    global fName
    global lName
    fName = "acer"
    lName = "SSD 512GB"
fullName()
print(fName)
print(lName)

# abstraction
class Employee:
    __firstName: str = "sai"
    __lastName: str = "teja"
    def fullName(self):
        return self.__firstName+" "+ self.__lastName
emp=Employee()
emp.__firstName= "ABC"
print(emp.fullName())



