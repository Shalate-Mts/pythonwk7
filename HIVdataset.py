import pandas as pd           # For data handling
import matplotlib.pyplot as plt  # For static plots
import seaborn as sns         # For statistical visualizations
import plotly.express as px   # For interactive plots
import geopandas as gpd

#Task 1
#reading the dataset available
try:
    df = pd.read_csv("hiv_prevalence.csv")
    print("Dataset read successfully.")
except Exception as e:
    print("Error reading dataset:", e)

#Task 2
#Calling the df to display the table
df.head()
#Check for missing values
df.isnull().sum()
#data per mean, median, standard deviation
df.describe()
#Grouping data per year
annual_deaths_by_year = df.groupby('Year of estimate').size().reset_index(name='Annual deaths from HIV/AIDS')
print('annual deaths per year',annual_deaths_by_year)

#Task3
# Creating the line chart

# Set the style for better visualization
sns.set_style("whitegrid")

# Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(annual_deaths_by_year['Year of estimate'], 
         annual_deaths_by_year['Annual deaths from HIV/AIDS'], 
         marker='o', 
         linestyle='-', 
         linewidth=2,
         color='#E41A1C',  # Red color for HIV/AIDS data
         markersize=8)

# Customize the plot
plt.title('Annual Deaths from HIV/AIDS Over Time', fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Deaths', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Add data labels for each point
for x, y in zip(annual_deaths_by_year['Year of estimate'], annual_deaths_by_year['Annual deaths from HIV/AIDS']):
    plt.text(x, y + (y * 0.02), f'{y:,}', ha='center', fontsize=9)

# Format y-axis with comma separators for thousands
plt.gca().get_yaxis().set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))

# Adjust layout and show plot
plt.tight_layout()
plt.show()

# Create a simple bar chart
# Sort by HIV cases in descending order and select top 10
top10 = df.sort_values(by='Number of people with HIV/AIDS', ascending=False).head(10)

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(top10['Country/Region'], top10['Number of people with HIV/AIDS'], color='crimson')
plt.xlabel('Country')
plt.ylabel('Number of people')
plt.title('Top 10 Countries with Highest Number of HIV Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Create a pie chart
# Sort by Adult prevalence of HIV/AIDS in descending order and select top 10
top10 = df.sort_values(by='Adult prevalence of HIV/AIDS', ascending=False).head(10)
#change % into float
top10['Adult prevalence of HIV/AIDS'] = top10['Adult prevalence of HIV/AIDS'].str.replace('%', '').astype(float)

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(top10['Adult prevalence of HIV/AIDS'], labels=top10['Country/Region'], autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Countries with Adult prevalence of HIV/AIDS')
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.tight_layout()
plt.show()