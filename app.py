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

# Creamos un checkbox para mostrar el histograma y su explicación.
ppg_checkbox = st.checkbox('Distribución de PPP de Steph Curry')

if ppg_checkbox:
    fig = px.histogram(curry_stats,
                       x="PTS",
                       title="Distribución de puntos por partido de Stephen Curry",
                       labels={'PTS': 'Número de puntos',
                               'count': 'Frecuencia de partidos'
                               }
                       )
    st.plotly_chart(fig, use_container_width=True)

    st.write('''Podemos ver la distribución de puntos por partido de Stephen Curry, es una distribución de Gauss
             cuya media esta alrededor de 24 a 25 puntos, podemos ver que los valores están en un rango de 0 a 63 puntos, 
             siendo 63 el "Carreer high" de Stephen Curry.''')

# Convertimos el resultado tipo categórico a tipo númerico para poder calcular la correlación si es necesario.
curry_stats['Numerical_result'] = curry_stats['Result'].str.replace(
    'W', '1').str.replace('L', '0').astype(int)

# Creamos otro checkbox para mostrar el gráfico de dispersión y su explicación.
corr_checkbox = st.checkbox(
    'Gráfico de dispersión: Puntos de Curry vs Resultado del partido')
if corr_checkbox:
    pts_vs_result = px.scatter(curry_stats,
                               x='PTS',
                               y='Numerical_result',
                               title='Puntos de Steph Curry vs resultado del equipo(victoria o derrota)',
                               labels={'PTS': 'Número de puntos',
                                       'Numerical_result': 'Resultado del partido(victoria=1, derrota=0)'})
    st.plotly_chart(pts_vs_result, use_container_width=True)

    st.write('''El gráfico de arriba nos muestra la relación que hay entre los puntos por partido
             de Stephen Curry y el resultado del partido, ya sea victoria o derrota para el equipo.
             Se puede ver que los datos están demasiado dispersos, lo que indica que no hay una 
             correlación fuerte entre estas dos variables, aunque la correlación es positiva, es debil. 
             Esto nos permite saber e identificar que existen muchos otros factores que influyen en el 
             resultado de un partido, no solo los puntos que Curry anota, aunque si influye.''')
