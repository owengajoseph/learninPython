#returning a dictionary
def buildPerson(firstName,lastName,age=''):
    """Return a dictionary of infromation about a person"""
    person={'first':firstName,'last':lastName}
    if age:
        person['age']=age
        return person



musician=buildPerson('jimi','hendrix')
print(musician)