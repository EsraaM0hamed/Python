
                                #<<Inheritance>>
#if you have two classes like Human and Mammel  and third class named employee 
#if employee inhert from human and mummal 
#and you make an object from employee then 
#Python will start by looking at First, and, if First doesn't have the attribute, then it will look at Second.
# For old-style classes, the only rule is depth-first, left-to-right. Thus, if an attribute is not found in DerivedClassName, it is searched in Base1, 
# then (recursively) in the base classes of Base1, and only if it is not found there, it is searched in Base2, and so on.

# (To some people breadth first — searching Base2 and Base3 before the base classes of Base1 — looks more natural.
#  However, this would require you to know whether a particular attribute of Base1 is actually defined in Base1 or in one of its base classes before you can 
# figure out the consequences of a name conflict with an attribute of Base2. The depth-first rule makes no differences between direct and inherited attributes of Base1.)
# For new-style classes, the method resolution order changes dynamically to support cooperative calls to super(). This approach is known in some other multiple-inheritance
#  languages as call-next-method and is more powerful than the super call found in single-inheritance languages.

# With new-style classes, dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships (where at least one of the parent
#  classes can be accessed through multiple paths from the bottommost class). For example, all new-style classes inherit from object, so any case of multiple inheritance provides 
# more than one path to reach object. To keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way that preserves the 
# left-to-right ordering specified in each class, that calls each parent only once, and that is monotonic (meaning that a class can be subclassed without affecting the precedence order 
# of its parents). Taken together, these properties make it possible to design reliable and extensible classes with multiple inheritance

class  Human:
    def __init__(self):
        print("Human constructor");
    def say(self):
        print("hello from Human");

class Mammel:
    def __init__(self):
        print("Mammel constructor");
    def say(self):
        print("hello from Mammel");


class Employee(Mammel,Human):
    def __init(self):
        Human.__init__(self);
        Mammel.__init__(self);
        print("Employee constructor")


emp=Employee()
h=Human()
m=Mammel()
emp.say();

#that will print Human first beacause it check from the first class that it 
# inheit from it  in the piece of code super  super.__init__(self);
        # super.__init__(self);
#that when i make object from emp it will call parent constructor first and print "Human Constructor"        

#using name of super class is better than using keyword super for less complexicity.


#if child inhert from 2 class and the two classes have the same method name 
# when the object call any of these method it will execute the method that belong 
# to the first class the inhert from it
#example here emp.say will execute say method in class Human beaceause it was the first class that emp inhert from it
# if class emp inhert like that Employee(Mammel,Human)
#and use method say .it witll print "Hello from Mammel".
# the method caller from right to left

