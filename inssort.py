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

def DispObj(rows):
# This procedure dumps the content of rows on the screen

      i=0
      while i < len(rows):
           print (rows[i])
           i += 1

def largest(rows, pos):
# this procedue scans the list, rows, from position 0 to position pos,
# returns the position of the largest object in the interval.

      for i in range(0, pos):
           print (str(i))

household = GetObj()
DispObj(household)

k = len(household) - 1
largest(household, k)