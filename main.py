import streamlit as st
from web_functions import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualise
}

# sidebar
st.sidebar.title("Navigasi")

# radio option
page = st.sidebar.radio("pages", list(Tabs.keys()))

# load dataset
df, x, y = load_data()

# kondisi call ap function
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()
