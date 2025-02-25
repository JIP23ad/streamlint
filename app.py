print("hola mundo")
import pandas  as pd
import streamlit as st
import utilidades as util
from PIL import Image



# pagina  de presentacion  o index
st.set_page_config (
    page_title="Info Liga Colombiana",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon=("45🆔"))

util.generarMenu()

# ESTRUCTURA  DE PRESENTACION
left_col, center_col, righ_col = st.columns([1,4,1],
                                   vertical_alignment="center")
#edito la  columna  central
with center_col:
    st.title("Informe de la  liga Colombina 2024-2")
    st.write("""
    En  este  espacio, se puede  mostrar  cual  fue  el  desempeño  de los  equipos  de  futbol,  durante la  Liga Betplay, en el año 2024,  segun semestre.
    En la pagina  informes, se puede  observar  los  datos y analisis""")

    imagen2= Image.open("Media\selec _colombia.jpg")
    st.image(imagen2, use_container_width=True, width=500,
    caption="Seleccion Colombia")

   