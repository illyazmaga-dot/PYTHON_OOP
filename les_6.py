"""
try:
    #print(gg)
    print(5/0)
except NameError:
    print("Сталась помилка NameError!")
except ZeroDivisionError as erorr:
    print("Сталась помилка! ZeroDivisionError", erorr)
except:
    print("Сталась помилка!")


def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry, we can't work with {type(var_1)}, "f"we need class str")
    else:
        return var_1

first_var = 10
checker(first_var)

class BuildingEror (Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"

def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "enough material"
    else:
        raise BuildingEror(amount_of_material)

materials = 123
check_material (materials, 300)


try:
    print("We have a problem!")
    try:
        print()
    except:
        print()
except:
    print("This is except")
else:
    print("This is else")
finally:
    print("This is finally")
"""
import warnings

import warnings

warnings.simplefilter("always", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("SyntaxWarning", SyntaxWarning)
warnings.warn("ImportWarning", ImportWarning)
print("Hello Class")