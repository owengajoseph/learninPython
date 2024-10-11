def makePizza(size, *toppings):
    """summarize the pizza we are about to make"""
    print('\nMaking a'+str(size)+'inch pizza with the following toppings:')

    for topping in toppings:
        print("-" + topping)
