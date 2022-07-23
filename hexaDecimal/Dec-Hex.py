from math import *
decimal = float(input("Enter the decimal: "))
DecimalRemainder = ""
NotZero = True
rounded = 0
item = 0
ListHexaDecimals = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
Mirroir = []

print("Calculating...")
while NotZero:
  decimal = decimal/16
  if decimal <= 1:
    NotZero = False
  rounded = floor(decimal)

  item = floor((decimal - rounded)* 16)
  DecimalRemainder += ListHexaDecimals[item]
  
for letter in DecimalRemainder:
  Mirroir.insert(0, letter)

DecimalRemainder = ""
for item in Mirroir:
  DecimalRemainder += item
print("The hexadecimal: " + DecimalRemainder)
