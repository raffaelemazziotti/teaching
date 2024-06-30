


import pandas as pd
import requests
import io
import plotly.express as px

# Define the URL of the Google Sheets file in CSV format
url = 'https://docs.google.com/spreadsheets/d/1B01BYV7M_jjYUnFPFVJOGsf5C3vrgineJBWQcwUvRsM/export?format=csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(url)

# Display the DataFrame
print( df.head() )


# plotting the scatter chart
fig = px.scatter(df, x="primo_mod", y="secondo_mod",hover_name='Matricola')

# showing the plot
fig.show()
fig.write_html('index.html', include_plotlyjs='cdn')
