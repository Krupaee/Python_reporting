# class Employee:           # Constructor non parametrized
#     def __init__(self):   # init - magic method (calls itself)
#         self.salary = 22000
#         self.age = 21

# e1 = Employee()
# e2 = Employee()

# print (e1.__dict__)  # attribute hai to see contents of obj

# class Employee:
#     def __init__(self, sal, ag):  # Parameterized constructor
#         self.salary = sal
#         self.age = ag

# e1 = Employee(35000, 28)
# e2 = Employee(33000, 29)

# print (e1.__dict__, e2.__dict__)


# Accessing class members

# class Employee:
#     def __init__(self, sal, ag):  
#         self.salary = sal             # attributes
#         self.age = ag

#     def display (self):             # Methods
#         print(f"Salary is {self.salary} and age is {self.age}")

# e1 = Employee(25000, 28)
# e2 = Employee(33000, 29)

# # Accessing attributes outside the class
# print(e1.salary)
# e1.salary = 34000
# print(e1.salary)

# # Accessing methods outside the class
# e2.display(), e1.display()

# # Built in Functions
# class Employee:
#     def __init__(self, nm, ag):  
#         self.name = nm
#         self.age = ag

# e1 = Employee ('raj', 21)
# e2 = Employee ('jay', 24)

# print(getattr(e1, 'age'))

# (setattr(e2, 'name', 'jayaraj'))
# print(e2.__dict__)

# delattr(e2,'age')
# print(e2.__dict__)

# print(hasattr(e1,'name'))


# # Built in attributes
# class Employee:
#     '''This is employee class to maintain employee in data'''
#     def __init__(self, nm, ag):  
#         self.name = nm
#         self.age = ag
    
#     def display (self):             
#         print(f"Salary is {self.salary} and age is {self.age}")

# e1 = Employee ('raj', 21)
# e2 = Employee ('jay', 24)

# print(Employee.__doc__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)


class Demo:
    pass
d1 = Demo()
class Employee:
    def __init__(self, nm, ag):  
        self.name = nm
        self.age = ag
    
    def display (self):             
        print(f"Salary is {self.salary} and age is {self.age}")

e1 = Employee ('raj', 21)
e2 = Employee ('jay', 24)

print (isinstance(d1,Employee))             # isistance()