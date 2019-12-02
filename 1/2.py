#!/usr/bin/env/python
import random
import os
global b
b = 0 
total = 0
lines = [line.rstrip('\n') for line in open('file')]

for a in lines:
    num = a
    while True:
        num = (int(num) // 3) - 2
        if num > 0:
            total = total + int(num)
        else:
            break

print(total)
