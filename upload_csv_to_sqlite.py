
# python3
# pydev
import csv
import sqlite3

conn = sqlite3.connect('nfl.db')
c = conn.cursor()

try:
    c.execute("DROP TABLE IF EXISTS NFL_TBL")
    conn.commit()
except sqlite3.Error as err:
    print('sqlite3 error')

# create table 64 columns -for now text format type on all fields
c.execute('''CREATE TABLE NFL_TBL
             (
                ID text, 
                Date text, 
                GameID text, 
                Drive text, 
                qtr text, 
                down text, 
                time text, 
                TimeUnder text, 
                TimeSecs text, 
                PlayTimeDiff text, 
                SideofField text, 
                yrdln text, 
                yrdline100 text, 
                ydstogo text, 
                ydsnet text, 
                GoalToGo text, 
                FirstDown text, 
                posteam text, 
                DefensiveTeam text, 
                PlayAttempted text, 
                YardsGained text, 
                sp text, 
                Touchdown text, 
                ExPointResult text, 
                TwoPointConv text, 
                DefTwoPoint text, 
                Safety text, 
                PuntResult text, 
                PlayType text, 
                Passer text, 
                PassAttempt text, 
                PassOutcome text, 
                PassLength text, 
                PassLocation text, 
                InterceptionThrown text, 
                Interceptor text, 
                Rusher text, 
                RushAttempt text, 
                RunLocation text, 
                RunGap text, 
                Receiver text, 
                Reception text, 
                ReturnResult text, 
                Returner text, 
                BlockingPlayer text, 
                Tackler1 text, 
                Tackler2 text, 
                FieldGoalResult text, 
                FieldGoalDistance text, 
                Fumble text, 
                RecFumbTeam text, 
                RecFumbPlayer text, 
                Sack text, 
                ChallengeReplay text, 
                ChalReplayResult text, 
                AcceptedPenalty text, 
                PenalizedTeam text, 
                PenalizedPlayer text, 
                PenaltyYards text, 
                PosTeamScore text, 
                DefTeamScore text, 
                ScoreDiff text, 
                AbsScoreDiff text, 
                Season text
                 )'''
          )
# 64 col
csv_reader = csv.reader(open('NFLplaybyplay2015.csv', encoding='utf-8'),
                        delimiter=',')


rd = (csv_reader)

# insert into from csv reader
for rd in csv_reader:
    c.execute('''INSERT INTO  NFL_TBL VALUES (?,?,?,?,?,?,?,?,
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', rd)


conn.commit()

# count of rows
print("____________count of rows_____________")
for row in c.execute(
    '''
                    SELECT Count(*) FROM NFL_tbl
                    '''
):
    print(row)

# drop table
c.execute("DROP TABLE IF EXISTS TEAMS")

# create table list of teams
for row in c.execute('''
                    CREATE TABLE TEAMS AS
                    SELECT DISTINCT 
                    posteam AS TEAM_ACR
                    FROM 
                    NFL_TBL 
                    ORDER BY 
                    posteam'''):
    print(row)

conn.commit()

# add columns
c.execute('''ALTER TABLE TEAMS ADD COLUMN ''' + 'CITY' + ''' TEXT''')
c.execute('''ALTER TABLE TEAMS ADD COLUMN ''' + 'TEAM_NAME' + ''' TEXT''')

# clean up outlier
c.execute(
    "DELETE FROM TEAMS WHERE TEAM_ACR IS NULL or TEAM_ACR = '' OR TEAM_ACR like '%posteam%';")
conn.commit()

# list of team acronymns
print("____________list of team acr_____________")
for row in c.execute('''
                    SELECT DISTINCT 
                    *
                    FROM 
                    TEAMS 
                    ORDER BY 
                    TEAM_ACR'''):
    print(row)

# print list of tables
print("____________list of tables_____________")

try:
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())
except sqlite3.Error as err:
    print('sqlite3 error')

conn.close()
