from math import *
decimal = float(input("Decimal: "))
DecimalRemainder = ""
zero = False
rounded = 0
item = 0
ListHexaDecimals = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

print("Calculating...")
while not(zero):
  item = decimal % decimal/16
  decimal = decimal/16
  if decimal <= 1:
    zero = True
    
  DecimalRemainder += ListHexaDecimals[item]
  mirroir = decimal_remainder
  for number in reversed(mirroir):
    decimal_remainder += number

print("HexaDecimal: " + DecimalRemainder)
