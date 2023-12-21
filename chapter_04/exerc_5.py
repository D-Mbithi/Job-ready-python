# Exercise 5: Simple interest

principal = float(input("Please enter the principla amount: "))
rate = float(input("Please enter the interest in fractions(e.g 0.05): "))
days = int(input("Please enter the days: "))

interest = principal * rate * days / 365

print(round(interest, 2))
