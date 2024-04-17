# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
my_countries = ['Afghanistan', 'Zimbabwe', 'Dominican Republic', 'Malaysia']
nscountries = ['Unites States', 'Greenland', 'Mexico', 'Brazil', 'Argentina', 'Chile']
eurocountries = ['Finland', 'Portugal', 'Ireland', 'Sweden', 'Scotland', 'France']
asiacountries = ['China', 'North Korea', 'South Korea', 'Thailand', 'Vietnam', 'Japan']
afrcountries = ['Ghana', 'Nigeria', 'Mozambique', 'South Africa', 'Kenya', 'Ethiopia']
# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)  # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

# Plot the data on a line graph
for c in unique_countries:
    if c in my_countries:
        # match country to one of our we want to look at and get a list of years
        years = df[df['Entity'] == c]['Year']

        # match country to one of our we want to look at and get a list of electriciy values
        sum_elec = df[df['Entity'] == c]['Access']

        plt.plot(years, sum_elec, label=c, marker="o", linestyle=":")

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()

for c in unique_countries:
    if c in nscountries:
        # match country to one of our we want to look at and get a list of years
        years = df[df['Entity'] == c]['Year']

        # match country to one of our we want to look at and get a list of electriciy values
        sum_elec = df[df['Entity'] == c]['Access']

        plt.plot(years, sum_elec, label=c, marker=">", linestyle="-.")

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()

for c in unique_countries:
    if c in eurocountries:
        # match country to one of our we want to look at and get a list of years
        years = df[df['Entity'] == c]['Year']

        # match country to one of our we want to look at and get a list of electriciy values
        sum_elec = df[df['Entity'] == c]['Access']

        plt.plot(years, sum_elec, label=c, marker="^", linestyle="--")

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()

for c in unique_countries:
    if c in asiacountries:
        # match country to one of our we want to look at and get a list of years
        years = df[df['Entity'] == c]['Year']

        # match country to one of our we want to look at and get a list of electriciy values
        sum_elec = df[df['Entity'] == c]['Access']

        plt.plot(years, sum_elec, label=c, marker="s", linestyle=":")

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()

for c in unique_countries:
    if c in afrcountries:
        # match country to one of our we want to look at and get a list of years
        years = df[df['Entity'] == c]['Year']

        # match country to one of our we want to look at and get a list of electriciy values
        sum_elec = df[df['Entity'] == c]['Access']

        plt.plot(years, sum_elec, label=c, marker="*", linestyle="-")

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()
