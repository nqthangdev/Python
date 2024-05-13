list = [0,1,2,3,4,5,6,7,8,9]
list2 = []
sum = 0

for i in list:

    if i%2 == 0:
        list2.append(i)
        sum = sum + i

    if len(list2) > 0:
        tbc = sum / len(list2)
    else:
        tbc = 0
    
print(list2)
print("Tong cua cac so chan la : ",sum)
print("Trung binh cong la : ",tbc )

    