import pandas as pd
import streamlit as st
import numpy as np

[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

Titulo_concurso = '<p style="text-align:center";"font-family:Courier; color:Blue; font-size: 20px;">Hackaton-Quantum Apps</p>'
st.markdown(Titulo_concurso, unsafe_allow_html=True)


Titulo_principal = '<p style="font-family:TimesNewRoman; color:DarkBlue; font-size: 42px;">Óptica Cuántica</p>'
st.markdown(Titulo_principal, unsafe_allow_html=True)

with st.sidebar:
    add_header = st.header(
        "Temas"
        
    )

st.subheader('Introduccion')