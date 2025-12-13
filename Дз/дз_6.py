result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
    except ZeroDivisionError:
        print("Ви не можете ділити на нуль!")

    except TypeError:
        print("Ви не можете ділити нечислові значення!")

    except ValueError:
        print("Сталася помилка ValueError!")

    except IndexError:
        print("Сталася помилка IndexError! b > 100")


data = {10: 2, 2: 5, "123": 4, 18: 0, "[]": 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)