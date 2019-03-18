# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path)
data=data.rename({"Total":"Total_Medals"},axis=1,)
data.head(10)
#Code starts here



# --------------
#Code starts here
import pandas as pd
import numpy as np


data["Better_Event"]=np.where(data["Total_Summer"]>data["Total_Winter"],"Summer","Winter")
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
better_event="Summer"


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries[:-1]

def top_ten(df,col_name):
    country_list=df.nlargest(10,col_name)
    return country_list["Country_Name"]

top_10=list(top_ten(top_countries,"Total_Medals"))
top_10_summer=list(top_ten(top_countries,"Total_Summer"))
top_10_winter=list(top_ten(top_countries,"Total_Winter"))

print(top_10)
print(top_10_summer)
print(top_10_winter)

def IntersecOfSets(arr1, arr2, arr3): 
    s1 = set(arr1) 
    s2 = set(arr2) 
    s3 = set(arr3) 
    
    set1 = s1.intersection(s2)       
    result_set = set1.intersection(s3) 
      
    common = list(result_set) 
    return common
common=IntersecOfSets(top_10,top_10_summer,top_10_winter)


# --------------
#Code starts here
summer_df=data[data["Country_Name"].isin(top_10_summer)]
winter_df=data[data["Country_Name"].isin(top_10_winter)]
top_df=data[data["Country_Name"].isin(top_10)]

plt.title("Summer olympis")
plt.xlabel("Country  name")
plt.ylabel("Medals counts")
plt.bar(summer_df["Country_Name"],summer_df["Total_Medals"])


plt.title("Winter olympis")
plt.xlabel("Country  name")
plt.ylabel("Medals counts")
plt.bar(winter_df["Country_Name"],winter_df["Total_Medals"])


plt.title("olympis")
plt.xlabel("Country  name")
plt.ylabel("Medals counts")
plt.bar(top_df["Country_Name"],top_df["Total_Medals"])


# --------------
#Code starts here
Golden_Ratio=round(summer_df["Gold_Summer"]/summer_df["Total_Summer"],2)
summer_max_ratio=Golden_Ratio.max()
summer_country_gold=data.iloc[Golden_Ratio.idxmax()][0]
print(summer_country_gold)

Golden_Ratio=round(winter_df["Gold_Winter"]/winter_df["Total_Winter"],2)
winter_max_ratio=Golden_Ratio.max()
winter_country_gold="Soviet Union"
print(winter_country_gold)

Golden_Ratio=round(top_df["Gold_Total"]/top_df["Total_Medals"],2)
top_max_ratio=Golden_Ratio.max()
top_country_gold=data.iloc[Golden_Ratio.idxmax()][0]
print(top_country_gold)


# --------------
#Code starts here
data_1=data[:-1]
data_1["Total_Points"]=data_1["Gold_Total"]*3+data_1["Silver_Total"]*2+data_1["Bronze_Total"]*1
most_points=data_1["Total_Points"].max()
best_country=data_1.iloc[data_1["Total_Points"].idxmax()][0]


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]


best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")


