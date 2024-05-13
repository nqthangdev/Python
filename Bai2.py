n = str(input("Nhap chuoi ki tu : "))

chuhoa = 0
chuthuong = 0

chuoihoa = ""
chuoithuong = ""

for i in n:
    if i.isupper():
        chuhoa += 1
        chuoihoa += i
    elif i.islower():
        chuthuong += 1
        chuoithuong+= i

print(f"Ky tu viet hoa : {chuoihoa} - {chuhoa}")
print(f"Ky tu viet thuong : {chuoithuong} - {chuthuong}")
