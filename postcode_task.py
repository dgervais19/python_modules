import requests

url = "http://api.postcodes.io/postcodes/"  # Assign the string of the website


# FIRST ITERATION
# user_postcode = input(" Please enter your postcode ")
# url_target = url + user_postcode
# live_response = requests.get(url_target)
#
# # print(response.status_code)
# print(live_response)
#
# # research how to convert this data into dictionary
# # HINT - python json library/module/method can be used to resolve this
#
# response_dict = live_response.json()
# # print(response_dict)
# # print(response_dict.keys())
# # iterate through the data and print RESULTS
# response_dict_result = response_dict["result"]
# print(response_dict_result)
# # print longitude and latitude (locations)
# print(response_dict_result["longitude"])
# print(response_dict_result["latitude"])
# Create a function that returns the longitude and latitude of the given postcode

# SECOND ITERATION
# Create a function
def long_and_lat():
    # Prompt the user to input the post code
    user_postcode = input(" Please enter your postcode ")
    url_target = url + user_postcode  # This adds the URL and inputted postcode to the variable 'url_target'
    live_response = requests.get(url_target)  # Request for the data passed through url_targets

    # Check to see if the page exists
    if live_response.status_code == 200:   # If the page exists,
        response_dict = live_response.json()  # converts the live_response from bytes to dictionary
        response_dict_result = response_dict["result"]
        # Assigns the results key in the newly converted dictionary to a variable
        print("The longitude is " + str(response_dict_result["longitude"])) # Print Longitude
        print("The latitude is " + str(response_dict_result["latitude"])) # Print Latitude
    elif live_response.status_code == 404: # Print "page not found" if the page doesnt exist
        print("Sorry, post code not found")
    else:
        print("Something went wrong, please try again")


long_and_lat()
