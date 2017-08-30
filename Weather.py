#https://www.wunderground.com/about/faq/US_cities.asp?MR=1
#Station                 State  ID    Lat    Lon   Elev  WMO
file = open('Stations.ss', 'r') 
stations=open('stations.csv','w')
stations.write("City,State,ID,Lat,Lon,Elev,WMO"+"\n")
for line in file: 
    line=line.replace("\n","")
    city=line[0:30]
    while city[-1]==" ":
        city=city[:-1]
    
    Rest= line[30:].replace("  "," ").replace("  "," ").split(" ")
    state=Rest[0]
    ID=Rest[1]
    Lat=Rest[2]
    Lon=Rest[3]
    Elev=Rest[4]
    WMO=Rest[5]
    stations.write(city+","+state+","+ID+","+Lat+","+Lon+","+Elev+","+WMO+"\n")
    