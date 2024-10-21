import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path  # Certifique-se de importar Path

# Lê o conjunto de dados
df = pd.read_csv(Path("..\\dados\\vehicles.csv"))

# Exibe a porcentagem de valores ausentes
st.write(df.isna().mean().sort_values(ascending=False).head(5))

# Cria um botão para gerar o histograma
hist_button = st.button('Criar histograma')

if hist_button:  # Se o botão for clicado
    # Escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um histograma
    fig = px.histogram(df, x="odometer")  # Altere 'car_data' para 'df'
    
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

   # Lê o conjunto de dados
df = pd.read_csv(Path("..\\dados\\vehicles.csv"))

# Exibe a porcentagem de valores ausentes
st.write(df.isna().mean().sort_values(ascending=False).head(5))

# Cria uma caixa de seleção para gerar o histograma
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:  # Se a caixa de seleção for marcada
    st.write('Criando um histograma para a coluna odometer')
    
    # Criar um histograma
    fig = px.histogram(df, x="odometer")  # Usando 'df' para criar o histograma
    
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
    

        


