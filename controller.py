#initialize

#create queue for Iceberg Objects

#read list of Iceberg objects from the database

#reach into queue, grab object, repeat until empty

#clean up

import iceberg
import sqlite3

#----------------------------------------
# modify:

base_path = "c:\\iceberg"
database_location = base_path + "\\database\\iceberg.db"
systems_list_name = base_path + "\\service\\systems.txt"

#----------------------------------------

iceberg.Iceberg.health_check(systems_list_name, base_path, database_location)

with sqlite3.connect(database_location) as connection:
	c = connection.cursor()

	c.execute("CREATE TABLE IF NOT EXISTS Systems(SystemName TEXT UNIQUE)")

	c.execute("INSERT OR IGNORE INTO Systems VALUES('Salesforce')")


system1 = iceberg.Iceberg(name="system1")
print(system1)