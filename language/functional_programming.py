
# Functions as Objects

def i_am_an_object(myarg):
     '''I am a really nice function. Please be my friend.'''
     return myarg

i_am_an_object(1)
# 1

an_object_by_any_other_name = i_am_an_object
an_object_by_any_other_name(2)
# 2

i_am_an_object
# <function i_am_an_object at 0x100432aa0>

an_object_by_any_other_name
# <function i_am_an_object at 0x100432aa0>

i_am_an_object.__doc__ # How did this get here?
# 'I am a really nice function.\n Please be my friend.'

# Higher Order Functions
# functions can accept other functions as arguments and return functions to the caller.

'''

In order to define non-default sorting in Python, both the sorted() function and the list's .sort() method accept a key argument. 
The value passed to this argument needs to be a function object that returns the sorting key for any item in the list or iterable.

For example, given a list of tuples, Python will sort by default on the first value in each tuple. 
In order to sort on a different element from each tuple, a function can be passed that returns that element
'''

def second_element(t):
     return t[1]

zepp = [('Guitar', 'Jimmy', 'Page'), ('Vocals', 'Robert', 'Plant'), ('Bass', 'John Paul', 'Jones'), ('Drums', 'John', 'Bonham')]

sorted(zepp)
# [('Bass', 'John Paul', 'Jones'), ('Drums', 'John', 'Bonham'), ('Guitar', 'Jimmy', 'Page'), ('Vocals', 'Robert', 'Plant')]

sorted(zepp, key=second_element)
# sorted using 2nd element in the tuple
# [('Guitar', 'Jimmy', 'Page'), ('Drums', 'John', 'Bonham'), ('Bass', 'John Paul', 'Jones'), ('Vocals', 'Robert', 'Plant')]

# Lambdas : used when passing a simple function as an argument to another function.

zepp = [('Guitar', 'Jimmy', 'Page'), ('Vocals', 'Robert', 'Plant'), ('Bass', 'John Paul', 'Jones'), ('Drums', 'John', 'Bonham')]
sorted(zepp, key=lambda t: t[2])
# [('Drums', 'John', 'Bonham'), ('Bass', 'John Paul', 'Jones'), ('Guitar', 'Jimmy', 'Page'), ('Vocals', 'Robert', 'Plant')]

# Nested Functions

# Closures

# Lexicaal Scoping


