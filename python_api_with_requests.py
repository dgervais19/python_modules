# importing requests to make an api call to www

import requests
from emoji import emojize

response = requests.get("https://www.bbc.co.uk/")

# it provides an integer as a response code

if response.status_code == 200:
    print(" mission successful !! " + str(response.status_code))
    print(emojize((":thumbs_ up:")))
else:
    print("OOPs something went wrong please try later")

