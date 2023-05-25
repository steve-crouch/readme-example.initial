#!/usr/bin/env python3

import argparse

from mymath.factorial import factorial


parser = argparse.ArgumentParser(description='Calculate the factorial of a given number')
parser.add_argument('--number', required=True, type=int, help='Non-negative integer to calculate factorial for')
args = parser.parse_args()

print(factorial(args.number))
