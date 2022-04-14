"""Being a student of VIT, Raj wants to calculate the GPA (Grade Point Average), which is calculated using the formula,
Sum of product of grade obtained in each subject and its corresponding credits / total credits.
"""
sub = []
grades = {
    "S":10,
    "A":9,
    "B":8,
    "C":7,
    "D":9,
    "E":8,
    "s":10,
    "a":9,
    "b":8,
    "c":7,
    "d":9,
    "e":8
}
no_of_sub = eval(input("Number of subject    :   "))
credit = []
grade = []
for i in range(no_of_sub):
    c = eval(input("Enter the credit of {} subject  ".format(i+1)))
    credit.append(c)
for j in range(no_of_sub):
    g = input("Enter the Grade of {} subject    ".format(j+1))
    grade.append(g)
s = 0
credit_sum = 0
for i in range(no_of_sub):
    g_val = grades.get(grade[i])
    s += credit[i]*g_val
    credit_sum += credit[i]
GPA = s/credit_sum
print("\n Your GPA is {:.2f}".format(GPA))
