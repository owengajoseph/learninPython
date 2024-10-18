#list is a collection of items in a particular order
bicycles = ['trek', 'cannondale', 'redlie','specialized']
print(bicycles)
print(bicycles[0])
#you get the idea
message="My first bycycles was a "+ bicycles[0].title()+"."
print (message)

#exercise
names=["james",'fred','freud',"frank",]
print(names)
message =names[1]+" \n1loves to eat "
print(message)
#continuation
names[0]="hanna"
print(names)
names.append("mercy")
print(names)
del names[0]
print(names)

motorcycles =['honda','yamaha', 'suzuki']
poped_motorcycle=motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
