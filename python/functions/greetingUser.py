def greetUser(names):
    """print a simple greeting to each usr in the list"""
    for name in names:
        msg="hello , "+name.title()+ "!"
        print(msg)



usernames=['hannah','ty','margot']
greetUser(usernames)

        
    