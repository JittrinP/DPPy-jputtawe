#!/usr/bin/env python3
while True :
    my_age = int(input("Please tell me your age : "))
    
    #incase user enter minus age
    if my_age < 0 :
        print("You are enter less than 0 years old , Please tell me your age again")

    #normal case
    else :
        print(f"You are currently {my_age} years old.")
        for i in range (10 , 31 ,10):
            print(f"In {i} years, you'll be {my_age + i} years old.")
        break