import sqlite3
import matplotlib.pyplot as plt
import numpy as np

fontdict1 = {'family': 'TIMES NEW ROMAN', 'color': 'black', 'fontsize': 9}
fontdict2 = {'family': 'TIMES NEW ROMAN', 'color': 'BLUE', 'fontsize': 10}
mode = np.array(['Bowled', 'Caught', 'Caught Behind', 'LBW', 'Stumped', 'Run Out'])

# Virat Kohli
dis = np.array([30, 87, 21, 8, 3, 6])
plt.subplot(3, 3, 1)
plt.pie(dis, labels=mode, shadow=True, autopct='%0.1f%%')
# plt.legend(title='Mode of dismissal',loc="upper left")
plt.title("Virat Kohli")


# MS Dhoni

dis = np.array([17, 66, 14, 5, 3, 9])
plt.subplot(3,3,2)
plt.pie(dis,labels=mode,shadow=True, autopct='%1.1f%%')
plt.title("MS Dhoni")


# David Warner

dis=np.array([25,68,14,4,5,7])
plt.subplot(3,3,3)
plt.pie(dis,labels=mode,shadow=True, autopct='%1.1f%%')
plt.title("David Warner")



# AB DE Villiers

dis=np.array([21,66,9,6,6,13])
plt.subplot(3,3,7)
plt.pie(dis,labels=mode,shadow=True, autopct='%1.1f%%')
plt.title("AB de Villiers")



# Rohit Sharma

dis=np.array([23,99,20,12,3,11])
plt.subplot(3,3,8)
plt.pie(dis,labels=mode,shadow=True, autopct='%1.1f%%')
plt.title("Rohit Sharma")




# Suresh Raina


dis=np.array([16,106,12,6,8,14])
plt.subplot(3,3,9)
plt.pie(dis,labels=mode,shadow=True, autopct='%1.1f%%')
plt.title("Suresh Raina")

plt.suptitle("Mode of dismissal")

plt.show()






