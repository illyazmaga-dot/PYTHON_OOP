def three(max_degree):
    for i in range(max_degree):
        yield 3 ** i

res = three(500)

for x in res:
    print(x)