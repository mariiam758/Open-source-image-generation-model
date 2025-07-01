import streamlit as st
import torch
from io import BytesIO
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler, EulerAncestralDiscreteScheduler
from diffusers.schedulers.scheduling_ddim import DDIMScheduler

# Style prompt presets
STYLE_PRESETS = {
    "🎨 Realism (Default)": "",
    "🖌 Oil Painting": "oil painting, canvas texture, brush strokes",
    "🎬 Cinematic": "cinematic lighting, shallow depth of field, movie still",
    "🌆 Futuristic City": "futuristic skyline, sci-fi architecture, neon lights",
    "🧝 Fantasy Art": "epic fantasy, detailed armor, glowing background",
    "🌀 Anime": "anime style, vibrant colors, clean lines, soft shading",
    "🎭 Surrealism": "dreamlike, abstract, Salvador Dali style"
}

# Scheduler loader
@st.cache_resource
def load_pipeline(scheduler_name):
    schedulers = {
        "DPMSolver": DPMSolverMultistepScheduler,
        "EulerA": EulerAncestralDiscreteScheduler,
        "DDIM": DDIMScheduler,
    }
    scheduler_cls = schedulers[scheduler_name]
    scheduler = scheduler_cls.from_pretrained("runwayml/stable-diffusion-v1-5", subfolder="scheduler")

    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        scheduler=scheduler,
        safety_checker=None,
        torch_dtype=torch.float32
    ).to("cpu")

    return pipe

st.title("🎨 Open Source Image Generator (CPU Edition)")

# User input
base_prompt = st.text_area("🖋️ Prompt (main subject)", "A futuristic city at night")
style = st.selectbox("🎨 Style Preset", list(STYLE_PRESETS.keys()))
negative_prompt = st.text_area("🚫 Negative Prompt", "blurry, low quality, distorted, deformed")

# Quality options
steps = st.slider("🧠 Inference Steps", 10, 50, 25)
width = st.slider("📏 Width", 256, 512, 384, step=64)
height = st.slider("📐 Height", 256, 512, 384, step=64)
scheduler_choice = st.selectbox("🧪 Sampler / Scheduler", ["DPMSolver", "EulerA", "DDIM"])

# Load model
pipe = load_pipeline(scheduler_choice)

# Generate full prompt
style_prompt = STYLE_PRESETS[style]
full_prompt = f"{base_prompt}, {style_prompt}" if style_prompt else base_prompt

# Image generation
if st.button("✨ Generate Image"):
    with st.spinner("🚀 Generating image... please wait..."):
        image = pipe(
            prompt=full_prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            height=height,
            width=width
        ).images[0]
        st.image(image, caption="🎉 Generated Image", use_column_width=True)

        # Save image in memory
        buf = BytesIO()
        image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Download button
        st.download_button(
            label="💾 Download Image",
            data=byte_im,
            file_name="generated_image.png",
            mime="image/png"
        )
