from pitchers import data
import datetime
import simplejson as json
from collections import OrderedDict as odd

def json_serial(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    return obj

d = dict(data)

bill = odd(d)

el = json.dumps(d, default = json_serial, indent = 4)

print(el)