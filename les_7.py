"""
my_list = [1, 2, 3]
iterator = iter(my_list)
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

iterator = iter(my_list)
for i in my_list:
    print(i)

class Counter:
    def __init__ (self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__ (self):
        self.i = 0
        return self

    def __next__ (self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

count = Counter(5)
for elem in count:
    print(elem)

count = Counter(5)
print(count.__next__())
print(count.__iter__())
print(next(count))
print(iter(count))
print(next(count))
count_2 = Counter(5)
print(iter(count_2))


for i in range(100, 20, 3):
    print(i)

def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number**i
        i += 1

res = raise_to_the_degrees(122345, 500)
print(res)
for a in res:
    print(a)
"""
class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"I will help you with your {self.work}. Afterwards I will help you with {work}"

helper = Helper("homework")


print(helper("cleaning"))
def helper(work):
    work_in_memory = work
    def helper(work):
        return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
    return helper

helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))