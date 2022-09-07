from math import *

decimal = int(input("Decimal: "))
decimal_remainder = ""
zero = False
item = 0
ListHexaDecimals = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
print("Calculating...")

while not(zero):
  item = decimal % 16
  decimal = floor(decimal/16)
  if decimal == 0:
    zero = True

  decimal_remainder += ListHexaDecimals[item]

print("HexaDecimal: " + decimal_remainder[::-1])
