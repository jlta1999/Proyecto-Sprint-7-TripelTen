#Librerías con las que se trabajará
import streamlit as st
import pandas as pd
import plotly.express as px

#Dataet
car_data  = pd.read_csv('data/vehicles_us.csv') 

# Título de la app
st.title("Análisis de vehículos en venta 🚗")


# Botones
col1, col2 = st.columns(2)
with col1:
    hist_button = st.button("Construir histograma", key="hist")
with col2:
    scatter_button = st.button("Construir dispersión", key="scatter")

# Histograma
if hist_button:
    st.write("Creación de un histograma para el odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Dispersión
if scatter_button:
    st.write("Gráfico de dispersión: precio vs. odómetro")
    # Si tu dataset tiene estas columnas, funcionará directo. (Ambas suelen existir en este dataset)
    fig2 = px.scatter(
        car_data,
        x="odometer",
        y="price",
        opacity=0.6
    )
    st.plotly_chart(fig2, use_container_width=True)