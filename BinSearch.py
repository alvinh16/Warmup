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
# you might get lucky & the target object might b at the top or bottom of the list
    if household[top] == pattern:
        final = top
    elif household[bottom] == pattern:
        final = bottom
    else:
        while (not found) and inlist:
              final = (bottom + top) // 2
              if (top == bottom+1) and (household [top]  != pattern or household[bottom] != pattern):
                  inlist = False
                  final = len(rows)
              elif household[final] == pattern :
                  found = True
              elif household[final] < pattern:
                  bottom = final
                  final = (bottom + top) // 2
              elif household[final] > pattern:
                  top = final
                  final = (bottom + top) // 2
              print ("the test position is currently", final)

    if final < len(rows):
        print ("the object is at position ", final)
    else:
        print ("The pattern is not in the list")


household = GetObj()
DispObj(household)
target = input("what is the object that u would like to know the position of? ")
finder(target, household)