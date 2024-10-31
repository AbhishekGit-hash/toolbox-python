
# Mutable Arguments and Binding of Default Values

def add_items(new_items, base_items = None):

  if base_items is None:
    base_items = []

for items in new_items :
  base_items.append(items)

return base_items

add_items((1, 2, 3))

# Accepting Variable Arguments

'''
In addition to named arguments, functions can accept two special collections of arguments. 
The first is a variable-length, named tuple of any additional positional arguments received by the function. 
This special argument is identified by prefixing it with a single asterisk (*).

The second is a variable-length dictionary containing all keyword arguments passed to the function 
that were not explicitly defined as part of the function arguments. 
This argument is identified by prefixing it with two asterisks (**).

'''

def mixed_function(a, b, c=None, *args, **kwargs):
  print('(a, b, c):', (a, b, c))
  print('args:', args)
  print('kwargs:', kwargs)

print(mixed_function(1, 2, 3, 4, 5, d=10, e=20))

'''
(a, b, c): (1, 2, 3)
args: (4, 5)
kwargs: {'e': 20, 'd': 10}
'''



