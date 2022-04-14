"""A person wants to know his Body Mass Index (BMI). He knows his weight in pounds and height in inches. The evaluator knows the formula for calculating BMI using the formula,
BMI = (weight in kilograms) / (height in m * height in m)
Help the person in finding his BMI by writing a program for him. (Use the conversion formulae: 1 pound =0.4536 kilograms, 1 inch = 2.54 cms)
"""
w = eval(input("Enter the weight in pound "))
h = eval(input("Enter the Height in inches "))
w = w*0.4536 # TO convert pound into kg
h = (h*2.54)/100 # To convert inches into meters
bmi = w/(h*h)
print("BMI : {:.2f}".format(bmi))
