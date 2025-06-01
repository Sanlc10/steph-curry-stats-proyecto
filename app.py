'''Importamos las siguientes librerias para la creación de la app, 
   pandas para el manejo de datos, plotly para las visualizaciones y 
   streamlit para la app propiamente. '''

import pandas as pd
import plotly.express as px
import streamlit as st

curry_stats = pd.read_csv('./steph_curry_regular_season_stats.csv')
