#!/usr/bin/env python3

# Author: Mitch Gregoris
# Author ID: 133349191
# Date Created: 2023-09-25

import sys

if(len(sys.argv) > 1):
    timer = int(sys.argv[1])
    while(timer != 0):
     print(timer)
     timer = timer - 1  
else:
    timer = 3
    while(timer != 0):
     print(timer)
     timer = timer - 1
print("blast off!")  





#while(timer != 0):
#    print(timer)
#    timer = timer - 1
#print("blast off!")    
