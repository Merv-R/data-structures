# -*- coding: utf-8 -*-

# Python has a dynamic data structure called as list, which we use to simulate how an array
# might behave by default (simulating a static array)

# Creating an integer array with random set of numbers

randomarray = [12,764,213,8,2,66,2321,5,9786,21]

# Looking up value with index [Lookup by index takes O(1) time]

print(randomarray[8])

# Searching for a value [Lookup by value takes O(n) time]

for i in range(len(randomarray)):
    if randomarray[i]==5:
        print("Item found at index %d"%i)

# Traversal [Printing all values will take O(n) time]

for i in randomarray:
    print(i)
    
# Inserting a new value in the array [This takes O(n) time]

randomarray.insert(5,6)
print(randomarray)

# Deleting a value from the array [Takes O(n) time]

randomarray.remove(8)
print(randomarray)
print("\n\n\n")

"""
Let us say your expense for every month are listed below,

    January - 2200
    February - 2350
    March - 2600
    April - 2130
    May - 2190

"""

expense = [2200,2350,2600,2130,2190]

# In Feb, how many dollars you spent extra compare to January?
print(f"Spent an extra of {expense[1]-expense[0]} dollars.")

# Find out your total expense in first quarter (first three months)
print(f"Total for the first quarter is {expense[0]+expense[1]+expense[2]}")

# Find out if you spent exactly 2000 dollars in any month
exact=False
for i in expense:
    if i==2000:
        exact=True
if exact:
    print("Spent exactly 2000 dollars in one of the months")

# June month just finished and your expense is 1980 dollar. 
# Add this item to our monthly expense list

expense.append(1980)
print(expense)

# You returned an item that you bought in a month of April and got a refund of 
# 200$. Make a correction to your monthly expense list based on this

expense[3]-=200
print(expense)
print("\n\n\n")

"""
Do the following with the given list
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with 
   doctor strange (because he is cool). Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to 
   list down all functions available in list)
"""

heroes=['spider man','thor','hulk','iron man','captain america']

print(len(heroes))

heroes.append("black panther")
print(heroes)

heroes.remove("black panther")
heroes.insert(3,"black panther")
print(heroes)

heroes[1:3]=["doctor strange"]
print(heroes)

heroes.sort()
print(heroes)
print("\n\n\n")

"""
Create a list of all odd numbers between 1 and a max number. Max number is 
something you need to take from a user using input() function
"""

oddarray=[]
limit=int(input("Enter the limit till which the odd numbers are to be generated: "))
for i in range(limit):
    if i%2!=0:
        oddarray.append(i)

print(oddarray)