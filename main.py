import streamlit as st
from web_functions import load_data

from Tabs import home, predict, visualise
from streamlit_option_menu import option_menu

# Define Tabs mapping
Tabs = {
    "Home": home,
    "Prediksi": predict,
    "Visualisasi": visualise
}

# Sidebar navigation
with st.sidebar:
    selected = option_menu("Navigasi", ["Home", "Prediksi", "Visualisasi"],
                           icons=["house", "robot", "diagram-3"], menu_icon="cast", default_index=0)

# Load dataset
df, x, y = load_data()

# Conditional rendering based on selected tab
if selected in ["Prediksi", "Visualisasi"]:
    Tabs[selected].app(df, x, y)
else:
    Tabs[selected].app()
