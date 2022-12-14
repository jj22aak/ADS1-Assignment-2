
# importing different libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""reading excel files of Urban Population,CO2 emissions, greenhouse gas emission
    and methane emissions into pandas data frame"""
    
df_urpop = pd.read_excel("C:/Users/HP/OneDrive - University of Hertfordshire/ADS1 Assignment 2/Urban Population.xlsx")
df_co2   = pd.read_excel("C:/Users/HP/OneDrive - University of Hertfordshire/ADS1 Assignment 2/CO2 Emmission.xlsx")
df_ghge  = pd.read_excel("C:/Users/HP/OneDrive - University of Hertfordshire/ADS1 Assignment 2/Total Greenhouse gas emissions.xlsx")
df_meth  = pd.read_excel("C:/Users/HP/OneDrive - University of Hertfordshire/ADS1 Assignment 2/Methane emissions.xlsx")

# concatenating the mix of excel files
df = pd.concat([df_urpop,df_co2,df_ghge,df_meth],ignore_index=True)
#printing concatenated data
print(df)

def read_file(df):
    """
    function read_file is read with an argument df
    and return mod_data and trans

    """
    # calculating and printing statistical datas like mean
    print(df.describe())
     
    #removing missing values
    mod_data = df.dropna()
    
    #removing the columns
    mod_datas = mod_data.drop(columns=["Series Name","Series Code","Country Code"])
    
    #interchanging row and column elements
    trans = np.transpose(mod_datas)
    return mod_data,trans
    
    
mod_data,trans = read_file(df)    

print(mod_data)
print(trans)
     
#for plotting bar graph of Urban Population
def urban_population(mod_data):
    """

    function urban_population is read with argument mod_data

    """
    #creating new figure
    plt.figure(figsize=(30,17))
    
    #splitting data into group
    mod_datas = mod_data.groupby(["Series Name"])
    #finding statistical data
    print(mod_datas.describe())
    d = mod_datas.get_group("Urban population (% of total population)")
    #evenly arrangin the data
    pop = np.arange(len(d["Country Code"]))
    width = 0.20
    #giving the title
    plt.title("Urban Population", size=50)
    #plotting bar graph
    plt.bar(pop-0.2,d["2012 [YR2012]"], width,label="2012",align="edge")
    plt.bar(pop-0.1,d["2014 [YR2014]"], width,label="2014",align="edge")
    plt.bar(pop+0.0,d["2016 [YR2016]"], width,label="2016",align="edge")
    plt.bar(pop+0.1,d["2018 [YR2018]"], width,label="2018",align="edge")
    plt.bar(pop+0.2,d["2020 [YR2020]"], width,label="2020",align="edge")
    plt.xticks(pop,d["Country Name"], fontsize=30)
    #labelling the x axis
    plt.xlabel("Country", size=25)
    plt.legend(prop={"size":25})
    #saving the figure
    plt.savefig("Urban Population bar plot.png")
    #displaying the figure
    plt.show()
    
urban_population(mod_data)

#function for plotting bar graph of greenhouse gas emission
def green_house(mod_data):
    
    plt.figure(figsize=(30,17))
    mod_datas = mod_data.groupby(["Series Name"])
    print(mod_datas.describe())
    
    d = mod_datas.get_group("Total greenhouse gas emissions (kt of CO2 equivalent)")
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

green_house(mod_data)

#function for plotting line graph of CO2 emissions
def co2(mod_data):
    
    mod_datas = mod_data.groupby(["Series Name"])
    print(mod_datas.describe())
    d = mod_datas.get_group("Total greenhouse gas emissions (kt of CO2 equivalent)")
    print(d)
    #accessing group of years from 1990 to 2015
    data1 = d.loc[:,"1990 [YR1990]":"2015 [YR2015]"]
    data1 = np.transpose(data1)
    print(data1)
    #renaming
    data1 = data1.rename(columns={20:"Argentina",21:"Belgium",22:"Canada",23:"China",24:"France",25:"Germany",26:"India",27:"Israel",28:"Singapore",29:"Ukraine"})
    plt.figure(figsize=(10,10))
    plt.title("CO2 emission", size=40)
    #plotting line graph for 10 countries
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
    #describing the elements
    plt.legend()
    plt.savefig("Total greenhouse gas emissions lineplot.png")

co2(mod_data)

def Methane_emissions(mod_data):
    mod_datas = mod_data.groupby(["Series Name"])
    print(mod_datas.describe())
    d = mod_datas.get_group("Methane emissions (kt of CO2 equivalent)")
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


Methane_emissions(mod_data)
