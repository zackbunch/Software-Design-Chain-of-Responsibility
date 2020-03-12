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


class AbstractHandler(object):

    """Parent class of all concrete handlers"""

    def __init__(self, nxt):

        """change or increase the local variable using nxt"""

        self._nxt = nxt

    def handle(self, request):

        """It calls the processRequest through given request"""

        handled = self.processRequest(request)

        """case when it is not handled"""

        if not handled:
            self._nxt.handle(request)
            print('Sequence of handlers:')
            print(self.__class__.__name__, 'does not handle this type of request')

    def processRequest(self, request):

        """throws a NotImplementedError"""

        raise NotImplementedError('First implement it !')


class DataHandler(AbstractHandler):

    """Concrete Handler # 1: Child class of AbstractHandler"""

    def processRequest(self, request):

        '''return True if request is handled '''
        if fnmatch.fnmatch(file,'*.csv'):
            try:
                os.startfile(file)
                print("{} handling request '{}'".format(self.__class__.__name__, request))
                return True
            except OSError:
                print('File not found:',input_file)
                sys.exit()



class MusicHandler(AbstractHandler):

    """Concrete Handler # 2: Child class of AbstractHandler"""

    def processRequest(self, request):

        '''return True if the request is handled'''
        if fnmatch.fnmatch(file,'*.mp3'):
            try:
                os.startfile(file)
                print("{} handling request '{}'".format(self.__class__.__name__, request))
                return True
            except OSError:
                print('File not found:',input_file)
                sys.exit()

class TextHandler(AbstractHandler):

    """Concrete Handler # 3: Child class of AbstractHandler"""

    def processRequest(self, request):

        '''return True if the request is handled'''

        if fnmatch.fnmatch(file,'*.txt'):
            try:
                os.startfile(file)
                print("{} handling request '{}'".format(self.__class__.__name__, request))
                return True
            except OSError:
                print('File not found:',input_file)
                sys.exit()


class WordHandler(AbstractHandler):

    """Concrete Handler # 3: Child class of AbstractHandler"""

    def processRequest(self, request):

        '''return True if the request is handled'''

        if fnmatch.fnmatch(file,'*.docx'):
            try:
                os.startfile(file)
                print("{} handling request '{}'".format(self.__class__.__name__, request))
                return True
            except OSError:
                print('File not found:',input_file)
                sys.exit()





class DefaultHandler(AbstractHandler):

    """Default Handler: child class from AbstractHandler"""

    def processRequest(self, request):

        """Gives the message that the request is not handled and returns true"""

        print("{} telling you that request '{}' has no handler right now.".format(self.__class__.__name__,
                                                                                          request))
        return True


class User:

    """User Class"""

    def __init__(self):

        """Provides the sequence of handles for the users"""

        initial = None

        self.handler = DataHandler(MusicHandler(TextHandler(WordHandler(DefaultHandler(initial)))))

    def agent(self, user_request):
        self.handler.handle(requests)

        """Iterates over each request and sends them to specific handles"""

        # for request in user_request:
        #     self.handler.handle(request)

"""main method"""

if __name__ == "__main__":

    """Create a client object"""
    user = User()

    """Create requests to be processed"""

    files_path = Path('testfiles/')

    input_file = input("Enter a file name: ") # get the file name from the user

    file = os.path.join(files_path,input_file)

    #string = "GeeksforGeeks"
    requests = file

    """Send the requests one by one, to handlers as per the sequence of handlers defined in the Client class"""
    user.agent(requests)
