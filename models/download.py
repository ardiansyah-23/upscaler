from pathlib import Path
import requests
import streamlit as st

MODEL_URL = (
    "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/"
    "RealESRGAN_x4plus.pth"
)

MODEL_DIR = Path("models/checkpoints")
MODEL_PATH = MODEL_DIR / "RealESRGAN_x4plus.pth"


def download_model():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    if MODEL_PATH.exists():
        return MODEL_PATH

    try:
        with st.spinner("Downloading AI model..."):
            response = requests.get(
                MODEL_URL,
                stream=True,
                timeout=60
            )

            response.raise_for_status()

            with open(MODEL_PATH, "wb") as f:
                for chunk in response.iter_content(8192):
                    if chunk:
                        f.write(chunk)

    except requests.RequestException as e:
        st.error(f"Gagal mengunduh model:\n{e}")
        raise

    return MODEL_PATH
