# When to use a static method vs when to use class method
class Item: 

    @staticmethod
    def is_integer(num):
        '''
        comment
        
        '''
        # When we will use static method?:Does something that has 
        # a relathionship with the class, but not something that must be
        # unique per instance

    @classmethod
    def instantiate_from_something(cls):
        '''
        comment
        
        '''
        # This should also be something that has a relationship
        # with the class, but usually, those are used to
        # manipulate different structures of data to instantiate
        # objects, e.g. the CSV that we used.

    # The mein diffrenece between the methods is that
    # static methods dont pass the object reference as the first argument
    # Notice we dont have special highlight for the first parameter 
    # like we do have is class methods 

# However those could be called from instances
item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()