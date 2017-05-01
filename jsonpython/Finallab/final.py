import json
import datetime

class Employee:
    def __init__(self, first, last, employee_id, dob, projects, phone):
        self.first = first
        self.last = last
        self.employee_id = employee_id
        self.dob = dob
        self.projects = projects
        self.phone = phone
        
    def __repr__(self):
        return 'Employee({first},{last},{dob})'.format(first = self.first, last = self.last, dob = self.dob)
        
        
class CustomDecoder(json.JSONDecoder):
    DATE_FORMAT = '%B %d, %Y'
    def __init__(self):
        super().__init__(object_hook = self.object_hook)
    def object_hook(self, dct):
        if 'dob' in dct:
            dt = datetime.datetime.strptime(dct['dob'], self.DATE_FORMAT).date()
            dct['dob'] = dt
        return dct

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, Employee):
            return {
                "first_name": obj.first,
                "last_name": obj.last,
                "dob": obj.dob,
                "employee_id": obj.employee_id,
                "projects" : obj.projects,
                "phone" : obj.phone
            }
        return super(CustomEncoder, self).default(obj)
        
proj = ["this","that","huh"]
phnum = {"cell" : 3365551234, "home" : 3369857894}
        
bob = Employee("bob", "billy", 24, "October 2, 2121", proj, phnum)

el = json.dumps(bob, cls=CustomEncoder, indent=4)
print(el)

lol = json.loads(el, cls=CustomDecoder)
print(lol)