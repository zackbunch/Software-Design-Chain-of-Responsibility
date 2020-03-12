# (1 points) Rework #1, using a switch statement or a nested if statement (your choice) to associate each of the file types with an action.


import os
import fnmatch

for file_name in os.listdir('testfiles/'):
    if fnmatch.fnmatch(file_name,'*.txt'):
        print(file_name)
        os.startfile(file_name)
