import matplotlib.pyplot as plt
import pandas as pd


#defining file read function
def readfile(file_name):
    """
    This function reads an excel file and transpose it.
    Parameter: file_name

    Returns
    -------
    Dataframes(original and transpose)
    """
    d = pd.read_excel(file_name)
    d = d.drop(['Series Name', 'Series Code','Country Code'], axis=1).dropna()
    d_trans = d.transpose()
    return d, d_trans

#defining bar graph function
def bar_graph(d_name, title, fig_name, y_label):
    """
    This function plots a bargrapgh.
    Parameters: d_name, title, fig_name, y_label
    """
    plt.figure(figsize=(17, 18))
    yrs = ["1990 [YR1990]",
             "1994 [YR1994]", "1998 [YR1998]", "2002 [YR2002]","2006 [YR2006]","2010 [YR2010]","2014 [YR2014]", "2018 [YR2018]"]
    d_name.plot(x="Country Name", y=yrs, kind='bar')
    plt.title(title, fontsize=12)
    plt.xlabel('Countries', fontsize=10)
    plt.xticks(fontsize=10, rotation=90)
    plt.ylabel(y_label, fontsize=10)
    plt.yticks(fontsize=10)
    plt.xticks(rotation=45)
    plt.legend(frameon=False, fontsize=10)
    #plt.savefig(fig_name, bbox_inches="tight", dpi=200)
    plt.show()

#defining line graph function
def line_graph(d_name, title, fig_name, y_label):
    """
    This function plots a linegrapgh.
    Parameters: d_name, title, fig_name, y_label
    """
    plt.figure(figsize=(17, 18))
    yrs = ["1990 [YR1990]",
             "1994 [YR1994]", "1998 [YR1998]", "2002 [YR2002]","2006 [YR2006]","2010 [YR2010]","2014 [YR2014]", "2018 [YR2018]"]
    d_name.plot(x="Country Name", y=yrs, kind='line')
    plt.title(title, fontsize=12)
    plt.xlabel('Countries', fontsize=10)
    plt.xticks(range(0, len(d_name.index)),
               d_name["Country Name"], rotation=90)
    plt.ylabel(y_label, fontsize=10)
    plt.yticks(fontsize=10)
    plt.xticks(rotation=45)
    plt.legend(frameon=False, fontsize=10)
    #plt.savefig(fig_name, bbox_inches="tight", dpi=200)
    plt.show()


    

# Reading the excel file 
population, population_trans = readfile(
    "C:/Users/babur/Desktop/Assignment 2/Population total.xlsx")
emission, emission_trans = readfile(
    "C:/Users/babur/Desktop/Assignment 2/CO2 emissions (metric tons per capita).xlsx")
coal, coal_trans = readfile(
    "C:/Users/babur/Desktop/Assignment 2/Electricity production from coal sources.xlsx")
consumption, consumption_trans = readfile("C:/Users/babur/Desktop/Assignment 2/Electric power consumption (kWh per capita).xlsx")


# Calling the function for plotting the line graph
line_graph(coal, "Electricity production from coal sources",
          "Electricity production from coal sources.png", "percentage of population")
line_graph(consumption , "Electric power consumption",
              "Electric power consumption Linegraph.png", "kWh per capita")

# Calling the function for plotting the bar graph
bar_graph(population, "Total population",
         "population Bargraph.png","world")
bar_graph(emission, "CO2 emission",
         "CO2 emission Bargraph.png","kt")

