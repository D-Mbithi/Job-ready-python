# Calculating simple interest

accBal = input("Please enter an account balance: ")
intRate = input("Please enter an interest rate: ")
time = input("Please enter a period of time in years: ")

accBalInt = int(accBal)
rateInt = float(intRate)
timeInt = int(time)

result = accBalInt * rateInt * timeInt

accBal = result + accBalInt

print(accBal)
