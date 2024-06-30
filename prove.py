


import pandas as pd
import requests
import io
import plotly.express as px
from plotly.subplots import make_subplots

# Define the URL of the Google Sheets file in CSV format
url = 'https://docs.google.com/spreadsheets/d/1B01BYV7M_jjYUnFPFVJOGsf5C3vrgineJBWQcwUvRsM/export?format=csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(url)
df['psize'] = 10
# Display the DataFrame
df['voto_finale'] = df['voto_finale'].apply(lambda x: x if x!='30eL' else 31)
df['voto_finale'] = df['voto_finale'].astype(int)
print( df.dtypes )

fig = make_subplots(rows=1, cols=2, subplot_titles=("Parziale", "Distribuzione Voti"))

# plotting the scatter chart
fig1 = px.scatter(df, x="primo_mod", y="secondo_mod", hover_name='Matricola',size='psize',size_max=10)
for trace in fig1.data:
    fig.add_trace(trace, row=1, col=1)

fig2 = px.histogram(df, x='voto_finale',range_x=[18,31])
for trace in fig2.data:
    fig.add_trace(trace, row=1, col=2)
#fig.update_layout(
#    width=800,
#    height=600,
#)

fig.show()
fig.write_html('index.html', include_plotlyjs='cdn')

