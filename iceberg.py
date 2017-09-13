from enum import Enum

import datetime
import os
import sys

class Phases(Enum):
	init = 1
	log_fetch = 2
	log_parse = 3
	complete = 4
	failed = 5


class Iceberg(object):

	def __init__(self, name=None):

		self.name = name
		self.start_time = datetime.datetime.now()
		self.phase = Phases.init

	def __str__(self):
		return self.name + " is in: " + str(self.phase)

	def nextPhase(self):
		pass

	def failObject(self):
		pass

	def finishObject(self):
		pass

	@staticmethod
	def health_check(path_to_systems_list, base_path, database_path):
		print("ICEBERG HEALTH CHECKS:")

		# check that the systems have an entry in the database
		with open(path_to_systems_list, "r") as f:
			for system in f:
				system = system.rstrip()
				print("(Health Check): " + system)

				# check that paths exist for each of the folders
				if not os.path.isdir(base_path + "\\systems\\" + system):
					print("(Health Check)" + base_path + "\\systems\\" + system + " path does not exist")
					print("(Health Check) FAIL")
					sys.exit()
		print("(Health Check): All Iceberg paths exist")

		# check that the database exists
		print("(Health Check): Checking if the database exists")
		if not os.path.exists(database_path):
			print("(Health Check): The database does not exist; this isn't critical right now but you should stop here if you care.")
			ok = input("Type ok to continue, everything else exits")
			if not ok == "ok":
				sys.exit()

		print("(Health Check): We are ok here. Moving on.")
















