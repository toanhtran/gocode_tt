'''

Open Weather Api is a json weather api to get weather data for most major cities.

In this exercise we are going to populate a small local database with all the min and max temperatures for last 16 days for a city.

We will use a json api to get the data, then store parts of that data in sqlite, which is small sql database.

Steps:

1) First inspect what is returned in json_data. You can use python print statements also download and use the chrome json formatter: https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en 

2) The data returned has a key "list" which is an array of hashes (horray!). Each element in the array is one day's temp info.

3) Write a loop to print out each days "min" and "max" temp as well as the "dt" key. dt is short for datetime.

DB)

4) Create a table to store this information. The table should be able to store

- id sql field type - INTEGER PRIMARY KEY
- city_name  sql field type - text
- datetime (dt) sql field type - text
- min_temp  sql field type - real
- max_temp  sql field type- real

5) Refactor your loop so that instead of just printing it inserts new rows for each day into the table.

6) Write queries to find the day with lowest temperature and the highest.
SELECT dt, MIN(min_temp) FROM weather;
SELECT dt, MAX(max_temp) FROM weather;

7) Write a query to find the average temp.
SELECT ROUND AVG(min_temp + max_temp)/2),2) FROM weather;

Extension:

Expand the code to be able to ask a user for a city, then populate the db with that cities data. 
Then allow the user to find maxes for one city or across all cities.


Further Reading:

http://zetcode.com/db/sqlitepythontutorial/

'''

import requests
import sqlite3


def db_open(filename):
    return sqlite3.connect(filename)#opens http connection and creates new db filename

def db_create(conn):
    c = conn.cursor()#opens connection with weather_database.db  and sets up to perform execute 
    c.execute("CREATE TABLE weather(ID INTEGER PRIMARY KEY, city_name, dt, min_temp, max_temp);")
    conn.commit()#save CREATE TABLE

def db_insert(conn, x):
    c = conn.cursor()#opens open w/ weather_database.db and sets upu to perform c.execute

    c.execute('''INSERT INTO weather (city_name, dt, min_temp, max_temp) VALUES(?,?,?,?)''', ("Berlin", x['dt'],x['temp']['min'],x['temp']['max']))

    conn.commit()#save INSERT table information

def db_close(conn):
    conn.close() # close file and connection

'''

Examples using the above functions:

conn = db_open("weather_database.db")

db_create(conn)

db_insert(conn)

db_close(conn)

'''


url = "http://api.openweathermap.org/data/2.5/forecast/daily?mode=json&units=metric&q=berlin&cnt=16"

json_data = requests.get(url).json()

conn = db_open("weather_database.db")#stores db with and open with specific file name "weather_database.db"


for x in json_data['list']:#loops through json_data key['list'] and prints out 
	db_insert(conn,x)
	print x # x is represented by Berlin
	print x['dt'] #prints out Berlin['dt'] datetime key values
	print x['temp']['min'] #prints out Berlin['temp']['min'] values
	print x['temp']['max'] # prints out Berlin['temp']['max'] values



db_close(conn)#calls db_close function to close HTTP connection




