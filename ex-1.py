import datetime
currentyear = datetime.datetime.now().year
name = input("Give me your name: ")
age = int(input("Enter your age: "))
print("Your name is " + name)
print ("You will be 100 years old at", str(currentyear + (100 - age))+".")