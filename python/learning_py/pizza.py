# store information about a pizza being orderd.

pizza = {'crust': 'thick', 'toppings': ['mushroom', 'extra cheese'], }

#summarize the order.
print("your ordered a "+ pizza['crust']+ "crust pizza "+ "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" ,topping)