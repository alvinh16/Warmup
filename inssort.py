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
      # clear the file from prev write
      dest_file = open("sortedlist.text","w")
      top = len(rows)
      for i in range (0, top):
           dest_file.write(rows[i])
           dest_file.write("\r\n")
           print (rows[i])
      dest_file.close()
def largest(rows, pos):
# this procedue scans the list, rows, from position 0 to position pos,
# returns the position of the largest object in the interval.
      biggest = pos
      for i in range(0, pos-1):
            if rows[i] > rows[biggest]:
                biggest = i
#                print ("The biggest object is now ", rows[biggest])
      print("the biggest is ", rows[biggest])
      return (biggest)

def swappos(rows, src, dest):
# This procedure swaps the position of 2 objects
# & returns the list with the 2 objects swapped
       tmpobj = rows[src]
       rows[src] = rows[dest]
       rows[dest] = tmpobj

def outerloop(toplist):
# this procedure executes the outer loop in searching for the largest object
# at the end of ea iteration, the largest obj will b at the top of the list

       countdown = toplist
       while countdown > 1:
            bignum = largest(household, countdown)
            print("The largest number is", bignum)
            if household[bignum] > household[countdown]:
                swappos(household, countdown, bignum)
            countdown -= 1

household = GetObj()
# DispObj(household)

k = len(household)-1
outerloop(k)
DispObj(household)
# bignum = largest(household, k)
# swappos(household, k, bignum)

