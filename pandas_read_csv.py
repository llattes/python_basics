# Import the pandas package
import pandas as pd
import matplotlib.pyplot as plt

# So that pandas display all columns
pd.set_option('display.max_columns', None)


def process_and_plot(filename, country):
    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    the_data = pd.DataFrame()

    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        # https://towardsdatascience.com/how-to-use-loc-and-iloc-for-selecting-data-in-pandas-bd09cb4c3d79
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        df_pop_arg = df_urb_pop.loc[df_urb_pop.CountryCode == country].copy()

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_arg["Total Population"], df_pop_arg["Urban population (% of total)"])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_arg.loc[:, 'Total Urban Population'] = [int(pop[0] * pop[1] * 0.01) for pop in pops_list]

        the_data = the_data.append(df_pop_arg)

    # Check out the head of the DataFrame
    print(the_data.head())
    print(the_data.describe())

    # Plot urban population data
    the_data.plot(kind='scatter', x='Year', y='Total Urban Population')
    # Find alternatives to this
    plt.draw()
    plt.pause(0.01)


process_and_plot("datasets/world_ind_pop_data.csv", "ARG")
process_and_plot("datasets/world_ind_pop_data.csv", "DOM")
process_and_plot("datasets/world_ind_pop_data.csv", "GBR")
input("Press enter to continue...")
