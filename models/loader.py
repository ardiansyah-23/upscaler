import streamlit as st

from models.download import download_model

@st.cache_resource
def load_model():

    model_path = download_model()

    print(model_path)

    # nanti di sini load RealESRGAN

    return model_path
