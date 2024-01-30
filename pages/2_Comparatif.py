import streamlit as st
import pandas as pd
import plotly.express as px

#Chargement des données
df = pd.read_csv('https://raw.githubusercontent.com/axelnyandwi/BTC_vs_NASDAQ/main/data_yfinance.csv')

df['Date'] = pd.to_datetime(df['Date'])

st.subheader('Analyse comparative et corrélation')

# Nuage de points pour afficher le prix de l'un en fonction de l'autre
scatter_fig = px.scatter(df, x='Close_BTC', 
                y='Close_NASDAQ', 
                title='Prix BTC vs NASDAQ', 
                labels={'Close_BTC': 'Prix BTC', 'Close_NASDAQ': 'Prix NASDAQ'})
st.plotly_chart(scatter_fig)

# Répartition des volumes échangés
latest_data = df.iloc[-1]
total_volume = latest_data['Volume_BTC'] + latest_data['Volume_NASDAQ']
pie_fig = px.pie(values=[latest_data['Volume_BTC']/total_volume, latest_data['Volume_NASDAQ']/total_volume], 
                names=['Volume BTC', 'Volume NASDAQ'], 
                title='Répartition des Volumes Échangés')
st.plotly_chart(pie_fig)

# Corrélations en fonction du temps
correlation_fig = px.line(df, x='Date', y='Rolling_Correlation', title='Corrélation BTC vs NASDAQ au fil du temps', labels={'Rolling_Correlation': 'Corrélation'})
st.plotly_chart(correlation_fig)