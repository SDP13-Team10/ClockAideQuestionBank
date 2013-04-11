import sqlite3

class QuestionBank:
	databaseLocation = ""
	connection = ""
	cursorObj = ""

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

	def getTime(self, difficulty=None):
		if difficulty is None:
			cursorObj.execute('SELECT * FROM questionBank ORDER BY RANDOM() LIMIT 1')
			row = cursorObj.fetchone()
			hour = str(row[1])
			minute = str(row[2])
			if minute == 0 or minute ==5:
				minute = "0" + minute
			return hour + "," + minute
		else:
			d = (difficulty,)
			cursorObj.execute('SELECT * FROM questionBank WHERE difficulty=? ORDER BY RANDOM() LIMIT 1', d)
			row = cursorObj.fetchone()
			hour = str(row[1])
			minute = str(row[2])
			if minute == 0 or minute ==5:
				minute = "0" + minute
			return hour + "," + minute
