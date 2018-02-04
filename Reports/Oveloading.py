
                        #    <<Ovelloading>>

# There is no function overloading in Python, meaning that you can't have multiple functions with the same name but different arguments.

# In your code example, you're not overloading __init__(). What happens is that the second definition rebinds the name __init__ to the new method, rendering the first method inaccessible.

# As to your general question about constructors.

def add(a,b):
    return a+b
 
def add(a,b,c):
    return a+b+c

print add(4,5)

# If you try to run the above piece of code, you get an error stating, “TypeError: add() takes exactly 3 arguments (2 given)”. This is because, Python understands the latest definition of
#  method add() which takes only two arguments. Even though a method add() that takes care of three arguments exists, it didn’t get called. Hence you would be safe to say,
#  overloading methods in Python is not supported.

# But, then there are folks who are more than willing to say, ‘Oh! Python supports all!’ Yes, Python supports overloading but in a Pythonic way. Here’s an example,

def add(instanceOf, *args):
    if instanceOf == 'int':
        result = 0
    if instanceOf == 'str':
        result = ''
    for i in args:
        result = result + i
    return result
 
print add('int', 3,4,5)
print add('str', 'I',' am',' in', ' Python')
 
# Output:
# 12
# I am in Python

# In the above code snippet, two things are achieved:

# –          Irrespective of the different number of arguments, method add() works well

# –          Also, based on the data type of input, data  type of output is changed

# So, overloading IS there in Python!!