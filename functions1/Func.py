#how to create function:
def my_function():
  print("hello")

my_function() #this is how to call it

def my_args(arg):
  print(arg)

my_args("hello 2")

def unknown_args(*say): #unknown number of arguements
  print(list(say))

unknown_args("hi ", "hello ", "bruh ")

def two_args(one, two):
  print("one: ", end = " ")
  print(one)
  print("two: ", end = " ")
  print(two)

two_args(two = "helo", one = " ello") #order of arguement doesn't matter if you do this

#use ** instead of * for unknown key value pairs (kwargs)


def say_something(word = "hello"): #default value setting
  print(word)

def return_word(): #this is how to return something
  return "word"
print(return_word)
#function block can't be empty so use pass to indicate no content

def say_string(word:str = "hello")->str: #this is how to introduce type hints. python ignores this but it's useful for coders to read
  print(word)