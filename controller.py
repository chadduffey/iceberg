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


def review_iceberg_systems_file():
	iceberg_systems = []
	with open(systems_list_name, "r") as f:
		for system in f:
			system = system.rstrip()
			iceberg_systems.append(system)
	return iceberg_systems


def database_setup(systems):
	print("(Database Setup): Checking...")
	with sqlite3.connect(database_location) as connection:
		c = connection.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS Systems(SystemName TEXT UNIQUE)")

		for system in systems:
			c.execute("INSERT OR IGNORE INTO Systems VALUES('" + system + "')")

		print("(Database Setup): Looking good.")

def iceberg_systems_from_db():
	all_iceberg_systems = []
	with sqlite3.connect(database_location) as connection:
		c = connection.cursor()
		c.execute("SELECT SystemName FROM Systems")
		for row in c.fetchall():
			all_iceberg_systems.append(row[0])
	return all_iceberg_systems

def iceberg_queue_smasher(queue):
	print("(Processing the queue): Smasher Iteration")
	for _ in range(len(queue)):
		print(queue[_].name)

#CHECK PATHS AND LOCATIONS MAKE SENSE
iceberg.Iceberg.health_check(systems_list_name, base_path, database_location)

#SETUP DATABASE
database_setup(review_iceberg_systems_file())

#BUILD ICEBERG OBJECTS FOR EACH SYSTEM AND ADD THEM TO THE QUEUE
controller_queue = []
for system in iceberg_systems_from_db():
	controller_queue.append(iceberg.Iceberg(name=system))

#MAIN LOOP
#while greater than zero in the queue loop will go here.
print("\n(Processing the Queue): Starting")
iceberg_queue_smasher(controller_queue)