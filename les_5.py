import requests, sys, inspect, les_2


def first_function(name = "Name"):
    my_name = name

class First_class:
    def first_function(self):
        pass


print(first_function.__name__)
print(First_class.__name__)
print(requests.__name__)
help(requests)
a = requests
print("a",a)
print(a.__name__)
print(__name__)
print(type(5))
print(type(5.5))
print(type("le"))
print(type(True))
print(type(first_function))
print(type(First_class))
print(type(requests))
print(hasattr(first_function, "name"))
print(callable(5))
print(sys.executable)
print(sys.version)
print(sys.argv)
print(__builtins__)

for metod in dir(__builtins__):
    print(metod)