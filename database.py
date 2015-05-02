import sqlite3 as lite
import pandas as pd
	
con = lite.connect("project_warmest.db")

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS cities;")
	cur.execute("DROP TABLE IF EXISTS weather;")
	cur.execute("CREATE TABLE cities (name text, region text)")
	cur.execute("CREATE TABLE weather (city text, warm_month text, average_high integer)")
	
	cur.execute("INSERT INTO cities VALUES('Istanbul', 'Marmara')")
	cur.execute("INSERT INTO cities VALUES('Ankara', 'Ic Anadolu')")
	cur.execute("INSERT INTO cities VALUES('Izmir', 'Ege')")
	cur.execute("INSERT INTO cities VALUES('Antalya', 'Akdeniz')")
	cur.execute("INSERT INTO cities VALUES('Bursa', 'Marmara')")
	
	cur.execute("INSERT INTO weather VALUES('Istanbul', 'July',24)")
	cur.execute("INSERT INTO weather VALUES('Ankara', 'July',21)")
	cur.execute("INSERT INTO weather VALUES('Izmir', 'July',27)")
	cur.execute("INSERT INTO weather VALUES('Antalya', 'August',30)")
	cur.execute("INSERT INTO weather VALUES('Bursa', 'July',23)")
	cur.execute("SELECT city FROM weather INNER JOIN cities ON name = city WHERE warm_month = 'July'")

	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns = cols)

print "The cities that are warmest in July are: %s" % ','.join(df["city"].values)