#!/usr/bin/env python3

import sys

param_count = len(sys.argv) - 1
print(f"Número de parâmetros: {param_count}.")

"""
[
  "./parameters.py",  # índice 0 → nome do script
  "isso",             # índice 1 → parâmetro 1
  "é",                # índice 2 → parâmetro 2
  "teste"             # índice 3 → parâmetro 3
]

-1 remove a contagem do nome do script.
"""