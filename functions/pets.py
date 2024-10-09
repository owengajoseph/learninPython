def describe_Pet(animal_type, pet_name):
    """Display information about a pet"""
    print('\n I have a '+ animal_type+ '.')
    print("My "+ animal_type+ "'s name is "+ pet_name.title()+".")
    
#positional argument
describe_Pet('hamster','harry')
#keyword argument
describe_Pet(pet_name='harry', animal_type='hamster')    