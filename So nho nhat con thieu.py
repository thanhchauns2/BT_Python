from re import A


def solution():
    a = int(input())
    C = list(map(int, input().split()))
    M = {}
    for i in range(0, a):
        M.update({C[i]: 0})
    for i in range(0, a + 2):
        M.update({i: 0})
    for i in C:
        M.update({i: M[i] + 1})
    for i in range(1, a + 2):
        if M[i] == 0:
            print(i)
            return


def main():
    N = 1
    while N > 0:
        N -= 1
        solution()

if __name__ == "__main__":
    main()