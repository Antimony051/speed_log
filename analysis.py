import re
import matplotlib.pyplot as plt

downSpeed=[]
f=open("/home/antimony/Desktop/speed_logs/log","r")
ll=f.readlines()

def extract_val(linetoextract):
    return float(re.findall(":.*,",linetoextract)[0][2:-1])

def mean_n_median_calculator(speedArr):
    mean=(sum(speedArr)/len(speedArr))
    median=(sorted(speedArr)[len(speedArr)//2])
    return(mean,median)

def find_full_mean():
    for x in ll:
        if "downloadSpeed" in x:
            downSpeed.append(extract_val(x))
    speedavg=mean_n_median_calculator(downSpeed)
    print(f'average speed is: {speedavg}')

def find_daily_mean():
    global ll
    speed=[[],[],[],[],[],[],[]]
    days=["sun","mon","tue","wed","thu","fri","sat"]
    for i,x in enumerate(ll):
        if "downloadSpeed" in x:
            day=int(ll[i-2][0])
            speed[day].append(extract_val(x))
    bargraph(speed,days,"daily average","day","speed in Mbps")

def bargraph(inparr,xarr,title,x_label,y_label):
    avgarr=[]
    for x in inparr:
        if len(x)>4:
            avgarr.append(sum(x)/len(x))
        else:
            avgarr.append(0)
    plt.bar(xarr,avgarr )
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def find_hourly_mean():
    global ll
    hourly_speed=[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    hours=[x for x in range(0,24)]
    for i,x in enumerate(ll):
        if "downloadSpeed" in x:
            hour=int(re.findall("..:",ll[i-2])[0][:-1])
            hourly_speed[hour].append(extract_val(x))

    bargraph(hourly_speed,hours,"hourly average","hour","speed in Mbps")

def plot(big_arr):
    axis_x=[]
    axis_y=[]
    for x in big_arr:
        if len(x)>0:
            axis_x.append(big_arr.index(x))
            axis_y.append(round(mean_n_median_calculator(x)[0]))
    plt.plot(axis_x, axis_y)
    plt.show()



print("1: daily mean (average of each day of the week)")
print("2: hourly mean")
print("")
inp=input("enter your choise: ")
if inp=="1":
    find_daily_mean()
if inp=="2":
    find_hourly_mean()
else:
    print(inp,"bad input")
