import sqlite3
conn = sqlite3.connect("tutorial.db")
c = conn.cursor()
def tableCreate():
    #this can only be done once
    c.execute("CREATE TABLE stuffToPlot (ID INT, datestamp TEXT,keyword TEXT, value REAL ) ") # create table and specify column, primary key is auto incremnting ID numbe

def dataEntry():
    c.execute("INSERT INTO stuffToPlot VALUES( 1,'2014-04-14','keyword1',100)")
    c.execute("INSERT INTO stuffToPlot VALUES( 2,'2014-05-14','keyword2',200)")
    c.execute("INSERT INTO stuffToPlot VALUES( 3,'2014-06-14','keyword3',300)")
    c.execute("INSERT INTO stuffToPlot VALUES( 4,'2014-07-14','keyword4',400)")
    conn.commit()
