import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header("Exploración de datos de vehículos 🚗")

# Leer datos
car_data = pd.read_csv('/Users/flavioramirezherreea/Desktop/sprint-7-repo/vehicles_us.csv')

# Casilla de verificación para histograma
show_hist = st.checkbox('Mostrar histograma (odometer)')

if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión (odometer vs price)')

if show_scatter:
    st.write('Creación de un gráfico de dispersión para analizar la relación entre precio y odómetro')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)