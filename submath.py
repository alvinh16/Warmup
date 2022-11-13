#!/usr/bin/python3

import math

def mysteryop(n):

     return(math.sqrt(n))

p = input("please enter a square number ")
print("The square root of ", str(p), " is ", str( float(mysteryop(float(p)))))
