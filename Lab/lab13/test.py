import random

import sqlite3
db = sqlite3.Connection("nums.db")
db.execute("CREATE TABLE nums AS SELECT 2 as n UNION SELECT 3;")
db.execute("INSERT INTO nums VALUES (?), (?), (?);", range(4, 7))
print(db.execute("SELECT * FROM nums;").fetchall())
db.commit()