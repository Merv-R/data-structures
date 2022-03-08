# -*- coding: utf-8 -*-

# Hash maps are implemented under the hood by python while using dict
# We make an implementation ourselves to understand how dic in python works
# The collision handling method used here is Chaining (Linked List) which is implemented using a list of tuples

# Look up time for a value in a hash map is O(1)
# Insertion/Deletion takes O(n) time

class Hashmap:
    # Initializing an array of size 100 for values to be stored
    def __init__(self):
        # self.valarr=[0 for i in range(100)]
        self.valarr=[ [] for i in range(10)]
    
    def hash_func(self,key):
        hashval=0
        for letter in key:
            hashval+=ord(letter)
        return hashval%10
    
    def __setitem__(self,key,val):
        i=self.hash_func(key)
        found=False
        for ind, item in enumerate(self.valarr[i]):
            if item[0]==key:
                self.valarr[i][ind]=(key,val)
                found=True
                break
        if not found:
            self.valarr[i].append((key,val))
    
    def __getitem__(self,key):
        i=self.hash_func(key)
        for item in self.valarr[i]:
            if item[0]==key:
                return item[1]
    
    def __delitem__(self,key):
        i=self.hash_func(key)
        for ind, item in enumerate(self.valarr[i]):
            if item[0]==key:
                del self.valarr[i][ind]

ha=Hashmap()
ha["march 5"]=140
ha["march 6"]=97
ha["dec 17"]=53
ha["jan 7"]=200
ha["march 5"]=140
ha["march 17"]=990

print(ha["march 5"])

print("\n\n",ha.valarr)

del ha["dec 17"]
print("\n\n",ha.valarr)

print(ha["march 17"])
print(ha["march 6"])

del ha["march 17"]
print(ha["march 17"])
print("\n\n",ha.valarr)
