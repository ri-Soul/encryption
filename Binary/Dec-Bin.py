from math import *

decimal = float(input("Decimal: "))
decimal_remainder = ""
zero = False
print("Calculating...")

while not(zero):
  decimal_remainder += str(decimal % 2)
  decimal = decimal/2
  if decimal <= 1:
    zero = True

mirroir = decimal_remainder
for rest in reversed(mirroir):
  decimal_remainder += rest

print("Binary: " + decimal_remainder)