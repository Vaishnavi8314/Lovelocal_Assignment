def digit(n):
    count = 0
    for i in range(len(str(n))):
        high = n // (10 ** (i + 1))
        present= (n // 10 **i) % 10
        low = n % (10 **i)
        count += (high * 10 **i)
        if present == 1:
            count += (low+ 1)
        elif present > 1:
            count += 10 **i
    return count
n = int(input("n = "))
result =digit(n)
print(result)
