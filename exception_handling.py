# We will have a look at the practical use cases and implementation of try, except, raise and finally

# we will create a variable to store a file data using open()

try: # let's use try block for a 1 line code where we know this will throw an error
    file = open("orders.text")
except:
    print(" PANIC ALERT!!! ")


# Iteration 2
try:
    file = open("orders.text")
except FileNotFoundError as errmsg: # creating an alias for FileNotFound Error in except block
    print("Please create a file first" + str(errmsg))
# if we still wanted them to see the actual exception together with our customised message
    raise # raise will send back the actual exception

finally: # finally will execute regardless of the above conditions
    print("Hope you had a good customer experience, please visit again soon!")
