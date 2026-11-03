#bibliotecas utilizadas
import streamlit as st
import pandas as pd
import plotly.express as px

# criando a tela do sistema
st.write("# Sistema de Vendas")

tabela = pd.read_csv("vendas.csv")
