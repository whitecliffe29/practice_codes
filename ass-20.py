def sum(*a):
    sum = 0
    i = 0
    for i in a:
        sum += i

    return sum


s = sum(5, 6, 2, 7, 1)

print("Sum is :", s)
