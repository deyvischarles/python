#!/usr/bin/env python3

import sys

params = sys.argv

if len(params) -1 != 1:
    print("none")
else:
    print(f"{params[1].lower()}")