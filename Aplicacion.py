import pandas as pd
import streamlit as st
import numpy as np

message = """
        __Selecciona el tema__
        """

st.set_page_config(page_title="Óptica Cuántica", layout = "wide")

import pkgutil
import importlib
import stlib

names = [ ]
modules = [intro,py, foto.py, ancho.py, max.py, energia.py, pola.py, inter.py, rendi.py, rendi.py, difra.py, reflex.py, refrac.py]
descriptions = [] 
package = stlib

for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    #print ("Found submodule %s (is a package: %s)" % (modname, ispkg))
    if modname.startswith('_'):
        pass  # ignore any modules beginning with _
    else:
        m = importlib.import_module('.'+modname,'stlib')
        names.append(modname)
        modules.append(m)
        # If the module has a description attribute use that in the select box
        # otherwise use the module name
        try:
            descriptions.append(m.description)
        except:
            descriptions.append(modname)

# The main app starts here

# Define a function to display the app
# descriptions instead of the module names
# in the selctbox, below
def format_func(name):
    return descriptions[names.index(name)]

# Display the sidebar with a menu of apps
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',names, format_func=format_func) 

# Run the chosen app
modules[names.index(page)].run()