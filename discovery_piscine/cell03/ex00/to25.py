#!/usr/bin/env python3
starter_number = int(input("Enter a number less than 25 :"))
if starter_number > 25 :
    print("Error")
else :
    while True :
        print(f"Inside the loop, my variable is {starter_number}")
        starter_number += 1
        if starter_number >25 :
            break