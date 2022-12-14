# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:57:58 2022

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_urpop = pd.read_excel("C:/Users/HP/OneDrive - University of Hertfordshire/ADS1 Assignment 2/Urban Population.xlsx")
df_co2   = pd.read_excel("C:/Users/HP/OneDrive - University of Hertfordshire/ADS1 Assignment 2/CO2 Emmission.xlsx")
df_ghge  = pd.read_excel("C:/Users/HP/OneDrive - University of Hertfordshire/ADS1 Assignment 2/Total Greenhouse gas emissions.xlsx")
df_meth  = pd.read_excel("C:/Users/HP/OneDrive - University of Hertfordshire/ADS1 Assignment 2/Methane emissions.xlsx")
a = pd.concat([df_urpop,df_co2,df_ghge,df_meth],ignore_index=True)
print(a)

def read_(a):
    """

    Parameters
    ----------
    a : TYPE
        DESCRIPTION.

    Returns
    -------
    o_data : TYPE
        DESCRIPTION.
    trans : TYPE
        DESCRIPTION.

    """
    print(a.describe())
    o_data = a.dropna()
    o_datas = o_data.drop(columns=["Series Name","Series Code","Country Code"])
    trans = np.transpose(o_datas)
    return o_data,trans
    
    
o_data,trans = read_(a)    

print(o_data)
print(trans)
    
    
    


def urban_population(o_data):
    plt.figure(figsize=(30,17))
    o_datas = o_data.groupby(["Series Name"])
    print(o_datas.describe())
    d = o_datas.get_group("Urban population (% of total population)")
    pop = np.arange(len(d["Country Code"]))
    width = 0.20
    plt.title("Urban Population", size=50)
    plt.bar(pop-0.2,d["2012 [YR2012]"], width,label="2012",align="edge")
    plt.bar(pop-0.1,d["2014 [YR2014]"], width,label="2014",align="edge")
    plt.bar(pop+0.0,d["2016 [YR2016]"], width,label="2016",align="edge")
    plt.bar(pop+0.1,d["2018 [YR2018]"], width,label="2018",align="edge")
    plt.bar(pop+0.2,d["2020 [YR2020]"], width,label="2020",align="edge")
    plt.xticks(pop,d["Country Name"], fontsize=30)
    plt.xlabel("Country", size=25)
    plt.legend(prop={"size":25})
    plt.savefig("Urban Population bar plot.png")
    plt.show()
urban_population(o_data)


def green_house(o_data):
    plt.figure(figsize=(30,17))
    o_datas = o_data.groupby(["Series Name"])
    print(o_datas.describe())
    d = o_datas.get_group("Total greenhouse gas emissions (kt of CO2 equivalent)")
    pop = np.arange(len(d["Country Code"]))
    width = 0.20
    plt.title("Total greenhouse gas emissions (kt of CO2 equivalent)", size=50)
    plt.bar(pop-0.2,d["2012 [YR2012]"], width,label="2012",align="edge")
    plt.bar(pop-0.1,d["2014 [YR2014]"], width,label="2014",align="edge")
    plt.bar(pop+0.0,d["2016 [YR2016]"], width,label="2016",align="edge")
    plt.bar(pop+0.1,d["2018 [YR2018]"], width,label="2018",align="edge")
    plt.bar(pop+0.2,d["2020 [YR2020]"], width,label="2020",align="edge")
    plt.xticks(pop,d["Country Name"], fontsize=30)
    plt.xlabel("Country", size=25)
    plt.legend(prop={"size":25})
    plt.savefig("Total greenhouse gas emissions (kt of CO2 equivalent) bar plot.png")
    plt.show()

green_house(o_data)
def co2(o_data):
    o_datas = o_data.groupby(["Series Name"])
    print(o_datas.describe())
    d = o_datas.get_group("Total greenhouse gas emissions (kt of CO2 equivalent)")
    print(d)
    data1 = d.loc[:,"1990 [YR1990]":"2015 [YR2015]"]
    data1 = np.transpose(data1)
    print(data1)
    data1 = data1.rename(columns={20:"Argentina",21:"Belgium",22:"Canada",23:"China",24:"France",25:"Germany",26:"India",27:"Israel",28:"Singapore",29:"Ukraine"})
    plt.figure(figsize=(10,10))
    plt.title("CO2 emission", size=40)
    plt.plot(data1.index,data1["Argentina"],label="Argentina")
    plt.plot(data1.index,data1["Belgium"],label="Belgium")
    plt.plot(data1.index,data1["Canada"],label="Canada")
    plt.plot(data1.index,data1["China"],label="China")
    plt.plot(data1.index,data1["France"],label="France")
    plt.plot(data1.index,data1["Germany"],label="Germany")
    plt.plot(data1.index,data1["India"],label="India")
    plt.plot(data1.index,data1["Israel"],label="Israel")
    plt.plot(data1.index,data1["Singapore"],label="Singapore")
    plt.plot(data1.index,data1["Ukraine"],label="Ukraine")
    plt.legend()
    plt.savefig("Total greenhouse gas emissions lineplot.png")

co2(o_data)

def Methane_emissions(o_data):
    o_datas = o_data.groupby(["Series Name"])
    print(o_datas.describe())
    d = o_datas.get_group("Methane emissions (kt of CO2 equivalent)")
    print(d)
    data1 = d.loc[:,"1990 [YR1990]":"2015 [YR2015]"]
    data1 = np.transpose(data1)
    print(data1)
    data1 = data1.rename(columns={30:"Argentina",31:"Belgium",32:"Canada",33:"China",34:"France",35:"Germany",36:"India",37:"Israel",38:"Singapore",39:"Ukraine"})
    plt.figure(figsize=(10,10))
    plt.title("Methane_emissions", size=40)
    plt.plot(data1.index,data1["Argentina"],label="Argentina")
    plt.plot(data1.index,data1["Belgium"],label="Belgium")
    plt.plot(data1.index,data1["Canada"],label="Canada")
    plt.plot(data1.index,data1["China"],label="China")
    plt.plot(data1.index,data1["France"],label="France")
    plt.plot(data1.index,data1["Germany"],label="Germany")
    plt.plot(data1.index,data1["India"],label="India")
    plt.plot(data1.index,data1["Israel"],label="Israel")
    plt.plot(data1.index,data1["Singapore"],label="Singapore")
    plt.plot(data1.index,data1["Ukraine"],label="Ukraine")
    plt.legend()
    plt.savefig("Methane_emissions lineplot.png")


Methane_emissions(o_data)
print("methan")