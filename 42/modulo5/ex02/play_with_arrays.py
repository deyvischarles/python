#!/usr/bin/env python3

default_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []

print(f"Original array: {default_list}")

for i in default_list:
    if i > 5:
        new_list.append(i + 2)

print(f"New array: {new_list}")
