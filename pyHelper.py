#!/usr/bin/env python3
import os
from os import listdir
from os.path import isfile, join
import random
import string
from LIB.foo_str.begApp import begApp
from LIB.foo_str.endAppWoExt import endAppWoExt
from LIB.foo_str.endAppWiExt import endAppWiExt

welcomeMsg = """
*------------------------------------------------*
|                    PyHelper                    |
*------------------------------------------------*
|                  add a string                  |
|[0] - exit                                      |
|[1] - to the beginning                          |
|[2] - to the end counting without the extension |
|[3] - to the end counting with the extension    |
*------------------------------------------------*
"""
options={
        '0': exit,
        '1': begApp,
        '2': endAppWoExt,
        '3': endAppWiExt
}

r = 0
response = "4"
while response != "0":
    if r == 0:
        response = input(welcomeMsg)


    if response not in options.keys():
        print('podaj prawidlowa opcje')
        continue
    inpC=input('is there an input, [1] - yes [o] - no n')
    inp=input('insert input')
    if inpC:
        options[response]("inp")
    else:
        options[response]()


    r = int(input('Do you want to restart[0] or quit[1]?'))

    if r == 1:
        raise SystemExit
# x = input('input?\n')

# def append(filename):
#     name, ext = os.path.splitext(filename)
#     return "{name}_{x}{ext}".format(name=name,x=x, ext=ext)

# #os.rename('a.txt', 'b.kml')
# for f in listdir(os.path.dirname(os.path.abspath(__file__))):
#     if not (f == 'pyHelper.py'):
#         os.rename(f, append(f))
#onlyfiles = [f for f in listdir(os.path.dirname(os.path.abspath(__file__)))]

#print(append_id("hello.txt"))
