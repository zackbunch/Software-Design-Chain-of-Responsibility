# (4 points) Implement a Chain of Responsibility-based program that does the following:
# Accepts the name of a file.
# Does one of the following actions:
# Identifies the file's type as known, based on its extension, then
# uses the associated utility to open the file,
# displays an error message if the open fails
# Displays an error message, noting that the file type isn't recognized.

import os
import fnmatch
from pathlib import Path
import sys
import  abc

class Handler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self.successor = successor

        @abc.abstractmethod
        def handle_request(self):
            pass




class DataHandler(Handler):
    def handle_request(self):
        if fnmatch.fnmatch(file,'*.csv'):
            os.startfile(file)
            print("{} handling request '{}'".format(self.__class__.__name__, input_file))



        elif self.successor is not None:
            print("{} passing request '{}'".format(self.__class__.__name__, input_file))
            self.successor.handle_request()


class DocumentHandler(Handler):
    def handle_request(self):
        if fnmatch.fnmatch(file,'*.pdf'):
            os.startfile(file)
            print("{} handling request '{}'".format(self.__class__.__name__, input_file))



        elif self.successor is not None:
            print("{} passing request '{}'".format(self.__class__.__name__, input_file))
            self.successor.handle_request()

class MusicHandler(Handler):

    def handle_request(self):
        if fnmatch.fnmatch(file,'*.mp3'):
            os.startfile(file)
            print("{} handling request '{}'".format(self.__class__.__name__, input_file))



        elif self.successor is not None:
            print("{} passing request '{}'".format(self.__class__.__name__, input_file))
            self.successor.handle_request()

class MusicHandler2(Handler):
    def handle_request(self):
        if fnmatch.fnmatch(file,'*.mp3'):
            os.startfile(file)
            print("{} handling request '{}'".format(self.__class__.__name__, input_file))


        elif self.successor is not None:
            print("{} passing request up '{}'".format(self.__class__.__name__, input_file))
            self.successor.handle_request()

def main():



    music_handler2 = MusicHandler2()
    music_handler = MusicHandler(music_handler2)
    document_handler = DocumentHandler(music_handler)
    data_handler = DataHandler(document_handler).handle_request()







if __name__ == "__main__":
    files_path = Path('testfiles/')

    input_file = input("Enter a file name: ") # get the file name from the user

    file = os.path.join(files_path,input_file)
    #
    main()
