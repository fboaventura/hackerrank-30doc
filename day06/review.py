#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Day 06 - Review
# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input('How many lines? '))
for line in range(0, t):
    S = input(f'Line {line + 1}: ')
    size_of_S = len(S)
    even = odd = ''
    for i in range(0, size_of_S):
        if i % 2 == 0:
            even += S[i]
        else:
            odd += S[i]

    print(f'Even: {even} :.: Odd: {odd}')

