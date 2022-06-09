from logging import PlaceHolder
import pandas as pd
import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    with st.form("login"):
        st.markdown("#### Painel de Login")
        st.text_input("Email", placeholder="Digite aqui seu email")
        st.text_input("Senha", placeholder="Digite aqui sua senha", type="password")
        st.form_submit_button("Login")