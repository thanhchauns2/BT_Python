import math
a = int(input())
while a > 10:
    b = str(a)
    c = (int)(len(b) / 2)
    if (int)(len(b)) % 2 == 1:
        c += 1
    d = 0
    tmp = 1
    while c > 0:
        c -= 1
        d = (int)((a % 10) * tmp + d)
        tmp *= 10
        a = int(a / 10)
    a = a + d
    print(a)