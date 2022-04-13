# n is the number of rows
n = 6
for i in range(1,n+2):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i):
        print("* ",end="")
    print("\n")
for i in range(0,n+2):
    for j in range(i):
        print(" ",end="")
    for k in range(1,n-i):
        print("* ",end="")
    print("\n")
    