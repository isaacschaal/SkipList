### Example ###

from SkipList import *

## Insert Keys

# Create a Skip List with N set to the 
# desired number of elements to be stored
a = SkipList(20)
lis = list(range(20, 0,-1))
for key in lis:
    a.insert(key)   
a.displayList()

## Check if a key is present
print ("\nDoes the list contain 3?", a.contains(3))

## Remove a key
a.remove(3)
a.displayList()
print ("\nDoes the list contain 3?", a.contains(3))

## Return the length of the skip list
print ("\nThe length of the skip list is :", len(a))

