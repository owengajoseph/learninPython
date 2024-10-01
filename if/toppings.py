requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("adding mushrooms.")
    if 'pepperoni' in requested_toppings:
        print("Ading pepperoni.")
        if 'extra cheese' in requested_toppings:
            print("Adding exra cheese.")

print("\nfinished making your pizza!")

# using if statements with Lists
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry , we are out of green peppers right now.")
else:
    print("Adding " + requested_topping+".")

print("\nFinished making your pizza!")

# cheking if a list is empty.
print("\n")
requested_toppings = []
if requested_topping:
    for requested_topping in requested_toppings:
        print("Ading " + requested_topping+".")
    else:
        print("Are you sure yo want a plain pizza?")

# using Multiples Lists
available_topings = ['mushrooms', 'olives', 'green peppes',
                     'pepperoni', 'pineapple', 'extra chesse']

requested_toppings = ['mushrooms ', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_topings:
        print("Adding " + requested_topping)
    else:
        print("sorry, we don't have "+requested_topping+".")
