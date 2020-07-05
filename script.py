import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import math
import string

# load rankings data here:

wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')



# write function to plot rankings over time for 1 roller coaster here:

def plot_ranking(dataset, coaster, park_name):
    #Fitlers dataframe by coaster name
    filter = lambda x: all(name.lower() in x.lower() for name in coaster)
    filter2 = lambda x: all(name.lower() in x.lower() for name in park_name)
    #Manipulating data to allow it to be plotted the way we want
    df_coaster1 = dataset.loc[dataset["Name"].apply(filter)]
    df_coaster = df_coaster1.loc[df_coaster1["Park"].apply(filter2)]

    x_values = np.array(df_coaster['Year of Rank'].to_list())
    y_values = np.array(df_coaster['Rank'].to_list())
    y_values_min = df_coaster['Rank'].min()
    y_values_max = df_coaster['Rank'].max()
    x_labels = df_coaster['Year of Rank'].to_list()
    ax = plt.subplot()
    plt.plot(x_values, y_values, marker='o')
    ax.set_yticks((range(y_values_min, y_values_max + 1)))
    ax.set_xticks(x_values)
    ax.set_xticklabels(df_coaster['Year of Rank'].to_list())
    ax.set_title('Ranking of ' + coaster + ' vs Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Rank')
    ax.invert_yaxis()
    plt.show()

plot_ranking(wood, 'Phoenix', 'Knoebels Amusement Resort')

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:

def plot_ranking_two(dataset, coaster1, park_name1, coaster2, park_name2):
    #Fitlers dataframe by coaster name
    filter = lambda x: all(name.lower() in x.lower() for name in coaster1)
    filter2 = lambda x: all(name.lower() in x.lower() for name in park_name1)
    filter3 = lambda x: all(name.lower() in x.lower() for name in coaster2)
    filter4 = lambda x: all(name.lower() in x.lower() for name in park_name2)
    #Manipulating data to allow it to be plotted the way we want
    df_coaster_mid = dataset.loc[dataset["Name"].apply(filter)]
    df_coaster = df_coaster_mid.loc[df_coaster_mid["Park"].apply(filter2)]
    
    df_coaster2_mid = dataset.loc[dataset["Name"].apply(filter3)]
    df_coaster2 = df_coaster2_mid.loc[df_coaster2_mid["Park"].apply(filter4)]
    
    #Setting x and y coordinates for each coaster by filtering dataframe
    x_values_1 = np.array(df_coaster['Year of Rank'].to_list())
    y_values_1 = np.array(df_coaster['Rank'].to_list())
    y_values_1_min = df_coaster['Rank'].min()
    y_values_1_max = df_coaster['Rank'].max()
    x_labels_1 = df_coaster['Year of Rank'].to_list()
    x_values_2 = np.array(df_coaster2['Year of Rank'].to_list())
    y_values_2 = np.array(df_coaster2['Rank'].to_list())
    y_values_2_min = df_coaster2['Rank'].min()
    y_values_2_max = df_coaster2['Rank'].max()
    x_labels_2 = df_coaster2['Year of Rank'].to_list()
    #Finding Mins and Maxs for Axis and Tick Marks
    if (y_values_2_max > y_values_1_max):
        y_max = y_values_2_max
    else:
        y_max = y_values_1_max
        
    if (y_values_2_min < y_values_1_min):
        y_min = y_values_2_min
    else:
        y_min = y_values_1_min
    #Combining both x lists to make one that contains all years 
    x_values = list(x_values_1)
    x_values.extend(x for x in x_values_2 if x not in x_values)
    x_labels = list(x_labels_1)
    x_labels.extend(x for x in x_labels_2 if x not in x_labels)

    #Plot both sets of x and y coordinates
    ax = plt.subplot()
    plt.plot(x_values_1, y_values_1, marker='o')
    plt.plot(x_values_2, y_values_2, marker='o')
    ax.set_yticks((range(y_min, y_max + 1)))
    ax.set_xticks(x_values)
    ax.set_xticklabels(x_labels)
    ax.set_title('Ranking of ' + coaster1 + ' and ' + coaster2 + ' vs Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Rank')
    ax.legend([coaster1, coaster2])
    ax.invert_yaxis()
    plt.show()


plot_ranking_two(wood, 'Phoenix', 'Knoebels Amusement Resort', 'Lightning Racer', 'Hersheypark')

plt.clf()

# write function to plot top n rankings over time here:

def plot_ranking_n(dataset, n):
    
    #Selected subset of dataset where the row had a rank equal to or less than n
    df_ranked = dataset[dataset['Rank'] <= n]
    ax = plt.subplot()
    #Looped through the 'Name' series and plotted the x and y values with year as x and rank as y
    coaster_names = []
    for coaster in set(df_ranked['Name']):
        ranked = df_ranked[df_ranked['Name'] == coaster]
        coaster_names.append(coaster)
        ax.plot(ranked['Year of Rank'], ranked['Rank'], label=coaster, marker='o')
    #Change Plot Visuals
    ax.invert_yaxis()
    ax.set_ylabel('Rank')
    ax.set_xlabel('Year')
    ax.set_title('Coasters Ranked ' + str(n) + ' or Less vs Time')
    #Moves legend outside of plot
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(coaster_names, loc='center left', bbox_to_anchor=(1.0, 0.5))
    
    plt.show()
    

plot_ranking_n(wood, 5)

plt.clf()

# load roller coaster data here:

roller_coasters = pd.read_csv('roller_coasters.csv')

# write function to plot histogram of column values here:

def histogram_plot(dataset, column_name):
    x_values = set(dataset[column_name])
    x_values_filtered = [x for x in x_values if not math.isnan(x)]
    ax = plt.subplot()
    plt.hist(x_values_filtered, bins=20)
    ax.set_ylabel('Frequency')
    ax.set_xlabel(string.capwords(column_name))
    ax.set_title('Roller Coaster ' + string.capwords(column_name) + ' Distribution')
    plt.show()

histogram_plot(roller_coasters, 'speed')

plt.clf()

# write function to plot inversions by coaster at a park here:

def inversion_plot(dataset, park_name):
    
    filter = lambda x: all(name.lower() in x.lower() for name in park_name)
    df = dataset.loc[dataset['park'].apply(filter)]
    ax = plt.subplot()
    ax.set_xlabel('Roller Coaster Name')
    ax.set_ylabel('Number of Inversion')
    ax.set_title(park_name + ' Inverted Roller Coasters')
    plt.bar(df['name'], df['num_inversions'])
    plt.xticks(rotation=90)
    plt.show()

inversion_plot(roller_coasters, 'Disneyland Park')
plt.clf()

# write function to plot pie chart of operating status here:

def operating_status(dataset):
    operating = dataset[dataset['status'] == 'status.operating']
    closed = dataset[dataset['status'] == 'status.closed.definitely']
    counts = [len(operating), len(closed)]
    ax = plt.subplot()
    ax.set_title('Operating vs Closed Roller Coasters')
    plt.pie(counts, autopct='%0.1f%%', labels=['Operating', 'Closed'])
    plt.show()

operating_status(roller_coasters)


plt.clf()

# write function to create scatter plot of any two numeric columns here:

def scatterplot(dataset, column1, column2):
    x = dataset[column1]
    y = dataset[column2]
    ax = plt.subplot()
    plt.scatter(x, y)
    ax.set_title(string.capwords(column2) + ' vs ' + string.capwords(column1))
    ax.set_ylabel(string.capwords(column2))
    ax.set_xlabel(string.capwords(column1))
    plt.show()

scatterplot(roller_coasters, 'speed', 'length')




plt.clf()
