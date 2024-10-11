def getFormatteName(firstName , lastName):
    """Return a fulll name, neatly formated"""
    fullName=firstName+' '+lastName
    return fullName.title()


musician=getFormatteName('jim ', 'hendrix')
print(musician)
     