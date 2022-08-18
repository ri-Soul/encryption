from math import *
HexaDecimal = input("Enter the hexadecimal: ")
decimal = 0
ListHexaDecimals = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
Filter = []
i = len(HexaDecimal)
item_change = 0
print("Calculating...")
for letter in HexaDecimal:
  i -= 1
  for item in ListHexaDecimals:
    if item == letter:
      power_i = int(pow(16, i)* ListHexaDecimals.index(item))
      Filter.append(power_i)
for itemcount in Filter:
  decimal += itemcount
print("The decimal: " + str(decimal))
