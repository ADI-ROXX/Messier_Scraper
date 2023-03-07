import requests
from bs4 import BeautifulSoup
import threading
import pandas as pd
dic={"Messier":[0],"RA_h":[0],"RA_m":[0],"RA_s":[0],"Dec_d":[0],"Dec_m":[0],"Dec_s":[0]}
df=pd.DataFrame(dic)
def threader(a,b):
    for i in range(a,b):
        if i==102:
            continue
        try:
            url="https://en.wikipedia.org/wiki/Messier_"+str(i)
            r = requests.get(url)
            h=str(r.content)


            a=str(h)







            soup=BeautifulSoup(h,"html.parser")
            a=str(soup)
            a=a.replace(r"\xe2\x88\x92","-")
            a=a.replace(r"\xc2\xb0","d")
            a=a.replace(r"\xe2\x80\xb2","\'")
            a=a.replace(r"\xe2\x80\xb3","\"")
            # print(a.split("external text")[1].split("rel=\"nofollow\">")[1].split("<sup>h</sup>")[1].split("<sup>m</sup>")[1].split("<sup>s</sup>")[1])
            ra_h=float(a.split("external text")[1].split("rel=\"nofollow\">")[1].split("<sup>h</sup>")[0])
            ra_m=a.split("external text")[1].split("rel=\"nofollow\">")[1].split("<sup>h</sup>")[1].split("<sup>m</sup>")[0]
            ra_s=a.split("external text")[1].split("rel=\"nofollow\">")[1].split("<sup>h</sup>")[1].split("<sup>m</sup>")[1].split("<sup>s</sup>")[0]
            # val=h.split("Apparent magnitude")[2].split("infobox-data\">")[1].split("<")[0]
            # print(ra_m)

            dec=a.split("external text")[1].split("rel=\"nofollow\">")[1].split("<sup>h</sup>")[1].split("<sup>m</sup>")[1].split("<sup>s</sup>,")[1]
            # print(dec)
            dec_d=float(dec.split("d")[0])
            dec_m=float(dec.split("d")[1].split("\'")[0])
            dec_s=float(dec.split("d")[1].split("\'")[1].split("\"")[0])
            df.loc[len(df.index)]=[i,ra_h,ra_m,ra_s,dec_d,dec_m,dec_s]
            print(ra_h,ra_m,ra_s,dec_d,dec_m,dec_s,sep=" ")

        except:
            df.loc[len(df.index)]=[i,"Null","Null","Null","Null","Null","Null"]#,"Null","Null","Null","
# print(h.split("Apparent magnitude")[2])#.split("infobox-data\">")[1])#.split("<")[0])
# print(h.split("Apparent magnitude")[2].split("infobox-data\">")[1].split("<")[0])
if __name__ =="__main__":
    # creating thread
#     for i in range(1,111,10):
    t1 = threading.Thread(target=threader, args=(1,41,))
    
    
    t2 = threading.Thread(target=threader, args=(41,81,))
    t3 = threading.Thread(target=threader, args=(81,111,))
    
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    t3.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    t2.join()
    t3.join()
    # wait until thread 2 is completely executed
df=df.sort_values(by=["Messier"])
# df.drop([df.columns[0]],axis=1,inplace=True)
colum=df['Messier']
# df.to_csv("coordadf_mess.csv")
for i in range(1,len(colum)):
    colum[i]="M"+str(colum[i])
df['Messier']=colum
df.to_csv("coord_mess.csv")
print(df)
print("Program finished.")