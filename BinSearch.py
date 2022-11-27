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
#       dest_file = open("sortedlist.text","w")
      top = len(rows)
      for i in range (0, top):
 #          dest_file.write(rows[i])
 #          dest_file.write("\r\n")
           print (rows[i])
 #     dest_file.close()

household = GetObj()
DispObj(household)