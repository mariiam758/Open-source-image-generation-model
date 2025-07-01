# 🎨 Open Source Image Generator (Stable Diffusion v1.5 - CPU Edition)

A simple, offline image generation web app using [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5), powered by the 🤗 `diffusers` library and built with Streamlit.  
It works on **CPU-only machines** and requires no GPU or cloud APIs.

---

## 🧠 Features

- ✅ Text-to-image generation using Stable Diffusion v1.5
- ✅ Style presets (anime, cinematic, oil painting, etc.)
- ✅ Adjustable inference steps, resolution, and schedulers
- ✅ Negative prompt support
- ✅ Works on CPU — no GPU or CUDA required
- ✅ Fully offline, no API key or internet required

---

## 📸 Demo Screenshot

![screenshot](demo_creenshot.png) 

---

## 🚀 Installation

> ⚠️ Requires Python 3.9–3.12

1. Clone this repo:

```bash
git clone https://github.com/yourusername/open-source-image-generator.git
cd open-source-image-generator

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate  # On Windows

3. Install dependencies (CPU-only version):

```bash
pip install -r requirements.txt --index-url https://download.pytorch.org/whl/cpu


---

## Running the App

```bash
streamlit run app.py



## File structure 

├── app.py                # Main Streamlit app
├── requirements.txt      # Dependency versions
├── README.md             # This file
└── demo_screenshot.png   # Screenshot for GitHub
└── output_screenshot.png   


## License

Model: Stable Diffusion v1.5 (CreativeML OpenRAIL-M license)
Code: MIT License


## Acknowledgements 

Hugging Face Diffusers
Stability AI
Streamlit