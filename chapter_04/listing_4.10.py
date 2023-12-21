# The banking applications with rounding added

accBal = 13445
locaBal = 16000
savBal = 4000
savInterest = 0.025
locInterest = 0.098
months = 12
years = 8.5
numString = "12345"


comInterest = savBal * ((1 + (savInterest / months)) ** (months * years))
print(round(comInterest, 2))

result1 = (savBal + accBal) - locaBal
print(result1)

result2 = (accBal - locaBal) * locInterest
print(round(result2, 2))

result3 = ((savInterest / months) + 1) ** (months * years)
print(result3)

result4 = ((locInterest * months * years) + 1) * locaBal
print(round(result4, 1))
