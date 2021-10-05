import sqlite3

#connect to database

conn=sqlite3.connect('ctmovie.db')

#create a cursor

na =conn.cursor()

#Query the database

na.execute("SELECT rowid, * FROM ctmovie")

items = na.fetchall()

print("Number\t| Movie Name\t\t\t| Lead Actor\t| Lead Actress\t\t| Year of Release| Director")
print("-------------------------------------------------------------------------------------------------------------------------------")

for item in items:
    print(str(item[0]) + "\t|"+ str(item[1]) + "\t|" + str(item[2]) + "\t|" + str(item[3]) + "\t|"+ str(item[4]) + "\t\t |" + str(item[5]))



#commit our commnd

conn.commit()

#close our connection

conn.close()
