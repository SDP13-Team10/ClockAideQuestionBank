import sqlite3

class QuestionBank:
	global databaseLocation = ""
	global connection = ""
	global cursorObj = ""

	def __init__ (pathToDB):
		global databaseLocation
		global connection
		global cursorObj
		databaseLocation = pathToDB
		connection = sqllite3.connect(databaseLocation)
		cursorObj = connection.cursor()

	def printDatabaseLocation(self):
		global databaseLocation
		print databaseLocation

	def getTime(self, difficulty=None):
		if difficulty is None:
			cursorObj.execute('SELECT * FROM questionBank ORDER BY RANDOM() LIMIT 1')
			row = cursorObj.fetchone()
			hour = row[1]
			minute = row[2]
			if minute == 0 or minute ==5:
				minute = str("0" + row[2])
			hour = str(row[1])
			return hour + "," + minute
		else:
			d = (difficulty,)
			cursorObj.execute('SELECT * FROM questionBank WHERE difficulty=? ORDER BY RANDOM() LIMIT 1', d)
			row = cursorObj.fetchone()
			row = cursorObj.fetchone()
			hour = row[1]
			minute = row[2]
			if minute == 0 or minute ==5:
				minute = str("0" + row[2])
			hour = str(row[1])
			return hour + "," + minute
