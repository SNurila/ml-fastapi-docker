import streamlit as st
import requests

st.set_page_config(
    page_title="Stock Price Predictor",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&display=swap');

* { font-family: 'Syne', sans-serif; }

.stApp {
    background: #0a0a0f;
    color: #e8e8f0;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 6rem 3rem; max-width: 1200px; }

.hero {
    padding: 3rem 0 2rem 0;
    border-bottom: 1px solid #1e1e2e;
    margin-bottom: 2.5rem;
}
.hero-tag {
    display: inline-block;
    background: #00ff88;
    color: #0a0a0f;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 2px;
    margin-bottom: 1rem;
}
.hero h1 {
    font-size: 3.2rem;
    font-weight: 800;
    line-height: 1.05;
    margin: 0.5rem 0;
    background: linear-gradient(135deg, #ffffff 0%, #a0a0c0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero p {
    color: #6060a0;
    font-size: 1rem;
    margin-top: 0.5rem;
    font-family: 'DM Mono', monospace;
}

.section-label {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #00ff88;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1e1e2e;
}

div[data-testid="stNumberInput"] {
    background: #111120;
    border: 1px solid #1e1e2e;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    transition: border-color 0.2s;
}
div[data-testid="stNumberInput"]:hover { border-color: #00ff88; }
div[data-testid="stNumberInput"] label {
    color: #8888bb !important;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
}
div[data-testid="stNumberInput"] input {
    color: #060626 !important;
    background: transparent !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 1.1rem !important;
    border: none !important;
    padding: 0 !important;
}

div[data-testid="stButton"] button {
    background: #00ff88 !important;
    color: #0a0a0f !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 0.8rem 2.5rem !important;
    width: 100% !important;
    transition: all 0.2s !important;
}
div[data-testid="stButton"] button:hover {
    background: #00cc6a !important;
    box-shadow: 0 8px 30px rgba(0, 255, 136, 0.25) !important;
}

.result-card {
    background: linear-gradient(135deg, #0d1f15 0%, #0a1a10 100%);
    border: 1px solid #00ff88;
    border-radius: 12px;
    padding: 2rem;
    margin-top: 1.5rem;
    text-align: center;
}
.result-label {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #00ff88;
    margin-bottom: 0.5rem;
}
.result-value {
    font-size: 3rem;
    font-weight: 800;
    color: #ffffff;
    font-family: 'DM Mono', monospace;
}
.result-sub {
    font-size: 0.8rem;
    color: #448866;
    margin-top: 0.3rem;
    font-family: 'DM Mono', monospace;
}

.error-card {
    background: #1a0a0a;
    border: 1px solid #ff4444;
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1.5rem;
    color: #ff8888;
    font-family: 'DM Mono', monospace;
    font-size: 0.85rem;
}

.divider { height: 1px; background: #1e1e2e; margin: 2rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-tag">ML Powered</div>
    <h1>Stock Price<br>Predictor</h1>
    <p>→ Enter market features to generate a price prediction</p>
</div>
""", unsafe_allow_html=True)

# ── Price Data ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Price Data</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    Open = st.number_input("Open", value=0.0, format="%.4f")
with col2:
    High = st.number_input("High", value=0.0, format="%.4f")
with col3:
    Low = st.number_input("Low", value=0.0, format="%.4f")
with col4:
    Volume = st.number_input("Volume", value=0.0, format="%.2f")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Returns & Changes ─────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Returns & Changes</div>', unsafe_allow_html=True)
col5, col6, col7, col8 = st.columns(4)
with col5:
    Daily_Return = st.number_input("Daily Return", value=0.0, format="%.6f")
with col6:
    Price_Range = st.number_input("Price Range", value=0.0, format="%.4f")
with col7:
    Price_Change = st.number_input("Price Change", value=0.0, format="%.4f")
with col8:
    Price_Change_Percent = st.number_input("Price Change %", value=0.0, format="%.4f")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Moving Averages & Volatility ──────────────────────────────────────────────
st.markdown('<div class="section-label">Moving Averages & Volatility</div>', unsafe_allow_html=True)
col9, col10, col11, col12 = st.columns(4)
with col9:
    MA_7 = st.number_input("MA 7", value=0.0, format="%.4f")
with col10:
    MA_30 = st.number_input("MA 30", value=0.0, format="%.4f")
with col11:
    MA_90 = st.number_input("MA 90", value=0.0, format="%.4f")
with col12:
    Volatility_7d = st.number_input("Volatility 7d", value=0.0, format="%.4f")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Predict Button ────────────────────────────────────────────────────────────
predict = st.button("⟶  Run Prediction")

# ── Result ────────────────────────────────────────────────────────────────────
if predict:
    data = {
        "Open": Open,
        "High": High,
        "Low": Low,
        "Volume": Volume,
        "Daily_Return": Daily_Return,
        "Price_Range": Price_Range,
        "Price_Change": Price_Change,
        "Price_Change_Percent": Price_Change_Percent,
        "MA_7": MA_7,
        "MA_30": MA_30,
        "MA_90": MA_90,
        "Volatility_7d": Volatility_7d
    }
    try:
        with st.spinner("Running model inference..."):
            response = requests.post("http://127.0.0.1:8000/predict", json=data)

        if response.status_code == 200:
            result = response.json()

            # Show raw response so we know the exact key name
            st.write("🔍 Raw API response:", result)

            # Try common key names — adjust after seeing raw response above
            prediction = (
                result.get("prediction")
                or result.get("predicted_price")
                or result.get("result")
                or result.get("close")
                or list(result.values())[0]  # fallback: just grab first value
            )

            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">Predicted Close Price</div>
                <div class="result-value">${float(prediction):,.4f}</div>
                <div class="result-sub">inference complete · model ready</div>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
            <div class="error-card">
                ✗ Server returned status {response.status_code}<br><br>
                {response.text}
            </div>
            """, unsafe_allow_html=True)

    except requests.exceptions.ConnectionError:
        st.markdown("""
        <div class="error-card">
            ✗ Connection refused — FastAPI is not running<br><br>
            → Run this in a separate terminal:<br>
            <strong>cd ~/Documents/ml && source .venv/bin/activate && uvicorn main:app --reload --port 8000</strong>
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"""
        <div class="error-card">
            ✗ Unexpected error:<br><br>{e}
        </div>
        """, unsafe_allow_html=True)