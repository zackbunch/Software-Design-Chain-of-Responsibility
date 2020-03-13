
import os
import fnmatch
from pathlib import Path
import sys

    # if fnmatch.fnmatch(file,'*.csv'):
    #     try:
    #         os.startfile(file)
# files_path = Path('testfiles/')
#
# input_file = input("Enter a file name: ") # get the file name from the user
#
# file = os.path.join(files_path,input_file)


file = input('Enter a file name:')
file_extension = file.split('.')
extension = str(file_extension[-1])



def DataHandler():
    print('Data Handler')
    os.startfile('testfiles\data.csv')


def MusicHandler():
    print('Music Handler')
    os.startfile('testfiles\musicfile.mp3')

def PDFHandler():
    print('PDF Handler')
    os.startfile('testfiles\document.pdf')

def WordHandler():
    print('In PDF handler')
    os.startfile('testfiles\word.docx')

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
