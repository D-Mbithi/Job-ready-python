# Calculating debt ratio

monthlyDebt = input("Enter the monthly debt payments:")
grossIncome = input("Enter the gross monthly income:")

# Convert the string into integers
debtInt = int(monthlyDebt)
incomeInt = int(grossIncome)

diRatio = debtInt / incomeInt
print(diRatio)
