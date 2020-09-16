#Challenge 12
#David Armstrong
#09-15-2020
#Using Psutil

import psutil

#Variables
#Format for retrieving cpu details
cpt = psutil.cpu_times()

#Main
#Time spent by normal processes executing in user mode
cpt[0]
#Time spent by processes executing in kernel mode
cpt[2]
#Time when system was idle
cpt[3]
#Time spent by priority processes executing in user mode
cpt[1]
#Time spent waiting for I/O to complete.
cpt[4]
#Time spent for servicing hardware interrupts
cpt[5]
#Time spent for servicing software interrupts
cpt[6]
#Time spent by other operating systems running in a virtualized environment
cpt[8]
#Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
cpt[9]

#End
