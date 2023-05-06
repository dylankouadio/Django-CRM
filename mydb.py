import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Kekedu87356!'

    )



cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE kdisco")

print("All Done!")