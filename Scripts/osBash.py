#Ops Challenge 06
#David Armstrong
#09-08-2020
#Run bash commands from py code

#Variables
contents = "ls"
user = "whoami"
ipinfo = "ip a"
hardware = "sudo lshw -short"

#Function
import os
def sys(var1):
    os.system(var1)

#Main
print("Here are the contents of this directory: ")
sys(contents)
print("Here is the user info: ")
sys(user)
print("Here is the ip info: ")
sys(ipinfo)
print("Here is the hardware info: ")
sys(hardware)

#End
