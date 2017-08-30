import requests
import urllib
import time
import ast
States=['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WU','WY']
header="State,Name,Website,Handle"
Unis=open("ListofUnis.csv", "w")
Unis.write(header+"\n")
#States=["IA"]
for p in range(0,len(States)):
    A=States[p]
    
    header="http://www.univsearch.com/state-search.php?state="
    Location=header+A #Songs
    r = requests.get(Location)
    outPut=r.content
    i=0
    m=0
    while i>-1:
        append=""
        footer=States[p]
        ProfileLink=outPut.find('<a href="/profile.php')
        ProfileLinkX=outPut[ProfileLink:].find('" title="For more information about ')
        
        A='Click here"'
        i=outPut.find(A)
        
        
        X=outPut[i:].find("</a></td>")
        
        
        
        
        if len(outPut[i+len(A)+1:i+X]) < 50 and (outPut[i+len(A)+1:i+X].find("ILIFF")<0 and outPut[i+len(A)+1:i+X].find("iliff")<0):
            B=outPut[i+len(A)+1:i+X]
            footer=footer+","+B
            print B
            websitelink= "http://www.univsearch.com/"+outPut[ProfileLink+len('<a href="')+1:ProfileLink+ProfileLinkX]
            try:
                data=requests.get(websitelink).content
                
            except:
                data=""
            UniSiteI= data.find('For more information about this Institution, visit')
            if UniSiteI > -1:
                UniSiteX=data[UniSiteI:].find('" target="_blank"')
                uniwebsite= data[UniSiteI+96:UniSiteI+UniSiteX]
                footer=footer+","+uniwebsite
                
                print uniwebsite
                try: 
                    data=requests.get(uniwebsite).content
                except:
                    data=""
                unitwitter=data.find('twitter.com')
                uniend=data[unitwitter+len('twitter.com'):].find('"')
                if unitwitter > -1:
                   #print data[unitwitter+len('twitter.com/'):unitwitter+len('twitter.com')+uniend]
                    append=data[unitwitter+len('twitter.com/'):unitwitter+len('twitter.com')+uniend]
                    append=append.replace("#!/","/")
                    if len(append)>0 and append[0]=="/":
                        append=append[1:]
                    if append.find("/")>-1:
                        append=append[:append.find("/")]
                    print append
                    if append.find("@")<0:
                        footer=footer+','+append                
                        Unis.write(footer+"\n")
                else:
                    B=B.replace(" ","%20")
                    while True:
                        try:  
                            Handle=requests.get("https://twitter.com/search?f=users&q="+B+"&src=typd").content
                            break
                        except:
                            print "Wait!"
                            time.sleep(60)
                            
                    C='data-screen-name="'
                    j=Handle.find(C)
                    Y=Handle[j+2:].find(' data-user-id=')
                    if len(Handle[j+len(C):j+Y-4]) < 50:
                        append=Handle[j+len(C):j+Y-4]
                        footer=footer+','+append+',404'                
                        Unis.write(footer+"\n")
                       #print Handle[j+len(C):j+Y-4]
            if UniSiteI < 0:
                B=B.replace(" ","%20")
                while True:
                    try:  
                        Handle=requests.get("https://twitter.com/search?f=users&q="+B+"&src=typd").content
                        break
                    except:
                        print "Wait!"
                        time.sleep(60)
                         
                C='data-screen-name="'
                j=Handle.find(C)
                Y=Handle[j+2:].find(' data-user-id=')
                if len(Handle[j+len(C):j+Y-4]) < 50:
                    append=Handle[j+len(C):j+Y-4]
                    footer=footer+',,'+append+',404'                
                                     
                    Unis.write(footer+"\n")
                        #print Handle[j+len(C):j+Y-4]
        print footer
        if len(outPut[i+len(A)+1:i+X]) > 50:
            break
        outPut=outPut[i+len(A)+1:]

