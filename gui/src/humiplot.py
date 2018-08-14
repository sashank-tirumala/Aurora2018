import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime
values=[]
times=[]
data = open("humigraph.txt","r")
x=data.readline()
x=x.split(",")
while(x[0]!=""):
    values.append(x[0])
    d=x[1].split("\n")
    times.append(d[0])
    x=data.readline()
    x=x.split(",")
data.close()
dates = md.datestr2num(times)
plt.plot_date(dates,values,linestyle='solid',marker='None')
plt.ylabel('Humidity')
plt.xlabel('Time')
plt.show()