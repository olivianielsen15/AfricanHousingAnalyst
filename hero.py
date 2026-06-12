import os


def get_hero_image_path() -> str:
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    if not os.path.isdir(assets_dir):
        return ""
    for fname in os.listdir(assets_dir):
        if fname.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            return os.path.join(assets_dir, fname)
    return ""


PAGE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.block-container { padding-top: 1rem !important; }

.hero-title {
    font-size: 2.2rem;
    font-weight: 800;
    color: #1a5632;
    text-align: center;
    margin: 1.25rem 0 0.25rem 0;
    line-height: 1.15;
}
.hero-sub {
    font-size: 1rem;
    color: #666;
    text-align: center;
    margin: 0 0 1.5rem 0;
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
