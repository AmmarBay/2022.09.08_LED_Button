import sqlite3

connection = sqlite3.connect("LED.db")
cursor = connection.cursor()

sql = "SELECT * FROM TLED"
cursor.execute(sql)


for dsatz in cursor:
    print("timeLED:",dsatz[1], "is_on:",dsatz[2])

connection.close()