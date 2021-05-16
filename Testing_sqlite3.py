import sqlite3
'''
Read the DATABASE README before using this code for SQLITE3.
The code to create and access the DB.SQLITE3 is attached below.
THE DB.SQLITE3 file in this Project is empty, so you can work on it directly with the driver code given below.

'''
try:
    db = sqlite3.connect('db.sqlite3')
    crsr = db.cursor()
    Query1 = '''YOUR QUERY GOES HERE'''
    Query2 = '''Multiple Queries like this can be added here'''
    '''
    If  Necessary, you can make your list as a list of strings and use a for loop to execute it
    Or USE cursor.executemany
    '''
    db.execute(Query1)
except sqlite3.OperationalError:
    print("AN ERROR OCCURED")
    