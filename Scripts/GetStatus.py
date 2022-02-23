#Challenge 13
#David Armstrong
#09-17-2020
#Using requests to retrieve information

import requests

#Variables

#Ask user for a web address
address = input("Please enter an address: ")
#Attach protocol to the beginning
address = "http://" + address
#Ask user for a reuest method
method = input("Please enter a method: ")
#place the request into a variable
if method == "get":
    fullrequest = requests.get(address)

#Main
print("You are about to request a status code for the requested webpage. \n Would you like to continue?\n")
#Assign input to a variable
yes_no = input()

#print(fullrequest.content)
if yes_no == "yes" or yes_no == "y":
    print(fullrequest)
else:
    print("")
#Set variable for status code
statcode = fullrequest.status_code
#Print human readable code response
if statcode == 200:
    print("Successful Connection!")
elif statcode == 404:
    print("Page not found")
else:
    print("I don't know that code")

y = fullrequest.headers
print(y)
