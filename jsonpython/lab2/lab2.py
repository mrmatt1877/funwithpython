import json

with open('planet.json', 'r') as f:
    el = json.load(f)
    print(len(el))
