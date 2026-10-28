#!/usr/bin/env python3
first_number = int(input("Give me the first number :"))
second_number = int(input("Give me the second number :"))
print("Thank you!")
print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
if (first_number/second_number).is_integer():
    print(f"{first_number} / {second_number} = {int(first_number / second_number)}")
else:
    print(f"{first_number} / {second_number} = {first_number / second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")

# second method : Use for loop for print
# results = [
#     ("+", first_number + second_number),
#     ("-", first_number - second_number),
#     ("/", first_number / second_number),
#     ("*", first_number * second_number),
# ]
# for symbol , result in results:
#     print(f"{first_number} {symbol} {second_number} = {result}")