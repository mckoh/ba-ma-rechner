# %%
from sqlite3 import connect

DB = "database.sqlite3"

def execute_statement(statement):
    cnt = connect(DB)
    crs = cnt.cursor()
    return crs.execute(statement)

def get_data(statement):
    res = execute_statement(statement)
    return res.fetchall()

def get_persons():
    return get_data("SELECT * FROM person;")

def insert_person(firstname, lastname):
    


print(get_persons())
# %%
