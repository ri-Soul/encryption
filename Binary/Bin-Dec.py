from math import *

binary = input("Binary: ")
l = len(binary)
decimal = 0
print("Calculating...")

for bit in binary:
  l -= 1
  decimal += (float(bit)* (pow(2, l)))

print("Decimal: " + str(decimal))
