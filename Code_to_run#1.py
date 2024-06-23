import requests
from bs4 import BeautifulSoup
import threading
import pandas as pd
from queue import Queue
from time import time
dic={"Messier":[0],"RA_h":[0],"RA_m":[0],"RA_s":[0],"Dec_d":[0],"Dec_m":[0],"Dec_s":[0]}
df=pd.DataFrame(dic)

def threader():
    while not q.empty():
        i=q.get()
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
            ra_h=float(a.split("external text")[1].split("rel=\"nofollow\">")[1].split("<sup>h</sup>")[0])
            ra_m=a.split("external text")[1].split("rel=\"nofollow\">")[1].split("<sup>h</sup>")[1].split("<sup>m</sup>")[0]
            ra_s=a.split("external text")[1].split("rel=\"nofollow\">")[1].split("<sup>h</sup>")[1].split("<sup>m</sup>")[1].split("<sup>s</sup>")[0]
            dec=a.split("external text")[1].split("rel=\"nofollow\">")[1].split("<sup>h</sup>")[1].split("<sup>m</sup>")[1].split("<sup>s</sup>,")[1]
            dec_d=float(dec.split("d")[0])
            dec_m=float(dec.split("d")[1].split("\'")[0])
            dec_s=float(dec.split("d")[1].split("\'")[1].split("\"")[0])
            df.loc[len(df.index)]=[i,ra_h,ra_m,ra_s,dec_d,dec_m,dec_s]
        except:
            df.loc[len(df.index)]=[i,"Null","Null","Null","Null","Null","Null"]#,"Null","Null","Null","
if __name__ =="__main__":
    start=time()
    q = Queue()
    for j in range(1,111):
        q.put(j)
    n_threads = eval(input("Enter the number of threads: "))
    threads = []
    for i in range(n_threads) :
        t1 = threading.Thread(target=threader )
        threads.append(t1)
    for i in threads:
        i.start()
    for j in threads:
        j.join()
    
    
df=df.sort_values(by=["Messier"])
# df.drop([df.columns[0]],axis=1,inplace=True)
colum=df['Messier']
# df.to_csv("coordadf_mess.csv")
for i in range(1,len(colum)):
    colum[i]="M"+str(colum[i])
df['Messier']=colum
df.to_csv("coord_mess.csv")
# print(df)
print("Program finished.")
end=time()
print("Time elapsed=", end-start)