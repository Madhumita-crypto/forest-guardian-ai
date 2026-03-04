import streamlit as st
import librosa
import numpy as np
import pickle

st.set_page_config(
    page_title="Forest Guardian",
    page_icon="🌲",
    layout="centered"
)

st.markdown("""
<style>

/* App background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        180deg,
        #02130f 0%,
        #06241c 40%,
        #0a2f25 70%,
        #0f3d30 100%
    );
}

/* Center container spacing */
.main .block-container {
    padding-top: 5rem;
    padding-bottom: 3rem;
}

.hero-title {
    font-size:80px;
    font-weight:900;
    text-align:center;
    color:#4CAF50;
}

.hero-subtitle {
    font-size:28px;
    text-align:center;
    color:#E8F5E9;
}

.hero-description {
    font-size:18px;
    text-align:center;
    color:#B0BEC5;
    margin-bottom:40px;
}

/* Upload section */
.upload-card {
    background: rgba(255,255,255,0.05);
    border-radius:16px;
    padding:40px;
    text-align:center;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)
st.markdown(
    '<p class="hero-title">🌲 Forest Guardian</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="hero-subtitle">AI-Powered Detection of Illegal Logging</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="hero-description">Protecting forests through intelligent acoustic monitoring</p>',
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("🌲 **Real-time Monitoring**")

with col2:
    st.markdown("🎧 **Acoustic Detection**")

with col3:
    st.markdown("🤖 **Machine Learning Powered**")

st.markdown('<div class="upload-card">', unsafe_allow_html=True)

st.subheader("Upload Forest Audio")
uploaded_file = st.file_uploader(
    "Upload a .wav file to analyze",
    type=["wav"]
)

st.markdown('</div>', unsafe_allow_html=True)