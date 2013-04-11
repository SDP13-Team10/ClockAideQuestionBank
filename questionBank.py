import sqlite3

class QuestionBank:
	databaseLocation = ""
	connection = ""
	cursorObj = ""
	randomHour = -1
	randomMinute = -1

	def __init__ (self,pathToDB):
		global databaseLocation
		global connection
		global cursorObj
		databaseLocation = pathToDB
		connection = sqlite3.connect(databaseLocation)
		cursorObj = connection.cursor()

	def printDatabaseLocation(self):
		global databaseLocation
		print databaseLocation

	def generateTime(self, difficulty=None):
		global randomHour
		global randomMinute

		if difficulty is None:
			cursorObj.execute('SELECT * FROM questionBank ORDER BY RANDOM() LIMIT 1')
			row = cursorObj.fetchone()
			randomHour = row[1]
			randomMinute = row[2]
		else:
			d = (difficulty,)
			cursorObj.execute('SELECT * FROM questionBank WHERE difficulty=? ORDER BY RANDOM() LIMIT 1', d)
			row = cursorObj.fetchone()
			randomHour = str(row[1])
			randomMinute = str(row[2])

	def getTimeString(self):
		global randomHour
		global randomMinute
		hour = str(randomHour)
		minute = str(row[2])
		if minute == 0 or minute ==5:
			minute = "0" + minute
		return hour + "," + minute

	def getTimeTouple(self):
		global randomHour
		global randomMinute
		timeTouple = randomHour, randomMinute
		return timeTouple
