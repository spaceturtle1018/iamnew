import streamlit as st
import streamlit.components.v1 as components

# Load and display your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_string = f.read()

st.title("Fintech")
components.html(html_string, height=600, scrolling=True)

