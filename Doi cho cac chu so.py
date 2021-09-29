def solve():
    n = int(input())
    a = []
    k = -1
    while n > 0:
        a.append(n % 10)
        n //= 10
    for i in range(0, len(a)-1):
        if a[i] < a[i+1]:
            k = i
            break
    n = len(a)
    if k == -1:
        print(-1)
        return

    c = a[k+1]
    x = -1
    inx = -1
    for i in range(k, -1, -1):
        if a[i] < c and x < a[i]:
            x = a[i]
            inx = i

    if x == 0 and k == len(a)-2:
        print(-1)
        return
    swap = a[inx]
    a[inx] = a[k+1]
    a[k+1] = swap
    for i in range(len(a)-1, -1, -1):
        print(a[i], end="")

    print()


if __name__ == "__main__":
    t = int(input())
    while t != 0:
        solve()
        t -= 1
