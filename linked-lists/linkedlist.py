# -*- coding: utf-8 -*-

# Linked List tries to tackle some of the problems that we deal with list 
# (dynamic arrays), especially when try ti insert in between the values of the
# array. Its benefits over arrays are the facts that there's no need to 
# pre-allocate the memory space at the start (see workings of dynamic array), 
# and the insertion operation is way easier.

# The Insertion/Deletion at the beginning of the LL takes O(1) time.
# But Insertion/Deletion at the end (and middle) still takes O(n) time.
# LL traversal takes O(n) time.
# Indexing/Lookup by index takes O(n) time.
# Lookup element by value takes O(n) time.

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self, data):
        node=Node(data, self.head)
        self.head=node
    
    def print_ll(self):
        if self.head==None:
            print("The Linked List is empty!")
            return
        
        itr=self.head
        ll_string=""
        while itr:
            ll_string+=str(itr.data)+"--->"
            itr=itr.next
        print(ll_string)
    
    def insert_at_end(self, data):
        if self.head==None:
            self.head=Node(data, None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data, None)
    
    def insert_values(self,datalist):
        self.head=None
        for i in datalist:
            self.insert_at_end(i)
    
    def get_len(self):
        c=0
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
        return c
    
    def remove_at(self,index):
        if index<0 or index>self.get_len():
            raise Exception("Invalid index entered")
        if index==0:
            self.head=self.head.next #Automatic garbage collection takes care of loose values in memory
            return
        itr=self.head
        c=0
        while itr:
            if c==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            c+=1
                
    def insert_at(self,index,data):
        if index<0 or index>self.get_len():
            raise Exception("Invalid index entered")
        if index==0:
            self.insert_at_beginning(data)
            return
        c=0
        itr=self.head
        while itr:
            if c==index-1:
                node=Node(data, itr.next)
                itr.next=node
                break
            itr=itr.next
            c+=1

    def remove_val(self, data):
        found=False
        itr=self.head
        if itr.data==data:
            self.head=itr.next
            return
        while itr:
            if itr.next.data==data:
                itr.next=itr.next.next
                return
            itr=itr.next
        if not found:
            raise Exception("Value not in Linked List")
    
    def insert_before_val(self, data_lookout, data_insert):
        itr=self.head
        while itr:
            if itr.next.data==data_lookout:
                node=Node(data_insert,itr.next)
                itr.next=node
                return
            itr=itr.next

if __name__=="__main__":
    
    linkl=Linkedlist()
    linkl.print_ll()
    
    linkl.insert_at_beginning(12)
    linkl.insert_at_beginning(5)
    linkl.insert_at_end(4)
    linkl.insert_at_beginning(44)
    linkl.insert_at_end(3)
    linkl.print_ll()
    
    linkl.insert_values([5,7,4,3])
    linkl.print_ll()
    
    print("Length of linked list: ",linkl.get_len())
    
    linkl.insert_values([5,7,6,2,4,3])
    linkl.print_ll()
    linkl.remove_at(3)
    linkl.print_ll()
    
    linkl.insert_values([5,6,4,3])
    linkl.print_ll()
    linkl.insert_at(1,7)
    linkl.print_ll()
    
    # linkl.remove_val(10)
    linkl.remove_val(4)
    linkl.print_ll()
    
    linkl.insert_before_val(3, 5)
    linkl.print_ll()