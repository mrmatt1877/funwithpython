import sqlite3


class Pets:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        
        
    def get_pets(self, category):
        query = "SELECT * FROM pets WHERE category = ?"
        cur = self.conn.cursor()
        cur.execute(query, [category])
        results = cur.fetchall()
        return results
        
    def get_sum(self, category):
        query = "SELECT sum(households) as SUM_households FROM pets WHERE category = ?"
        cur = self.conn.cursor()
        cur.execute(query, [category])
        results = cur.fetchone()
        return results
    
    def get_list(self, category):
        query = "SELECT animal FROM pets WHERE category = ? ORDER BY households"
        cur = self.conn.cursor()
        cur.execute(query, [category])
        results = cur.fetchall()
        return results[:3]


el = Pets('pets.db').get_sum('rodents')
lol = Pets('pets.db').get_list('rodents')
ela = Pets('pets.db').get_pets('rodents')


print(el)
print(lol)
print(ela)