import streamlit as st
import librosa
import numpy as np
import pickle

# Page config
st.set_page_config(
    page_title="Forest Guardian",
    page_icon="🌲",
    layout="centered"
)

# ---------- LOAD MODEL ----------
model = pickle.load(open("chainsaw_detector.pkl", "rb"))

# ---------- FEATURE EXTRACTION ----------
def extract_features(file):
    audio, sample_rate = librosa.load(file, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled = np.mean(mfccs.T, axis=0)
    return mfccs_scaled

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

/* Background forest gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        180deg,
        #02130f 0%,
        #06241c 40%,
        #0a2f25 70%,
        #0f3d30 100%
    );
}

/* spacing */
.main .block-container {
    padding-top:4rem;
}

/* Title */
.hero-title {
    font-size:96px;
    font-weight:900;
    text-align:center;
    color:#66BB6A;
    letter-spacing:1px;
}

/* subtitle */
.hero-subtitle {
    font-size:30px;
    text-align:center;
    color:#E8F5E9;
}

/* description */
.hero-description {
    font-size:20px;
    text-align:center;
    color:#B0BEC5;
    margin-bottom:50px;
}

/* feature row */
.feature-row {
    text-align:center;
    font-size:18px;
    margin-bottom:40px;
}

/* upload card */
.upload-card {
    background: rgba(255,255,255,0.06);
    border-radius:18px;
    padding:45px;
    text-align:center;
    margin-top:25px;
    transition:0.3s;
}

/* glow effect */
.upload-card:hover {
    box-shadow:0px 0px 25px rgba(76,175,80,0.4);
}

/* result card */
.result-card {
    text-align:center;
    font-size:28px;
    font-weight:700;
    padding:25px;
    border-radius:16px;
    margin-top:35px;
}

.safe {
    background:rgba(76,175,80,0.15);
    color:#A5D6A7;
}

.alert {
    background:rgba(244,67,54,0.15);
    color:#EF9A9A;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown('<p class="hero-title">🌲 Forest Guardian</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="hero-subtitle">AI-Powered Detection of Illegal Logging</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="hero-description">Protecting forests through intelligent acoustic monitoring</p>',
    unsafe_allow_html=True
)

# ---------- FEATURE ROW ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("🌲 **Real-time Monitoring**")

with col2:
    st.markdown("🎧 **Acoustic Detection**")

with col3:
    st.markdown("🤖 **Machine Learning Powered**")

# ---------- UPLOAD CARD ----------
st.markdown('<div class="upload-card">', unsafe_allow_html=True)

st.subheader("Upload Forest Audio")

uploaded_file = st.file_uploader(
    "Upload a .wav file to analyze",
    type=["wav"]
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- PREDICTION ----------
if uploaded_file is not None:

    features = extract_features(uploaded_file)
    features = features.reshape(1, -1)

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.markdown(
            '<div class="result-card alert">⚠ Chainsaw Detected<br>Possible Illegal Logging Activity</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="result-card safe">✅ No Chainsaw Detected</div>',
            unsafe_allow_html=True
        )

# -------- FOOTER --------
st.markdown(
"""
---

Built by **Madhumita Ash & Team**
AI-powered acoustic monitoring for forest protection 🌲
"""
)




