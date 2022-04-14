# Write a program to delete a sentence from a file if the file contains a specific word.

with open("text.txt","r") as f:
    words = f.readlines()  
    print(words)
with open("text.txt","w") as new_file:
    b = True
    specific_word = input("Enter specific word to delete a sentence  ")
    contains = ""    
    for line in words:
        if specific_word not in line.strip("\n"):
            contains += line    
        else:
            b = False       
    if b :
        print("   {} is not present in any lines of the file!!!!!!!!!".format(specific_word))   
        new_file.write(contains)
    else:
        new_file.write(contains)
        print("-----------------------------Sucessfully Deleted-----------------------------")
