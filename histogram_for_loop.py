

import sqlite3
import seaborn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

seaborn.set()  # set plot style

conn = sqlite3.connect('nfl.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS QB")
c.execute("DROP TABLE IF EXISTS QB_Weekly_Stats")

print("Passers")
print("______________________")
c.execute('''
                    CREATE TABLE QB AS
                    SELECT Passer,
                    COUNT(Passer) AS Count1
                    FROM 
                    NFL_TBL
                    Where
                    PASSER <> 'NA'
                    GROUP BY
                    Passer
                    HAVING 
                    COUNT(PASSER) >500
                    ORDER BY 
                    COUNT(Passer) desc
                    ''')


# print list of tables
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

# next step create a table of game_date, passer, and sum of yards
print("Passers")
print("______________________")
# SELECT QUERY
c.execute('''
                    create table QB_Weekly_Stats as 
                    select
                    passer,
                    gameid,
                    sum(yardsgained) as SumOfYardsGained
                    from 
                    NFL_TBL
                    where 
                    (
                        passer  <>  'NA'
                            and
                        playtype like '%pass%'
                            and
                        passoutcome like '%complete%'
                    )
                    group by
                    gameid,
                    passer
                    order by
                    passer,
                    gameid
                    ''')

# create a dataframe from a sql query
df = pd.read_sql_query(
    '''SELECT *
                            FROM
                            QB_Weekly_Stats
                            WHERE
                            PASSER LIKE '%DALTON%'
                         ''', conn)

# print(df)

print("--------------list--------------")
list1 = ['bortles', 'rivers', 'brees']

for x in list1:
    sql2 = "select * from qb_weekly_stats where passer like '%" + x + "%';"
    df2 = pd.read_sql_query(sql2, conn)
    yards = np.array(df2['SumOfYardsGained'])
    plt.hist(yards)
    plt.title(x)
    plt.xlabel('xlabel')
    plt.ylabel('ylabel')
    plt.show()

conn.close()
