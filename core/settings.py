import streamlit as st

def load_settings():

    if "scale" not in st.session_state:
        st.session_state.scale = 4

    if "model" not in st.session_state:
        st.session_state.model = "RealESRGAN"

    if "device" not in st.session_state:
        st.session_state.device = "Auto"   
