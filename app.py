import streamlit as st
from PIL import Image

from config import APP_NAME
from core.settings import load_settings
from core.gpu import get_device
from ui.sidebar import draw_sidebar
from ui.home import show_home
from models.loader import load_model

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🖼️",
    layout="wide"
)

# ==========================================================
# LOAD SETTINGS
# ==========================================================

load_settings()

# ==========================================================
# LOAD AI MODEL (Cached)
# ==========================================================

with st.spinner("Loading AI Model..."):
    model = load_model()

# ==========================================================
# DEVICE INFO
# ==========================================================

device = get_device()

# ==========================================================
# UI
# ==========================================================

show_home()

scale, model_name = draw_sidebar()

st.success(
    f"Device : {device['device']} | {device['name']}"
)

# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg", "webp"]
)

# ==========================================================
# IMAGE PREVIEW
# ==========================================================

image = None

if uploaded_file:

    image = Image.open(uploaded_file)

    width, height = image.size

    st.info(f"Resolution : {width} × {height}")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original")

        st.image(image, use_container_width=True)

    with col2:

        st.subheader("Output")

        st.info("Belum diproses")

# ==========================================================
# START BUTTON
# ==========================================================

if st.button("🚀 Start Upscale", use_container_width=True):

    if image is None:

        st.warning("Silakan upload gambar terlebih dahulu.")

    else:

        progress = st.progress(0)

        status = st.empty()

        status.write("Preparing...")

        progress.progress(20)

        status.write("Loading AI Model...")

        progress.progress(40)

        status.write("Processing Image...")

        # ==================================================
        # Nanti RealESRGAN dipanggil di sini
        #
        # output = upscale_image(
        #     model,
        #     image,
        #     scale
        # )
        #
        # ==================================================

        progress.progress(80)

        status.write("Finishing...")

        progress.progress(100)

        st.success("Upscale selesai (Dummy Mode).")

        st.image(
            image,
            caption="Output Preview",
            use_container_width=True
        )

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption("AI Upscaler Pro v0.1 | Powered by Streamlit")
