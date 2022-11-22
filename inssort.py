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

      top = len(rows)
      for i in range (0, top):
           print (rows[i])

def largest(rows, pos):
# this procedue scans the list, rows, from position 0 to position pos,
# returns the position of the largest object in the interval.

      biggest = pos
      for i in range(0, pos-1):
            print("the curr position is ", str(i))
            if rows[i] > rows[biggest]:
                biggest = i
#       print("the biggest is ", rows[i])
      return (biggest)

household = GetObj()
DispObj(household)
k = len(household)-1

# dest_file = open("sortedlist.text","w")
# dest_file.writelines("")
# dest_file = open("sortedlist.text","a")
# dest_file.close()

print ("the largest object is in position ", largest(household, k))