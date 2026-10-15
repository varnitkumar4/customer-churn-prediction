import math
import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

# =========================================================
# ChurnIQ — Customer Churn Prediction Dashboard
# Single file app · Streamlit · 19 features
# =========================================================
st.set_page_config(
    page_title="ChurnIQ | Customer Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# 1. THEME / CSS
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background:
      radial-gradient(900px 420px at 6% -6%, rgba(99,102,241,.20), transparent 55%),
      radial-gradient(800px 380px at 98% 4%, rgba(34,211,238,.13), transparent 50%),
      radial-gradient(700px 500px at 50% 115%, rgba(16,185,129,.08), transparent 55%),
      #0a0f1e;
    color: #eef3ff;
}

[data-testid="stHeader"] { background: rgba(10,15,30,.80); backdrop-filter: blur(10px); }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0e1630 0%, #0b1226 100%);
    border-right: 1px solid #22315a;
}
[data-testid="stSidebar"] * { color: #dfe8ff; }
.block-container { padding-top: 1.4rem; max-width: 1500px; }

/* ---------- brand ---------- */
.brand { display:flex; align-items:center; gap:11px; margin-bottom:4px; }
.brand-logo {
    width:38px; height:38px; border-radius:11px;
    background:linear-gradient(135deg,#6366f1,#22d3ee);
    display:flex; align-items:center; justify-content:center;
    font-size:18px; font-weight:900; color:white;
    box-shadow:0 6px 18px rgba(99,102,241,.45);
}
.brand-name { font-size:19px; font-weight:900; color:#fff; letter-spacing:.3px; }
.brand-tag  { font-size:10px; font-weight:700; letter-spacing:2px; color:#7f8fc5; }

/* ---------- hero ---------- */
.hero {
    position:relative; overflow:hidden;
    border:1px solid rgba(129,140,248,.35);
    border-radius:22px; padding:26px 30px; margin-bottom:20px;
    background:linear-gradient(115deg, rgba(79,70,229,.30), rgba(14,165,233,.14) 55%, rgba(16,185,129,.10));
    box-shadow:0 16px 40px rgba(0,0,0,.25);
}
.hero::after {
    content:""; position:absolute; right:-70px; top:-90px;
    width:260px; height:260px; border-radius:50%;
    background:radial-gradient(circle, rgba(34,211,238,.22), transparent 65%);
}
.hero-kicker { color:#a5b4fc; font-size:11px; letter-spacing:2.2px; font-weight:800; text-transform:uppercase; }
.hero h1 { color:#fff; font-weight:900; font-size:clamp(26px,3vw,36px); margin:8px 0 8px; line-height:1.15; }
.hero h1 span { background:linear-gradient(90deg,#a5b4fc,#67e8f9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.hero p { color:#c2d0ec; font-size:13.5px; line-height:1.7; max-width:760px; margin:0; }
.pill {
    display:inline-flex; align-items:center; gap:6px;
    border:1px solid rgba(165,180,252,.30); border-radius:999px;
    padding:5px 12px; font-size:11px; font-weight:700; color:#dbe6ff;
    background:rgba(10,15,30,.45);
}

/* ---------- KPI cards ---------- */
.kpi {
    background:linear-gradient(150deg, rgba(24,34,60,.95), rgba(15,23,42,.95));
    border:1px solid #26355c; border-radius:18px; padding:18px 20px;
    box-shadow:0 10px 26px rgba(0,0,0,.22);
    transition:transform .15s ease, border-color .15s ease;
}
.kpi:hover { transform:translateY(-3px); border-color:#3b82f6; }
.kpi-top { display:flex; align-items:center; gap:9px; }
.kpi-icon {
    width:34px; height:34px; border-radius:10px; font-size:17px;
    display:flex; align-items:center; justify-content:center;
}
.kpi-label { font-size:10.5px; font-weight:800; letter-spacing:1px; color:#93a5cd; text-transform:uppercase; }
.kpi-value { font-size:24px; font-weight:900; color:#fff; margin-top:12px; }
.kpi-note { font-size:11.5px; color:#7d90b8; margin-top:4px; }

/* ---------- section headings ---------- */
.sec-title { font-size:18px; font-weight:800; color:#f4f7ff; margin:6px 0 2px; }
.sec-sub { font-size:12px; color:#8ea0c4; margin-bottom:12px; }
.group-label {
    font-size:12px; font-weight:800; letter-spacing:1px; text-transform:uppercase;
    color:#a5b4fc; margin-bottom:8px; display:flex; align-items:center; gap:8px;
}

/* ---------- bordered containers (form groups) ---------- */
[data-testid="stVerticalBlockBorderWrapper"] {
    background:rgba(17,26,48,.75);
    border:1px solid #26355c !important;
    border-radius:16px !important;
    padding:14px 16px 6px !important;
}

/* ---------- result card ---------- */
.result-shell {
    background:linear-gradient(160deg, rgba(24,34,60,.95), rgba(13,20,38,.97));
    border:1px solid #2a3a63; border-radius:20px; padding:24px 22px;
    box-shadow:0 14px 34px rgba(0,0,0,.28);
}
.donut-wrap { display:flex; justify-content:center; margin:6px 0 4px; }
.risk-chip {
    display:inline-block; padding:5px 14px; border-radius:999px;
    font-size:11px; font-weight:800; letter-spacing:1.2px; text-transform:uppercase;
}
.chip-high { background:rgba(251,113,133,.14); color:#fda4af; border:1px solid rgba(251,113,133,.45); }
.chip-mid  { background:rgba(251,191,36,.12); color:#fcd34d; border:1px solid rgba(251,191,36,.40); }
.chip-low  { background:rgba(52,211,153,.12); color:#6ee7b7; border:1px solid rgba(52,211,153,.40); }

.flag {
    display:inline-block; margin:3px 4px 0 0; padding:4px 10px; border-radius:8px;
    background:rgba(99,102,241,.13); border:1px solid rgba(129,140,248,.30);
    color:#c7d2fe; font-size:11px; font-weight:600;
}
.action-item {
    display:flex; gap:11px; align-items:flex-start;
    padding:10px 0; border-bottom:1px solid #223158;
    font-size:13px; color:#cdd9f2; line-height:1.55;
}
.action-item:last-child { border-bottom:none; }
.action-num {
    min-width:22px; height:22px; border-radius:7px;
    background:linear-gradient(135deg,#6366f1,#22d3ee);
    color:#fff; font-size:11px; font-weight:800;
    display:flex; align-items:center; justify-content:center;
}

.empty {
    border:1.5px dashed #31437a; border-radius:16px;
    padding:44px 20px; text-align:center; color:#7d90b8;
}
.empty .ico { font-size:36px; margin-bottom:10px; }
.empty b { color:#dbe6ff; font-size:14px; display:block; margin-bottom:5px; }

/* ---------- inputs ---------- */
div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
    background:#101a33; border-color:#31437a; border-radius:9px;
}
input { color:#eef3ff !important; }
label { color:#ccd9f5 !important; font-size:12px !important; font-weight:600 !important; }
[data-testid="stForm"] { border:0; padding:0; background:transparent; }
hr { border-color:#26355c; }

/* ---------- buttons ---------- */
div[data-testid="stFormSubmitButton"] > button {
    background:linear-gradient(100deg,#6366f1,#8b5cf6 50%,#22d3ee);
    color:#fff; border:0; border-radius:12px; min-height:50px;
    font-weight:800; font-size:15px; letter-spacing:.3px;
    box-shadow:0 10px 26px rgba(99,102,241,.35);
    transition:transform .15s ease, filter .15s ease;
}
div[data-testid="stFormSubmitButton"] > button:hover {
    filter:brightness(1.12); transform:translateY(-1px); color:#fff;
}

.footer { text-align:center; color:#5f7196; font-size:11px; padding:26px 0 6px; }
div[data-testid="stAlert"] { border-radius:12px; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# 2. LOAD MODEL
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
MODEL_CANDIDATES = [
    BASE_DIR / "models" / "churn_pipeline.pkl",
    BASE_DIR.parent / "models" / "churn_pipeline.pkl",
    BASE_DIR / "churn_pipeline.pkl",
]

@st.cache_resource
def load_model(path: str):
    return joblib.load(path)

model_path = next((p for p in MODEL_CANDIDATES if p.exists()), None)
if model_path is None:
    st.error("⚠️ Model file not found. Place `churn_pipeline.pkl` inside a `models/` folder next to `app.py`.")
    st.code("project/\n├── app.py\n└── models/\n    └── churn_pipeline.pkl", language="text")
    st.stop()

try:
    model = load_model(str(model_path))
except Exception as exc:
    st.error(f"Model load failed: {exc}")
    st.stop()

# =========================================================
# 3. HELPERS
# =========================================================
def churn_probability(frame: pd.DataFrame) -> tuple[float, bool]:
    """Works whether classes are 'Yes'/'No' or 1/0."""
    pred = model.predict(frame)[0]
    probs = model.predict_proba(frame)[0]
    classes = list(model.classes_)
    if "Yes" in classes:
        return float(probs[classes.index("Yes")]), pred == "Yes"
    if 1 in classes:
        return float(probs[classes.index(1)]), int(pred) == 1
    return float(probs[-1]), bool(pred)


def risk_band(p: float):
    if p >= 0.60:
        return "high", "High risk", ("#fb7185", "#e11d48")
    if p >= 0.35:
        return "mid", "Medium risk", ("#fbbf24", "#f59e0b")
    return "low", "Low risk", ("#34d399", "#10b981")


def risk_flags(row: dict) -> list[str]:
    flags = []
    if row["Contract"] == "Month-to-month":
        flags.append("📄 Month-to-month contract")
    if row["InternetService"] == "Fiber optic" and row["OnlineSecurity"] == "No":
        flags.append("🌐 Fiber without security")
    if row["TechSupport"] == "No":
        flags.append("🛠️ No tech support")
    if row["PaymentMethod"] == "Electronic check":
        flags.append("💳 Electronic check billing")
    if row["tenure"] < 12:
        flags.append("🕐 Tenure under 12 months")
    if row["MonthlyCharges"] >= 70:
        flags.append("💰 High monthly bill")
    return flags


def playbook(row: dict, p: float) -> list[str]:
    tips = []
    if row["Contract"] == "Month-to-month":
        tips.append("Offer a 12-month plan with a loyalty discount or rate lock.")
    if row["InternetService"] == "Fiber optic" and row["OnlineSecurity"] == "No":
        tips.append("Bundle Online Security + Tech Support with the fiber plan.")
    if row["PaymentMethod"] == "Electronic check":
        tips.append("Move billing to auto-pay (card or bank transfer).")
    if row["tenure"] < 12:
        tips.append("Schedule a 30-day onboarding check-in call.")
    if row["MonthlyCharges"] >= 70:
        tips.append("Review plan fit — the bill may feel high for actual usage.")
    if p < 0.35:
        tips.append("Low risk — maintain service quality, no discount needed.")
    return tips[:4] or ["No strong risk flags — standard customer care."]


def donut_svg(p: float, colors: tuple[str, str]) -> str:
    r, c = 62, 2 * math.pi * 62
    offset = c * (1 - p)
    return f"""
    <svg width="168" height="168" viewBox="0 0 168 168">
      <defs>
        <linearGradient id="dg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="{colors[0]}"/>
          <stop offset="100%" stop-color="{colors[1]}"/>
        </linearGradient>
      </defs>
      <circle cx="84" cy="84" r="{r}" fill="none" stroke="#1c2a4d" stroke-width="13"/>
      <circle cx="84" cy="84" r="{r}" fill="none" stroke="url(#dg)" stroke-width="13"
        stroke-linecap="round" stroke-dasharray="{c:.1f}" stroke-dashoffset="{offset:.1f}"
        transform="rotate(-90 84 84)"/>
      <text x="84" y="80" text-anchor="middle" fill="#ffffff" font-size="29"
        font-weight="800" font-family="Inter">{p:.0%}</text>
      <text x="84" y="103" text-anchor="middle" fill="#8296c2" font-size="10"
        font-weight="700" letter-spacing="2" font-family="Inter">CHURN RISK</text>
    </svg>
    """

# =========================================================
# 4. SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown("""
    <div class="brand">
      <div class="brand-logo">C</div>
      <div>
        <div class="brand-name">ChurnIQ</div>
        <div class="brand-tag">CUSTOMER INTELLIGENCE</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("**🟣 Churn Prediction**  · active")
    st.markdown("⚪ Batch Scoring *(soon)*")
    st.markdown("⚪ Model Monitoring *(soon)*")
    st.divider()
    st.markdown("**🤖 Model**")
    st.caption("Algorithm · Logistic Regression")
    st.caption("Task · Binary classification")
    st.caption("Features · 19")
    st.divider()
    st.markdown("**🎚️ Risk bands**")
    st.caption("🟢 Low  ·  below 35%")
    st.caption("🟡 Medium  ·  35% – 60%")
    st.caption("🔴 High  ·  above 60%")
    st.divider()
    st.caption("Python · Pandas · Scikit-learn · Streamlit")

# =========================================================
# 5. HERO
# =========================================================
st.markdown("""
<div class="hero">
  <div class="hero-kicker">✦ Machine learning · Retention analytics</div>
  <h1>Predict churn <span>before it happens.</span></h1>
  <p>Score any telecom customer in seconds. ChurnIQ reads contract, service and billing
     signals to estimate churn probability — then suggests the next best retention action.</p>
  <div style="margin-top:14px; display:flex; gap:8px; flex-wrap:wrap;">
    <span class="pill">⚡ Instant scoring</span>
    <span class="pill">🧩 19 features</span>
    <span class="pill">🎯 Risk bands</span>
    <span class="pill">📋 Retention playbook</span>
  </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 6. KPI CARDS (3 columns — Dataset Churn Rate removed)
# =========================================================
k1, k2, k3 = st.columns(3, gap="medium")
kpis = [
    (k1, "🤖", "#6366f1", "ML Algorithm", "Logistic Regression", "Pipeline · encoded + scaled"),
    (k2, "🧩", "#22d3ee", "Input Features", "19", "Profile · services · billing"),
    (k3, "💚", "#10b981", "Business Goal", "Retention", "Act before customers leave"),
]
for col, icon, color, label, value, note in kpis:
    with col:
        size = "18px" if len(value) > 14 else "24px"
        st.markdown(f"""
        <div class="kpi">
          <div class="kpi-top">
            <span class="kpi-icon" style="background:{color}26">{icon}</span>
            <span class="kpi-label">{label}</span>
          </div>
          <div class="kpi-value" style="font-size:{size}">{value}</div>
          <div class="kpi-note">{note}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# =========================================================
# 7. MAIN — form (left) + result (right)
# =========================================================
form_col, result_col = st.columns([1.45, 1], gap="large")

with form_col:
    st.markdown('<div class="sec-title">👤 Customer Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Defaults are a typical subscriber — adjust to your customer, then score.</div>', unsafe_allow_html=True)

    with st.form("customer_form"):
        with st.container(border=True):
            st.markdown('<div class="group-label">🧑 Personal & Account</div>', unsafe_allow_html=True)
            a, b, c, d = st.columns(4)
            gender    = a.selectbox("Gender", ["Female", "Male"])
            senior    = b.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x else "No")
            partner   = c.selectbox("Partner", ["Yes", "No"])
            dependents = d.selectbox("Dependents", ["Yes", "No"])
            a, b = st.columns([1, 3])
            phone     = a.selectbox("Phone Service", ["Yes", "No"])
            tenure    = b.slider("Tenure (months)", 0, 72, 12)

        with st.container(border=True):
            st.markdown('<div class="group-label">📡 Services & Add-ons</div>', unsafe_allow_html=True)
            a, b, c = st.columns(3)
            internet  = a.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
            lines     = b.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
            sec       = c.selectbox("Online Security", ["No", "Yes", "No internet service"])
            a, b, c = st.columns(3)
            backup    = a.selectbox("Online Backup", ["No", "Yes", "No internet service"])
            device    = b.selectbox("Device Protection", ["No", "Yes", "No internet service"])
            tech      = c.selectbox("Tech Support", ["No", "Yes", "No internet service"])
            a, b = st.columns(2)
            tv        = a.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
            movies    = b.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

        with st.container(border=True):
            st.markdown('<div class="group-label">💳 Contract & Billing</div>', unsafe_allow_html=True)
            a, b = st.columns(2)
            contract  = a.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
            paperless = b.selectbox("Paperless Billing", ["Yes", "No"])
            payment   = st.selectbox("Payment Method", [
                "Electronic check", "Mailed check",
                "Bank transfer (automatic)", "Credit card (automatic)",
            ])
            a, b = st.columns(2)
            monthly   = a.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0, 1.0)
            total     = b.number_input("Total Charges ($)", 0.0, 10000.0, 840.0, 10.0)

        submitted = st.form_submit_button("✨  Predict Customer Churn", use_container_width=True)

    if submitted:
        row = {
            "gender": gender, "SeniorCitizen": senior, "Partner": partner,
            "Dependents": dependents, "tenure": tenure, "PhoneService": phone,
            "MultipleLines": lines, "InternetService": internet,
            "OnlineSecurity": sec, "OnlineBackup": backup, "DeviceProtection": device,
            "TechSupport": tech, "StreamingTV": tv, "StreamingMovies": movies,
            "Contract": contract, "PaperlessBilling": paperless,
            "PaymentMethod": payment, "MonthlyCharges": monthly, "TotalCharges": total,
        }
        try:
            p, will_churn = churn_probability(pd.DataFrame([row]))
            st.session_state["result"] = {
                "p": p, "will_churn": will_churn,
                "flags": risk_flags(row), "actions": playbook(row, p), "row": row,
            }
        except Exception as exc:
            st.session_state.pop("result", None)
            st.error(f"Prediction failed: {exc}")

with result_col:
    st.markdown('<div class="sec-title">📊 Score Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Live output from your trained pipeline.</div>', unsafe_allow_html=True)

    if "result" not in st.session_state:
        st.markdown("""
        <div class="empty">
          <div class="ico">🎯</div>
          <b>No score yet</b>
          Complete the profile and press<br><i>Predict Customer Churn</i>.
        </div>
        """, unsafe_allow_html=True)
    else:
        r = st.session_state["result"]
        p = r["p"]
        band, band_label, band_colors = risk_band(p)
        headline = "⚠️ Churn Risk Identified" if r["will_churn"] else "✅ Likely to Stay"

        flags_html = "".join(f'<span class="flag">{f}</span>' for f in r["flags"]) \
                     or '<span class="flag">✨ No major risk flags</span>'

        st.markdown(f"""
        <div class="result-shell">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="risk-chip chip-{band}">{band_label}</span>
            <span style="color:#7d90b8; font-size:11px; font-weight:600;">MODEL OUTPUT</span>
          </div>
          <div class="donut-wrap">{donut_svg(p, band_colors)}</div>
          <div style="text-align:center; color:#fff; font-weight:800; font-size:17px; margin-bottom:14px;">
            {headline}
          </div>
          <div style="margin-bottom:6px;">{flags_html}</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(min(max(p, 0.0), 1.0))

        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="group-label">📋 Recommended actions</div>', unsafe_allow_html=True)
        st.markdown('<div class="result-shell" style="padding:8px 20px;">', unsafe_allow_html=True)
        for i, tip in enumerate(r["actions"], 1):
            st.markdown(
                f'<div class="action-item"><span class="action-num">{i}</span><span>{tip}</span></div>',
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

        with st.expander("🔎 View input summary"):
            st.dataframe(pd.DataFrame([r["row"]]), use_container_width=True, hide_index=True)

# =========================================================
# 8. FOOTER
# =========================================================
st.markdown("""
<div class="footer">
  ChurnIQ · Customer Churn Prediction · Python + Scikit-learn + Streamlit<br>
  Predictions are estimates and should support, not replace, business judgment.
</div>
""", unsafe_allow_html=True)