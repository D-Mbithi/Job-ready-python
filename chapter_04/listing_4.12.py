# A new banking python script

import math

loan1 = 12383.89
loan2 = 48339.99

roundLoanA = math.ceil(loan1 * 0.078)
roundLoanB = math.floor(loan2 * 0.19)

print(roundLoanA + roundLoanB)
