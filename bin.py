bl = 0

def solution():
    a = int(input())
    b = str(input())
    c = ""
    for i in range(0, len(b)):
        if b[i] == 'U':
            c += 'D'
        elif b[i] == 'D':
            c += 'U'
        else:
            c += b[i]
    print(c)

def main():
    # N = int(input())
    while bl == 0:
        solution()

if __name__ == "__main__":
    main()