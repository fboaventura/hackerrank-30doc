#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""
Solve day2 of 30 days of code challenge.
"""


def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    meal_cost += tip + tax
    return meal_cost


def main():
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    print(int(round(solve(meal_cost, tip_percent, tax_percent))))


# Main body
if __name__ == '__main__':
    main()
