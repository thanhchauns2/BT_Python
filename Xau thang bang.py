def check(a, b):
    if len(a) != len(b):
        return False
    c = len(a)
    for i in range(c - 1):
        if abs((a[i]) - (a[i + 1])) != abs((b[i]) - (b[i + 1])):
            return False
    return True

def solution():
    a = input()
    b = a[::-1]
    a = [ord(x) for x in a]
    b = [ord(x) for x in b]
    if (check(a, b)):
        print("YES")
    else:
        print("NO")

def main():
    N = int(input())
    while N > 0:
        solution()
        N -= 1

if __name__ == "__main__":
    main()