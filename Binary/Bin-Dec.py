from math import *
binary = input("Enter the Binary: ")
i = len(binary)
decimal = 0
print("Calculating...")

for letter in binary:
  i -= 1
  decimal += (float(letter)* (pow(2, i)))

print("The decimal: " + str(decimal))
