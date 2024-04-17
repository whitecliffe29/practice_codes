def binToDec(n):
    res = 0
    i = 0
    while n > 0:
        digit = n % 10
        res += digit * (2 ** i)
        n //= 10
        i = i + 1

    return res


n = int(input("Enter a number : "))

dec = binToDec(n)

print("Decimal is :", dec)
