# (4 points) Implement a Chain of Responsibility-based program that does the following:
# Accepts the name of a file.
# Does one of the following actions:
# Identifies the file's type as known, based on its extension, then
# uses the associated utility to open the file,
# displays an error message if the open fails
# Displays an error message, noting that the file type isn't recognized.

filename = input("Enter a file name: ")

from pathlib import Path

entries = Path('testfiles/')

for entry in entries.iterdir():
    print(entry.name)
