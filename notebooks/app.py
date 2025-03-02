import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
df = pd.read_csv("vehicles_us.csv")

# Encabezado
st.header("Análisis de vehículos")

# Botón para construir el histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig_hist = px.histogram(df, x="odometer")  # Histograma de odómetro
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión para analizar la relación entre el precio y el odómetro")
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Relación entre odómetro y precio")  # Gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)

