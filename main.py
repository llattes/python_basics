import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gapminder = pd.read_csv('datasets/gapminder.csv')

gdp_cap = gapminder['gdp_cap'].to_list()
life_exp = gapminder['life_exp'].to_list()
np_population = gapminder['population'].to_numpy()

# Express population in millions and then double the values for plot impact
np_population = np_population / 1000000
np_population = np_population * 2

continent_colour = {
    'Asia': 'red',
    'Europe': 'blue',
    'Africa': 'black',
    'Americas': 'green',
    'Oceania': 'yellow',
}

# Use the dictionary to map continent to a specific colour
country_colour = gapminder['cont'].map(continent_colour).to_list()

# Basic scatter plot, log scale; s is a size argument for the scatter plot
plt.scatter(gdp_cap, life_exp, s = np_population, c = country_colour, alpha = 0.8)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# Additional customizations
plt.text(12800, 75, 'Argentina', weight="bold")
plt.text(5000, 73, 'China', weight="bold")
plt.text(2450, 65, 'India', weight="bold")
plt.text(43000, 78, 'USA', weight="bold")

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
