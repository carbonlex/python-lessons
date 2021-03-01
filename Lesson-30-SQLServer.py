import pypyodbc




mySQLServer = "localhost:5432"
myDataBase = 'db'

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDataBase + ';'
                              'uid=postgres;'
                              'pwd=postgres;')

cursor = connection.cursor()

mySQLQuery = ""