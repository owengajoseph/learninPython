def makePizza(*toppings):
    """summarize the pizza we are about to make """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)


makePizza('pepperoni')
makePizza('mushrooms', 'green peppers', 'extra cheese')
