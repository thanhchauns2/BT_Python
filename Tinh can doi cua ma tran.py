import math

def solution():
    N = int(input())
    K = [[0] * N] * N
    for i in range(N):
        K[i] = list(map(int, input().split()))
    t = 0
    t2 = 0
    diff = int(input())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            elif i > j:
                t2 += K[i][j]
            else:
                t += K[i][j]
    if abs(t - t2) <= diff:
        print("YES")
    else:
        print("NO")
    print((int)(abs(t - t2)))

def main():
    N = 1
    while N > 0:
        N -= 1
        solution()

if __name__ == "__main__":
    main()