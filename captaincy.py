
import numpy as np
import matplotlib.pyplot as plt
# dhoni,rohit,kohli,warner,dk,iyer,gilchrist,sourav

won = [110, 70, 58, 34, 22, 23, 35, 17]
lost = [78, 46, 64, 29, 22, 18, 39, 25]

# win percentage:
wp = []
lp = []
x = 0
for x in range(len(won)):
    w = won[x] / (won[x] + lost[x]) * 100
    l = 100.00 - w
    wp.append(w)
    lp.append(l)
k=len(won)
skippers = ['MS DHONI', 'Rohit Sharma', 'Virat Kohli', 'David Warner', 'Dinesh Karthik', 'Shreyas Iyer',
            'Adam Gilchrist', 'Sourav Ganguly']
plt.bar(skippers,won,width=0.4,label="Won")
plt.bar(skippers,lost,width=0.4,label="Lost",bottom=won)
plt.show()
