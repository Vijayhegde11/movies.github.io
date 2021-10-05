import sqlite3

# connect to database

conn = sqlite3.connect('ctmovie.db')

#create a cursor

na = conn.cursor()

#create a table

na.execute("""CREATE TABLE ctmovie (
            name text,
            lead_actor text,
            lead_actress text,
            year_of_release integer,
            director text
            ) """)

#Adding records into the table

an =[
    ('Vishnuvardhana         ','Sudeep      ','Priyamani         ',2011,'Pon Kumarana'),
    ('Kempe Gowda            ','Sudeep      ','Ragini            ',2011,'Sudeep'),
    ('Bachahan               ','Sudeep      ','Bhavana           ',2013,'Shashank'),
    ('Maanikya               ','Sudeep      ','Ramya             ',2014,'Sudeep'),
    ('Veera Madakari         ','Sudeep      ','Ragini            ',2009,'Sudeep'),
    ('Huchha                 ','Sudeep      ','Rekha Vedavyas    ',2001,'Om Prakash Rao'),
    ('Kotibba-3              ','Sudeep      ','Shraddha Das      ',2020,'Shiva Karthik'),
    ('Hebbuli                ','Sudeep      ','Amala Paul        ',2017,'S Krishna'),
    ]

na.executemany("INSERT INTO ctmovie VALUES (?,?,?,?,?)",an)

#commit our commnd

conn.commit()

#close our connection

conn.close()
