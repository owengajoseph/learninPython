def getFormatedName(firstName, secondName):
    """return a full name neatly formated"""
    fullName = firstName+' ' + secondName
    return fullName


while True:

    print('\nplease tell me your namr:')
    print("enter q at any time to quit")

    firstName = input("first name")
    if firstName == 'q':
        break

    lastName = input("last name: ")
    if lastName == 'q':
        break

    formatedName = getFormatedName(firstName, lastName)
    print("\nHello,"+formatedName+"!")
