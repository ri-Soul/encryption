from math import *
binary = input("Binary: ")
l = len(binary)
decimal = 0
print("Calculating...")

for digit in binary:
  l -= 1
  decimal += (float(digit)* (pow(2, i)))

print("Decimal: " + str(decimal))
