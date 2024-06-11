import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("world_population.csv")

# Knowing what kind of columns we have is a good way to help us think of how to look through our data. Although it might just be easy to 
# do the same using excel for an easier understanding of our columns headers. 
print("\nColumn headers:")
print(df.columns, "\n")

# Calculate the total population for each continent in 2022 rounding the percentages
continent_population = df.groupby('Continent')['2022 Population'].sum().reset_index()
total_world_population = df['2022 Population'].sum()
continent_population['Population Percentage'] = (continent_population['2022 Population'] / total_world_population) * 100
continent_population['Population Percentage'] = continent_population['Population Percentage'].round(2)
continent_population_sorted = continent_population.sort_values(by='Population Percentage', ascending=False)
print(continent_population_sorted)


# Calculate total world population in 2022
total_population_2022 = df['2022 Population'].sum()
print(" ")
print("Earth's Population in 2022:", total_population_2022,"\n")


# creating a pie chart
plt.figure(figsize=(10, 8))
plt.pie(continent_population['2022 Population'], labels=continent_population['Continent'], autopct='%1.1f%%', startangle=140)
plt.title(f"Earth's Population in 2022: {total_population_2022:,}")
plt.legend(title='Continents', loc='upper left')
plt.show()

# Count the number of unique countries in each continent
countries_per_continent = df.groupby('Continent')['Country/Territory'].nunique()
print("Total unique countries per continent:\n", countries_per_continent, "\n")

# 4. Countries with the least and highest population in 2022
idx_least_population = df['2022 Population'].idxmin()
idx_highest_population = df['2022 Population'].idxmax()
country_least_population = df.loc[idx_least_population, 'Country/Territory']
country_highest_population = df.loc[idx_highest_population, 'Country/Territory']
print("\nCountry with the Least Population:", country_least_population)
print("Country with the Highest Population:", country_highest_population, "\n")

# 5. Population of countries in North America and South America
na_sa_countries = df[df['Continent'].isin(['North America', 'South America'])]
na_sa_population = na_sa_countries[['Country/Territory', '2022 Population']]
na_sa_population_sorted = na_sa_population.sort_values(by='2022 Population', ascending=False)
print("\nPopulation of Countries in North America and South America:")
print(na_sa_population_sorted)


# 8. Create a quick graph with the 5 countries with the most km2

top_5_countries_area = df.nlargest(5, 'Area (km²)')
plt.figure(figsize=(10, 6))
plt.bar(top_5_countries_area['Country/Territory'], top_5_countries_area['Area (km²)'], color='skyblue')
plt.title('Top 5 Countries by Area (km²)')
plt.xlabel('Country')
plt.ylabel('Area (km²)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# HYPOTHESIS

# For the last line of code, I found it interesting how
# Countries like Russia and Canada are not in the top 3 
# of countries with the highest population in 2022 despite
# the mention countries being way larger in territory. We can deduse
# land does not equal to larger population. There are a lot more factors
# that come into consideration when understanding why an area is densily
# more populated than others. It is also interesting the fact that Oceania as a continent
# is not even in the top 5 of population by continent, in fact it is the last one on the list
# DESPITE having more countries than South America.
# NOTE: I did not verify how many countries there are per continent since there might be extra territories taken/not taken into consideration. I solely based on the dataset
# Sourced from Kaggle. 
