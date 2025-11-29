"""
class Human:
    height = 170
    satiety = 50

class Student(Human):
    satiety = 0
    __password = "OOUjfnjs;"
    _second_password = "OOUjfnjs;"

class Worker (Human):
    satiety = 100


Illay = Student
print(Illay.height)
print(Illay.satiety)
print(Illay._second_password)
#print(Illay.__password)


class Hello:
    def __init__(self):
        print("Hello!")

class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("World!")
hello_world = Hello_World()



class Grandparent:
    def about(self):
        print("I am GrandParent")

    def about_myself(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")

class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

nick = Child()
"""

class Computer:
    def calculate(self):
        print("Calculating…")

class Display:
    def display(self):
        print("I display the image on the screen…")

class SmartPhone(Display, Computer):
        pass

iphone = SmartPhone()
iphone.calculate()
iphone.display()
