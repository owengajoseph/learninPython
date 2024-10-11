# start with some designs that need to be printed
unprintedDesing = ['iphone case', 'robot pending', 'dodecahedron']
complitedModels = []

# simulate printing each design, until none are left.
# move each design to complete models after  printing.
while unprintedDesing:
    currentdesign = unprintedDesing.pop()

# simulate creating a 3D print from the design.
    print("printing model:" + currentdesign)
    complitedModels.append(currentdesign)

# Display all completed models
print("\nThe following models have been printed:")

for complitedModel in complitedModels:
    print(complitedModel)


# wriwritten using functions
def printModels(unprinteDesings, completeModels):
    """simulate printing each design, untill none are left.move each design to completedModels after printing."""

    while unprintedDesing:
        currentdesign = unprintedDesing.pop()
        # simulate creating a 3D print from the Design.
        print("printing model :"+currentdesign)
        complitedModel.append(currentdesign)


def showCompletedModels(compliteModels):
    """show all the models that were printed."""
    print("\nthe following models have been printed : ")
    for completeModel in complitedModel:
        print(completeModel)


unprintedDesings = ['i phone case', 'robot pendant', 'dodecahedron']


binary=format(14, '#b')
print(binary)