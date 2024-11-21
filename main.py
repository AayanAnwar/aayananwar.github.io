import streamlit as st

st.set_page_config(
    page_title="Aayan Anwar's Blog",
    page_icon=':black_nib:'
)

#HEADER#

st.title("-(.Aayan Anwar's Blog.)-")







hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)