st = input("Enter a string ")
rvst = st[::-1]
yes = True
for i in range(len(st)):
   if st[i] != rvst[i]:
       yes = False
if yes:
    print(st," is a palindrome string")
else:
    print(st," is not a palindrome string")
