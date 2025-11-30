class Animal:
    def __init__(self, name):
        self.name = name
    def play(self):
        print("Тварина грається")

class Dog(Animal):
    def play(self):
        print("Собака грається з м’ячем")

class Cat(Animal):
    def play(self):
        print("Кіт грається з клубком")

dog = Dog("Беті")
cat = Cat("Пушок")

dog.play()
cat.play()