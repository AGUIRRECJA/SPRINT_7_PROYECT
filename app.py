import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("🚗 Demo Vehiculos con Streamlit")

st.header("Histograma del Odometro", divider=True)

car_data = pd.read_csv(
    r'C:\Users\jeyso\NUEVA CARPETA\SPRINT_7\SPRINT_7_PROYECT\vehicles_us.csv')

hist_button = st.checkbox('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Crear un scatter plot utilizando plotly.graph_objects
# Se crea una figura vacía y luego se añade un rastro de scatter
st.header("Relacion Precio vs Odometro", divider=True)

scatter_button = st.button('Construir Grafico de Dispersión')

if scatter_button:
    st.write('Creación de un Grafico de dispersion')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                                     y=car_data['price'], mode='markers')])
    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')
    # Mostrar el gráfico Plotly
    st.plotly_chart(fig)
