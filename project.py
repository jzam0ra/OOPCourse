import csv

class Item: # a function inside a class is called a method
    #there are attributes that belong to the whole class, e.g.
    pay_rate = 0.8 #this is a class attribute that refers to the 20% discount
    all = [] #this is in case you want to have all instances (items) on a list in order to access them
    def __init__(self, name: str, price: float, quantity = 0) -> None: #this method executed by python once you create an instance and it calls its actions
        #attributes can be defined to have default values in case they are not specified
        #you always take care of the attributes of an object inside __init__
        
        #run validations to received arguments
        assert price >= 0, f"Price{price} is not grater than zero!"
        assert quantity >= 0, f"Quantity{quantity} is not grater than zero!"

        #assign attributes to self object
        self.name = name #this allows us to dynamically define an attribute of the instance without the need of doing it outside of the method
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self) #this adds each item to the "all" list

    def calculate_total_price(self): #self is necessary in order to receive a default parameter
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # this is how you call a class level attribute inside a method: Item.pay_rate, but you can also use self.pay_rate if it is specified for a particular instance

    @classmethod
    def instantiate_from_csv(cls): #this is a class method because it is designed to instantiate instances. 
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )


    @staticmethod    # A static method has a logical connection to a class. The static methods never send in the background the instance as the first argument. Static methods never send object as argument
    def is_integer(num):
        # we will count the floats that are point zero, e.g. 5.0
        if isinstance(num, float):
            #count the floats that are decimal
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Item('{self.name}',{self.price},{self.quantity})"


item1 = Item("Phone", 100, 5) #We create an instance of the class item
#item1.name = "Phone" -- this becomes unneccessary because we defined it inside __init__
#these are attributes of an instance (item1) of the class Item
#this makes item1 have datatype of Item
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3) #We create an instance of the class item

item2.has_numpad = False #you can still define attributes that are proper to a specific object
item2.pay_rate = 0.7 #you can also assign a diffrent value of a class attribute to an instance 
# print(item1.calculate_total_price()) -- this calls the method that calculates the price

#print(Item.__dict__) gives all the attributes for class level
#print(item1.__dict__) gives all the attributes for instance level

#Item.instantiate_from_csv()
#print(Item.all)
Item.is_integer(7.05)

class Phone(Item):
    pass
# if we were to define this attribute for
# determine the amount of broken phones of a type,
# we want to create a method that calculates the phones
# that aren't broken. This is in principle hard to calculate 
#because it isn't an attribute assigned to self in class Item
# That's the reason why we create a new Phone class that inherites
# the item class properties
phone1 = Item("jscPhonev10", 500, 5)
phone1.broken_phones = 1 
phone2 = Item("jscPhonev20",700,5)
phone2.broken_phones = 1
