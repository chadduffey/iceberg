from enum import Enum

import datetime

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
		return self.name + " " + self.phase

	def nextPhase(self):
		pass

	def failObject(self):
		pass

	def finishObject(self):
		pass








