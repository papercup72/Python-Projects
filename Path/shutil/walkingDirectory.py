import os
from pathlib import Path

p = Path.home()

for folderName, subfolders, filenames in os.walk('/users/sketchmaster/documents/github/python-projects/path'):
    print('the current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')