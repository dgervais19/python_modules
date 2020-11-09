# importing requests to make an api call to www

import requests
from emoji import emojize

response = requests.get("https://www.bbc.co.uk/")

# it provides an integer as a response code

print(response.headers)
print(type(response.content))


# first iteration
# if response.status_code == 200:
#     print(" mission successful !! " + str(response.status_code))
#     print(emojize((":thumbs_up:")))
# elif response.status_code == 404:
#     print(" the site is unavailable until further notice please contact your provider: ")
# else:
#     print("OOPs something went wrong please try later")

# Second Iteration

# def check_response_code():
#     if response.status_code == 200:
#         print(" mission successful !! " + str(response.status_code))
#         print(emojize(":thumbs_up:"))
#     elif response.status_code == 404:
#         print(" the site is unavailable until further notice please contact your provider: ")
#     else:
#         print("OOPs something went wrong please try later")
#
# check_response_code()

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
#