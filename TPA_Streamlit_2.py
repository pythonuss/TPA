import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Gráficos con Matplotlib y Streamlit")

# Menú para subir el archivo
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Cargar el archivo en un DataFrame
    df = pd.read_csv(uploaded_file)

    # Mostrar el DataFrame
    st.subheader("DataFrame")
    st.write(df)

    # Selección del tipo de gráfico
    tipo_grafico = st.selectbox("Selecciona el tipo de gráfico", ["Dispersión", "Líneas", "Barras"])

    # Selección de columnas para el eje x e y
    x_column = st.selectbox("Selecciona una columna para el eje x", df.columns)
    y_column = st.selectbox("Selecciona una columna para el eje y", df.columns)

    # Crear el gráfico con Matplotlib
    fig, ax = plt.subplots()
    
    if tipo_grafico == "Dispersión":
        # Dispersión plot
        ax.scatter(df[x_column], df[y_column])
        ax.set_title("Gráfico de Dispersión")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
    elif tipo_grafico == "Líneas":
        # Gráfico de líneas
        ax.plot(df[x_column], df[y_column])
        ax.set_title("Gráfico de Líneas")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
    elif tipo_grafico == "Barras":
        # Gráfico de barras
        ax.bar(df[x_column], df[y_column])
        ax.set_title("Gráfico de Barras")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)

    # Mostrar el gráfico con Streamlit
    st.pyplot(fig)
