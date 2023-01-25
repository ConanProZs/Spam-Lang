import sys
import os
from execute import execute_line



#check stuff
try:
    file = sys.argv[1]
except IndexError:
    print("enter file:")
    file = input(">> ")

if os.stat(file).st_size == 0:
    print('warning: File empty')


#read file
on_line = 0
with open(file) as file_in:
    for line in file_in:
        on_line += 1
        ##print(line, end="")

        #error-ing
        error = execute_line(line, on_line)
        if error != None:
            if error == 0:
                print("\n")
                exit()
            else:
                print("\n")
                print("error: " + str(error))
                exit()