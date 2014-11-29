'''Hacker Rank: Basic Calculator Problem

You are given two real numbers and your task is to print the
Addition
Subtraction
Multiplication
Divison
Integer Divison
of the two numbers in 5 separate lines. Keep a precision of two digits after decimal. 

Original problem: https://www.hackerrank.com/challenges/basic-calculator '''


import sys

lines = [[float(x) for x in line.split()] for line in sys.stdin]
a = lines[0][0]
b = lines[1][0]

sum = "{:.2f}".format(a + b, 2)
sub = "{:.2f}".format(a - b, 2)
mult = "{:.2f}".format(a * b, 2)
div = "{:.2f}".format(a // b, 2)
idiv = "{:.2f}".format(a / b, 2)

n = "\n"

print (str(sum) + n + str(sub) + n + str(mult) + n + str(idiv) + n + str(div))
