def sum_eo(n ,t):
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1
    return sum(range(start, n, 2))


x = sum_eo(11, 'spam')
y = sum_eo(10, 'e')
z = sum_eo(7, 'o')

print(x)
print(y)
print(z)