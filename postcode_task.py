import requests


url = "http://api.postcodes.io/postcodes/"

user_postcode = input(" Please enter your postcode ")
url_target = url + user_postcode
live_response = requests.get(url_target)

# print(response.status_code)
print(live_response)

# research how to convert this data into dictionary
# HINT - python json library/module/method can be used to resolve this

response_dict = live_response.json()
print(response_dict)
print(response_dict.keys())
# iterate through the data and print RESULTS
# print longitude and latitude (locations)

# Create a function that returns the longitude and latitude of the given postcode

