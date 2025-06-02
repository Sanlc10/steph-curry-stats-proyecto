'''Importamos las siguientes librerias para la creación de la app, 
   pandas para el manejo de datos, plotly para las visualizaciones y 
   streamlit para la app propiamente. '''

import pandas as pd
import plotly.express as px
import streamlit as st

# Abrimos el archivo csv para elaborar nuestras visualizaciones.
curry_stats = pd.read_csv('./steph_curry_regular_season_stats.csv')

st.header('EDA: Stephen Curry (PTS per game / 3\'s per game)')
st.write('''Stephen Curry es un jugador profesional de la NBA ampliamente 
         reconocido por revolucionar el juego con su precisión en los tiros 
         de tres puntos. En este análisis exploratorio de datos (EDA), 
         visualizamos sus estadísticas de puntos por partido y triples por 
         partido durante la temporada regular desde 2009 hasta 2021.''')

ppg_button = st.button('Distribución de PPP de Steph Curry')

if ppg_button:
    fig = px.histogram(curry_stats,
                       x="PTS",
                       title="Distribución de puntos por partido de Stephen Curry",
                       labels={'PTS': 'Número de puntos',
                               'count': 'Frecuencia de partidos'
                               }
                       )
    st.plotly_chart(fig, use_container_width=True)
