"working with files"
FILENAME = '/home/user426/learnpython/files/one_million_of.txt'
with open(FILENAME)as file_object:
    lines = file_object.readlines()


PI_STRING = ''
for line in lines:
    PI_STRING += line.strip()

print(PI_STRING[:54]+"...")
print(len(PI_STRING))

birthday = input("enter your birthday: in the form mmddyy")
if birthday in PI_STRING:
    print("your birtday appears in the pi string")
else:
    print("your birtday does not appear in pi")
