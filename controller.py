#initialize

#create queue for Iceberg Objects

#read list of Iceberg objects from the database

#reach into queue, grab object, repeat until empty

#clean up

import iceberg
import sqlite3

#----------------------------------------
# modify:

database_name = "iceberg.db"
database_location = "c:\\iceberg\\database\\"

#----------------------------------------

with sqlite3.connect(database_location + database_name) as connection:
	c = connection.cursor()

	c.execute("CREATE TABLE IF NOT EXISTS Systems(SystemName TEXT UNIQUE)")

	c.execute("INSERT OR IGNORE INTO Systems VALUES('Salesforce')")


system1 = iceberg.Iceberg(name="system1")
print(system1)