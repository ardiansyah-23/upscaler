from pathlib import Path
import requests

MODEL_URL = "https://YOUR_MODEL_URL"

MODEL_DIR = Path("models/checkpoints")

MODEL_PATH = MODEL_DIR / "RealESRGAN_x4plus.pth"


def download_model():

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    if MODEL_PATH.exists():
        return MODEL_PATH

    print("Downloading model...")

    response = requests.get(MODEL_URL, stream=True)

    response.raise_for_status()

    with open(MODEL_PATH, "wb") as f:

        for chunk in response.iter_content(8192):

            if chunk:

                f.write(chunk)

    print("Download selesai")

    return MODEL_PATH
