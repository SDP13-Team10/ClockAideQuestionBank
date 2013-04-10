import sqllite3

class QuestionBank:
	global databaseLocation
	global connection
	global cursorObj

	def __init__ (pathToDB):
		global databaseLocation
		global connection
		connection = sqllite3.connect(databaseLocation)
		cursorObj = connection.cursor()

	def printDatabaseLocation():
		global databaseLocation
		print databaseLocation

	def getRandomTime(difficulty):
		d = (difficulty,)
		cursorObj.execute('SELECT * FROM questionBank WHERE difficulty=? ORDER BY RANDOM() LIMIT 1', d)
		row = cursorObj.fetchone()
		return row[3]

	def getRandomTime():
		cursorObj.execute('SELECT * FROM questionBank ORDER BY RANDOM() LIMIT 1')
		row = cursorObj.fetchone()
		return row[3]