def end(a):
    for i in range(4):
        if a[i] != 0:
            return False
    return True

def check(a):
    for i in range(4):
        if a[i] != a[0]: 
            return False
    return True

def solution():
    a = list(map(int, input().split()))
    if end(a):
        return 0
    t = 0
    while check(a) != True:
        b = abs(a[3] - a[0])
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = b
        t += 1
    print(t)
    return 1

def main():
    # N = int(input())
    while solution() == 1:
        o = 0

if __name__ == "__main__":
    main()