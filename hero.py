import base64
import os


def get_hero_image_base64() -> tuple[str, str]:
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    if not os.path.isdir(assets_dir):
        return "", ""
    for fname in os.listdir(assets_dir):
        if fname.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            with open(os.path.join(assets_dir, fname), "rb") as f:
                ext = fname.rsplit(".", 1)[-1].lower()
                if ext == "jpg":
                    ext = "jpeg"
                return base64.b64encode(f.read()).decode(), ext
    return "", ""


def get_page_bg_css() -> str:
    b64, ext = get_hero_image_base64()
    if b64:
        bg = f"url('data:image/{ext};base64,{b64}') center/cover no-repeat fixed"
    else:
        bg = "linear-gradient(135deg, #0a1f0d, #122a15, #1a3a1e)"

    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

/* Full-page background image */
[data-testid="stAppViewContainer"] {{
    background: {bg};
}}

/* Dark overlay on main area */
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.45);
    z-index: 0;
    pointer-events: none;
}}

/* Make main content sit above overlay */
.block-container {{
    position: relative;
    z-index: 1;
    padding-top: 2rem !important;
    max-width: 800px !important;
}}

/* Sidebar styling */
section[data-testid="stSidebar"] {{
    background: rgba(255,255,255,0.97);
}}

/* Chat messages - frosted glass */
div[data-testid="stChatMessage"] {{
    background: rgba(255,255,255,0.1) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 14px !important;
    color: #fff !important;
}}

div[data-testid="stChatMessage"] p,
div[data-testid="stChatMessage"] li,
div[data-testid="stChatMessage"] h1,
div[data-testid="stChatMessage"] h2,
div[data-testid="stChatMessage"] h3,
div[data-testid="stChatMessage"] h4,
div[data-testid="stChatMessage"] td,
div[data-testid="stChatMessage"] th,
div[data-testid="stChatMessage"] strong,
div[data-testid="stChatMessage"] span {{
    color: rgba(255,255,255,0.92) !important;
}}

/* Chat input styling */
div[data-testid="stChatInput"] {{
    background: transparent !important;
}}

div[data-testid="stChatInput"] textarea {{
    background: rgba(255,255,255,0.12) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 14px !important;
    color: #fff !important;
    font-family: 'Inter', sans-serif !important;
}}

div[data-testid="stChatInput"] textarea::placeholder {{
    color: rgba(255,255,255,0.5) !important;
}}

/* Spinner */
div[data-testid="stSpinner"] p {{ color: rgba(255,255,255,0.7) !important; }}

/* Sidebar internals */
.sidebar-logo {{ text-align: center; padding: 0.5rem 0; }}
.sidebar-logo h2 {{ color: #1a5632; margin: 0.25rem 0 0 0; font-size: 1.2rem; font-weight: 700; }}
.sidebar-section {{ background: #f8f9fa; border-radius: 10px; padding: 1rem; margin-bottom: 0.75rem; }}
.sidebar-section h4 {{ margin-top: 0; color: #1a5632; font-size: 0.9rem; }}
.sidebar-disclaimer {{ text-align: center; padding-top: 0.75rem; }}
.sidebar-disclaimer p {{ font-size: 0.73rem; color: #999; line-height: 1.4; }}
</style>
"""


TITLE_HTML = """
<div style="text-align: center; margin-bottom: 2rem;">
    <h1 style="
        font-family: 'Inter', sans-serif;
        font-size: 3.2rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0 0 0.5rem 0;
        line-height: 1.1;
        text-shadow: 0 3px 20px rgba(0,0,0,0.5);
    ">African Housing Analyst</h1>
    <p style="
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: rgba(255,255,255,0.75);
        margin: 0;
        text-shadow: 0 1px 8px rgba(0,0,0,0.4);
    ">Ask me anything about housing in Africa</p>
</div>
"""
