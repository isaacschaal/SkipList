# SkipList
Python Implementation of a Skip List

# Overview

This python package implements a Skip List, which was first concieved of by William Pugh in 1989. A skip list is a probabilistic data structure which maintains a sorted list. They central feature is that it supports a seach operatin with an average of O(lgn) time comlexity. It does this by creating multiple levels of the list, where all keys are present on the bottom level and a key is represented the next levels with a certain probabilty. When searching for a key, it starts at the higest level and finds the key the largest key that is smaller than the key being searched for. It then drops a level and repeats the process, untill it gets to the bottom level. As there are fewer keys on higher levels, it essentially skips keys as it progresses across, hence the name. At the bottom level, if the searched for key is in the list, it will be to one position right of the largest key smaller than it (as it is as sorted list).

## Operations

The skip list supports several operations.

### Insert 
A key can be inserted into the skip list with an average case time complexity of O(lgn).

### Delete
A key can be deleted from the skip list with an average case time complexity of O(lgn).

### Find
A key can be found in the skip list (if it is present) with an average case time complexity of O(lgn).

## Example

An example of a skip list is displayed below (initiated with N = 20):

Skip List

Level 0:  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

Level 1:  3 4 5 10 13 15 16 19 20 

Level 2:  5 10 

Level 3:  5 10 

The keys 1-20 have been inserted into the Skip List. Imagine we wish to see if the key 15 is in the skip list. If we had an ordinary list (represented by the level 0), we would have to check each element in the list (with a time complexity of O(n)). In this specific example, we would make 15 checks before we find the key 15.

With our skip list, we would start on level 3, check 5 and 10 and see that 10 is the largest element smaller than 15. We move down two level 2, start at 10, and see that it is the largest element smaller than 15. We move down to level 1, start at 10, move to 13 and see that it is the largest element smaller than 15. We then move down to level 0, start at 13, move to 14, and see that it is the largest element smaller than 15. Thus if 15 is in the list, it will be one position to the right of 14. It is, and we have a succesful search. Overall, we made 7 checks to find if 15 was in the list.

## Analysis

There are two important aspects of the skip list that make the implementation function. Firstly, each element inserted into the Skip List is a node ( a `_SkipNode`) which contains the key and a list, called `next`. This list contains the next element after the key on each level that the key is present on. When a key is inserted or deleted, the appropriate next lists are updated.  

This is done by creating an update list. This is the central function of the Skip List, as the other operations depend on it and it creates the average case time complexity of O(lgn). 


# Implementation 

This implementation uses p = 0.5 as the probability that a key with level i will have a level i+1. It requires the packages `random` and `math` to run. The key domain is any object that can be compared in python. A key can only be inserted if it is not presently in the Skip List. When creating a Skip List, specify N as the expected number of items to be stored in the skip list. This will set the level capacity (highest level a key can have) as the ceiling of log_2 (N). More or fewer keys than N may be inserted, but the operations will not be optimized.


Inspired by:

Pugh, William. Skip lists: a probabilistic alternative to balanced trees. In: Communications of the ACM, June 1990, 33(6)668-676.


# Getting Started

Follow example.py for an example of functionality.

## Prerequisite
`import random
import math`

# Authors
Isaac Schaal

# License
This project is licensed under the MIT License - see the LICENSE.txt file for details
