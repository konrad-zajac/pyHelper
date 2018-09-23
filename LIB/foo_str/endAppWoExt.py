import os
from os import listdir

def endAppWoExt():

    x = input('input?\n')

    def append(filename):
        name, ext = os.path.splitext(filename)
        return "{name}{x}{ext}".format(name=name,x=x, ext=ext)


    for f in listdir(os.path.dirname(os.path.abspath(__file__))):
        if (f != 'pyHelper.py') and (f != 'LIB'):
            os.rename(f, append(f))
