string = "xd"
String = 'xd' #strings can be created these two ways
print("String Tests 1: ")
print("\t"+string) 
print("\t" + String)
print(bool("")) 
print(bool("a")) 
print(bool(' '))#using strings in bool: a blank string will return false. anything else will be true. note that a space counts as not blank

string = "stringarray"
print(string[0]) #you can get characters from a string like an array. it's also zero based
print(string[-1]) #arrays also use negative symbol to get the reverse. this should print y(it's not zero based)
print(string[0:3])#introducing string slicing. this prints from index 0 to 3
#[start:stop:step] <this is how it works. kinda like a for loop. it has a start and stop index. the step represents how much to go by
print(string[::3]) # also stops itself from going outOfBounds
#leaving parts blank will default it:
#[0:string.lenght()-1:1]


#type cast:
x = str(1) 