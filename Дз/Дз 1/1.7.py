a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
operation = input("Введіть дію (+, -, *, /): ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print(a / b)
else:
    print("Невідома дія")
