import sqlite3
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect("Batting.db")
cur = conn.cursor()
# # cur.execute("Create Table IF NOT EXISTS MOSTRUNS(POS integer,player_name text,Innings integer,RUNS integer)")
# cur.execute("Insert into MOSTRUNS values(1,'Virat Kohli',184,5878)")
# cur.execute("Insert into MOSTRUNS values(2,'Suresh Raina',189,5368)")
# cur.execute("Insert into MOSTRUNS values(3,'David Warner',142,5254)")
# cur.execute("Insert into MOSTRUNS values(4,'Rohit Sharma',195,5230)")
# cur.execute("Insert into MOSTRUNS values(5,'Shikar Dhawan',175,5197)")
# cur.execute("Insert into MOSTRUNS values(6,'AB de Villiers',156,4849)")
# cur.execute("Insert into MOSTRUNS values(7,'Chris Gayle',131,4772)")
# cur.execute("Insert into MOSTRUNS values(8,'MS Dhoni',182,4632)")
# cur.execute("Insert into MOSTRUNS values(9,'Robin Uthappa',182,4607)")
# cur.execute("Insert into MOSTRUNS values(10,'Gautam Gambhir',152,4217)")
# cur.execute("Insert into MOSTRUNS values(11,'Ajinkya Rahane',140,3933)")
# cur.execute("Insert into MOSTRUNS values(12,'Shane Watson',141,3874)")
# cur.execute("Insert into MOSTRUNS values(13,'Dinesh Karthik',184,3823)")
# cur.execute("Insert into MOSTRUNS values(14,'Ambati Rayudu',151,3659)")
# cur.execute("Insert into MOSTRUNS values(15,'Manish Pandey',135,3268)")
conn.commit()
batsmen = []
runs = []

for item in cur.execute("Select Distinct player_name,RUNS from MOSTRUNS"):
    pname, run = item
    batsmen.append(pname)
    runs.append(run)

batter = np.array(batsmen)
orangecap = np.array(runs)
plt.ylabel("Batsman")
plt.xlabel("Runs Scored")
plt.title("Highest Run Getters")
plt.barh(batter, orangecap)
plt.show()
# cur.close()
# conn.close()

# ****Season-wise performance of some top batsmen[virat kohli,suresh raina,MS Dhoni,AB de Villiers,Rohit Sharma,David Warner]


year = np.array(['2017', '2018', '2019', '2020'])
vk = np.array([308, 530, 464, 466])
sr = np.array([442, 445, 383, 0])
msd = np.array([290, 455, 416, 200])
abd = np.array([216, 480, 442, 454])
rg = np.array([333, 286, 405, 332])
dw = np.array([641, 0, 692, 548])

fontdict1 = {'family': 'TIMES NEW ROMAN', 'color': 'black', 'fontsize': 9}
fontdict2 = {'family': 'TIMES NEW ROMAN', 'color': 'BLUE', 'fontsize': 10}

# Virat Kohli:

plt.xlabel("Season", fontdict=fontdict1)
plt.ylabel("Runs Scored", fontdict=fontdict1)

plt.subplot(3, 3, 1)
plt.plot(year, vk, marker='o')
plt.title("Virat Kohli", fontdict=fontdict2)



# Suresh Raina

plt.xlabel("Season", fontdict=fontdict1)
plt.ylabel("Runs Scored", fontdict=fontdict1)

plt.subplot(3, 3, 2)
plt.plot(year, sr, marker='o')
plt.title("Suresh Raina", fontdict=fontdict2)


# MS Dhoni

plt.xlabel("Season", fontdict=fontdict1)
plt.ylabel("Runs Scored", fontdict=fontdict1)

plt.subplot(3,3,3)
plt.plot(year, msd, marker='o')
plt.title("MS Dhoni", fontdict=fontdict2)


# Rohit Sharma

plt.xlabel("Season", fontdict=fontdict1)
plt.ylabel("Runs Scored", fontdict=fontdict1)

plt.subplot(3,3,7)
plt.plot(year, rg, marker='o')
plt.title("Rohit Sharma", fontdict=fontdict2)


# AB de Villiers

plt.xlabel("Season", fontdict=fontdict1)
plt.ylabel("Runs Scored", fontdict=fontdict1)

plt.subplot(3,3,8)
plt.plot(year, abd, marker='o')
plt.title("AB de Villiers", fontdict=fontdict2)


# David Warner

plt.xlabel("Season", fontdict=fontdict1)
plt.ylabel("Runs Scored", fontdict=fontdict1)

plt.subplot(3,3,9)
plt.plot(year, dw, marker='o')
plt.title("David Warner", fontdict=fontdict2)

plt.suptitle("Season-Wise performance of batsmen:")
plt.show()


#********** Top Run scorers of 2020 season******************


#cur.execute("CREATE TABLE IF NOT EXISTS MAX2020(pos ineger,player_name text,Innings integer,RUNS integer,AVG real )")
# cur.execute("INSERT INTO MAX2020 Values(1,'KL Rahul',14,670,55.83)")
# cur.execute("INSERT INTO MAX2020 Values(2,'Shikar Dhawan',17,618,44.14)")
# cur.execute("INSERT INTO MAX2020 Values(3,'David Warner',16,548,39.14)")
# cur.execute("INSERT INTO MAX2020 Values(4,'Shreyas Iyer',17,519,34.60)")
# cur.execute("INSERT INTO MAX2020 Values(5,'Ishan Kishan',13,516,57.33)")
# cur.execute("INSERT INTO MAX2020 Values(6,'Quinton de Kock',16,503,35.92)")
# cur.execute("INSERT INTO MAX2020 Values(7,'Suryakumar Yadav',15,480,40.00)")
# cur.execute("INSERT INTO MAX2020 Values(9,'Virat Kohli',15,466,42.36)")
# cur.execute("INSERT INTO MAX2020 Values(10,'AB de Villiers',14,454,45.40)")
# cur.execute("INSERT INTO MAX2020 Values(8,'Devdutt Padikkal',14,473,31.14)")
conn.commit()

batsmen=[]
RUNS=[]
for item in cur.execute("SELECT distinct player_name,RUNS from MAX2020"):
    pname,runs=item
    batsmen.append(pname)
    RUNS.append(runs)


batter=np.array(batsmen)
scores=np.array(RUNS)
plt.xlabel("Runs Scored",fontdict=fontdict1)
plt.ylabel("Player Name",fontdict=fontdict1)
plt.title("Best Batsmen of IPL 2020",fontdict=fontdict2)
plt.barh(batter,scores,height=0.1)
plt.show()

batsmen=[]
AVG=[]
for item in cur.execute("SELECT distinct player_name,AVG from MAX2020"):
    pname,avg=item
    batsmen.append(pname)
    AVG.append(avg)

color=np.array([11,21,31,41,51,61,71,81,91,76,88])
plt.xlabel("Batsman",fontdict=fontdict1)
plt.ylabel("Average",fontdict=fontdict1)
plt.title("Average of the top 10 run getters in IPL 2020:")
plt.scatter(batsmen,AVG,c=color,cmap='viridis')
plt.colorbar()
plt.show()


cur.execute("Create TABLE IF NOT EXISTS LOKESHRAHUL(TEAM text,Innings INTEGER,RUNS integer,AVG real)")
# cur.execute("INSERT INTO LOKESHRAHUL VALUES('CSK',8,292,36.50)")
# cur.execute("INSERT INTO LOKESHRAHUL VALUES('DC',9,211,23.44)")
# cur.execute("INSERT INTO LOKESHRAHUL VALUES('KKR',9,297,37.13)")
# cur.execute("INSERT INTO LOKESHRAHUL VALUES('MI',12,580,64.44)")
# cur.execute("INSERT INTO LOKESHRAHUL VALUES('RR',10,481,60.13)")
# cur.execute("INSERT INTO LOKESHRAHUL VALUES('RCB',8,371,74.20)")
# cur.execute("INSERT INTO LOKESHRAHUL VALUES('SRH',8,300,42.86)")
conn.commit()
teams=[]
runs=[]
avg=[]

for item in cur.execute("SELECT  TEAM, RUNS, AVG FROM  LOKESHRAHUL"):
    t,r,a=item
    teams.append(t)
    runs.append(r)
    avg.append(a)


teams=np.array(teams)
runs=np.array(runs)
avg=np.array(avg)

plt.xlabel("TEAMS",fontdict=fontdict1)
plt.ylabel("RUNS SCORED",fontdict=fontdict1)
plt.title("KL RAHUL Performance against each team",fontdict=fontdict2)
plt.plot(teams,runs,marker='o')
plt.show()
plt.xlabel("TEAMS",fontdict=fontdict1)
plt.ylabel("Average")
plt.plot(teams,avg,marker='o')
plt.show()



