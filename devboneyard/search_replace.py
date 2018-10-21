# Useful to replace text in all source files recursively

import os, fnmatch

def findReplace(directory, find, replace, filePattern="*.py"):
    """
    Used to make updates to strings across codebase.

    :param directory: relative directory path to find stuff
    :param find: string to search for recursively
    :param replace: string to replace with
    :param filePattern: a pattern using gnmatch.filter with some form of glob
                        support, *.py works fine
    """
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)


findReplace(".", "import gtk", ".", "*.py")
