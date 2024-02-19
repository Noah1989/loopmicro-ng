#!/bin/python3

import sys, re

for line in sys.stdin:
    print(re.sub(r'[\x20-\x7F\w]', ' ', line.expandtabs(8), flags=re.UNICODE), end="")
