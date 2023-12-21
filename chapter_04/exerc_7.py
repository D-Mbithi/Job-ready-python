# Exercise 7: Playing with Numbers

from math import sqrt

num = int(input("Please enter a number: "))
numbool = bool(num)
numbinary = 1 if numbool else 0
numsqrt = sqrt(num)

print("You have selected", num)
print("The boolean of your number is", numbool)
print("The binary equivalent of your number is", numbinary)
print("The square root of your number is", numsqrt)
