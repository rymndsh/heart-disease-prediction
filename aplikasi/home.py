import streamlit as st

st.set_page_config(
    page_title="Heart Disease Prediction",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=Playfair+Display:wght@600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background-color: #f5f8fc !important;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { background: #ffffff !important; border-right: 0.5px solid #d6e4f5; }

[data-testid="stAppViewContainer"] { background-color: #f5f8fc !important; }
[data-testid="stHeader"] { background-color: #ffffff !important; }
[data-testid="stMain"] { background-color: #f5f8fc !important; }

.navbar {
    background: #ffffff;
    border-bottom: 0.5px solid #d6e4f5;
    padding: 14px 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 100;
}
.nav-logo {
    font-size: 14px;
    font-weight: 500;
    color: #1a5fa8;
    letter-spacing: 0.04em;
    display: flex;
    align-items: center;
    gap: 8px;
}
.nav-dot {
    width: 8px; height: 8px;
    background: #1a5fa8;
    border-radius: 50%;
    display: inline-block;
}
.hero {
    padding: 72px 40px 48px;
    max-width: 760px;
}
.badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #e6f1fb;
    color: #185fa5;
    font-size: 11px;
    font-weight: 500;
    padding: 5px 14px;
    border-radius: 20px;
    margin-bottom: 24px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.hero-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 46px;
    font-weight: 600;
    color: #0d2d5e;
    line-height: 1.2;
    margin: 0 0 18px;
}
.hero-title span { color: #1a5fa8; }
.hero-sub {
    font-size: 16px;
    color: #5a7a9e;
    line-height: 1.75;
    max-width: 540px;
    margin: 0 0 36px;
}
.cards-section {
    padding: 0 40px 64px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}
.card {
    background: #ffffff;
    border: 0.5px solid #d6e4f5;
    border-radius: 12px;
    padding: 20px;
}
.card-icon {
    width: 36px; height: 36px;
    background: #e6f1fb;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 12px;
    font-size: 18px;
}
.card h3 {
    font-size: 13px;
    font-weight: 500;
    color: #0d2d5e;
    margin: 0 0 6px;
}
.card p {
    font-size: 12px;
    color: #7a9abf;
    line-height: 1.65;
    margin: 0;
}
.divider {
    border: none;
    border-top: 0.5px solid #d6e4f5;
    margin: 0 40px 48px;
}
.footer {
    background: #ffffff;
    border-top: 0.5px solid #d6e4f5;
    padding: 20px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.footer p {
    font-size: 12px;
    color: #9ab0cb;
    margin: 0;
}
div.stButton > button {
    background: #1a5fa8 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 12px 28px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    cursor: pointer !important;
    transition: background 0.2s !important;
}
div.stButton > button:hover {
    background: #154d8c !important;
}
</style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
<div class="navbar">
    <div class="nav-logo"><span class="nav-dot"></span> HeartSense</div>
    <div style="font-size:13px; color:#4a7ab5;">
        <span style="color:#1a5fa8; font-weight:500; border-bottom:1.5px solid #1a5fa8; padding-bottom:2px;">Home</span>
        &nbsp;&nbsp;
        <span>Prediction</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <div class="badge">⚕ Machine Learning · Medical</div>
    <h1 class="hero-title">Heart Disease<br><span>Prediction System</span></h1>
    <p class="hero-sub">
        Early detection of heart disease risk using machine learning based on medical data.
        Enter your health data and get prediction results along with probability levels.
    </p>
</div>
""", unsafe_allow_html=True)

# Button
col1, col2 = st.columns([1, 5])
with col1:
    if st.button("Start Prediction →"):
        st.switch_page("pages/prediksi_penyakit_jantung.py")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Feature Cards
st.markdown("""
<div class="cards-section">
    <div class="card">
        <div class="card-icon">✅</div>
        <h3>High Accuracy</h3>
        <p>Model trained on trusted medical datasets to deliver accurate predictions.</p>
    </div>
    <div class="card">
        <div class="card-icon">⏱</div>
        <h3>Instant Results</h3>
        <p>Get your prediction results and probability levels immediately.</p>
    </div>
    <div class="card">
        <div class="card-icon">🔒</div>
        <h3>Secure Data</h3>
        <p>Your health information is processed locally and never stored.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 Reymond · Heart Disease Prediction System</p>
    <p>Built with Streamlit & Python</p>
</div>
""", unsafe_allow_html=True)