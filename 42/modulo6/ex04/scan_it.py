#!/usr/bin/env python3

import sys
import re

params = sys.argv[1:]  # ignora o nome do script

if len(params) != 2:
    print("none")
else:
    keyword = params[0]
    text = params[1]

    # count = text.count(keyword)
    matches = re.findall(keyword, text)

    if len(matches) > 0:
        # print(count)
        print(len(matches))
    else:
        print("none")