
# Exception Handling Structure

try:
    something_that_is_error_prone()
except Exception as err:
    raise Exception("This is my error message!")  
    print("I got an error")
    print(err)
else:
    print("Everything is good, nothing to see here")
finally:
    print("No matter what, I'll do this last")

