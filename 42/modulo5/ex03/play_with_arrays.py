#!/usr/bin/env python3

orig_list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = set() # set NÃO preserva ordem

print(f"{orig_list}")

for value in orig_list:
    if value > 5:
        new_list.add(value + 2)

print(f"{new_list}")

""" 
| value | >5? | value+2 | entra no set? |
| ----- | --- | ------- | ------------- |
| 2     | não | –       | não           |
| 8     | sim | 10      | sim           |
| 9     | sim | 11      | sim           |
| 48    | sim | 50      | sim           |
| 8     | sim | 10      | já existe     |
| 22    | sim | 24      | sim           |
| -12   | não | –       | não           |
| 2     | não | –       | não           | 
"""