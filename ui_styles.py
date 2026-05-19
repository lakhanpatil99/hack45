"""AutoNQ AI — Premium SaaS Design System v4.0
Palette: #16425B #2F6690 #3A7CA5 #81C3D7 #D9DCD6
"""

_NAMED_COLORS = {
    "cyan":    ("#81C3D7", "rgba(129,195,215,0.13)"),
    "blue":    ("#3A7CA5", "rgba(58,124,165,0.13)"),
    "navy":    ("#2F6690", "rgba(47,102,144,0.13)"),
    "emerald": ("#6ECBA0", "rgba(110,203,160,0.13)"),
    "amber":   ("#E0A84D", "rgba(224,168,77,0.13)"),
    "rose":    ("#D9605A", "rgba(217,96,90,0.13)"),
    "violet":  ("#9B8EC4", "rgba(155,142,196,0.13)"),
    "orange":  ("#D4875E", "rgba(212,135,94,0.13)"),
    "gray":    ("#8A9BA5", "rgba(138,155,165,0.13)"),
}

def _resolve_color(color: str) -> tuple:
    if color in _NAMED_COLORS:
        return _NAMED_COLORS[color]
    if isinstance(color, str) and color.startswith("#") and len(color) == 7:
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        return (color, f"rgba({r},{g},{b},0.13)")
    return _NAMED_COLORS["cyan"]

THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
@import url('https://cdn-uicons.flaticon.com/2.1.0/uicons-regular-rounded/css/uicons-regular-rounded.css');

@keyframes spin { to { transform: rotate(360deg); } }
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
@keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.6; } }
@keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }

:root {
    --bg-base: #0A1929;
    --bg-surface: #0E2236;
    --bg-card: #132D44;
    --bg-raised: #16425B;
    --bg-hover: #1E5572;
    --primary: #81C3D7;
    --primary-dim: rgba(129,195,215,0.15);
    --secondary: #3A7CA5;
    --tertiary: #2F6690;
    --border-dim: rgba(129,195,215,0.08);
    --border-mid: rgba(129,195,215,0.16);
    --border-hi: rgba(129,195,215,0.28);
    --t1: #FFFFFF;
    --t2: #D9DCD6;
    --t3: #9BADB8;
    --t4: #5E7A8A;
    --t5: #3A5060;
    --success: #6ECBA0;
    --warning: #E0A84D;
    --error: #D9605A;
    --info: #81C3D7;
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 20px;
    --shadow-sm: 0 2px 8px rgba(10,25,41,0.3);
    --shadow-md: 0 4px 16px rgba(10,25,41,0.4);
    --shadow-lg: 0 8px 32px rgba(10,25,41,0.5);
    --glass-bg: rgba(19,45,68,0.55);
    --glass-border: rgba(129,195,215,0.1);
    --glass-blur: blur(16px);
}

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"], .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: var(--bg-base) !important;
    color: var(--t2) !important;
}

.block-container {
    padding: 1.5rem 2.5rem 4rem !important;
    max-width: 1320px !important;
    animation: fadeIn 0.35s ease-out;
}

header[data-testid="stHeader"] {
    background: var(--bg-surface) !important;
    border-bottom: 1px solid var(--border-dim) !important;
    backdrop-filter: var(--glass-blur) !important;
    -webkit-backdrop-filter: var(--glass-blur) !important;
    height: 3rem !important;
}

[data-testid="stDecoration"] { display: none !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--bg-surface) 0%, #0B1D2E 100%) !important;
    border-right: 1px solid var(--border-dim) !important;
    min-width: 240px !important;
    max-width: 240px !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 0 !important;
    overflow-x: hidden !important;
}

[data-testid="stSidebar"] .stRadio > label { display: none !important; }

[data-testid="stSidebar"] .stRadio > div {
    display: flex !important;
    flex-direction: column !important;
    gap: 2px !important;
    padding: 0 12px !important;
}

[data-testid="stSidebar"] .stRadio > div > label > div:first-child,
[data-testid="stSidebar"] .stRadio input[type="radio"] {
    display: none !important;
    visibility: hidden !important;
    width: 0 !important; height: 0 !important;
    margin: 0 !important; padding: 0 !important;
}

[data-testid="stSidebar"] .stRadio > div > label {
    background: transparent !important;
    padding: 10px 14px !important;
    border-radius: var(--radius-sm) !important;
    font-weight: 500 !important;
    font-size: 13.5px !important;
    color: var(--t3) !important;
    cursor: pointer !important;
    transition: all 0.2s cubic-bezier(0.4,0,0.2,1) !important;
    border: 1px solid transparent !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    width: 100% !important;
    letter-spacing: 0.01em !important;
}

/* ── Uicons for Navigation ── */
[data-testid="stSidebar"] .stRadio > div:nth-child(1) > label::before { content: "\\f4c2"; font-family: uicons-regular-rounded !important; font-size: 1.25rem; }
[data-testid="stSidebar"] .stRadio > div:nth-child(2) > label::before { content: "\\f333"; font-family: uicons-regular-rounded !important; font-size: 1.25rem; }
[data-testid="stSidebar"] .stRadio > div:nth-child(3) > label::before { content: "\\f2d4"; font-family: uicons-regular-rounded !important; font-size: 1.25rem; }
[data-testid="stSidebar"] .stRadio > div:nth-child(4) > label::before { content: "\\f76a"; font-family: uicons-regular-rounded !important; font-size: 1.25rem; }
[data-testid="stSidebar"] .stRadio > div:nth-child(5) > label::before { content: "\\f9b2"; font-family: uicons-regular-rounded !important; font-size: 1.25rem; }
[data-testid="stSidebar"] .stRadio > div:nth-child(6) > label::before { content: "\\f79f"; font-family: uicons-regular-rounded !important; font-size: 1.25rem; }
[data-testid="stSidebar"] .stRadio > div:nth-child(7) > label::before { content: "\\f614"; font-family: uicons-regular-rounded !important; font-size: 1.25rem; }
[data-testid="stSidebar"] .stRadio > div:nth-child(8) > label::before { content: "\\f93c"; font-family: uicons-regular-rounded !important; font-size: 1.25rem; }

[data-testid="stSidebar"] .stRadio > div > label > div {
    display: inline !important;
}

[data-testid="stSidebar"] .stRadio > div > label:hover {
    background: rgba(129,195,215,0.06) !important;
    color: var(--t1) !important;
    border-color: var(--border-mid) !important;
    transform: translateX(2px);
}

[data-testid="stSidebar"] .stRadio > div > label[data-checked="true"],
[data-testid="stSidebar"] .stRadio > div > label[aria-checked="true"] {
    background: linear-gradient(135deg, rgba(58,124,165,0.18), rgba(129,195,215,0.1)) !important;
    color: var(--primary) !important;
    border-color: rgba(129,195,215,0.3) !important;
    font-weight: 700 !important;
    box-shadow: inset 3px 0 0 var(--primary);
}

/* ── TYPOGRAPHY ── */
h1, h2, h3, h4 {
    font-family: 'Inter', sans-serif !important;
    color: var(--t1) !important;
    margin-bottom: 0.25rem !important;
    letter-spacing: -0.02em !important;
}
h1 { font-size: 1.85rem !important; font-weight: 800 !important; }
h2 { font-size: 1.35rem !important; font-weight: 700 !important; }
h3 { font-size: 1.1rem !important; font-weight: 700 !important; }
p  { color: var(--t2) !important; line-height: 1.7 !important; }
li { color: var(--t2) !important; }

/* ── BUTTONS ── */
div.stButton {
    max-width: 340px;
    margin-left: auto;
    margin-right: auto;
}

div.stButton > button,
button[data-testid="stBaseButton-primary"],
button[data-testid="stBaseButton-secondary"],
button[kind="primary"], button[kind="secondary"] {
    border-radius: var(--radius-sm) !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    font-family: 'Inter', sans-serif !important;
    padding: 0.6rem 1.6rem !important;
    transition: all 0.25s cubic-bezier(0.4,0,0.2,1) !important;
    letter-spacing: 0.01em !important;
    border: none !important;
    cursor: pointer !important;
    position: relative !important;
    overflow: hidden !important;
}

div.stButton > button,
button[data-testid="stBaseButton-primary"],
button[kind="primary"] {
    background: linear-gradient(135deg, #3A7CA5 0%, #81C3D7 100%) !important;
    color: #0A1929 !important;
    box-shadow: 0 2px 12px rgba(129,195,215,0.25) !important;
}

div.stButton > button:hover,
button[data-testid="stBaseButton-primary"]:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 24px rgba(129,195,215,0.35) !important;
    filter: brightness(1.08) !important;
}

div.stButton > button:active { transform: translateY(0) scale(0.98) !important; }

button[data-testid="stBaseButton-secondary"],
button[kind="secondary"] {
    background: var(--bg-card) !important;
    color: var(--t2) !important;
    border: 1px solid var(--border-mid) !important;
}

button[data-testid="stBaseButton-secondary"]:hover {
    background: var(--bg-raised) !important;
    border-color: var(--primary) !important;
    color: var(--primary) !important;
}

button:disabled {
    opacity: 0.45 !important;
    cursor: not-allowed !important;
    transform: none !important;
    filter: grayscale(0.4) !important;
}

/* ── FORM INPUTS ── */
input[type="text"], input[type="number"], input[type="email"],
input[type="password"], input[type="search"], textarea,
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea,
[data-testid="stNumberInput"] input, .stTextInput input,
.stTextArea textarea, .stNumberInput input {
    background: var(--bg-card) !important;
    border: 1.5px solid var(--border-mid) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--t1) !important;
    font-size: 14px !important;
    font-family: 'Inter', sans-serif !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
    caret-color: var(--primary) !important;
    padding: 10px 14px !important;
}

input[type="text"]:focus, input[type="number"]:focus, textarea:focus,
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px var(--primary-dim) !important;
    outline: none !important;
}

input::placeholder, textarea::placeholder,
[data-testid="stTextInput"] input::placeholder,
[data-testid="stTextArea"] textarea::placeholder {
    color: var(--t4) !important;
    opacity: 1 !important;
}

/* ── DATE INPUT ── */
[data-testid="stDateInput"] > div,
[data-testid="stDateInput"] > div > div,
[data-testid="stDateInput"] [data-baseweb="input"],
[data-testid="stDateInput"] [data-baseweb="base-input"] {
    background: var(--bg-card) !important;
    border: 1.5px solid var(--border-mid) !important;
    border-color: var(--border-mid) !important;
    border-radius: var(--radius-sm) !important;
    box-shadow: none !important;
    outline: none !important;
    color-scheme: dark !important;
}

[data-testid="stDateInput"] > div:focus-within,
[data-testid="stDateInput"] > div > div:focus-within,
[data-testid="stDateInput"] [data-baseweb="input"]:focus-within,
[data-testid="stDateInput"] [data-baseweb="base-input"]:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px var(--primary-dim) !important;
}

[data-testid="stDateInput"] input {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
    color: var(--t1) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    color-scheme: dark !important;
    padding: 10px 14px !important;
}

[data-testid="stDateInput"] * { box-shadow: none !important; }
[data-testid="stDateInput"] *:focus { outline: none !important; }
[data-testid="stDateInput"] svg { color: var(--t3) !important; }

/* ── SELECTBOX ── */
[data-testid="stSelectbox"] > div > div,
.stSelectbox > div > div > div {
    background: var(--bg-card) !important;
    border: 1.5px solid var(--border-mid) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--t1) !important;
}

[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px var(--primary-dim) !important;
}

[data-testid="stSelectbox"] span, [data-testid="stSelectbox"] p { color: var(--t1) !important; }
[data-testid="stSelectbox"] svg { color: var(--t3) !important; }

[data-testid="stSelectbox"] ul, [role="listbox"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-mid) !important;
    border-radius: var(--radius-sm) !important;
    box-shadow: var(--shadow-lg) !important;
}

[role="option"] {
    color: var(--t2) !important;
    background: transparent !important;
    font-size: 14px !important;
    transition: background 0.15s !important;
}
[role="option"]:hover, [role="option"][aria-selected="true"] {
    background: var(--bg-hover) !important;
    color: var(--t1) !important;
}

/* ── FIELD LABELS ── */
[data-testid="stTextInput"] label, [data-testid="stTextArea"] label,
[data-testid="stNumberInput"] label, [data-testid="stSelectbox"] label,
[data-testid="stDateInput"] label, [data-testid="stFileUploader"] label,
[data-testid="stCheckbox"] label, [data-testid="stRadio"] label,
.stTextInput label, .stTextArea label, .stSelectbox label,
.stDateInput label, label {
    color: var(--t3) !important;
    font-size: 11.5px !important;
    font-weight: 600 !important;
    letter-spacing: 0.07em !important;
    text-transform: uppercase !important;
    margin-bottom: 4px !important;
}

[data-testid="stTextInput"] label span,
[data-testid="stTextArea"] label span,
[data-testid="stSelectbox"] label span { color: var(--t3) !important; }

/* ── FILE UPLOADER ── */
[data-testid="stFileUploader"] {
    background: var(--bg-card) !important;
    border: 2px dashed var(--border-mid) !important;
    border-radius: var(--radius-md) !important;
    transition: border-color 0.25s !important;
}
[data-testid="stFileUploader"]:hover { border-color: var(--primary) !important; }

[data-testid="stFileUploader"] section,
[data-testid="stFileUploader"] section > div,
[data-testid="stFileUploadDropzone"],
[data-testid="stFileUploadDropzone"] > div {
    background: transparent !important;
    border: none !important;
}

[data-testid="stFileUploader"] button,
[data-testid="stFileUploadDropzone"] button {
    background: var(--bg-raised) !important;
    color: var(--t1) !important;
    border: 1px solid var(--border-hi) !important;
    border-radius: var(--radius-sm) !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 6px 16px !important;
    width: auto !important;
    max-width: none !important;
}
[data-testid="stFileUploader"] button:hover {
    background: var(--primary-dim) !important;
    border-color: var(--primary) !important;
    color: var(--primary) !important;
}

[data-testid="stFileUploader"] p,
[data-testid="stFileUploadDropzone"] p,
[data-testid="stFileUploadDropzone"] span { color: var(--t4) !important; font-size: 13px !important; }

/* ── CHECKBOX ── */
[data-testid="stCheckbox"] input[type="checkbox"] {
    accent-color: var(--primary) !important;
    width: 17px !important;
    height: 17px !important;
    cursor: pointer !important;
    flex-shrink: 0 !important;
}

[data-testid="stCheckbox"] [data-baseweb="checkbox"] > div:first-child,
[data-testid="stCheckbox"] [role="checkbox"] > div:first-child {
    background-color: var(--bg-card) !important;
    border: 1.5px solid var(--border-mid) !important;
    border-radius: 5px !important;
    width: 18px !important;
    height: 18px !important;
    transition: background-color 0.18s, border-color 0.18s, box-shadow 0.18s !important;
    flex-shrink: 0 !important;
}

[data-testid="stCheckbox"] [data-baseweb="checkbox"]:hover > div:first-child,
[data-testid="stCheckbox"] [role="checkbox"]:hover > div:first-child {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px var(--primary-dim) !important;
}

[data-testid="stCheckbox"] [data-baseweb="checkbox"][aria-checked="true"] > div:first-child,
[data-testid="stCheckbox"] [role="checkbox"][aria-checked="true"] > div:first-child,
[data-testid="stCheckbox"] [data-baseweb="checkbox"][data-checked="true"] > div:first-child {
    background: linear-gradient(135deg, #3A7CA5 0%, #81C3D7 100%) !important;
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px var(--primary-dim) !important;
}

[data-testid="stCheckbox"] [data-baseweb="checkbox"] svg,
[data-testid="stCheckbox"] [role="checkbox"] svg {
    color: #0A1929 !important;
    fill: #0A1929 !important;
}

[data-testid="stCheckbox"] [data-baseweb="checkbox"] span,
[data-testid="stCheckbox"] [role="checkbox"] ~ span,
[data-testid="stCheckbox"] p {
    color: var(--t2) !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    letter-spacing: 0 !important;
    text-transform: none !important;
    cursor: pointer !important;
}

/* ── CAMERA INPUT ── */
[data-testid="stCameraInput"] {
    background: var(--bg-card) !important;
    border: 1.5px solid var(--border-mid) !important;
    border-radius: var(--radius-md) !important;
    overflow: hidden !important;
}

[data-testid="stCameraInput"] > div,
[data-testid="stCameraInput"] section,
[data-testid="stCameraInput"] section > div,
[data-testid="stCameraInputButton"],
[data-testid="stCameraInput"] [data-testid="stCameraInputButton"] {
    background: var(--bg-card) !important;
    border: none !important;
}

[data-testid="stCameraInput"] video,
[data-testid="stCameraInput"] iframe,
[data-testid="stCameraInput"] > div > div {
    background: var(--bg-card) !important;
    border-radius: var(--radius-sm) !important;
}

[data-testid="stCameraInput"] > div > div > div {
    background: var(--bg-raised) !important;
    border-radius: var(--radius-sm) !important;
}

[data-testid="stCameraInput"] img,
[data-testid="stCameraInput"] svg {
    filter: invert(0.6) sepia(1) saturate(2) hue-rotate(170deg) !important;
    opacity: 0.6 !important;
}

[data-testid="stCameraInput"] p,
[data-testid="stCameraInput"] span,
[data-testid="stCameraInput"] small {
    color: var(--t4) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
}

[data-testid="stCameraInput"] a {
    color: var(--primary) !important;
    text-decoration: none !important;
    font-weight: 600 !important;
}
[data-testid="stCameraInput"] a:hover {
    color: var(--t1) !important;
    text-decoration: underline !important;
}

[data-testid="stCameraInputButton"],
[data-testid="stCameraInput"] button {
    background: linear-gradient(135deg, #3A7CA5 0%, #81C3D7 100%) !important;
    color: #0A1929 !important;
    border: none !important;
    border-radius: 0 0 var(--radius-md) var(--radius-md) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 0.02em !important;
    padding: 12px 0 !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: filter 0.2s, box-shadow 0.2s !important;
    box-shadow: 0 -1px 0 rgba(129,195,215,0.15) !important;
}

[data-testid="stCameraInputButton"]:hover,
[data-testid="stCameraInput"] button:hover {
    filter: brightness(1.1) !important;
    box-shadow: 0 4px 20px rgba(129,195,215,0.3) !important;
}

/* ── METRICS ── */
[data-testid="stMetric"] {
    background: var(--glass-bg) !important;
    backdrop-filter: var(--glass-blur) !important;
    -webkit-backdrop-filter: var(--glass-blur) !important;
    border: 1px solid var(--glass-border) !important;
    border-top: 2px solid var(--primary) !important;
    border-radius: var(--radius-md) !important;
    padding: 20px !important;
}
[data-testid="stMetricLabel"] > div, [data-testid="stMetricLabel"] label {
    color: var(--t4) !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}
[data-testid="stMetricValue"] > div {
    color: var(--t1) !important;
    font-size: 1.0rem !important;
    font-weight: 800 !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── EXPANDER ── */
.streamlit-expander, [data-testid="stExpander"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-mid) !important;
    border-radius: var(--radius-md) !important;
    overflow: hidden !important;
}
.streamlit-expanderHeader {
    font-weight: 600 !important;
    font-size: 14px !important;
    color: var(--t2) !important;
    background: var(--bg-card) !important;
}

/* ════════════════════════════════════════════════════════════════
   ── DATAFRAME & DATA EDITOR — Full Dark Theme Override ──
   ════════════════════════════════════════════════════════════════ */

/* Outer wrapper */
.stDataFrame,
[data-testid="stDataFrame"],
[data-testid="stDataEditor"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-mid) !important;
    border-top: 2.5px solid var(--primary) !important;
    border-radius: var(--radius-md) !important;
    overflow: hidden !important;
    box-shadow: 0 4px 24px rgba(10,25,41,0.45), 0 0 0 1px rgba(129,195,215,0.06) !important;
}

/* All inner div layers — force dark background */
[data-testid="stDataFrame"] > div,
[data-testid="stDataFrame"] > div > div,
[data-testid="stDataFrame"] > div > div > div,
[data-testid="stDataEditor"] > div,
[data-testid="stDataEditor"] > div > div,
[data-testid="stDataEditor"] > div > div > div {
    background: var(--bg-card) !important;
    color: var(--t2) !important;
}

/* Resizable wrapper */
[data-testid="stDataFrameResizable"],
[data-testid="stDataFrameResizable"] > div {
    background: var(--bg-card) !important;
    border-radius: var(--radius-md) !important;
    overflow: hidden !important;
}

/* ── Toolbar / fullscreen bar ── */
[data-testid="stDataFrame"] > div > div > div:first-child,
[data-testid="stDataEditor"] > div > div > div:first-child {
    background: var(--bg-raised) !important;
    border-bottom: 1px solid var(--border-mid) !important;
    padding: 4px 10px !important;
}

[data-testid="stDataFrame"] > div > div > div:first-child button,
[data-testid="stDataEditor"] > div > div > div:first-child button {
    color: var(--t3) !important;
    background: transparent !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    padding: 4px 6px !important;
    transition: color 0.2s, background 0.2s !important;
}
[data-testid="stDataFrame"] > div > div > div:first-child button:hover,
[data-testid="stDataEditor"] > div > div > div:first-child button:hover {
    color: var(--primary) !important;
    background: var(--primary-dim) !important;
}

/* ── iframe (Glide Data Grid canvas host) ── */
[data-testid="stDataFrame"] iframe,
[data-testid="stDataEditor"] iframe {
    background: var(--bg-card) !important;
    border-radius: 0 0 var(--radius-md) var(--radius-md) !important;
    color-scheme: dark !important;
    /* Force the iframe document background dark via CSS filter trick */
    filter: none !important;
}

/* ── Glide Data Grid: header row ── */
[data-testid="stDataFrame"] [role="columnheader"],
[data-testid="stDataEditor"] [role="columnheader"],
[data-testid="stDataFrame"] .dvn-stack [role="columnheader"],
[data-testid="stDataEditor"] .dvn-stack [role="columnheader"] {
    background: var(--bg-raised) !important;
    color: var(--t3) !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.07em !important;
    border-bottom: 1px solid var(--border-mid) !important;
    border-right: 1px solid var(--border-dim) !important;
    font-family: 'Inter', sans-serif !important;
    padding: 0 12px !important;
}

/* ── Glide Data Grid: data cells ── */
[data-testid="stDataFrame"] [role="gridcell"],
[data-testid="stDataEditor"] [role="gridcell"],
[data-testid="stDataFrame"] .dvn-stack [role="gridcell"],
[data-testid="stDataEditor"] .dvn-stack [role="gridcell"] {
    background: var(--bg-card) !important;
    color: var(--t2) !important;
    font-size: 13px !important;
    font-family: 'Inter', sans-serif !important;
    border-bottom: 1px solid var(--border-dim) !important;
    border-right: 1px solid rgba(129,195,215,0.04) !important;
}

/* ── Glide Data Grid: hover row ── */
[data-testid="stDataFrame"] [role="row"]:hover [role="gridcell"],
[data-testid="stDataEditor"] [role="row"]:hover [role="gridcell"] {
    background: var(--bg-raised) !important;
    transition: background 0.15s !important;
}

/* ── Glide Data Grid: selected cell ── */
[data-testid="stDataFrame"] [role="gridcell"][aria-selected="true"],
[data-testid="stDataEditor"] [role="gridcell"][aria-selected="true"] {
    background: rgba(129,195,215,0.1) !important;
    outline: 1px solid var(--primary) !important;
    outline-offset: -1px !important;
}

/* ── Index / row number column ── */
[data-testid="stDataFrame"] [role="rowheader"],
[data-testid="stDataEditor"] [role="rowheader"] {
    background: var(--bg-raised) !important;
    color: var(--t4) !important;
    font-size: 11.5px !important;
    font-family: 'Inter', sans-serif !important;
    border-right: 1px solid var(--border-mid) !important;
    font-weight: 600 !important;
}

/* ── Scrollbars inside dataframe ── */
[data-testid="stDataFrame"] ::-webkit-scrollbar,
[data-testid="stDataEditor"] ::-webkit-scrollbar { width: 5px; height: 5px; }
[data-testid="stDataFrame"] ::-webkit-scrollbar-track,
[data-testid="stDataEditor"] ::-webkit-scrollbar-track { background: var(--bg-card); }
[data-testid="stDataFrame"] ::-webkit-scrollbar-thumb,
[data-testid="stDataEditor"] ::-webkit-scrollbar-thumb {
    background: var(--t5);
    border-radius: 99px;
}
[data-testid="stDataFrame"] ::-webkit-scrollbar-thumb:hover,
[data-testid="stDataEditor"] ::-webkit-scrollbar-thumb:hover { background: var(--t4); }

/* ── Fallback: classic <table> rendering ── */
[data-testid="stDataFrame"] table,
[data-testid="stDataEditor"] table {
    background: var(--bg-card) !important;
    width: 100% !important;
    border-collapse: collapse !important;
}

[data-testid="stDataFrame"] thead tr th,
[data-testid="stDataEditor"] thead tr th {
    background: var(--bg-raised) !important;
    color: var(--t3) !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.07em !important;
    border-bottom: 1.5px solid var(--border-mid) !important;
    border-right: 1px solid var(--border-dim) !important;
    padding: 12px 16px !important;
    font-family: 'Inter', sans-serif !important;
    white-space: nowrap !important;
}

[data-testid="stDataFrame"] tbody tr td,
[data-testid="stDataEditor"] tbody tr td {
    color: var(--t2) !important;
    border-bottom: 1px solid var(--border-dim) !important;
    border-right: 1px solid rgba(129,195,215,0.04) !important;
    padding: 10px 16px !important;
    font-size: 13px !important;
    background: var(--bg-card) !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stDataFrame"] tbody tr:nth-child(even) td,
[data-testid="stDataEditor"] tbody tr:nth-child(even) td {
    background: rgba(22,66,91,0.25) !important;
}

[data-testid="stDataFrame"] tbody tr:hover td,
[data-testid="stDataEditor"] tbody tr:hover td {
    background: var(--bg-raised) !important;
    transition: background 0.15s !important;
}

[data-testid="stDataFrame"] tbody tr:last-child td,
[data-testid="stDataEditor"] tbody tr:last-child td {
    border-bottom: none !important;
}

/* ── st.table (static table) ── */
.stTable table,
[data-testid="stTable"] table {
    background: var(--bg-card) !important;
    width: 100% !important;
    border-collapse: collapse !important;
    border: 1px solid var(--border-mid) !important;
    border-top: 2.5px solid var(--primary) !important;
    border-radius: var(--radius-md) !important;
    overflow: hidden !important;
    box-shadow: var(--shadow-md) !important;
}

.stTable table thead tr th,
[data-testid="stTable"] table thead tr th {
    background: var(--bg-raised) !important;
    color: var(--t3) !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.07em !important;
    border-bottom: 1.5px solid var(--border-mid) !important;
    padding: 12px 16px !important;
    font-family: 'Inter', sans-serif !important;
}

.stTable table tbody tr td,
[data-testid="stTable"] table tbody tr td {
    color: var(--t2) !important;
    border-bottom: 1px solid var(--border-dim) !important;
    padding: 10px 16px !important;
    font-size: 13px !important;
    background: var(--bg-card) !important;
    font-family: 'Inter', sans-serif !important;
}

.stTable table tbody tr:nth-child(even) td,
[data-testid="stTable"] table tbody tr:nth-child(even) td {
    background: rgba(22,66,91,0.25) !important;
}

.stTable table tbody tr:hover td,
[data-testid="stTable"] table tbody tr:hover td {
    background: var(--bg-raised) !important;
    transition: background 0.15s !important;
}

/* ════════════════════════════════════════════════════════════════ */

/* ── TABS ── */
[data-testid="stTabs"] > div > div:first-child { border-bottom: 1px solid var(--border-mid) !important; }
button[data-baseweb="tab"] {
    color: var(--t4) !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    background: transparent !important;
    border: none !important;
    padding: 10px 20px !important;
    transition: color 0.2s !important;
}
button[data-baseweb="tab"]:hover { color: var(--t2) !important; }
button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--primary) !important;
    border-bottom: 2px solid var(--primary) !important;
}

/* ── ALERTS ── */
[data-testid="stAlert"] { border-radius: var(--radius-sm) !important; }
.stInfo    { background: rgba(129,195,215,0.08) !important; border-left: 3px solid var(--info) !important; }
.stSuccess { background: rgba(110,203,160,0.08) !important; border-left: 3px solid var(--success) !important; }
.stWarning { background: rgba(224,168,77,0.08) !important; border-left: 3px solid var(--warning) !important; }
.stError   { background: rgba(217,96,90,0.08) !important;  border-left: 3px solid var(--error) !important; }

/* ── PROGRESS ── */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--secondary), var(--primary)) !important;
    border-radius: 99px !important;
}
.stProgress > div > div > div {
    background: var(--border-dim) !important;
    border-radius: 99px !important;
}

/* ── MISC ── */
hr { border: none !important; border-top: 1px solid var(--border-dim) !important; margin: 1.5rem 0 !important; }

::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg-base); }
::-webkit-scrollbar-thumb { background: var(--t5); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: var(--t4); }

.stMarkdown, .stText, [data-testid="stMarkdownContainer"] { color: var(--t2) !important; }
[data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li { color: var(--t2) !important; }
[data-testid="stCaptionContainer"] { color: var(--t4) !important; font-size: 12px !important; }

/* ── TOAST ── */
[data-testid="stToast"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-mid) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--t1) !important;
    box-shadow: var(--shadow-lg) !important;
}

/* ── SLIDER ── */
[data-testid="stSlider"] > div > div > div > div {
    background: linear-gradient(90deg, var(--secondary), var(--primary)) !important;
}
[data-testid="stSlider"] > div > div > div > div > div {
    background: var(--primary) !important;
    border: 2px solid var(--bg-base) !important;
    box-shadow: 0 0 0 2px var(--primary) !important;
}

/* ── RESPONSIVE ── */
@media (min-width: 1600px) {
    .block-container { max-width: 1400px !important; }
    div.stButton { max-width: 380px; }
}
@media (max-width: 768px) {
    .block-container { padding: 1rem 1rem 3rem !important; }
    [data-testid="stSidebar"] { min-width: 200px !important; max-width: 200px !important; }
    div.stButton { max-width: 100%; }
}

/* ── SPINNER OVERLAY ── */
[data-testid="stSpinner"] {
    background: rgba(10,25,41,0.6) !important;
    backdrop-filter: blur(4px) !important;
    border-radius: var(--radius-md) !important;
    padding: 16px !important;
}
[data-testid="stSpinner"] > div { color: var(--primary) !important; }

/* ── STREAMLIT NATIVE RED FOCUS KILL ── */
*:focus { outline-color: var(--primary) !important; }
[data-baseweb] *:focus { outline-color: var(--primary) !important; }
[data-baseweb="input"]:focus-within { border-color: var(--primary) !important; }
[data-baseweb="select"]:focus-within { border-color: var(--primary) !important; }
div[data-baseweb="popover"] { background: var(--bg-card) !important; border: 1px solid var(--border-mid) !important; border-radius: var(--radius-sm) !important; }

/* ── HORIZONTAL DIVIDER SECTION SPACING ── */
hr {
    margin: 2rem 0 !important;
}

/* ── SUBHEADER STYLING ── */
.stMarkdown h5 {
    color: var(--t3) !important;
    font-size: 11.5px !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    margin-bottom: 12px !important;
    padding-bottom: 6px !important;
    border-bottom: 1px solid var(--border-dim) !important;
}
</style>
"""


SIDEBAR_LOGO = """
<div style="
    padding: 24px 16px 20px;
    border-bottom: 1px solid rgba(129,195,215,0.08);
    margin-bottom: 12px;
">
    <div style="display:flex; align-items:center; gap:12px;">
        <div style="
            width: 40px; height: 40px; flex-shrink: 0;
            background: linear-gradient(135deg, #3A7CA5, #81C3D7);
            border-radius: 10px;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 4px 12px rgba(129,195,215,0.25);
        "><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0A1929" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect x="4" y="8" width="16" height="12" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg></div>
        <div>
            <div style="
                font-family: 'Inter', sans-serif;
                font-weight: 800; font-size: 1.25rem;
                background: linear-gradient(135deg, #81C3D7, #3A7CA5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                line-height: 1.15;
                letter-spacing: -0.02em;
            ">AutoNQ AI</div>
            <div style="
                color: #5E7A8A; font-size: 10px; font-weight: 600;
                letter-spacing: 0.1em; text-transform: uppercase; margin-top: 2px;
            ">Audit Intelligence</div>
        </div>
    </div>
</div>
"""

NAV_ITEMS = [
    "Audit Entry",
    "Summary",
    "Audit Plan",
    "Daily Q-Check",
    "Process Audit",
    "Follow-up",
    "External Tracker",
    "Repeatability",
]

LOADING_HTML = """
<div style="text-align:center;padding:48px 20px;">
    <div style="
        display:inline-block;width:40px;height:40px;
        border:3px solid rgba(129,195,215,0.15);
        border-top:3px solid #81C3D7;
        border-radius:50%;
        animation:spin 0.8s linear infinite;
    "></div>
    <p style="color:#5E7A8A;font-size:14px;margin-top:16px;font-weight:500;
              font-family:'Inter',sans-serif;">
        Processing with AI…
    </p>
</div>
<style>@keyframes spin{to{transform:rotate(360deg);}}</style>
"""

def sidebar_section(label: str) -> str:
    return f"""
    <div style="
        padding: 10px 14px 4px; font-size: 10px; font-weight: 700;
        color: #5E7A8A; letter-spacing: 0.12em; text-transform: uppercase;
        margin-top: 8px; font-family: 'Inter', sans-serif;
    ">{label}</div>"""


def kpi_card(icon: str, label: str, value, color: str = "cyan", trend: str = "") -> str:
    if isinstance(color, str) and color.startswith("#") and len(color) == 7:
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        hex_c, bg_c = color, f"rgba({r},{g},{b},0.1)"
    else:
        _map = {
            "cyan":    ("#81C3D7","rgba(129,195,215,0.1)"),
            "blue":    ("#3A7CA5","rgba(58,124,165,0.1)"),
            "navy":    ("#2F6690","rgba(47,102,144,0.1)"),
            "emerald": ("#6ECBA0","rgba(110,203,160,0.1)"),
            "amber":   ("#E0A84D","rgba(224,168,77,0.1)"),
            "rose":    ("#D9605A","rgba(217,96,90,0.1)"),
            "violet":  ("#9B8EC4","rgba(155,142,196,0.1)"),
            "orange":  ("#D4875E","rgba(212,135,94,0.1)"),
        }
        hex_c, bg_c = _map.get(color, _map["cyan"])

    trend_html = (
        f'<div style="color:{hex_c};font-size:11px;font-weight:600;margin-top:8px;'
        f'font-family:Inter,sans-serif;">{trend}</div>' if trend else ""
    )
    return f"""
    <div style="
        background:{bg_c};
        backdrop-filter:blur(8px); -webkit-backdrop-filter:blur(8px);
        border:1px solid {hex_c}22; border-top:2.5px solid {hex_c};
        border-radius:14px; padding:22px 16px 18px; text-align:center;
        transition: transform 0.2s, box-shadow 0.2s;
    ">
        <div style="font-size:1.2rem;margin-bottom:8px;line-height:1;
                    filter:drop-shadow(0 2px 4px rgba(0,0,0,0.2));">{icon}</div>
        <div style="
            color:#9BADB8; font-size:10.5px; font-weight:700;
            letter-spacing:0.08em; text-transform:uppercase; margin-bottom:8px;
            font-family:'Inter',sans-serif;
        ">{label}</div>
        <div style="
            color:#FFFFFF; font-size:1.8rem; font-weight:800;
            font-family:'Inter',sans-serif; line-height:1;
            letter-spacing:-0.02em;
        ">{value}</div>
        {trend_html}
    </div>"""


def section_header(icon: str, title: str, subtitle: str = "") -> str:
    # If icon is an SVG string, use it directly; otherwise wrap in a span
    if icon.strip().startswith("<svg"):
        icon_html = icon
    else:
        icon_html = f'<span style="font-size:1.2rem;line-height:1;">{icon}</span>'
    sub = (
        f'<p style="color:#9BADB8;font-size:13px;margin:4px 0 0;font-weight:400;'
        f'font-family:Inter,sans-serif;">{subtitle}</p>' if subtitle else ""
    )
    return f"""
    <div style="
        display:flex;align-items:flex-start;gap:14px;
        margin-bottom:24px;padding-bottom:16px;
        border-bottom:1px solid rgba(129,195,215,0.08);
    ">
        <div style="
            width:42px;height:42px;flex-shrink:0;
            background:#132D44;
            border:1px solid rgba(129,195,215,0.18);
            border-radius:10px;
            display:flex;align-items:center;justify-content:center;
            font-size:1.2rem;line-height:1;
        ">{icon_html}</div>
        <div>
            <h2 style="
                font-family:'Inter',sans-serif;
                color:#FFFFFF;font-size:1.3rem;font-weight:800;margin:0;line-height:1.2;
                letter-spacing:-0.02em;
            ">{title}</h2>
            {sub}
        </div>
    </div>"""


def ai_output_card(title: str, content: str) -> str:
    return f"""
    <div style="
        background:rgba(19,45,68,0.5);
        backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px);
        border:1px solid rgba(129,195,215,0.15);
        border-left:3px solid #81C3D7;border-radius:14px;
        padding:22px 24px;margin:16px 0;
    ">
        <div style="
            display:flex;align-items:center;gap:8px;
            margin-bottom:14px;padding-bottom:12px;
            border-bottom:1px solid rgba(129,195,215,0.06);
        ">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#81C3D7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M12 8V4H8"/><rect x="4" y="8" width="16" height="12" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>
            <span style="
                color:#81C3D7;font-weight:700;font-size:11.5px;
                letter-spacing:0.08em;text-transform:uppercase;
                font-family:'Inter',sans-serif;
            ">{title}</span>
            <span style="
                margin-left:auto;
                background:rgba(129,195,215,0.1);color:#81C3D7;
                font-size:10.5px;font-weight:600;padding:3px 12px;border-radius:99px;
                border:1px solid rgba(129,195,215,0.2);
                font-family:'Inter',sans-serif;
            ">AI Generated</span>
        </div>
        <div style="
            color:#D9DCD6;font-size:14px;line-height:1.8;
            white-space:pre-wrap;font-family:'Inter',sans-serif;
        ">{content}</div>
    </div>"""


def status_badge(connected: bool = True) -> str:
    if connected:
        return """<span style="
            display:inline-flex;align-items:center;gap:6px;
            background:rgba(110,203,160,0.1);border:1px solid rgba(110,203,160,0.25);
            color:#6ECBA0;font-size:12px;font-weight:600;
            padding:5px 14px;border-radius:99px;
            font-family:'Inter',sans-serif;
        "><span style="width:7px;height:7px;background:#6ECBA0;border-radius:50%;
            box-shadow:0 0 8px #6ECBA0;display:inline-block;"></span>System Online</span>"""
    return """<span style="
        display:inline-flex;align-items:center;gap:6px;
        background:rgba(217,96,90,0.1);border:1px solid rgba(217,96,90,0.25);
        color:#E8847E;font-size:12px;font-weight:600;
        padding:5px 14px;border-radius:99px;
        font-family:'Inter',sans-serif;
    "><span style="width:7px;height:7px;background:#D9605A;border-radius:50%;
        display:inline-block;"></span>Disconnected</span>"""


def empty_state(message: str) -> str:
    return f"""
    <div style="
        text-align:center;padding:48px 24px;
        background:#0E2236;
        border:1px solid rgba(129,195,215,0.10);
        border-radius:14px;margin:8px 0;
    ">
        <div style="
            width:56px;height:56px;
            background:#132D44;
            border:1px solid rgba(129,195,215,0.12);
            border-radius:14px;
            display:flex;align-items:center;justify-content:center;
            margin:0 auto 14px;font-size:1.6rem;line-height:1;
        ">📭</div>
        <p style="
            color:#9BADB8 !important;font-size:13.5px;
            max-width:340px;margin:0 auto;line-height:1.7;
            font-family:'Inter',sans-serif;font-weight:400;
        ">{message}</p>
    </div>"""


def callout(message: str, type: str = "info") -> str:
    cfg = {
        "info":    ("#81C3D7", "rgba(129,195,215,0.07)", "rgba(129,195,215,0.18)", "ℹ️"),
        "success": ("#6ECBA0", "rgba(110,203,160,0.07)", "rgba(110,203,160,0.18)", "✅"),
        "warning": ("#E0A84D", "rgba(224,168,77,0.07)",  "rgba(224,168,77,0.18)",  "⚠️"),
        "danger":  ("#D9605A", "rgba(217,96,90,0.07)",   "rgba(217,96,90,0.18)",   "🚨"),
    }
    c, bg, bd, icon = cfg.get(type, cfg["info"])
    return f"""
    <div style="
        background:{bg};border:1px solid {bd};border-left:3px solid {c};
        border-radius:10px;padding:14px 18px;
        display:flex;align-items:flex-start;gap:10px;margin:12px 0;
    ">
        <span style="font-size:0.95rem;flex-shrink:0;margin-top:1px;">{icon}</span>
        <span style="color:#D9DCD6;font-size:13.5px;line-height:1.65;
                     font-family:'Inter',sans-serif;">{message}</span>
    </div>"""


def data_row(label: str, value: str) -> str:
    return f"""
    <div style="
        display:flex;justify-content:space-between;align-items:center;
        padding:10px 0;border-bottom:1px solid rgba(129,195,215,0.06);
    ">
        <span style="color:#9BADB8;font-size:13px;font-weight:500;
                     font-family:'Inter',sans-serif;">{label}</span>
        <span style="color:#FFFFFF;font-size:13.5px;font-weight:600;
                     font-family:'Inter',sans-serif;">{value}</span>
    </div>"""


def severity_badge(level: str) -> str:
    lvls = {
        "Critical": ("#D9605A", "rgba(217,96,90,0.12)"),
        "Major":    ("#E0A84D", "rgba(224,168,77,0.12)"),
        "Minor":    ("#3A7CA5", "rgba(58,124,165,0.12)"),
        "OK":       ("#6ECBA0", "rgba(110,203,160,0.12)"),
    }
    c, bg = lvls.get(level, lvls["Minor"])
    return f"""<span style="
        background:{bg};color:{c};border:1px solid {c}44;
        font-size:11px;font-weight:700;letter-spacing:0.05em;
        padding:3px 12px;border-radius:6px;text-transform:uppercase;
        font-family:'Inter',sans-serif;
    ">{level}</span>"""


def page_header(title: str, subtitle: str = "", right_content: str = "") -> str:
    right = f'<div style="margin-left:auto;">{right_content}</div>' if right_content else ""
    sub = (f'<p style="color:#9BADB8;font-size:13.5px;margin:4px 0 0;'
           f'font-family:Inter,sans-serif;">{subtitle}</p>' if subtitle else "")
    return f"""
    <div style="
        display:flex;align-items:flex-start;
        margin-bottom:28px;padding-bottom:20px;
        border-bottom:1px solid rgba(129,195,215,0.08);
    ">
        <div>
            <h1 style="
                font-family:'Inter',sans-serif;font-weight:800;
                font-size:1.85rem;color:#FFFFFF;margin:0;line-height:1.15;
                letter-spacing:-0.02em;
            ">{title}</h1>
            {sub}
        </div>
        {right}
    </div>"""


def card(content: str, padding: str = "22px 24px") -> str:
    return f"""
    <div style="
        background:rgba(19,45,68,0.55);
        backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px);
        border:1px solid rgba(129,195,215,0.1);
        border-radius:14px;padding:{padding};margin:12px 0;
        box-shadow: 0 4px 16px rgba(10,25,41,0.3);
    ">{content}</div>"""


def progress_bar(label: str, value: float, color: str = "#81C3D7") -> str:
    pct = max(0.0, min(100.0, float(value)))
    return f"""
    <div style="margin:12px 0;">
        <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
            <span style="color:#9BADB8;font-size:13px;font-weight:500;
                         font-family:'Inter',sans-serif;">{label}</span>
            <span style="color:#FFFFFF;font-size:13px;font-weight:700;
                         font-family:'Inter',sans-serif;">{pct:.0f}%</span>
        </div>
        <div style="background:rgba(129,195,215,0.08);border-radius:99px;height:6px;overflow:hidden;">
            <div style="
                width:{pct}%;height:100%;
                background:linear-gradient(90deg,{color},{color}99);
                border-radius:99px;
                transition: width 0.5s ease;
            "></div>
        </div>
    </div>"""


def priority_badge(level: str) -> str:
    colors = {
        "High":   ("#D9605A", "rgba(217,96,90,0.12)"),
        "Medium": ("#E0A84D", "rgba(224,168,77,0.12)"),
        "Low":    ("#6ECBA0", "rgba(110,203,160,0.12)"),
    }
    c, bg = colors.get(level, colors["Medium"])
    return (
        f'<span style="background:{bg};color:{c};border:1px solid {c}44;'
        f'font-size:11px;font-weight:700;letter-spacing:0.05em;'
        f'padding:3px 12px;border-radius:6px;text-transform:uppercase;'
        f'font-family:\'Inter\',sans-serif;display:inline-block;">{level}</span>'
    )


def domain_tag(domain: str) -> str:
    colors = {
        "Safety":  ("#D9605A", "rgba(217,96,90,0.10)"),
        "Quality": ("#E0A84D", "rgba(224,168,77,0.10)"),
        "Process": ("#3A7CA5", "rgba(58,124,165,0.10)"),
    }
    c, bg = colors.get(domain, colors["Process"])
    return (
        f'<span style="background:{bg};color:{c};border:1px solid {c}33;'
        f'font-size:10px;font-weight:700;letter-spacing:0.06em;'
        f'padding:2px 10px;border-radius:99px;text-transform:uppercase;'
        f'font-family:\'Inter\',sans-serif;display:inline-block;margin-left:6px;">{domain}</span>'
    )


def _parse_ai_markdown(text: str) -> str:
    import re
    if not text:
        return "<p style='color:#5E7A8A;'>No content available.</p>"
    lines = text.strip().split("\n")
    html = []
    in_sec = False
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if s.startswith("**") and s.endswith("**") and len(s) > 4:
            heading = s.strip("*").strip()
            if in_sec:
                html.append("</div>")
            html.append(
                f'<div style="display:flex;align-items:center;gap:8px;margin:18px 0 8px;'
                f'padding-top:12px;border-top:1px solid rgba(129,195,215,0.06);">'
                f'<span style="color:#81C3D7;font-weight:700;font-size:13px;'
                f'letter-spacing:0.03em;font-family:\'Inter\',sans-serif;">{heading}</span></div>'
                f'<div style="padding-left:4px;">'
            )
            in_sec = True
        elif s.startswith(("- ", "• ", "* ")):
            bt = re.sub(r'\*\*(.+?)\*\*', r'<strong style="color:#FFFFFF;">\1</strong>', s[2:].strip())
            html.append(
                f'<div style="display:flex;gap:8px;margin:5px 0 5px 4px;">'
                f'<span style="color:#81C3D7;flex-shrink:0;margin-top:2px;">•</span>'
                f'<span style="color:#D9DCD6;font-size:13.5px;line-height:1.6;">{bt}</span></div>'
            )
        elif s[0].isdigit() and "." in s[:4]:
            nt = re.sub(r'\*\*(.+?)\*\*', r'<strong style="color:#FFFFFF;">\1</strong>', s.split(".", 1)[-1].strip())
            html.append(
                f'<div style="display:flex;gap:8px;margin:5px 0 5px 4px;">'
                f'<span style="color:#81C3D7;flex-shrink:0;font-weight:700;font-size:12px;'
                f'margin-top:2px;">{s.split(".")[0]}.</span>'
                f'<span style="color:#D9DCD6;font-size:13.5px;line-height:1.6;">{nt}</span></div>'
            )
        else:
            pt = re.sub(r'\*\*(.+?)\*\*', r'<strong style="color:#FFFFFF;">\1</strong>', s)
            html.append(f'<p style="color:#D9DCD6;margin:6px 0;font-size:13.5px;line-height:1.6;">{pt}</p>')
    if in_sec:
        html.append("</div>")
    return "\n".join(html)


def structured_ai_card(title: str, content: str) -> str:
    body = _parse_ai_markdown(content)
    return (
        f'<div style="background:rgba(19,45,68,0.5);backdrop-filter:blur(12px);'
        f'-webkit-backdrop-filter:blur(12px);border:1px solid rgba(129,195,215,0.15);'
        f'border-left:3px solid #81C3D7;border-radius:14px;padding:22px 24px;margin:16px 0;">'
        f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;'
        f'padding-bottom:12px;border-bottom:1px solid rgba(129,195,215,0.06);">'
        f'<span style="font-size:1rem;">🤖</span>'
        f'<span style="color:#81C3D7;font-weight:700;font-size:11.5px;letter-spacing:0.08em;'
        f'text-transform:uppercase;font-family:\'Inter\',sans-serif;">{title}</span>'
        f'<span style="margin-left:auto;background:rgba(129,195,215,0.1);color:#81C3D7;'
        f'font-size:10.5px;font-weight:600;padding:3px 12px;border-radius:99px;'
        f'border:1px solid rgba(129,195,215,0.2);font-family:\'Inter\',sans-serif;">AI Generated</span>'
        f'</div><div style="color:#D9DCD6;font-size:14px;line-height:1.8;'
        f'font-family:\'Inter\',sans-serif;">{body}</div></div>'
    )


def mail_preview_card(content: str) -> str:
    body = _parse_ai_markdown(content)
    return (
        f'<div style="background:#132D44;border:1px solid rgba(129,195,215,0.12);'
        f'border-top:2.5px solid #3A7CA5;border-radius:14px;padding:24px;'
        f'font-family:\'Inter\',sans-serif;">'
        f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;'
        f'padding-bottom:12px;border-bottom:1px solid rgba(129,195,215,0.06);">'
        f'<span style="font-size:1rem;">📧</span>'
        f'<span style="color:#81C3D7;font-weight:700;font-size:11.5px;letter-spacing:0.08em;'
        f'text-transform:uppercase;">Mail Preview</span></div>'
        f'<div style="color:#D9DCD6;font-size:13.5px;line-height:1.8;">{body}</div></div>'
    )


def tracker_issue_card(
    index, line, station, issue, recurrence,
    action, root_cause="", owner="", priority="Medium", domain_name="Process"
):
    pri = priority_badge(priority)
    dom = domain_tag(domain_name)
    rc_html = ""
    if root_cause:
        rc_html = (
            f'<div style="margin-top:10px;">'
            f'<span style="color:#9BADB8;font-size:11px;font-weight:700;'
            f'letter-spacing:0.06em;text-transform:uppercase;">Root Cause</span>'
            f'<p style="color:#D9DCD6;font-size:13px;margin:4px 0 0;line-height:1.5;">{root_cause}</p></div>'
        )
    own_html = ""
    if owner:
        own_html = (
            f'<span style="background:rgba(129,195,215,0.08);color:#9BADB8;font-size:11px;'
            f'font-weight:600;padding:3px 10px;border-radius:99px;border:1px solid '
            f'rgba(129,195,215,0.12);margin-left:8px;">👤 {owner}</span>'
        )
    return (
        f'<div style="background:rgba(19,45,68,0.45);backdrop-filter:blur(8px);'
        f'border:1px solid rgba(129,195,215,0.12);border-radius:14px;padding:20px 22px;margin:12px 0;">'
        f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;flex-wrap:wrap;">'
        f'<span style="color:#FFFFFF;font-weight:700;font-size:14px;font-family:\'Inter\',sans-serif;">'
        f'#{index}</span><span style="color:#9BADB8;font-size:12px;">Line {line} — {station}</span>'
        f'{pri}{dom}{own_html}'
        f'<span style="margin-left:auto;color:#9BADB8;font-size:12px;font-weight:600;">🔁 x{recurrence}</span></div>'
        f'<div style="margin-bottom:10px;">'
        f'<span style="color:#9BADB8;font-size:11px;font-weight:700;letter-spacing:0.06em;'
        f'text-transform:uppercase;">Issue</span>'
        f'<p style="color:#FFFFFF;font-size:13.5px;font-weight:500;margin:4px 0 0;line-height:1.5;">{issue}</p></div>'
        f'{rc_html}'
        f'<div style="margin-top:10px;padding-top:10px;border-top:1px solid rgba(129,195,215,0.06);">'
        f'<span style="color:#9BADB8;font-size:11px;font-weight:700;letter-spacing:0.06em;'
        f'text-transform:uppercase;">Corrective Action</span>'
        f'<p style="color:#6ECBA0;font-size:13px;font-weight:500;margin:4px 0 0;line-height:1.5;">{action}</p>'
        f'</div></div>'
    )
