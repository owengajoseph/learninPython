import json

FILENAME='userName.json'

with open(FILENAME)as f_obj:
    usrname=json.load(f_obj)
    print("welcome back "+usrname+" !")
