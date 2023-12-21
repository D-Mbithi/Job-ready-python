# Exercise 1: Prompting the user

number = input("Please enter a number: ")

if int(number):
    print("Integer")
elif float(number):
    print("Float")
elif complex(number):
    print("Complex")
else:
    print("Please pprovide a number.")
