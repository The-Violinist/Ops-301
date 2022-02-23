#challenge11
#David Armstrong
#09-14-2020
#Using File commands
import os

#Variables
#Write, Append, and Read a file
file_w = open("challenge11.txt", "w")
file_a = open("challenge11.txt", "a")
file_r = open("challenge11.txt", "r")

#Write then append lines to file
file_w.write("Well\n")
file_a.write("Hello\n")
file_a.write("There\n")

#Reset object index to beginning
file_w.seek(0)

#Print one line of the file
print(file_r.readline())
#Close all instances of the opened file
file_r.close()
file_a.close()
file_w.close()

#Remove the file
os.remove("challenge11.txt")
#End
