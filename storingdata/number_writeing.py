"working with json"
import json

numbers = [2, 3, 4, 5, 11, 13]
FILENAME = 'numbers.json'
with open (FILENAME, 'w')as f_obj:
    json.dump(numbers, f_obj)
