'''Mr.KAM used to extract the company name from a given email addresses.
Format of email is username@company.com or username@company.ac.in'''

email = input("Enter your email address : ")
st = email.split('@')
flag = False
i = len(st)
if i > 1:
    ch = st[1]
    for c in ch:
        if c == '.':
            flag = True
else:
    pass
if flag:
    c_name = st[1].split('.')
    company = c_name[0]
    print("your company name is {}".format(company))
else:
    print("Email is not valid")
