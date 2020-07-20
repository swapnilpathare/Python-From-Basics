#Loops with example

## For Loop
#example 1
# How to use 'For' Loop in python to print statement 3 times
for i in range ( 3 ):
  print ( "Hello, World...!" )
# output- Hello, World...!                    
#         Hello, World...!
#         Hello, World...!

#example 2
for i in (0, 1, 2, 3, 4, 5):
  if i == 2 or i == 4:
    continue
  print(i)
# output- 0
#         1
#         3
#         5


# How to use 'While' Loop in python to print statement 3 times
# example 1
i = 1                                 #defining the variable
while i < 6:                          #while loop with condition
  print(i)                            #print statement
  i += 1                              #i++ to increment value by 1
# outout- 1
#         2

# example 2
c=2                                   #define the variable
while c==2:                           #declaring while loop with condition
    if c == 2:                        #condition to be check
        print('Hello, World...!')     #printing an output
    break                             #break keyword to break the condition
#output- Hello, World...!




