import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:

wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')



# write function to plot rankings over time for 1 roller coaster here:

def plot_ranking(dataset, coaster):
    
    filter = lambda x: all(name.lower() in x.lower() for name in coaster)
    df_coaster = dataset.loc[dataset["Name"].apply(filter)]
    x_values = range(0, dataset['Year of Rank'].nunique())
    y_values = df_coaster['Rank'].to_list()
    rev = y_values.reverse()
    x_labels = df_coaster['Year of Rank'].to_list()
    print(x_values)
    print(y_values)
    print(x_labels)
    print(rev)
    
    ax = plt.subplot()
    plt.plot(x_values, y_values)
    ax.set_yticks(y_values)
    ax.set_xticks(x_values)
    ax.set_xticklabels(df_coaster['Year of Rank'].to_list())
    ax.set_xlabel('Year')
    ax.set_ylabel('Rank')
    plt.show()

plot_ranking(wood, 'Boulder Dash')






plt.clf()

# write function to plot rankings over time for 2 roller coasters here:










plt.clf()

# write function to plot top n rankings over time here:










plt.clf()

# load roller coaster data here:



# write function to plot histogram of column values here:










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
