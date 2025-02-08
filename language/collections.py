
'''
Lists
String slicing
Tuples
Dictionaries
Sets
'''

# Lists
#---------------------------------------------------------------------
# Empty Lists
mylist = []

# Initializing Lists
mylist = ['a', 'b', 'c']

# shallow copying lists
mylist2 = list(mylist)

# Converting string to list of characters
char_list = list('abcdef') # Returns ['a', 'b', 'c', 'd', 'e', 'f']

# Adding to lists
mylist = []
mylist.append('a')
mylist.append('b')
mylist.insert(0, 'a')

# Removig items fom lists
mylist.remove('a')
# collections.deque

# Iterating
for letter in mylist:
  print(letter)

# Iterating with while
while len(mylist):
  print(mylist.pop())

# Iterating with an index
for i in range(len(mylist)):
  print(i, mylist[i])

# Access and Slicing**
# Negative indexing : -1 denotes the last element
# mylist[start : end : stride] ex: mylist[2:7:2] -> would take every 2nd item from the list
mylist = list('abcdefgh') # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
mylist[3] # 'd'
mylist[-3] # 'f'
mylist[1:4] # ['b', 'c', 'd']
mylist[1:-1] # ['b', 'c', 'd', 'e', 'f', 'g']
mylist[1:-1:2] # ['b', 'd', 'f']
mylist[::-1] # ['h', 'g' , 'f', 'e', 'd', 'c', 'b', 'a'] -> reverses the list

# Presence and  Finding
is_g_present = 'g' in mylist
index_of_g = mylist.index('g')

#---------------------------------------------------------------------

# String slicing

#---------------------------------------------------------------------

# 1. split()
s = 'abc.def'
parts = s.split('.')
# ['abc', 'def']

# 2. join()
new_string = '/'.join(parts)
# 'abc/def'

# 3. Slicing like lists
s = 'hello world'
len(s)
# 11
s[4]
# 'o'
s[2:10:2]
# 'lowr'

# 4. strip(), lstrip() , rstrip()
s = ' abc '
s.strip()
#'abc'

#---------------------------------------------------------------------

# Tuples
# A tuple is like an immutable list. It is slightly faster and smaller than a list, so it is useful.
#---------------------------------------------------------------------

# Creating

t = ()
t2 = tuple()

# Initializing with value
t = ('Iron Man', )
t = ('Iron Man', 'Ultron')

# Creating tuple from list
mylist = ['Iron Man', 'Ultron']
t = tuple(mylist)

# Unpacking
t = ('Iron Man', 'Ultron')
hero, villain = t
# hero = Iron Man
# villain = Ultron

# Accessing and Slicing
t[0] # Iron Man
t = ('Iron Man', 'Ultron', 'Pepper Potts')
t[0::2] # ('Iron Man', 'Pepper Potts')

# Iterating
t = ('Iron Man', 'Ultron')
for character in t:
  print(character)

# Since a tuple is iterable, a mutable copy is easily created using the list() builtin
list(t) # ['Iron Man', 'Ultron']


# Indexed List Iteration
mylist = ['a', 'b', 'c']
for i, letter in enumerate(mylist):
  print(i, letter)


#---------------------------------------------------------------------

# Dictionaries

#---------------------------------------------------------------------

# Creating
characters = {'hero': 'Iron Man', 'villain': 'Ultron', 'friend': 'War Machine'}

# Adding
characters['companion'] = 'Pepper Potts'

# Modifying
characters['villain'] = 'The Mandarin'

# failed lookups
characters.get('team', 'Some Default Text if the key for lookup is not present')

# Iterating
for role in characters:
  print(role, characters[role])

#  items() method will return 2-tuples of key, value pairs, which can be unpacked in the for loop.
characters.items()
# dict_items([('villain', 'The Mandarin'), ('hero', 'Iron Man'), ('friend', 'War Machine'), ('companion', 'Pepper Potts')])

for role, name in characters.items():
  print(role, name)

#---------------------------------------------------------------------

# Sets
# A set is a mutable, unordered, unique collection of objects. 
# It is designed to reflect the properties and behavior of a true mathematical set. 
# A frozenset has the same properties as a set, except that it is immutable.
#---------------------------------------------------------------------

# Creating
s = set()
s = set(['Beta', 'Gamma', 'Alpha', 'Delta', 'Gamma', 'Beta'])
# set(['Alpha', 'Beta', 'Gamma', 'Delta'])

# Accessing
while len(s):
  print(s.pop())

# Set Operations
s1 = # set(['Beta', 'Gamma', 'Alpha', 'Delta', 'Gamma', 'Beta'])
s2 = # set(['Beta', 'Alpha', 'Epsilon', 'Omega'])
s1
# set(['Alpha', 'Beta', 'Gamma', 'Delta'])
s2
# set(['Alpha', 'Beta', 'Omega', 'Epsilon'])

s1.union(s2)
# set(['Epsilon', 'Beta', 'Delta', 'Alpha', 'Omega', 'Gamma'])
s1 | s2
# set(['Epsilon', 'Beta', 'Delta', 'Alpha', 'Omega', 'Gamma'])

s1.intersection(s2)
# set(['Alpha', 'Beta'])
s1 & s2
# set(['Alpha', 'Beta'])

s1.difference(s2)
# set(['Gamma', 'Delta'])
s1 - s2
# set(['Gamma', 'Delta'])

s1.symmetric_difference(s2)
# set(['Epsilon', 'Delta', 'Omega', 'Gamma'])
s1 ^ s2
# set(['Epsilon', 'Delta', 'Omega', 'Gamma'])


