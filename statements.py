#if statements
if 1>2:
  #remember to indent
  x = 1
  #you must put something inside. you can't have a empty if, else, or elif block
if 1>2:
  #else
  x = 1
else:
  x = 1
  #else

if 1>2:
  x = 1
elif 1<2:
  y = 2
else:
  z = 1


#if [a condition]:
  #code to execute(at least one line of executable code)

#while

#while [condition]:
  #at least one line of executable code
#[else: "runs this code once after while loop finishes"]
i = 1
print("looping:")
while i<=5:
  print(i)
  i +=1
else:
  print("done")

#for loops
#for each:
print("for each loop:")
one_three = (1,2,3);
for i in one_three:
  print(i)
#use in keyword. 
print("for loop:")
#normal for loop uses range() 
for x in range(2,10,2):
  print(x)
#range(start, stop, steps)
#similar to java (int i = 2;i<=10;i+=2)

#you can't have a blank for loop so use pass if you need a loop to do nothing
for x in range(1,3):
  pass

  