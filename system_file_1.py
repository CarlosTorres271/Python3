

'''
comment code June 18, 2018 .. back in the lab and shit

command line basics:

python3 
(to get version)


quit()
(back to home dir)

pip3 install sqlalchemy
(install library on python3)

pip3 list:
beautifulsoup4 (4.6.0)
bs4 (0.0.1)
certifi (2018.4.16)
chardet (3.0.4)
et-xmlfile (1.0.1)
idna (2.6)
jdcal (1.4)
numpy (1.14.3)
openpyxl (2.5.3)
pandas (0.23.0)
pip (9.0.3)
python-dateutil (2.7.3)
pytz (2018.4)
requests (2.18.4)
selenium (3.12.0)
setuptools (39.0.1)
six (1.11.0)
SQLAlchemy (1.2.8)
urllib3 (1.22)


'''
'''
# nflplaybyplay2015
# print columns

import numpy as np
import pandas as pd

data = pd.read_csv('NFLPlaybyPlay2015.csv')

print(data.columns)

https://stackoverflow.com/questions/49265260/pandas-unrecognized-by-python3/49265845#49265845

print("test version")
import sys

print(sys.version_info)

'''


import sqlite3

import numpy as np
import pandas as pd


#import pandas as pd
#data = pd.read_csv('NFLPlaybyPlay2015.csv')
# print(data.columns)
# retrieve the index of the DataFrame
# print(data.index)
# print first five rows
# print(data.head())
# print distinct
# data.GameID.unique()
data = pd.read_csv('sd_employers.csv')

# print(data.head())
print(data.columns)

# create sqlite db

conn = sqlite3.connect('jobs.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS SD_EMP")
# Create table
c.execute('''CREATE TABLE SD_EMP
             (COMPANY text, 
             ADDRESS text, 
             CITY text, 
             DESC TEXT, 
             EE TEXT)'''
          )

#c.execute('''select * from SD_EMP''')

# Insert a row of data
c.execute("INSERT INTO SD_EMP VALUES ('field1_data','field2_data','field3_data','field4_data','b')")
c.execute("INSERT INTO SD_EMP VALUES ('field1_data','field2_data','field3_data','field4_data','c')")
c.execute("INSERT INTO SD_EMP VALUES ('field1_data','field2_data','field3_data','field4_data','d')")


c.executemany("INSERT INTO SD_EMP (Company, Address, City, DESC, EE) VALUES(?,?,?,?,?)",
              list(data[['Company', 'Address', 'City', 'Desc', 'EE']].to_records(index=False)))


# for row in c.execute('SELECT * FROM SD_EMP ORDER BY Company'):
# print(row)

for row in c.execute('SELECT Company, length(Company) FROM SD_EMP where length(Company) > 10 ORDER BY length(Company) DESC'):
    print(row)

conn.close()
