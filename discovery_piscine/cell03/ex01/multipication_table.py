#!/usr/bin/env python3
roll_number = int(input("Enter a number\n"))
i = 0;
while True :
    print(f"{i} x {roll_number} = {i * roll_number}")
    i += 1
    if i == 10 :
        break