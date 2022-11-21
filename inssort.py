#!/usr/bin/python3
#
# This program uses an index sort method
# to put an randomly ordered list into a sorted 
#

household = []

def GetObj():
# This procedue reads from the input file, objectlist.text
# & populates the list household
#
     source_file = open("objectlist.text", "r")
     Organize = source_file.readlines()
     i=0
     for words in Organize :
          household.append(words.rstrip("\r\n"))
          i += 1

     source_file.close()
     return(household)

household = GetObj()
