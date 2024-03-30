import sqlite3

db = sqlite3.connect('schedule.db')

c = db.cursor()

# c.execute("SELECT * FROM rasp")

c.execute("INSERT INTO rasp (day,data) VALUES ('ПОНЕДЕЛЬНИК', 25.03)")




db.commit()

db.close()
