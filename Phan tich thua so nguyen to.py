M = []

def pre():
    N = [0] * 100000
    N[0] = 1
    N[1] = 1
    for i in range(0, 100000):
        if N[i] == 0:
            for j in range(i * i, 100000, i):
                N[j] = 1
    for i in range(0, 100000):
        if N[i] == 0:
            M.append((int)(i))

def solution():
    a = int(input())
    ans = "1"
    for i in range(0, len(M)):
        k = 0
        while a % M[i] == 0:
            k += 1
            a /= M[i]
        if k > 0:
            ans += " * "
            ans += str((int)(M[i])) + "^" + str((int)(k))
        if M[i] * M[i] > a:
            break
    if a > 2:
        ans += " * " + str((int)(a)) + "^1"
    print(ans)


def main():
    N = int(input())
    pre()
    while N > 0:
        N -= 1
        solution()

if __name__ == "__main__":
    main()