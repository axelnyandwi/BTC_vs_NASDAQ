import streamlit as st
import pandas as pd
import plotly.express as px

#Chargement des données
df = pd.read_csv('https://raw.githubusercontent.com/axelnyandwi/BTC_vs_NASDAQ/main/data_yfinance.csv')

df['Date'] = pd.to_datetime(df['Date'])

st.subheader('Aperçu à date')
#Filtre Date
select_date = st.date_input("Sélectionnez une date", min_value=df['Date'].min(), max_value=df['Date'].max(), value=df['Date'].max())
filtre_date = df[df['Date'] == pd.Timestamp(select_date)]

#Affichage prix actuel
prix_btc = filtre_date.iloc[-1]['Close_BTC']
st.write(f'Prix du BTC au {select_date}: {prix_btc}')
prix_nasdaq = filtre_date.iloc[-1]['Close_NASDAQ']
st.write(f'Prix du NASDAQ au {select_date}: {prix_nasdaq}')

# Graphique des prix
price_fig = px.line(df, x='Date', 
                        y=['Close_BTC','Close_NASDAQ'],
                        title = 'Évolution des prix',
                        labels={'value': 'Prix en USD', 
                        'variable': 'Série'})
st.plotly_chart(price_fig)

# Graphique des volumes échangés
volume_fig = px.bar(df, x='Date', 
                        y=['Volume_BTC', 'Volume_NASDAQ'],
                        title = 'Volumes échangés', 
                        barmode='group', 
                        labels={'value': 'Volume', 'variable': 'Série'})
st.plotly_chart(volume_fig)
