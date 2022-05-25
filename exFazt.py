# Important items viewed in Python Course for beginners

'''Datatypes:
  Strings
  Numbers:
    Integers
    Floats 
  Lists ()
  Tuples []
  Dictionaries { key:value }
  Sets {}
Variables =
Conditionals if, else, elif, and, or, not
Functions def()
Loops: While, For in, continue - break
Modules'''

#python modoules

import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=180000))

from datetime import timedelta, date
print(timedelta(minutes=1000), date.today())

#own modules

def add(n1, n2):
    print(n1 + n2)

def substract(n1, n2):
    print(n1 - n2)

import fileName #the modules are in other location, especific file names for import it

#first way
fileName.add(54,8)
fileName.substrac(52,4)

from fileName import add, substract

substract(52,5)
add(58,52)

#third modules (internet) console
# https://pypi.org/ website with modules

pip install colorama #module name for show color in console

import colorama

from colorama import Fore, Style
init(convert=True) #necessary for windows console
print(Fore.RED + "Text background colored")

#recommended modules (frameworks), django, (pymodule) tkinder


