"usefull when working with multiple programs"
import json
FILENAME = '/home/user426/learnpython/numbers.json'
with open('numbers.json')as f_obj:
    numbers=json.load(f_obj)    
print(numbers)
