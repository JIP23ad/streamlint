import pandas as pd
import utilidades as util
import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns

 # configuramos encabezado  de la  pagina 

st.set_page_config(
    page_title= "informen de la  liga", 
    page_icon="",
    initial_sidebar_state="expanded",
    layout="centered"
)
util.generarMenu()

#  visualizacion
st.title ("Datos de la liga Colombiana 2024")
ruta= "Data\\tctClean.csv"
df= pd.read_csv(ruta)

#  configuramos  la  visualizacion
tex=" hola"
util.informeDatos(df,tex)
                                


