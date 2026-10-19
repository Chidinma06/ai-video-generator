import streamlit as st
import os
from script_generator import generate_script
from voice_generator import generate_voice
from visual_fetcher import fetch_images
from video_composer import compose_video

st.set_page_config(page_title="AI Video Generator", layout="centered")

st.title("🎬 AI-Powered Marketing Video Generator")
st.subheader("Create professional marketing videos for your business in minutes — no skills needed.")

st.markdown("---")

business_name = st.text_input("Business Name", placeholder="e.g. Adaeze Fabrics")
description = st.text_area("Business Description", placeholder="e.g. A fabric store selling Ankara and lace materials in Lagos")
target_audience = st.text_input("Target Audience", placeholder="e.g. Nigerian women aged 20 to 45")
tone = st.selectbox("Video Tone", ["warm and energetic", "professional", "fun and playful", "elegant and luxurious"])
keyword = st.text_input("Visual Keyword", placeholder="e.g. African fashion fabric Nigeria")

st.markdown("---")

if st.button("🚀 Generate My Video"):
    if not business_name or not description or not target_audience or not keyword:
        st.error("Please fill in all fields before generating.")
    else:
        with st.spinner("Step 1 of 4 — Generating your marketing script..."):
            script = generate_script(business_name, description, target_audience, tone)

        st.success("✅ Script generated!")
        script = st.text_area("Your Script (you can edit this before video is created)", value=script, height=200)

        with st.spinner("Step 2 of 4 — Converting script to voiceover..."):
            generate_voice(script)
        st.success("✅ Voiceover ready!")

        with st.spinner("Step 3 of 4 — Fetching relevant images..."):
            fetch_images(keyword)
        st.success("✅ Images fetched!")

        with st.spinner("Step 4 of 4 — Composing your video... please wait"):
            compose_video("assets/images", "voiceover.mp3", business_name=business_name)

        st.success("🎉 Your video is ready!")

        with open("final_video.mp4", "rb") as f:
            st.download_button(
                label="⬇️ Download Your Video",
                data=f,
                file_name=f"{business_name}_marketing_video.mp4",
                mime="video/mp4"
            )