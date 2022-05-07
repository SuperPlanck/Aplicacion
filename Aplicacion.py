

import pandas as pd
import streamlit as st
import numpy as np
st.set_page_config(page_title="Óptica Cuántica",page_icon="🎇")


Titulo_concurso = '<p style="text-align:center";"font-family:Courier; color:Blue; font-size: 20px;">Hackaton-Quantum Apps</p>'
st.markdown(Titulo_concurso, unsafe_allow_html=True)


Titulo_principal = '<p style="font-family:TimesNewRoman; color:DarkBlue; font-size: 42px;">Óptica Cuántica</p>'
st.markdown(Titulo_principal, unsafe_allow_html=True)

st.caption('Esta aplicacón fue hecha con el propósito de introducir hacia los fenómenos cuánticos, especificamente dentro de la rama de la óptica cuántica, que ha sido de dificil comprensión para la cual nuestro objetivo es demostrar tales fenómenos con ejemplos visuales y prácticos de entender')

page_names = ['Introducción', 'Efecto Fotoeléctrico', 'Ecuaciones de Maxwell', 'Energía transportada por ondas', 'Polarización','Interferencia','Experimento de la doble rendija','Difracción','Reflexión','Refracción']

Temas = st.sidebar.radio("Escoge el tema",page_names)      


if Temas == 'Introducción':
    
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
    st.image("https://cdn.kastatic.org/ka-perseus-images/01f944ab4471010d09766560f4d1c6da4846d97d.png", caption='Espectro electromagnético')
    st.markdown("Dentro del espectro electromagnético se encuentra la luz visible, esta es una pequeña parte de todo el espectro que en seres humanos es la única visualizable; arrastra el punto para ver que color se obtiene a diferentes longitudes")
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

    st.markdown("No se entendía muy bien el concepto de luz hasta 1900, cuando el físico Max Planck empezó a estudiar cuerpos negros (Objetos teóricos que absorven la energía radiante totalmente), estos se calentaban y empezaban a brillar.")
    st.image("http://nuclear-power.com/wp-content/uploads/blackbody-radiation-chart-min.png",width=700)
    st.markdown("Planck descubrió que la radiación electromagnética emitida por estos cuerpos no podia ser explicada por la física clásica; que postulaba que la energía podía ser emitida y absorbida por la materia en cualquier cantidad")
    st.markdown("Un cuerpo negro absorbe energía en modo de calor y emite luz, la física clásica postulaba que el cuerpo tiene la capacidad de absorber la energía hasta emitir ondas electromagnéticas por encima de la luz visible, emitiendo ondas de alta energía como las UV,  de rayos x y gamma")
    st.markdown("![Alt Text](https://steemitimages.com/DQmSXqSXPGdcPQiP3EfaZZQhipbZJg2RsAZmVTpUJvcGetZ/output_final_radiation.gif)")
    st.markdown("A esto se le llamó la catástrofe ultravioleta")
    st.image("https://slideplayer.es/slide/5497387/17/images/12/LEY+DE+RAYLEIGH-JEANS+Cat%C3%A1strofe+ultravioleta.jpg")
    st.markdown("Planck observó que la materia absorbía o emitía la energia en multiplos enteros del valor de la constante de Planck, pequeños paquetes conocidos como cuántos, por lo que Einstein propuso su teoría del efecto fotoeléctrico")
    st.latex('h=6.626^{-34}J')
    st.caption('El efecto fotoeléctrico nos dice que si un electrón absorbe la energía de un fotón y este tiene más energía que la función del trabajo el electrón es arrancado del material, explicando porque los materiales no absorben energia hasta emitir ondas de alta energía')
    st.markdown("Los fotones pueden ser emitidos o absorbidos por los átomos, se absorben por completo y al momento de que el átomo pierde energía se emiten, cargando con la energía exacta que se perdió la cual es directamente proporcional a su frecuencia.")
    st.markdown("Eso demostró que la luz se comporta también como una partícula")
    st.markdown("Esta relación es descrita por la famosa **Ecuación de Planck**:")
    st.latex('E=hf')
    st.caption("*Las frecuencias más altas nos hacen más daño, porque significan más energía")

if Temas == 'Efecto Fotoeléctrico':
    st.subheader('')
    st.markdown('')
    st.markdown('')
    

if Temas == 'Ecuaciones de Maxwell':
    st.write(":c")

if Temas == 'Energía transportada por ondas':
    st.subheader('Energía transportada por ondas')
    st.markdown('La cantidad transferida de energía mediante ondas electromagnéticas se expresa por')
    st.latex('T_{RE}')
    st.markdown('La rapidez de transferencia de energía en una onda electromagnética se representa mediante un vector que se define como:')
    st.latex(r'''
     \overrightarrow{S} = \frac{1}{\mu} \overrightarrow{E} \cdotp \overrightarrow{B}
     ''')
    s = st.latex(r''\overrightarrow{S}''),
    st.markdown("donde", s)

if Temas == 'Polarización':
    st.write("pq")

if Temas == 'Interferencia':
    st.write("alguien")

if Temas == 'Experimento de la doble rendija':
    st.write("Mateme")

if Temas == 'Difracción':
    st.write("Porfavor")

if Temas == 'Reflexión':
    st.write(":,,")

if Temas == 'Refracción':
    st.write("refraccion")
