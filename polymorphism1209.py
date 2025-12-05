# 12 Sept
"""
# Polymorphism => - It is one of the imp pilars of OOP
                  - same name entity behaves differently at different time is called polymorphism.

                poly => many
                morphs => forms

   # Types of polymorphism =>

   1] Overloading =>
        i. Operator Overloading 
       ii. method / constructor overloading

   2] Overriding =>
        i. method overiding 
       ii. variable overriding
"""
# print(10+20)
# print("10 "+"20")

"""
1] Overloading =>
        i. Operator Overloading => Operator oveloading only happens in " Python"
                                - defining logic for magic methods(__add__, __sub__, etc) for operators as per our choice 
                                 - Using the same operator or method name in different ways in the same class.


"""
# 1] Operator overloading =>
""" not polymorphism =>
# class Book:
#     def __init__(self,n,p):
#             self.n=n
#             self.p=p

# b1= Book("Python", 800)
# print(b1.n) #Python
# b2=Book("Java",900)
        
# print(b1.p + b2.p)    #1700
# print(b1.n + b2.n)    #PythonJava
# print(b1  + b2)"""

# class Book:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

#         def __add__(self,other):
#             return self.price + other.price

# b1=Book("Python ",200)
# b2=Book("java",300)
# print(b1.price +b2.price) # 500


# print(b1.name +b2.name) #Python java
# print(b1 + b2)
# print(b1 - b2)
# print(b1 * b2)
# print(b1 / b2)
# print(b1 // b2)
# print(b1 > b2)
# print(b1 < b2)
# print(b1 == b2)
# print(b1 != b2)
"""
2] Method / constructor overlading =>
            - Same name  (multiple methods /const.)methods / Constructor with different parameters in same class is called methods / constructor overloadind

            - Using the same operator or method name in different ways in the same class.

            Method Overloading (simulated in Python), Python does not support method overloading directly.
            But you can simulate it using:

"""
"""
def m1():
pass

def m2():
pass

def m3():
pass
"""

class Student:
    def __init__(self,r):
         self.roll=r

    def __init__(self,r,n):
         self.roll=r
         self.name=n

    def __init__(self,r,n,m):
          self.roll=r
          self.name=n
          self.marks=m

s1=Student()


# 15 Sept

"""
1] Method overriding =>
                        Re-defining  parent class method (property) into child class is called as method overriding.
                        -wthiout inheritance we cannot do method overriding

 # Super method =>  We  can call any attribute of base class

 2] variable overriding =>
                        Re-defining  parent class variable into child class is called as method overriding
"""

# class Parent:
#     lang = "Java"

#     def property(self):
#         print("This is parent class")
        
#         def marry(self):
#             print(super().__str__())
#             print("marry with girl A ")

# class Child(Parent):
#     lang="Python"
    
#     def __init__(self,n,r):
#         self.name=n
#         self.roll=r
#     def property2(self):
#         print("This is childs class")

#     def marry(self):
#         # super.marry()
#         print("marry with girl B")

#     def __str__(self):
#         return self.name +" "+str(self.roll)



# jay = Child()
# jay.marry()
# jay.property()
# jay.property2()



