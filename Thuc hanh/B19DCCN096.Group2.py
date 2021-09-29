import math
import operator
def tim_chan_le():
    print('Nhap so phan tu cua day:')
    a = int(input())
    print('Nhap cac phan tu cua day:')
    b = []
    while len(b) < a:
        c = list(map(int, input().split(' ')))
        for x in c:
            b.append(x)
    while len(b) > a:
        b.pop
    s = ""
    for i in b:
        if i % 2 == 0:
            s += str(i)
            break
    if len(s) == 0:
        return "Khong co dap an"
    for i in b:
        if i % 2 == 1:
            s += ", " + str(i)
            break
    if len(s) == 1:
        return "Khong co dap an"
    return '(' + s + ')'
def tong_phan_tu():
    print('Nhap so phan tu cua day:')
    a = int(input())
    print('Nhap cac phan tu cua day:')
    b = []
    while len(b) < a:
        c = list(map(int, input().split(' ')))
        for x in c:
            b.append(x)
    while len(b) > a:
        b.pop
    print('Nhap gioi han trai va phai cua pham vi: ')
    m, n = map(int, input().split())
    return sum(b[m - 1 : n])
def dao_nguoc_chuoi():
    print('Nhap so phan tu cua day:')
    a = int(input())
    print('Nhap cac phan tu cua day:')
    b = []
    while len(b) < a:
        c =  input().split(' ')
        for x in c:
            b.append(x)
    while len(b) > a:
        b.pop
    for i in range(len(b)):
        b[i] = b[i][::-1]
    return b
def tim_phan_tu_chung():
    print('Nhap so danh sach:')
    a = int(input())
    print('Nhap so phan tu cua moi danh sach:')
    f = list(map(int, input().split()))
    b = [[]]
    for i in range(a):
        print('Nhap cac phan tu cua danh sach thu ' + str(i + 1) + ':')
        b.append([])
        while len(b[i]) < f[i]:
            c = list(map(int, input().split(' ')))
            for x in c:
                b[i].append(x)
        while len(b[i]) > f[i]:
            b[i].pop
    ans = b[0]
    for i in range(1, a):
        ans = [value for value in b[i] if value in ans]
    return ans
def kiem_tra_tinh_duy_nhat():
    print('Nhap so phan tu cua day:')
    a = int(input())
    print('Nhap cac phan tu cua day:')
    b = []
    while len(b) < a:
        c = list(map(int, input().split(' ')))
        for x in c:
            b.append(x)
    while len(b) > a:
        b.pop
    if (len(set(b)) == len(b)):
        return "True"
    return "False"
def kiem_tra_day_da_sap_xep():
    print('Nhap so phan tu cua day:')
    a = int(input())
    print('Nhap cac phan tu cua day:')
    b = []
    while len(b) < a:
        c = list(map(int, input().split(' ')))
        for x in c:
            b.append(x)
    while len(b) > a:
        b.pop
    c = b[:]
    b.sort()
    if (b == c):
        return "True"
    return "False"
def tim_cac_phan_tu_xuat_hien_nhieu_lan():
    print('Nhap so phan tu cua day:')
    a = int(input())
    print('Nhap cac phan tu cua day:')
    b = []
    while len(b) < a:
        c = list(map(int, input().split(' ')))
        for x in c:
            b.append(x)
    while len(b) > a:
        b.pop
    c = []
    curr = 0
    for i in b:
        if b.count(i) > curr:
            c.clear()
            curr = b.count(i)
            c.append(i)
    c.sort()
    c = list(set(c))
    return c
def trich_xuat_cot():
    print('Nhap so danh sach:')
    a = int(input())
    print('Nhap so phan tu cua moi danh sach:')
    f = list(map(int, input().split()))
    b = [[]]
    for i in range(a):
        print('Nhap cac phan tu cua danh sach thu ' + str(i + 1) + ':')
        b.append([])
        while len(b[i]) < f[i]:
            c = list(map(int, input().split(' ')))
            for x in c:
                b[i].append(x)
        while len(b[i]) > f[i]:
            b[i].pop
    b.pop()
    d = int(input('Nhap cot ban muon lay ra:')) - 1
    k = []
    for i in b:
        k.append(i[d])
    return k
def xoa_mot_cot():
    print('Nhap so danh sach:')
    a = int(input())
    print('Nhap so phan tu cua moi danh sach:')
    f = list(map(int, input().split()))
    b = [[]]
    for i in range(a):
        print('Nhap cac phan tu cua danh sach thu ' + str(i + 1) + ':')
        b.append([])
        while len(b[i]) < f[i]:
            c = list(map(int, input().split(' ')))
            for x in c:
                b[i].append(x)
        while len(b[i]) > f[i]:
            b[i].pop
    b.pop()
    d = int(input('Nhap cot muon xoa'))
    [i.pop(d - 1) for i in b]
    return b
def cmp(a):
    c = 0
    for i in a:
        c += i
    return c
def sap_xep_ma_tran_theo_tong_cac_hang():
    print('Nhap so danh sach:')
    a = int(input())
    print('Nhap so phan tu cua moi danh sach:')
    f = list(map(int, input().split()))
    b = [[]]
    for i in range(a):
        print('Nhap cac phan tu cua danh sach thu ' + str(i + 1) + ':')
        b.append([])
        while len(b[i]) < f[i]:
            c = list(map(int, input().split(' ')))
            for x in c:
                b[i].append(x)
        while len(b[i]) > f[i]:
            b[i].pop
    b.pop()
    b.sort(key = cmp)
    return b
def main():
    print('-----------------------------------------------------------------------------------------')
    print('------------------------Nhap chuc nang ma ban muon: ')
    print('---1: Tim so chan va so le dau tien trong danh sach')
    print('---2: Tim tong cac so trong danh sach trong mot pham vi')
    print('---3: Dao nguoc cac chuoi trong danh sach')
    print('---4: Tim cac phan tu chung cua mot to hop danh sach')
    print('---5: Kiem tra xem cac phan tu trong danh sach co phai la duy nhat hay khong')
    print('---6: Kiem tra xem danh sach da duoc sap xep hay khong')
    print('---7: Tim (cac) phan tu xuat hien nhieu nhat trong danh sach')
    print('---8: Trich xuat mot cot trong danh sach long nhau')
    print('---9: Xoa mot cot trong danh sach long nhau')
    print('---10: Sap xep mot ma tran theo tong cac hang trong danh sach')
    a = int(input())
    if a == 1:
        print(tim_chan_le())
    elif a == 2:
        print(tong_phan_tu())
    elif a == 3:
        print(dao_nguoc_chuoi())
    elif a == 4:
        print(tim_phan_tu_chung())
    elif a == 5:
        print(kiem_tra_tinh_duy_nhat())
    elif a == 6:
        print(kiem_tra_day_da_sap_xep())
    elif a == 7:
        print(tim_cac_phan_tu_xuat_hien_nhieu_lan())
    elif a == 8:
        print(trich_xuat_cot())
    elif a == 9:
        print(xoa_mot_cot())
    elif a == 10:
        print(sap_xep_ma_tran_theo_tong_cac_hang())

if __name__ == '__main__':
    main()
