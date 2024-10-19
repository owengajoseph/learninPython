"files "
with open('/home/user426/learnpython/files/pidigits.txt') as file_object:
    contents = file_object.read()
    print(contents)


FILENAME = '/home/user426/learnpython/files/pidigits.txt'
with open(FILENAME) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
