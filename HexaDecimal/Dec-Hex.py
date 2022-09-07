from math import *

decimal = float(input("Decimal: "))
decimal_remainder = ""
zero = False
item = 0
ListHexaDecimals = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
print("Calculating...")

while not(zero):
  item = decimal % 16
  decimal = decimal/16
  if decimal <= 1:
    zero = True

  decimal_remainder += ListHexaDecimals[item]

mirroir = decimal_remainder
for rest in reversed(mirroir):
  decimal_remainder += rest

print("HexaDecimal: " + decimal_remainder)
