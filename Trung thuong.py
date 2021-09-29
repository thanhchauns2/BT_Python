def solution():
    a = int(input())
    M = {}
    N = []
    for i in range(0, a):
        N.append(int(input()))
        M.update({N[i]: 0})
    for i in range(0, a):
        M.update({N[i]: M[N[i]] + 1})
    mn = -1
    time = 0
    for i in range(0, a):
        if M[N[i]] > time:
            mn = N[i]
            time = M[N[i]]
        elif M[N[i]] == time and N[i] < mn:
            mn = N[i]
    print(mn)

def main():
    N = int(input())
    while N > 0:
        N -= 1
        solution()

if __name__ == "__main__":
    main()