#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# #advance case
# new_array = [i + 2 for i in original_array if i > 5]

#normal case
new_array = []
for i in original_array :
    if i > 5:
        new_array.append(i+2)


print(original_array)
print(new_array)