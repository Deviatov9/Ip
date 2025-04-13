def f(n):
    s = []
    while n!=0:
        s.append(n % 49)
        n = n //49
    return s

c = 0
n = 16807**35 + 2401**2 * 343**9-49**52+7**3-2005
a = f(n)
for i in a:
    if i >9:
        c+=1
print (c)