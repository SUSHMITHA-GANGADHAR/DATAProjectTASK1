'''Create a bar chart or histogram to
visualize the distribution of a categorical or continuous variable,
such as the distribution of ages or genders in a population.'''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/DELL/Downloads/task1.csv', skiprows=4)

# Process data and calculate mean population by year
years = [str(year) for year in range(1999, 2020)]
mean_population_by_year = data[years].mean()
fig, axes = plt.subplots(2, 1, figsize=(8, 10))

# Bar chart
sns.barplot(x=mean_population_by_year.index, y=mean_population_by_year, palette="husl", ax=axes[0])
axes[0].set_title('Average Population by Year (Bar Chart)')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Average Population')
axes[0].grid(True)

# Histogram
sns.histplot(mean_population_by_year, kde=False, color='pink', edgecolor='black', ax=axes[1])
axes[1].set_title('Distribution of Average Population (Histogram)')
axes[1].set_xlabel('Average Population')
axes[1].set_ylabel('Frequency')
axes[1].grid(True)

fig.subplots_adjust(hspace=1)
plt.tight_layout()
plt.show()
