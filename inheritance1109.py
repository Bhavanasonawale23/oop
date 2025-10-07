# 11 Sept 
"""
Inheritance:
        - It is one of the most imp. pillar of OOP.
        - Acquring all properties of base class into derived class is called inheritance.

        - Base class => is also called as Super / parent class.
        - Derived class is also called as child / sub-class.


Syntax :
          class Parent:
                # parent class

          class Child(Parent):
                # child class inherits from Parent



Adv. of inheritance =>

1] We need inheritance for memory saving purpose.
2] To avoid code repitation / code redundancy.
3] code reusability.
4] It will reduce project complition time.
5] without inheritance we cannot achieve method overriding.

# types =>
1] simple / single
2] Multi-level inheritance
3] Hierarchical
4] Multiple
5] Hybrid
6] cyclic
"""
""" 
1] simple /single inheritance => - One parent class and one child class kind of inheritance called as single /simple inheritance.
                                 - child class inherits properties from parent class


                                 class parent
                                        |
                                        |
                                        ↓
                                 class child
"""
# class Parent:
#     def m1(self):
#         l=["land", "money","gold","house"]
#         print(l)

# class child(Parent):
#     def m2(self):
#         l=["python"]
#         print(l)

# jay= child()
# jay.m1()
# jay.m2()

# class Animals:
#     def speak(self):
#         print("Animals speaks")

# class Dog(Animals):
#     def bark(self):
#         print("Dog barks")

# d = Dog()
# d.speak()
# d.bark()

"""
2] Multi-level inheritance => A class inherits from a class that itself inherited from another class.

                                  class A
                                     ↓
                                  class B
                                     ↓
                                  class C

"""
# class Grandparent:
#     def house(self):
#         print("Grandparent's house")

# class Parent(Grandparent):
#     def car(self):
#         print("Parent's car")

# class Child(Parent):
#     def bike(self):
#         print("Child's bike")

# c1= Child()
# c1.house()
# c1.car()
# c1.bike()

# class Grandparent:
#     def m1(self):
#         l=["land", "money","gold","house"]
#         print(l)

# class Parent(Grandparent):
#     def m2(self):
#         l=["car","flat"]
#         print(l)

# class child(Parent):
#     def m3(self):
#         l=["python"]
#         print(l)

# jay= child()
# jay.m1()
# jay.m2()
# jay.m3()

"""
3] Hierarchical inheritance => - one parent class and multiple child class
                               -  Multiple classes inherit from the same parent class.

                              class A
                                / \
                               /   \
                        class B     class C
"""
# class Parent:
#     def m1(self):
#         l=["land", "money","gold","house"]
#         print(l)

# class child1(Parent):
#     def m2(self):
#         l=["car","flat"]
#         print(l)

# jay=child1()
# jay.m1()
# jay.m2()


# class child2(Parent):
#     def m3(self):
#         l=["python"]
#         print(l)

# viru= child2()
# viru.m1()
# viru.m3()


# class Vehicle:
#     def fuel(self):
#         print("Needs fuel")

# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")

# class Bike(Vehicle):
#     def ride(self):
#         print("Bike is riding")


# car = Car()
# bike = Bike()

# car.fuel()
# car.drive()
# bike.fuel()

"""
4] multiple inheritance => - one child and multiple parents kind of inheritance
                           -  A class inherits from more than one parent class.

                        class A     class B
                             \      /
                              \    /
                             class C


"""
class Grandparent1:
    def m5(self):
        l=["land", "money"]
        print(l)

class P1(Grandparent1):
    def m1(self):
        l=["car","flat"]
        print(l)

class Grandparent2:
    def m4(self):
        l=["gold","house"]
        print(l)

class P2(Grandparent2):
    def m3(self):
        l=["bunglow","cash"]
        print(l)

class child(P1,P2):
    def m(self):
        l=["python"]
        print(l)

jay= child()
jay.m1()
jay.m4()
jay.m3()
jay.m5()
jay.m()

# class Flyable:
#     def fly(self):
#         print("Can fly")

# class Swimmable:
#     def swim(self):
#         print("Can swim")

# class Duck(Flyable, Swimmable):
#     pass

# d = Duck()
# d.fly()
# d.swim()

"""
5] hybrid inheritance => one parent and multiple childs kind of inheritance.

"""
# class Person:
#     def info(self):
#         print("I am a person")

# class Employee(Person):
#     def work(self):
#         print("I am an employee")

# class Student(Person):
#     def study(self):
#         print("I am a student")

# class Intern(Employee, Student):
#     def intern_info(self):
#         print("I am an intern")

# i = Intern()
# i.info()
# i.work()
# i.study()
# i.intern_info()

"""
6] Cyclic inheritance =>
                    cyclic inheritance is a concept and not used
"""

"""

"""