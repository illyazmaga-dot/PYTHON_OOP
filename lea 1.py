import random

print("Hello Class")

class Student:
    amount_of_students = 0
    def __init__(self, name="Стівен", height = 160):
        self.name = name
        self.height = height
        self.gladness = 50
        self.progress = 0
        self.alive = True
        Student.amount_of_students += 1
        print("Hi")
        print("I am alive!")

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive ()

    def __str__(self):
        return f"Hello. My name {self.name}. My height is {self.height}"

    def __bool__(self):
        return False

    def __int__(self):
        return self.height

    def printer(self):
        #print("Hello. My height is ", self.height)
        print("Hello. My name {}. My height is {}".format(self.name, self.height))
        print(f"Hello. My name {self.name}. My height is {self.height}")


first_student = Student()
print(first_student.height)
second_student = Student("Алекс", 171)
print(second_student.height)
print(Student.amount_of_students)
second_student.printer()
print(second_student)
#type(str(second_student))
a = int("5")
b = bool(77)
print(bool(second_student))
print(int(second_student)+150)


for day in range(365):
    if second_student.alive == False:
        break
    second_student.live(day)
