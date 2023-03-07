import requests
from bs4 import BeautifulSoup
# import pandas as pd
url = "http://people.tamu.edu/~kevinkrisciunas/ra_dec_sun_2023.html"
ht=requests.get(url)
cont=ht.content
soup=BeautifulSoup(cont,'html.parser')
stri=soup.find('pre').get_text()
values=stri[105:]
values=values.replace(',','')
values="Date,RA(hms),Dec(dms)\n"+values
values=values.replace("           ",'')
values=values.replace("       ",",")

print(values)
file=open("Sun_values.csv","w")
file.write(values)
file.close()


