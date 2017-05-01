import sqlite3

with sqlite3.connect('pets.db') as conn:
    cur = conn.cursor()
    query = """
    SELECT *
    FROM pets
    WHERE category = ?
    ORDER BY animal
    """
    
    cur.execute(query, ['rodents'])
    for row in cur:
        print(row)