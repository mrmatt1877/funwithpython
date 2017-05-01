import json
import datetime

class Olympics:
    def __init__(self, city, country, year, ceremonies=None):
        self.city = city
        self.country = country
        self.year = year
        self.ceremonies = ceremonies

    def __repr__(self):
        return "Olympics({city} {country}, {year})".format(
            city=self.city,
            country=self.country,
            year=self.year,
        )

class CustomDecoder(json.JSONDecoder):
    DATE_FORMAT = '%B %d, %Y'
    def __init__(self):
        super().__init__(object_hook = self.object_hook)
    def object_hook(self, dct):
        if 'ceremonies' in dct:
            for key in ('opening', 'closing'):
                dt = datetime.datetime.strptime(dct['ceremonies'][key], self.DATE_FORMAT).date()
                dct['ceremonies'][key] = dt
        return dct
        
with open('json.json', 'r') as f:
    hello = json.load(f, cls=CustomDecoder)
    print(hello)
        

