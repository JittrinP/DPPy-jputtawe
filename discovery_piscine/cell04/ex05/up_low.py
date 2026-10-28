#!/usr/bin/env python3
viceVersa = input()
for i in viceVersa:
    if i.isupper():
        print(i.lower(), end="")
    elif i.islower():
        print(i.upper(), end="")
    else:
        print(i, end="")
print()
