from math import *
mirroir = []
decimal = float(input("Enter the decimal: "))
decimal_remainder = ""
decimal_round = 0.0
zero = True
print("Calculating...")

while zero:
  decimal = decimal/2
  decimal_remainder += str(int((decimal - floor(decimal))* 2))
  if decimal <= 1:
    zero = False    
for letter in decimal_remainder:
  Mirroir.insert(0, letter)
decimal_remainder = ""
for item in mirroir:
  decimal_remainder += item
file = open("Binary.txt", "w")
file.write(str(decimal_remainder))
file.close()
print("Saved in Binary.txt")
print("The Binary: "str(decimal_remainder))
