import requests
import csv
import urllib
import time
import ast
import json
import datetime
filehead="city,state,station,LAT,Lon,Elev,date,time,windchillm, wind_direction', windchilli,hail,thunder,pressurei,snow,pressurem,fog,conds,tornado,humidty,tempi,tempm,dewptm,rain,dewpti"



STNAME=[]
ID=[]
with open("stations.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')    
    m=0
    for row in readCSV:
        if m>0:
            STNAME.append(row[2])
            ID.append(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+","+row[5])
                
        m=m+1
Weather=open('weather.csv','w')
Weather.write(filehead+"\n")
#https://www.wunderground.com/history/airport/KSBA/2012/10/1/MonthlyHistory.html?format=1&_ga=2.118175817.1171146497.1504041222-1699946922.1504041222
#b9221cfef3d4a359
date1 = '2016-01-01'
date2 = '2017-08-29'
start = datetime.datetime.strptime(date1, '%Y-%m-%d')
end = datetime.datetime.strptime(date2, '%Y-%m-%d')
step = datetime.timedelta(days=1)
DATE=[]
while start <= end:
    DATE.append(str(start.date()).replace("-",""))
    start += step
    
#header="http://api.wunderground.com/api/113327932bd5a372/history_20170508/q/"+Name+".json"

for k in range(0,len(STNAME)):
    for i in range(0,len(DATE)):
        if i%30==0:
            header="http://api.wunderground.com/api/b9221cfef3d4a359/history_"+DATE[i]+"/q/"+STNAME[k]+".json"
            Location=header
            r = requests.get(Location)
            outPut=r.content
            d = json.loads(outPut)
            if i%20==0:
                print i
    
            for j in range(0,len(d['history']['observations'])):
        #    print d['history']['observations'][j]
    
                Footer=ID[k]+","+d['history']['observations'][j]['date']['year']+d['history']['observations'][j]['date']['mon']+d['history']['observations'][j]['date']['mday']+","+ d['history']['observations'][j]['date']['hour']+":"+d['history']['observations'][j]['date']['min']+","+d['history']['observations'][j]['windchillm']+","+d['history']['observations'][j]['wdird']+","+d['history']['observations'][j]['windchilli']  +","+d['history']['observations'][j]['hail']    +","+d['history']['observations'][j]['thunder']    +","+d['history']['observations'][j]['pressurei']    +","+d['history']['observations'][j]['snow']    +","+d['history']['observations'][j]['pressurem']    +","+d['history']['observations'][j]['fog']   +","+d['history']['observations'][j]['conds']        +","+d['history']['observations'][j]['tornado']    +","+d['history']['observations'][j]['hum']    +","+d['history']['observations'][j]['tempi']    +","+d['history']['observations'][j]['tempm']    +","+d['history']['observations'][j]['dewptm']    +","+d['history']['observations'][j]['rain']    +","+d['history']['observations'][j]['dewpti']    
                Weather.write( Footer+"\n")
    
    
        print i    