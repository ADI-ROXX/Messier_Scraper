import requests
from bs4 import BeautifulSoup
c=1
import pandas as pd
dic={"Number":[0],"Brightness":[0]}
a=pd.DataFrame(dic)
for i in range(1,111):
    try :
        url="https://en.wikipedia.org/wiki/Messier_"+str(i)
        r = requests.get(url)
        h=str(r.content)
        val=h.split("Apparent magnitude")[2].split("infobox-data\">")[1].split("<")[0]
        a.loc[len(a.index),:]=[i,val]
        c+=1
        print(val)
    except:
        a.loc[len(a.index),:]=[i,"Null"]
        print("null")
a.to_csv("App_mag.csv")
