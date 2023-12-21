# Banking application

version = 1.1
bank_name = "Biometrics Bank"
isLogged = False

print("Hello, Welcome to", bank_name)
print("You are using the banking portal version", version)
print("In this portal, you can handle all your banking needs.")
print("Please enter a selection from the following menu.")

print("Type Quit to quit.")
print("Type Login to log in.")

selection = input("")

print("You have selected.")
print(selection)


acctBal = 13445
locBal = 16000
savBal = 4000
savInterest = 0.025
locInterest = 0.098

months = 12
years = 8.5
numString = "12345"

compInt = savBal * ((1 + (savInterest / months)) ** (months * years))
print(compInt)

results1 = (acctBal + savBal) - locBal
print(results1)
results2 = (acctBal - locBal) * locInterest
print(results2)
results3 = ((savInterest / months) + 1) ** (months * years)
print(results3)
