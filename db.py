import mysql.connector

class Database:

	def createDB(self, hostname, username, password, database):
		mydb = mysql.connector.connect(
  			host="localhost",
  			user="root",
  			passwd="mypass",
  			database="dehat"
		)

		mycursor = mydb.cursor()

		mycursor.execute("CREATE TABLE Query (Query_variable VARCHAR(255), Query_year VARCHAR(255), Output VARCHAR(255)")

	def insertData(self, Query_variable, Query_year, result):
		mydb = mysql.connector.connect(
  			host="localhost",
  			user="root",
  			passwd="mypass",
  			database="dehat"
		)

		mycursor = mydb.cursor()
		
		sql = "INSERT INTO Query (Query_variable, Query_year, Output) VALUES (%s, %s, %s)"
		val = (Query_variable, Query_year, result)
		mycursor.execute(sql, val)

		mydb.commit()