import streamlit as st

from config import APP_NAME

from ui.home import show_home
from ui.sidebar import draw_sidebar

from core.settings import load_settings
from core.gpu import get_device

from engine.image_loader import load_image

st.set_page_config(

    page_title=APP_NAME,
    layout="wide"
)

load_settings()

gpu = get_device()

scale, model = draw_sidebar()

show_home()

st.success(
    f"Device : {gpu['device']} ({gpu['name']})"
)

uploaded = st.file_uploader(

    "Upload Image",

    type=["png","jpg","jpeg","webp"]
)

if uploaded:

    image = load_image(uploaded)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original")

        st.image(image, use_container_width=True)

    with col2:

        st.subheader("Output")

        st.info("AI Upscale belum diimplementasikan.")

if st.button("🚀 Start Upscale"):

    st.success(
        f"Upscale {scale}x menggunakan {model}"
    )
