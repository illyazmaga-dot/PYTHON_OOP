import random

secret = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. Вгадай!")

for i in range(attempts):
    guess = int(input("Введи число: "))

    if guess == secret:
        print("Вітаю! Ти вгадав!")
        break
    elif guess > secret:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Спроби закінчились! Загадане число було: {secret}")