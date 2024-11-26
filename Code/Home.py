<<<<<<< HEAD
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Death of a Shadow",
    page_icon=':black_nib:',
    layout='wide'
)

# HEADER
st.title("Death of a Shadow")
st.write("The official website for Death of a Shadow.")
st.write("---")
st.title("Aayan Anwar's Github:")
st.subheader("[Github](https://github.com/AayanAnwar)")
st.title("Chapter List:")
st.subheader("[DoaS Chapter List](pages/All_Chapters.py)")  # Link to Chapter List
st.write("---")

# Sidebar Styling
hide_streamlit_style = """
    <style>
    [data-testid="stToolbar"] {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
=======
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
>>>>>>> a151047b8059ad4563e67c42caabf7dd3a2b2bdd
