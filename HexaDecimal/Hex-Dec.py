from math import *

hexadecimal = input("Hexadecimal: ")
l = len(hexadecimal)
decimal = 0
hexadecimal_table = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
print("Calculating...")

for letter in hexadecimal:
  l -= 1
  for item in hexadecimal_table:
    if item == letter:
      decimal += int(pow(16, l)* hexadecimal_table.index(item))

print("Decimal: " + str(decimal))
