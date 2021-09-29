def check(n):
    m = "".join(reversed(str(n)))
    if(len(m)%2!=0):
        return False
    for i in range(0,len(m)):
        if m[i]!=str(0) and m[i]!=str(2) and m[i]!=str(4) and m[i]!=str(6) and m[i] != str(8):
            return False
    if m == str(n):
        return True
    return False

def solve():
    n = int(input())
    for i in range(22, n, 22):
        if check(i) and i % 2 == 0:
            print(i,end=" ")

if __name__ == "__main__":
    t = int(input())
    while t!=0:
        solve()
        print("")
        t-=1