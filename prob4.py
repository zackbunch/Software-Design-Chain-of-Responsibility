
import os
import fnmatch
from pathlib import Path
import sys

    # if fnmatch.fnmatch(file,'*.csv'):
    #     try:
    #         os.startfile(file)

#
# input_file = input("Enter a file name: ") # get the file name from the user
#


files_path = Path('testfiles/')
file = input('Enter a file name:')
full_path = os.path.join(files_path,file)
file_extension = file.split('.')
extension = str(file_extension[-1])



def DataHandler():
    print('Data Handler')
    try:
        os.startfile(full_path)
    except OSError:
        print('File not found:',file)
        sys.exit()



def MusicHandler():
    print('Music Handler')
    try:
        os.startfile(full_path)
    except OSError:
        print('File not found:',file)
        sys.exit()

def PDFHandler():
    print('PDF Handler')
    try:
        os.startfile(full_path)
    except OSError:
        print('File not found:',file)
        sys.exit()

def WordHandler():
    print('In PDF handler')
    try:
        os.startfile(full_path)
    except OSError:
        print('File not found:',file)
        sys.exit()

extensions = {
    'csv': DataHandler,
    'mp3': MusicHandler,
    'pdf': PDFHandler,
    'docx': WordHandler
}





if extension in extensions:
    extensions[extension]()
else:
    print(f'ERROR: {extension} is not a valid extension.')
