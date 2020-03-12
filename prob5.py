# (1 points) Rework #1, using a switch statement or a nested if statement (your choice) to associate each of the file types with an action.


import os
import fnmatch
from pathlib import Path
import sys




files_path = Path('testfiles/')

input_file = input("Enter a file name: ") # get the file name from the user

file = os.path.join(files_path,input_file)



if fnmatch.fnmatch(file,'*.txt'):
    try:
        os.startfile(file)
    except OSError:
        print('Could not open the file:',input_file)
        sys.exit()


elif fnmatch.fnmatch(file,'*.csv'):
    try:
        os.startfile(file)
    except OSError:
        print('Could not open the file:',input_file)
        sys.exit()


elif fnmatch.fnmatch(file,'*.mp3'):
    try:
        os.startfile(file)
    except OSError:
        print('Could not open the file:',input_file)
        sys.exit()



elif fnmatch.fnmatch(file,'*.docx'):
    try:
        os.startfile(file)
    except OSError:
        print('Could not open the file:',input_file)
        sys.exit()




else:
    print('Error')
