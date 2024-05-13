chuoi = input("Nhap : ")
n = {}

for i in chuoi : 
    if i not in n.keys():
        n[i] = chuoi.count(i)

print(n)