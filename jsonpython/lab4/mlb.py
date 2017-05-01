import json
import datetime

def parse_json(dct):
    if 'is_date' in dct:
        return datetime.datetime.strptime(dct['value'], ISO_DATETIME_FORMAT)
    return dct
    
with open('mlb.json', 'r') as f:
    obj = json.load(f, object_hook = parse_json)
    print(obj)
    print(type(obj))