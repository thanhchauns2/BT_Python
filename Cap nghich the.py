def solution():
    a = int(input())
    C = list(map(int, input().split()))
    ttl = 0
    for i in range(0, a):
        for j in range(i + 1, a):
            if (C[j] < C[i]): ttl += 1
    print(ttl)

def main():
    N = 1
    for i in range(0, N):
        solution()

if __name__ == "__main__":
    main()