#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""
Day 3: Intro to Conditional Statements.
"""

def main():
    if N in range(1, 101):
        if N % 2 == 1:
            print('Weird')
        else:
            if N in range(2,6) or N > 20:
                print('Not Weird')
            else:
                print('Weird')
    else:
        print('Wrong Number')


# Main body
if __name__ == '__main__':
    N = int(input())
    main()
