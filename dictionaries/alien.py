alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# working with dictionaries
new_points = alien_0['points']
print("you just earnde "+str(new_points)+" point")

# Adding New key-value pairs
print('\n')
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# starting wiht an empty dictionary
# self explanatory

# modifiying values in a dictionary
alien_0 = {'color': 'green'}
print("The alien is"+alien_0['color']+".")

alien_0['color'] = 'yellow'
print("The alein is now "+alien_0['color']+".")
print('\n')

# *******************************************#

alien_0 = {'x_position': 0, 'y_postion': 25, 'speed': 'medium'}
print("original x-position "+str(alien_0['x_position']))

# move the alien to the right.abs
# Determine how far the alien  based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment=2
else:
    # This must be a fast alien
    x_increment=3

    
alien_0['x_position']=alien_0['x_position']+x_increment

print("New x-position :"+str(alien_0['x_position']))
    
