import sqlite3
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect("Bowling.db")
cur = conn.cursor()


#******BEST BOWLERS IN THE HISTORY OF THE IPL*************************************"

cur.execute(
    "CREATE TABLE IF NOT EXISTS MAXWICKETS(POS integer,player_name text,overs real,AVG real,economy real,wickets integer)")

cur.execute("INSERT INTO MAXWICKETS VALUES(1,'Lasith Malinga',471.1,19.80,7.14,170)")
cur.execute("INSERT INTO MAXWICKETS VALUES(2,'Amit Mishra',526.5,24.19,7.87,160)")
cur.execute("INSERT INTO MAXWICKETS VALUES(3,'Piyush Chawla',541.4,27.32,7.87,156)")
cur.execute("INSERT INTO MAXWICKETS VALUES(4,'Dwayne Bravo',452,24.81,8.40,153)")
cur.execute("INSERT INTO MAXWICKETS VALUES(5,'Harbhajan Singh',562.2,26.44,7.05,150)")
cur.execute("INSERT INTO MAXWICKETS VALUES(6,'Ravichandran Ashwin',471.1,26.81,6.87,138)")
cur.execute("INSERT INTO MAXWICKETS VALUES(7,'Bhuvneshwar Kumar',449.3,23.91,7.23,136)")
cur.execute("INSERT INTO MAXWICKETS VALUES(8,'Sunil Narine',464.2,24.77,6.77,127)")
cur.execute("INSERT INTO MAXWICKETS VALUES(9,'Yuzvendra Chahal',359,22.84,7.69,121)")
cur.execute("INSERT INTO MAXWICKETS VALUES(10,'Umesh Yadav',420.2,30.07,8.51,119)")
cur.execute("INSERT INTO MAXWICKETS VALUES(11,'Ravindra Jadeja',452.1,30.43,7.67,114)")
cur.execute("INSERT INTO MAXWICKETS VALUES(12,'Jasprit Bumrah',352.4,23.52,7.40,111)")
cur.execute("INSERT INTO MAXWICKETS VALUES(13,'Sandeep Sharma',342.5,24.27,7.71,109)")
cur.execute("INSERT INTO MAXWICKETS VALUES(14,'Ashish Nehra',318,23.53,7.84,106)")
cur.execute("INSERT INTO MAXWICKETS VALUES(15,'Vinay Kumar',353.3,28.24,8.39,105)")
conn.commit()

bowler=[]
Dis=[]
for item in cur.execute("Select distinct player_name,wickets from MAXWICKETS"):
    pname,wickets=item
    bowler.append(pname)
    Dis.append(wickets)


bowler=np.array(bowler)
Dis=np.array(Dis)

plt.barh(bowler,Dis,height=0.3,fc='green',ec='black')
plt.show()

cur.execute(
    "CREATE TABLE IF NOT EXISTS MAXWICKETS2020(pos integer,player_name text,wickets,economy real)")

cur.execute("INSERT INTO MAXWICKETS2020 VALUES(1,'Kagiso Rabada',30,8.34)")
cur.execute("INSERT INTO MAXWICKETS2020 VALUES(2,'Jasprit Bumrah',27,6.73)")
cur.execute("INSERT INTO MAXWICKETS2020 VALUES(3,'Trent Boult',25,7.97)")
cur.execute("INSERT INTO MAXWICKETS2020 VALUES(4,'Anrich Nortje',22,8.39)")
cur.execute("INSERT INTO MAXWICKETS2020 VALUES(5,'Yuzvendra Chahal',21,7.08)")
cur.execute("INSERT INTO MAXWICKETS2020 VALUES(6,'Rashid Khan',20,5.37)")
cur.execute("INSERT INTO MAXWICKETS2020 VALUES(7,'Jofra Archer',20,6.55)")
cur.execute("INSERT INTO MAXWICKETS2020 VALUES(8,'Mohammad Shami',20,8.57)")
cur.execute("INSERT INTO MAXWICKETS2020 VALUES(9,'Varun Chakravarthy',17,6.84)")
cur.execute("INSERT INTO MAXWICKETS2020 VALUES(10,'T Natarajan',16,8.02)")
