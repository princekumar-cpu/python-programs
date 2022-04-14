ls1 = [2,3,8,67,78]
n = len(ls1)
ls2 = [6,7,8,9,12,34,56]
result = []
m = len(ls2)
x = 0
y = 0
while True:
    if (x == n - 1) or(y == m - 1):
        break
    if ls1[x]<ls2[y]:
        result.append(ls1[x])
        x += 1
    elif ls1[x]==ls2[y]:
        result.append(ls1[x])
        x += 1
        result.append(ls2[y])
        y += 1
    else:
        result.append(ls2[y])
        y += 1
    
if (x != n - 1):
    while (x != n ):
        result.append(ls1[x])
        x += 1
if (y != m - 1):
    while (y != m ):
        result.append(ls2[y])
        x += 1
print("__________Two sorted list__________\nList 1 : {}\nList 2 : {}".format(ls1,ls2))
print("list after merging both list : {}".format(result))
