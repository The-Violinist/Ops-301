#!/bin/bash
# Script Name: Ops Challenge 03
# Author: David Armstrong
# Date of last revision: 09-02-2020
# Description of purpose: Change file permissions

# Variables
i=1
xyz=1
num1=0
num2=0
num3=0

# Functions
# Create the files to change permissions
function create_files(){
until [ $i -gt 10 ]
do
	cp $0 /home/osboxes/bin/permissions/test_file$i
	((i++))
done
}

# yes or no
function ask_user (){
	read -p "Would you like to add another option? Y/N: " yes_or_no
	if [ $yes_or_no = "Y" ] || [ $yes_or_no = "y" ]
	then
		xyz=1
    else
		xyz=100
   	fi
}

# Types of permissions
function questions(){
echo "Press 1 if you would like to give permission to read."
echo "Press 2 if you would like to give permission to write."
echo "Press 3 if you would like to give permission to execute."
}

# Permission options
function permissions(){
until [ $xyz == 100 ]
do
questions
read user_input
	if [ $user_input == 1 ]
	then
		#Read only
		num1=4
	elif [ $user_input == 2 ]
	then	
		#Write only
		num2=2
	else [ $user_input == 3 ]
		#Execute only
  		num3=1
	fi

ask_user
done
}
# Main
create_files
read -p "Please enter the path directory to alter user permissions" path
permissions
user=$((($num1 + $num2 + $num3) * 100))

# chmod number
mod_num=$(($user + 77))

chmod -R $mod_num $path
ls -l $path
# End
