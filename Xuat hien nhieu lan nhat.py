def solution():
    a = int(input())
    b = {}
    C = list(map(int, input().split()))
    for i in range(0, a):
        b.update({C[i]: 0})
    for i in range(0, a):
        b.update({C[i]: b[C[i]] + 1})
    x = 0
    y = 0
    for i in range(0, a):
        if x < b[C[i]] and b[C[i]] > (int)(a / 2):
            x = b[C[i]]
            y = C[i]
    if y == 0:
        y = "NO"
    print(y)

def main():
    N = int(input())
    for i in range(0, N):
        solution()

if __name__ == "__main__":
    main()