#!/usr/bin/env python3
Original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# case 1
New_array = []
for i in Original_array:
    New_array.append(i + 2)

# case 2
# new_array = [i + 2 for i in Original_array]
# print(new_array)

print(f"Original array : {Original_array}")
print(f"New array : {New_array}")
