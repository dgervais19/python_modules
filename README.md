# This lesson covers Python Modules

- Built in functions
- Python Library
- What is pip and how do we use it
- APIs with python
- Built in functions help us accelerate our development of software

### Using built in functions from python library

```
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
```













## What is pip?
* Package manager for python and helps us install external packages such as requests

* syntax: pip install name_of_the_package

### APIs with python
```
# importing requests to make an api call to www

import requests
from emoji import emojize

response = requests.get("https://www.bbc.co.uk/")

# it provides an integer as a response code

print(response.headers)
print(type(response.content))


# first iteration
if response.status_code == 200:
    print(" mission successful !! " + str(response.status_code))
    print(emojize((":thumbs_up:")))
elif response.status_code == 404:
    print(" the site is unavailable until further notice please contact your provider: ")
else:
    print("OOPs something went wrong please try later")

# Second Iteration

def check_response_code():
    if response.status_code == 200:
        print(" mission successful !! " + str(response.status_code))
        print(emojize(":thumbs_up:"))
    elif response.status_code == 404:
        print(" the site is unavailable until further notice please contact your provider: ")
    else:
        print("OOPs something went wrong please try later")

check_response_code()

# Third Iteration
# What does requests module bring to the table
# It gives us the boolean value of the success of the code.

def check_response_code():
    if response.status_code:  # This means we would not have to give the condition response.status_code == 200
        print(" mission successful !! " + str(response.status_code))
        print(emojize(":thumbs_up:"))
    elif response.status_code:
        print(" the site is unavailable until further notice please contact your provider: ")
    else:
        print("OOPs something went wrong please try later")

check_response_code()

# It will evaluate to True if the status code was between 200 - 400, otherwise False

```
## What is CRUD 

![](CRUD.png)

## Json basics
* Java script object notation
* use cases - browser data
* data is in key value pairs
* Json encoding from a Dictionary
* Json decoding into a dictionary
* Handling/creating files with python
* writing to file
* reading from file