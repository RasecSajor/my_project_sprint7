import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header("CONJUNTO DE DATOS DE ANUNCIOS DE VENTA DE COCHES")

# crear dos casillas de verificación
hist_checkbox = st.checkbox('Mostrar histograma') 
scatt_checkbox = st.checkbox('Mostrar gráfico de dispersión')

# Si se selecciona la casilla de histograma
if hist_checkbox:
    # escribir un mensaje
    st.write('Distribución de kilometraje de los vehículos anunciados')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Si se selecciona la casilla de dispersión
if scatt_checkbox:
    # escribir un mensaje
    st.write('Relación de kilometraje y precio')
    
    # crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, user_container_width=True)