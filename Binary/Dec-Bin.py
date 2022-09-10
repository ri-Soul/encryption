from math import *

decimal = int(input("Decimal: "))
decimal_remainder = ""
zero = False
print("Calculating...")

while not(zero):
  decimal_remainder += str(decimal % 2)
  decimal = floor(decimal/2)
  if decimal == 0:
    zero = True

print("Binary: " + decimal_remainder[::-1])