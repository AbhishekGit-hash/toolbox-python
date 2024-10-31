
# List Comprehensions

colors = ['red', 'yellow', 'blue']
color_lines = ['%s\n' % color for color in colors if 'l' in color]
color_lines
# ['yellow\n', 'blue\n']

colors = ['red', 'yellow', 'blue']
clothes = ['hat', 'shirt', 'pants']
colored_clothes = ['{0} {1}'.format(color, garment) for color in colors for garment in clothes]
colored_clothes
# ['red hat', 'red shirt', 'red pants', 'yellow hat', 'yellow shirt', 'yellow pants', 'blue hat', 'blue shirt', 'blue pants']

# Dictionary Comprehensions

clothes = (('hat', 'red'), ('shirt', 'blue'), ('pants', 'yellow'))
colored_clothes = {x[0]: x[1] for x in clothes}
colored_clothes
# {'hat': 'red', 'shirt': 'blue', 'pants': 'yellow'}

# Generator Expressions

'''
Storing a new list as the output of a list comprehension is not always optimal behavior. 
Particularly in a case where that list is intermediary or where the total size of the contents is quite large.

For such cases, a slightly modified syntax (replacing square brackets with parentheses) leads to the creation of a generator instead of a new list. 
The generator will produce the individual items in the list as each one is requested, which is generally while iterating over that new list.

'''

colors = ['red', 'yellow', 'blue']
color_lines = ('{0}\n'.format(color) for color in colors)
color_lines
# <generator object <genexpr> at 0x10041ac80>
color_lines.__next__()
'red\n'
color_lines.__next__()
'yellow\n'
color_lines.__next__()
'blue\n'
color_lines.__next__()
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''

# Generator Functions

'''

The type of object created by the generator expression in the previous section is unsurprisingly called a generator. This is a term for a type of iterator that generates values on demand.

While the generator expression notation is very compact, there may be cases where there is more logic to be performed than can be effectively expressed with this notation. For such cases, a generator function can be used.

A generator function uses the yield statement in place of return and usually does so inside a loop. When the interpreter sees this statement, it will actually return a generator object from the function. Each time the next() function is called on the generator object, the function will be executed up to the next yield. When the function completes, the interpreter will raise a StopIteration error to the caller.

'''

def one_color_per_line():
    colors = ['red', 'yellow', 'blue']
    for color in colors:
        yield '{0}\n'.format(color)

gen = one_color_per_line()
gen
# <generator object one_color_per_line at 0x10041acd0>
gen.__next__()
# 'red\n'
gen.__next__()
# 'yellow\n'
gen.__next__()
# 'blue\n'
gen.__next__()
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''

'''
Note that a second call to the same generator function will return a new generator object (shown at a different address) as each generator should be capable of maintaining its own state.
'''
gen = one_color_per_line()
gen
# <generator object one_color_per_line at 0x10041ad20>

'''
Of course, the more typical use case would be to allow the calls to next() to be handled by a for ... in loop.
'''

for line in one_color_per_line():
   print(line)


# Itertation Helpers : itertools

# chain() -> retuens iterator
import itertools
l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']
chained = itertools.chain(l1, l2)
[l for l in chained]
# ['a', 'b', 'c', 'd', 'e', 'f']

l1.extend(l2)
l1
# ['a', 'b', 'c', 'd', 'e', 'f']

# zip() ->  pairs up the contents of two lists into an iterable of 2-tuples.
import itertools
name = ['Jimmy', 'Robert', 'John Paul', 'John']
instruments = ['Guitar', 'Vocals', 'Bass', 'Drums']
zepp = zip(name, instruments)
zepp
# <zip object at 0x0254C580>
[x for x in zepp]
# [('Jimmy', 'Guitar'), ('Robert', 'Vocals'), ('John Paul', 'Bass'), ('John', 'Drums')]


