def solution():
    a = input()
    b = [1] * len(a)
    c = len(a)
    s = ""
    for i in range(1, c):
        if a[i] == a[i - 1]:
            b[i] = b[i - 1] + 1
    for i in range(0, c - 1):
        if a[i] != a[i + 1]:
            s += str(b[i])
            s += a[i]
    s += str(b[c - 1])
    s += a[c - 1]
    print(s)

def main():
    N = int(input())
    while N > 0:
        solution()
        N -= 1

if __name__ == "__main__":
    main()