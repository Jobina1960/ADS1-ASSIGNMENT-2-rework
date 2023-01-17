import matplotlib.pyplot as plt
import pandas as pd


#defining file read function
def readfile(file_name):
    """
    

    Parameters
    ----------
    file_name : string
        full address of the file to be read.

    Returns
    -------
    d : dataframe
        input data as dataframe.
    d_trans : dataframe
        Transpose of the input dataframe.

    """
    
    #reading the file
    d = pd.read_excel(file_name)
    
    #removing unwanted columns
    d = d.drop(['Series Name', 'Series Code','Country Code'], axis = 1).dropna()
    
    #taking transpose
    d_trans = d.transpose()
    
    return d, d_trans

#defining bar graph function
def bar_graph(d_name, title, fig_name, y_label):
    """
    This function plots a bargrapgh from given input data

    Parameters
    ----------
    d_name : string
        name of dataframe.
    title : string
        Name of image to be saved as.
    fig_name : string
        Title of the graph.
    y_label : string
        label of y axis.

    Returns
    -------
    None.

    """
    
    plt.figure(figsize = (17, 18))
    yrs = ["1990 [YR1990]", "1994 [YR1994]", "1998 [YR1998]", "2002 [YR2002]","2006 [YR2006]","2010 [YR2010]","2014 [YR2014]", "2018 [YR2018]"]
    d_name.plot(x = "Country Name", y = yrs, kind ='bar')
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
    

    Parameters
    ----------
    d_name : dataframe
        dataframe to be used in plotting.
    title : string
        Name of image to be saved as.
    fig_name : string
        Title of the graph.
    y_label : string
        label of y axis.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(17, 18))
    yrs = ["1990 [YR1990]", "1994 [YR1994]", "1998 [YR1998]", "2002 [YR2002]","2006 [YR2006]","2010 [YR2010]","2014 [YR2014]", "2018 [YR2018]"]
    d_name.plot(x = "Country Name", y = yrs, kind ='line')
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
consumption, consumption_trans = \
    readfile("C:/Users/babur/Desktop/Assignment 2/Electric power consumption (kWh per capita).xlsx")


# Calling the function for plotting the line graph
line_graph(coal, "Electricity production from coal sources",
          "Electricity production from coal sources.png", 
          "Electricity production from coal sources (% of total)")

line_graph(consumption , "Electric power consumption",
              "Electric power consumption Linegraph.png", "kWh per capita")

# Calling the function for plotting the bar graph
bar_graph(population, "Total population",
         "population Bargraph.png","world")
bar_graph(emission, "CO2 emission",
         "CO2 emission Bargraph.png","CO2 emissions (metric tons per capita)")

