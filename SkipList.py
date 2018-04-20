import random
import math


class _SkipNode(object):
    """
    This class implements the SkipNode,
    which is used in the SkipList class.
    """
    
    def __init__(self, key = None, level = 0):
        self.key = key
        # A list that stores the next key at each level
        self.next = [None]*level
        
        
class SkipList(object):
    """
    A class that implements a Skip List
    
    Operations:
        
        insert: Inserts a key into the skip list,
            with an average time complexity of O(lgn)
            
        remove: Removes a key from the skip list,
            with an an average time complexity of O(lgn)
        
        find: Find a key within the skip list (if it
            is present) and returns it, with an average
            time complexity of O(lgn)
        
        contains: Returns a boolean value verifying if a key
            is in the skip list, with an average time complexity
            of O(lgn)
            
    Key Domain:
        
        This implementation of a skip list allows keys that can be
        compared in python (i.e. ints, strings, etc.) Note that this
        Skip List also only allows keys that are not already present
        in the list to be inserted
        
    """
    
    def __init__(self, N):
        # The maximum level of any key currently in the Skip List
        self.maxLevel = 0
        # The length of the list
        self.len = 0
        # The head node, which initializes the skip list
        self.head = _SkipNode()
        # The expected number of objects to be stored
        self.N = N
        # The upper bound on levels allowed in the Skip List
        self.levelCap = math.ceil(math.log(N,2))
    

    def __len__(self):
        """
        Objective: Return the length of the Skip List
        
        Parameters: None
        
        Output: Length of the Skip List
        
        """
        return self.len
    
    def updateList(self, key):
        """
        Objective: Creates an update list, which is central
            to all operations on a Skip List. The update list
            is a list of the largest key less than the input key
            on all levels of the Skip List. This operation has an
            average time complexity of O(lgn), which is the central
            component to the scaling of the other operations.
        
        Parameters: 
            Key - The key that the update list is being made
            around.
        
        Output: A list of length = the number of levels currently in 
            the Skip List (self.maxLevel), with each element being a key.

        """
        # Create a blank list, whose length is the
        # number of levels in the key
        update = [None]*self.maxLevel
        x = self.head
        
        for i in reversed(range(self.maxLevel)):
            # Find the largest value that is less than
            # the key on level i
            while x.next[i] != None and x.next[i].key < key:
                x = x.next[i]
            # add the key to the update list and move to the
            # next level down
            update[i] = x
        return update
    
    def insert(self, key):
        """
        Objective: Insert a key into the Skip List. An update
            list is made ( O(lgn) ) to determine the correct
            location for the key. A new node is created for the
            key (with a random level) and the next lists of all keys
            in the update list are updated with the new key, while
            the new key recieves its next list from all keys in the
            update list.
            
        
        Parameters:
            key - The key to be inserted
        
        Output: Returns nothing but inserts the key into the Skip List
        
        """
        # Creates a node object for the new key,
        # using the randomHeight() function
        node = _SkipNode(key = key, level = self.randomHeight())
    
        #updates the maxLevel if the new node has a higher level
        self.maxLevel = max(self.maxLevel, len(node.next))
        # and makes the head.next list the correct length
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(key)  
        # Ensure that the key is not already in the list
        if self.find(key, update) == None:
            #Fills the next list of our new key
            # with the appropriate keys from the update list 
            # and replaces each next with our new key,
            # essentially inserting our new key in between
            # the keys
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
                
            # updates the length of the skip list
            self.len += 1
    
    # Creates the number of levels for a given node, 
    # adding a level each succesful coin flip (with 
    # probaility 0.5) and stopping after a failure
    # or when the levelCap is reached.
    def randomHeight(self):
        """
        Objective: Randomally choose a height for a new node.
            Coin flips (with probability 0.5) are performed and 
            each succesful flip adds a level, stopping at a 
            unsuccesful flip or when the self.levelCap is reached
        
        Parameters: 
            None
        
        Output: A height (int) between 1 and the self.levelCap
        
        """
        height = 1
        while random.random() < .5 and height != self.levelCap:
            height += 1
        return height
            
    def remove(self, key):
        """
        Objective: Remove a key from the skip list. An update list 
            is created, and all keys whose next list contains the 
            removed key have that element replaced by the appropriate
            key from the next list of the removed key
        
        Parameters:
            key - The key to be removed
        
        Output: Returns nothing but removes the key from the Skip List
        
        """

        update = self.updateList(key)
        # find the key
        x = self.find(key, update)
        if x != None:
            # Replace all next keys from the update
            # list with next key from the removed key
            for i in reversed(range(len(x.next))):
                update[i].next[i] = x.next[i]
                #If the removed key was the only key on a
                # level, delete the level
                if self.head.next[i] == None:
                    self.maxLevel -= 1
            # updates the length
            self.len -= 1  
            
    def find(self, key, update = None):
        """
        Objective: Find a given key in the Skip List.
            Create an update list. If the key is present,
            it will be the next key of the lowest key in
            the update list.
        
        Parameters:
            Key - the key to be found
            
            Update - an update list, if None is 
            specified, an update list will be created
        
        Output: Return the key (if it is present) and None
            if not
        
        """
        
        if update == None:
            update = self.updateList(key)
            
        if len(update) > 0:
            # Update[0] is the largest element
            # smaller than the key, so if the key
            # is in the list, it will be the next element
            candidate = update[0].next[0]
            if candidate != None and candidate.key == key:
                return candidate
            
        return None
    
    def contains(self, key, update = None):
        """
        Objective:  Determine if a key is present in the Skip List 
            by running the self.find() function.
            If no update list is provided, the time complexity
            will be on average O(lgn)
        
        Parameters: 
            Key - the key in focus
            
            Update - an update list, if None is 
            specified, an update list will be created.
        
        Output: A boolean value, True if the key is present and 
            False if not
        
        """
        return self.find(key, update) != None
            
    def displayList(self):
        """
        Objective: Print the Skip List in an 
            easy to understand format
        
        Parameters: 
            None
        
        Output: Prints each level of the skip list
            with the keys that are in that level
        
        """
        print("\nSkip List")
        head = self.head
        for lvl in range(self.maxLevel):
            print("Level {}: ".format(lvl), end=" ")
            node = head.next[lvl]
            while(node != None):
                print(node.key, end=" ")
                node = node.next[lvl]
            print("")