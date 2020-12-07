#dictionary
#python equivalent of java-hashmaps
#a structure that stores keys that direct to values

user_dict = {1:"Bob", 2:"Joe"}; #how looks
print(user_dict[1]) #how to call
user_dict[3] = "Bobby" # how to assign

whole_list = user_dict.items() #creates a list from pairs
print(whole_list);
whole_list = list(user_dict.items())
print(whole_list) #casting to list makes it look nicer

# .keys() get keys. .values() get values
user_dict.pop(3) #removes key and value pair