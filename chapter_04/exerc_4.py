# Exercise 4: Current value

P = float(input("Please enter the initial deposit: "))
r = float(input("Please enter interest in fractions(e.g 0.05): "))
n = int(input("Please enter the number of times per year interest is calculated: "))
t = int(input("Please enter the number of years since the initial deposit: "))

V = P * (1 + r / n) ** (n * t)

print(round(V, 2))
