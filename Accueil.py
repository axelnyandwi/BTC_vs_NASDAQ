import streamlit as st
import pandas as pd
import plotly.express as px

#Chargement des données
df = pd.read_csv('https://raw.githubusercontent.com/axelnyandwi/BTC_vs_NASDAQ/main/data_yfinance.csv')

df['Date'] = pd.to_datetime(df['Date'])

st.set_page_config(
    page_title="Accueil",
)

st.title("Données financières : BTC VS NASDAQ")

st.markdown(
    """
    L'objectif de cette étude est d'exploiter les informations fournies par « Yahoo
    Finance » pour effectuer une étude comparative approfondie entre la
    cryptomonnaie Bitcoin et l'indice boursier Nasdaq.
    Le Bitcoin, lancé en 2009, est la première et la plus célèbre des crypto-monnaies.
    Il a gagné une popularité immense, devenant un actif d'investissement majeur,
    tout en étant sujet à une volatilité et à des débats intenses sur sa valeur et son
    utilité à long terme.
    Le Nasdaq, est un marché boursier américain reconnu pour sa forte
    concentration en entreprises technologiques. Il est souvent considéré
    comme un baromètre de l'industrie technologique et des tendances du
    marché.
    L'étude comparative du Bitcoin et du Nasdaq offre une perspective unique sur
    deux des aspects les plus dynamiques et influents du monde financier
    moderne. Comprendre la corrélation, ou son absence, entre ces deux entités
    peut non seulement aider à mieux comprendre chaque entité, mais aussi à
    anticiper les mouvements futurs dans le monde de la finance.
"""
)
