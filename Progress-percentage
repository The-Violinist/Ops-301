#!/bin/bash

# Variables
counter=0

# File to copy
input='/var/log/syslog'

# Functions

# Count number of lines in file
function lines(){
wc -l $input | awk '{print $1}'
}

# Main

# Assign number of lines to variable
line_num=$(lines)

# Copy file line by line and show progress
while IFS= read -r line
do
  echo "$line" >> syslog_copy
  counter=$((counter+1))
  #Divide number of lines copied by total lines
  echo $((100 * $counter/$line_num))%
  sleep .0005
  done < "$input"
  
# End
