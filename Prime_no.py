prime_no = []
count = 0
print("Prime number between 1 to 100 ")
for i in range(2,100):
    for j in range(1,i+1):
        if i % j == 0:
            count = count + 1
    if count < 3 :
        prime_no.append(i)
    count = 0
for num in prime_no:
    print(num,end=" ")
