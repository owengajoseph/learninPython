import json
# load the usr name, if it has been stored previously
# other wise prompt for the usrname and store it
FILENAME = '/home/user426/learnpython/userName.json'
try:
    with open(FILENAME)as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what is your username ? ")
    with open(FILENAME, 'w')as f_obj:
        json.dump(username, f_obj)
        print("we will remember you when you comeback, "+username+" !")
else:
    print("wlcome back " + username)
