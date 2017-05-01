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

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year
        
        
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, Olympics):
            return {
                "name": obj.city,
                "country": obj.country,
                "year": obj.year,
                "ceremonies": obj.ceremonies
            }
        return super(CustomEncoder, self).default(obj)
        
ceremonies = {
    "opening": datetime.date(1968, 10, 12),
    "closing": datetime.date(1968, 10, 27)
}
o = Olympics('Mexico City', 'Mexico', 1968, ceremonies)

j = json.dumps(o, cls=CustomEncoder, indent=4)
print(j)
