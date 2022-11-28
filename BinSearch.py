#!/usr/bin/python3
household = []

def GetObj():
# This procedue reads from the input file, objectlist.text
# & populates the list household
#
     source_file = open("sortedlist.text", "r")
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
      top = len(rows)
      for i in range (0, top):
           print (rows[i])

def finder(target, rows):
    inlist = True
    found = False
    pattern = target.rstrip("\r\n")
    bottom = 0
    top = len(rows)-1
    print ("searching between ", bottom, " & ", top)
    if household[top] == pattern:
        final = top
    elif household[bottom] == pattern:
        final = bottom
    else:
        while (not found) and inlist:
              print ("now searching at position ", (bottom + top) // 2)
              inlist = False
              final = len(rows)
              print ("The pattern is not in the list")

    print ("the object is at position ", final)
household = GetObj()
DispObj(household)
target = input("what is the object that u would like to know the position of? ")
finder(target, household)