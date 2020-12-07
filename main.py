#python runs from .py files

#yes. "#" is the thing to use for comments
#no multi line so just use "#" line 
#python runs from top

x = 10   # variable name = value
y = "yes" #you don't have to specify the type or use semicolon

o1 = True #btw, no assigning names that start with numbers

#print to print. discuss printf later
print(x)
print(y)
print(o1)

#______________________________________________________
# importing other files 
import end 
# use as keyword to change the name when calling it
#import end as e
#e.function() 
#note: importing automatically runs all the code from that file
#if end hypothetically had a function, you can call it like in java. example: end.run() 

#_______________________________________________________
#four common built-in types:
#btw use this below to figure out class
type(o1)
print(type(o1))
print()


#confusing python modules stuff. from ____(module name) import ______(files names). The module must contain __init__.py to run
from types1 import num, boo, string    
from structures1 import datastructure
import input
import statements
from functions1 import all


