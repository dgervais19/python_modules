# Let's have a look at some built in functions in python

# import is the key word we use to call modules from Python library

# first Iteration
import random
import math
# We have random method in python library which we use by importing

print(random.random())
# # It generates float number between 0-1
#
# num_float = 23.44
# print(" Floor method rounds the figure to lower end")
# print(math.floor(num_float))
#
# print(" ceil() method rounds the figure to higher end of the value")
# print(math.ceil(num_float))

# Task
num2_float = float(input("please enter a float number "))
if (num2_float % 1) < .50:
    print(math.floor(num2_float))
else:
    print(math.ceil(num2_float))