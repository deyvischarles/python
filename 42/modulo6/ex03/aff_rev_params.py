#!/usr/bin/env python3

import sys

params = sys.argv[1:] # ignora o nome do script

if len(params) < 2:
    print("none")
else:
    for p in reversed(params):
        print(p)