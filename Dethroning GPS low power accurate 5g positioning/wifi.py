
import math
from math import pi
import pandas as pd
import csv
from math import pow
import numpy as np
import matplotlib.pyplot as plot

rssi_arr_1=np.genfromtxt('/content/Wifi_ap_0.5.csv',delimiter=',')
rssi_arr_2=np.genfromtxt('/content/Wifi_ap_1.csv',delimiter=',')
rssi_arr_3=np.genfromtxt('/content/Wifi_ap_1.5.csv',delimiter=',')

n=1.5
a=-36
def calc_dist(rss,a,n):
    cal_d= pow(10,((rss-a)/(-10*n)))
    return cal_d


dist_arr_1=[]
dist_arr_2=[]
dist_arr_3=[]
weight_arr_1=[]
weight_arr_2=[]
weight_arr_3=[]

for  x in rssi_arr_1:
  cal_d=calc_dist(x,a,n)
  dist_arr_1=np.append(dist_arr_1,cal_d)
  weight_arr_1=np.append(weight_arr_1,(1/cal_d))

for  x in rssi_arr_2:
  cal_d=calc_dist(x,a,n)
  dist_arr_2=np.append(dist_arr_2,cal_d)
  weight_arr_2=np.append(weight_arr_2,(1/cal_d))

for  x in rssi_arr_3:
  cal_d=calc_dist(x,a,n)
  dist_arr_3=np.append(dist_arr_3,cal_d)
  weight_arr_3=np.append(weight_arr_3,(1/cal_d))

rssi_var1=np.nanvar(rssi_arr_1)
rssi_var2=np.nanvar(rssi_arr_2)
rssi_var3=np.nanvar(rssi_arr_3)

print("variance of rssi of APs are respectively(in dBm)=",rssi_var1,rssi_var2,rssi_var3)

mean_1=np.nanmean(dist_arr_1)
mean_2=np.nanmean(dist_arr_2)
mean_3=np.nanmean(dist_arr_3)
wmean_1=np.nanmean(weight_arr_1)
wmean_2=np.nanmean(weight_arr_2)
wmean_3=np.nanmean(weight_arr_3)

arr_weight=[wmean_1,wmean_2,wmean_3]

print("calculated distance from ref.point 1=",mean_1)
print("calculated distance from ref.point 2=",mean_2)
print("calculated distance from ref.point 3=",mean_3)


fig = plot.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)


ax1.plot(dist_arr_1)
ax1.axhline(y=mean_1, color='g', linestyle='-')
ax1.axhline(y=0.5, color='r', linestyle='-')

ax2.plot(dist_arr_2)
ax2.axhline(y=mean_2, color='g', linestyle='-')
ax2.axhline(y=1, color='r', linestyle='-')

ax3.plot(dist_arr_3)
ax3.axhline(y=mean_3, color='g', linestyle='-')
ax3.axhline(y=1.5, color='r', linestyle='-')
plot.show()

x=[2,1.5,0]
y=[0,1,0]

def wcl(weight,x,y):
    xiwi=np.multiply(x,weight)
    yiwi=np.multiply(y,weight)
    xw=np.sum(xiwi)/np.sum(weight)
    yw=np.sum(yiwi)/np.sum(weight)
    return xw,yw

res_x,res_y=wcl(arr_weight,x,y) 
print("resultant location coordinates(x,y)=",res_x,res_y)

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  
print("distance between calculated and setup coordinates in meteres=", calculateDistance(1.5, 0, res_x, res_y) )