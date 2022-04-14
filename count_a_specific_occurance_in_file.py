# Write a program to count specific word from a file if the file.

with open("newtext.txt","r") as f1:
    contain = f1.readlines()
count = 0
s_word = input("Enter a word to count from file  : ").lower()
sentence = ""
for line in contain:
    sentence += line.replace("\n","")
    sentence = sentence.lower()
count = sentence.count(s_word)
if count == 0:
    print("Sorry '{}' this not found in file".format(s_word))
else:
    print(s_word," present {} times ".format(count))
