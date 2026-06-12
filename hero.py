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


def get_hero_html() -> str:
    b64, ext = get_hero_image_base64()
    if b64:
        img_tag = f'<img src="data:image/{ext};base64,{b64}" style="width:100%; border-radius: 18px; display: block;" />'
    else:
        img_tag = '<div style="height: 300px; background: linear-gradient(135deg, #0a1f0d, #1a3a1e); border-radius: 18px;"></div>'

    return f"""
<div style="position: relative; margin-bottom: 1.5rem;">
    {img_tag}
    <div style="
        position: absolute; bottom: 0; left: 0; right: 0;
        padding: 2.5rem 2.5rem 1.5rem 2.5rem;
        background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.5) 60%, transparent 100%);
        border-radius: 0 0 18px 18px;
    ">
        <h1 style="
            font-family: 'Inter', sans-serif;
            font-size: 2.4rem; font-weight: 800;
            color: #ffffff; margin: 0 0 0.3rem 0;
            line-height: 1.15;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        ">African Housing Analyst</h1>
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 1rem; color: rgba(255,255,255,0.8);
            margin: 0;
            text-shadow: 0 1px 6px rgba(0,0,0,0.5);
        ">AI-powered insights on housing markets, policy &amp; investment across Africa</p>
    </div>
</div>
"""


PAGE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.chat-header {
    font-size: 1.6rem; font-weight: 700; color: #1a5632;
    margin-bottom: 0.5rem; padding-bottom: 0.75rem;
    border-bottom: 2px solid #e8f5e9;
}

.sidebar-logo { text-align: center; padding: 0.5rem 0; }
.sidebar-logo h2 { color: #1a5632; margin: 0.25rem 0 0 0; font-size: 1.2rem; font-weight: 700; }
.sidebar-section { background: #f8f9fa; border-radius: 10px; padding: 1rem; margin-bottom: 0.75rem; }
.sidebar-section h4 { margin-top: 0; color: #1a5632; font-size: 0.9rem; }
.sidebar-disclaimer { text-align: center; padding-top: 0.75rem; }
.sidebar-disclaimer p { font-size: 0.73rem; color: #999; line-height: 1.4; }

div[data-testid="stChatMessage"] { border-radius: 12px; }
</style>
"""
