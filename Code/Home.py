import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Aayan's Site",
    page_icon=':black_nib:',
    layout='wide'
)

# HEADER
st.title("Aayan Anwar's Site")
st.write("This is my very own site, made with Python!")
st.write("---")
st.title("Some of my Works:")
st.subheader("[Github](https://github.com/AayanAnwar)")
st.subheader("[DoaS Chapter List](pages/All_Chapters.py)")  # Link to Chapter List
st.write("---")

# Sidebar Styling (optional)
hide_streamlit_style = """
    <style>
    [data-testid="stToolbar"] {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
