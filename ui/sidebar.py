import streamlit as st

def draw_sidebar():

    st.sidebar.title("⚙ AI Upscaler")

    scale = st.sidebar.selectbox(
        "Upscale",
        [2,4,8]
    )

    model = st.sidebar.selectbox(
        "Model",
        [
            "RealESRGAN",
            "SwinIR"
        ]
    )

    return scale, model
