import pandas as pd
from datetime import datetime
df=pd.read_csv("Opposition_time_messiers.csv")
df=df.drop([df.columns[0]],axis=1)
lis=[]
for i in df['Opp_date']:
    date_as_list=i.split()
    month={"JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,"JUL":7,"AUG":8,"SEP":9,"OCT":10,"NOV":11,"DEC":11}
    dates=''
    date_in_fomat=str(month[date_as_list[0]])+"/"+date_as_list[1]+"/"+date_as_list[2]
    deta=datetime.strptime(date_in_fomat, '%m/%d/%Y')
    
    lis.append(deta)
    
 
df["Opp_date"]=lis
df=df.sort_values(by=["Opp_date","Brightness"])
df.to_csv("OrderedData.csv")