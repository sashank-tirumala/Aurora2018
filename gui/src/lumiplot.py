import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime
values=[]
times=[]
#time_format = '%H:%M:%S.%f'
data = open("luminositygraph.txt","r")
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
plt.ylabel('Lux')
plt.gcf().autofmt_xdate()
plt.show()

