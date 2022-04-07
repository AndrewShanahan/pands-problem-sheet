# Author: Andrew Shanahan
# Task: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root
# Reference 1: https://www.w3schools.com/python/python_functions.asp
# Reference 2: https://en.wikipedia.org/wiki/Newton%27s_method#Square_root_of_a_number
# Reference 3: https://stackoverflow.com/questions/1623375/writing-your-own-square-root-function
def sqrt(t):
  # r = t/2.0; t = float(t)
    i = 0
    while i &lt; 10:
            r = (r+t/r)/2.0
            i += 1