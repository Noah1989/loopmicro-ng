#!/bin/python3

import sys

for line in sys.stdin:
    print(line.expandtabs(8), end="")
