def f(n):
    s = []
    while n != 0:
        s.append(n % 7)
        n = n // 7
    return s
c = 0
n = 7**21 + 49**13 - 7**10
a = f(n)
for i in a:
    if i == 6:
        c+=1
print(c)