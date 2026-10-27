#!/usr/bin/env python3
print("Cell2-3 Multiplication")
first_number = int(input("Please enter first number :"))
second_number = int(input("Please enter second number :"))
print(f"{first_number} x {second_number} = {first_number*second_number}")
if first_number*second_number > 0 :
    print("The result is positive")
elif first_number*second_number < 0 :
    print("The result is negative")
else :
    print("The result is positive and negative")