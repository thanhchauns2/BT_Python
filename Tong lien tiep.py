import math
a = int(input())
for i  in range(0, a):
    ttl = 0
    x = int(input())
    x2 = (int)(math.sqrt(2 * x))
    # print(x2)
    for y in range(2, x2 + 1):
        # print(y)
        if (2 * x) % y == 0:
            z = (int)(2 * x / y)
            # print(z)
            m = (int)(z - y) % 2
            # print(m)
            if m == 1:
                ttl += 1
    print(ttl)