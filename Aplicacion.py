

import pandas as pd
import streamlit as st
import numpy as np
st.set_page_config(page_title="Óptica Cuántica")


Titulo_concurso = '<p style="text-align:center";"font-family:Courier; color:Blue; font-size: 20px;">Hackaton-Quantum Apps</p>'
st.markdown(Titulo_concurso, unsafe_allow_html=True)


Titulo_principal = '<p style="font-family:TimesNewRoman; color:DarkBlue; font-size: 42px;">Óptica Cuántica</p>'
st.markdown(Titulo_principal, unsafe_allow_html=True)

st.caption('Esta aplicacón fue hecha con el propósito de introducir hacia los fenómenos cuánticos, especificamente dentro de la rama de la óptica cuántica, que ha sido de dificil comprensión para la cual nuestro objetivo es demostrar tales fenómenos con ejemplos visuales y prácticos de entender')

with st.sidebar:
    add_header = st.header(
        "Temas")
    Introduccion = st.button("Introducción")  

st.write(Introduccion)
if Introduccion:
    st.subheader('Introducción')
    st.markdown('**¿Qué es la luz?**')
    st.markdown('Una pregunta que los seres humanos han tratado de responder durante siglos.')
    
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("newton.png", width=600, caption='Figura No.1 Newton y el estudio de la luz')

    with col3:
        st.write("")

    st.markdown('Newton, principal aportador de la teoria de la luz estipulaba que las partículas de luz provenian de una fuente luminosa que estimulaba la vista.')
    st.markdown('Esta idea le permitió justificar las bases de la refracción y reflexión')
    st.markdown('Durante su vida sostuvó que la luz podría seguir un movimiento ondulatorio lo cual fue demostrado por Thomas Young, que bajo condiciones de difracción los rayos de luz interfieren unos con otros al igual que con las ondas mecánicas')

    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.markdown("![Alt Text](http://blog.soton.ac.uk/soundwaves/files/2013/12/light1.gif)")

    with col3:
        st.write("")

    #("![Your Awsome GIF](https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif)") 

    st.markdown('Ahora se sabe que la luz actúa como una onda y una particula, que es a lo que llamamos la naturaleza dual de la luz; la luz sigue principios de electromagnetismo, por lo que decimos que son ondas electromagnéticas.')
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("onda.png", width=450, caption='Onda electromangnética')

    with col3:
        st.write("")

    st.markdown("Las ondas electromagnéticas pueden ser clasificadas por su longitud de onda o su frecuencia; esta clasificación se llama **Espectro electromagnético**")
    longitud = st.slider('Longitud de onda visible en nm',380,750,380)
    if longitud < 450:
        st.markdown('Color Morado')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Morado.png/250px-Morado.png",width=200)
    if 450 < longitud < 495:
        st.markdown('Color Azul')
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/52/Tipos_de_azules.png",width=200)
    if 495 < longitud < 570:
        st.markdown('Color Verde')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Tipos_de_verde.png/250px-Tipos_de_verde.png",width=200)
    if 570 < longitud < 590:
        st.markdown('Color Amarillo')
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/5b/Amarillos.png",width=200)
    if 590 < longitud < 620:
        st.markdown('Color Naranja')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Shades_of_orange.png/250px-Shades_of_orange.png",width=200)
    if 620 < longitud < 750:
        st.markdown('Color Rojo')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Rojos.png/250px-Rojos.png",width=200)

    st.markdown("No se entendía muy bien el concepto de luz hasta 1900 cuando el físico Max Planck empezó a estudiar cuerpos negros(Objetos teóricos que absorven la energía radiante totalmente), estos se calentaban y empezaban a brillar.")
    st.image("http://nuclear-power.com/wp-content/uploads/blackbody-radiation-chart-min.png",width=700)





st.subheader('Introducción')
st.markdown('**¿Qué es la luz?**')
st.markdown('Una pregunta que los seres humanos han tratado de responder durante siglos.')

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("newton.png", width=600, caption='Figura No.1 Newton y el estudio de la luz')

with col3:
    st.write("")

st.markdown('Newton, principal aportador de la teoria de la luz estipulaba que las partículas de luz provenian de una fuente luminosa que estimulaba la vista.')
st.markdown('Esta idea le permitió justificar las bases de la refracción y reflexión')
st.markdown('Durante su vida sostuvó que la luz podría seguir un movimiento ondulatorio lo cual fue demostrado por Thomas Young, que bajo condiciones de difracción los rayos de luz interfieren unos con otros al igual que con las ondas mecánicas')

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.markdown("![Alt Text](http://blog.soton.ac.uk/soundwaves/files/2013/12/light1.gif)")

with col3:
    st.write("")

#("![Your Awsome GIF](https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif)") 

st.markdown('Ahora se sabe que la luz actúa como una onda y una particula, que es a lo que llamamos la naturaleza dual de la luz; la luz sigue principios de electromagnetismo, por lo que decimos que son ondas electromagnéticas.')
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("onda.png", width=450, caption='Onda electromangnética')

with col3:
    st.write("")

st.markdown("Las ondas electromagnéticas pueden ser clasificadas por lu longitud de onda o su frecuencia; esta clasificación se llama **Espectro electromagnético**")

longitud = st.slider('Longitud de onda visible en nm',380,750,380)
if longitud < 450:
    st.markdown('Color Morado')
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Morado.png/250px-Morado.png",width=200)
if 450 < longitud < 495:
    st.markdown('Color Azul')
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/52/Tipos_de_azules.png",width=200)
if 495 < longitud < 570:
    st.markdown('Color Verde')
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Tipos_de_verde.png/250px-Tipos_de_verde.png",width=200)
if 570 < longitud < 590:
    st.markdown('Color Amarillo')
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5b/Amarillos.png",width=200)
if 590 < longitud < 620:
    st.markdown('Color Naranja')
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Shades_of_orange.png/250px-Shades_of_orange.png",width=200)
if 620 < longitud < 750:
    st.markdown('Color Rojo')
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Rojos.png/250px-Rojos.png",width=200)

st.markdown("No se entendía muy bien el concepto de luz hasta 1900 cuando el físico Max Planck empezó a estudiar cuerpos negros(Objetos teóricos que absorven la energía radiante totalmente), estos se calentaban y empezaban a brillar.")
st.image("http://nuclear-power.com/wp-content/uploads/blackbody-radiation-chart-min.png",width=700)



