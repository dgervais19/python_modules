# Let's have a look at some built in functions in python

# import is the key word we use to call modules from Python library

# first Iteration
import random  # Use the syntax... "print(random.random())" because you need to declare the class

# Second iteration
from random import random
# use print(random()).... because the class is already called in the "from"
import math
# We have random method in python library which we use by importing

print(random.random())
# It generates float number between 0-1

num_float = 23.44
print(" Floor method rounds the figure to lower end")
print(math.floor(num_float))

print(" ceil() method rounds the figure to higher end of the value")
print(math.ceil(num_float))

Task
num2_float = float(input("please enter a float number "))
if (num2_float % 1) < .50:
    print(math.floor(num2_float))
else:
    print(math.ceil(num2_float))


import os
# To find out the system configuration or system related information
# Based on the information provided we can handle the user request
import math, datetime, sys

working_dir = os.getcwd()

print(working_dir)

# Lets find out the name of our ps
# only available in linux
print(os.uname())

# Lets count the number of cpus

print(os.cpu_count())
# os.cpu_count() gives us the total number of cpus in our system/OS

print(datetime.datetime.today())
# datetime module gives us the ability to find the current date and time etc.

# To find our system path

print(sys.path)

