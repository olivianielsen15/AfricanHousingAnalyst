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
        bg_style = f"background: url('data:image/{ext};base64,{b64}') center/cover no-repeat;"
    else:
        bg_style = "background: linear-gradient(135deg, #0a1f0d, #122a15, #1a3a1e);"

    return f"""
<div style="
    {bg_style}
    border-radius: 20px;
    overflow: hidden;
    position: relative;
    min-height: 85vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
">
    <!-- Dark overlay -->
    <div style="
        position: absolute; inset: 0;
        background: radial-gradient(
            ellipse at center,
            rgba(0,0,0,0.45) 0%,
            rgba(0,0,0,0.35) 40%,
            rgba(0,0,0,0.5) 100%
        );
    "></div>

    <!-- Content centered -->
    <div style="
        position: relative; z-index: 1;
        text-align: center;
        max-width: 680px;
        padding: 2rem;
    ">
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: #a5d6a7;
            margin: 0 0 0.75rem 0;
            text-shadow: 0 1px 6px rgba(0,0,0,0.6);
        ">Housing Intelligence for Africa</p>

        <h1 style="
            font-family: 'Inter', sans-serif;
            font-size: 3rem;
            font-weight: 800;
            color: #ffffff;
            margin: 0 0 0.75rem 0;
            line-height: 1.1;
            text-shadow: 0 3px 15px rgba(0,0,0,0.5);
        ">African Housing<br>Analyst</h1>

        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 1.05rem;
            color: rgba(255,255,255,0.8);
            margin: 0 0 2rem 0;
            line-height: 1.6;
            text-shadow: 0 1px 8px rgba(0,0,0,0.5);
        ">Data-driven insights on housing markets, policy, finance &amp; investment across 54 African countries</p>

        <!-- Prompt box -->
        <div style="
            background: rgba(255,255,255,0.12);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 14px;
            padding: 1.25rem 1.5rem;
            text-align: left;
        ">
            <p style="
                font-family: 'Inter', sans-serif;
                font-size: 0.95rem;
                color: rgba(255,255,255,0.95);
                margin: 0 0 1rem 0;
                font-weight: 500;
            ">Try asking:</p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
                <span style="background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.85); padding: 0.35rem 0.75rem; border-radius: 10px; font-size: 0.78rem; font-family: 'Inter', sans-serif; border: 1px solid rgba(255,255,255,0.12);">What are the risks of a housing PPP in Nigeria?</span>
                <span style="background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.85); padding: 0.35rem 0.75rem; border-radius: 10px; font-size: 0.78rem; font-family: 'Inter', sans-serif; border: 1px solid rgba(255,255,255,0.12);">Feasibility analysis for 500 units in Kenya</span>
                <span style="background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.85); padding: 0.35rem 0.75rem; border-radius: 10px; font-size: 0.78rem; font-family: 'Inter', sans-serif; border: 1px solid rgba(255,255,255,0.12);">Compare mortgage markets in East Africa</span>
                <span style="background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.85); padding: 0.35rem 0.75rem; border-radius: 10px; font-size: 0.78rem; font-family: 'Inter', sans-serif; border: 1px solid rgba(255,255,255,0.12);">How does rent-to-own work?</span>
            </div>
        </div>
    </div>

    <!-- Bottom bar -->
    <div style="
        position: absolute; bottom: 0; left: 0; right: 0;
        display: flex; justify-content: center; gap: 2.5rem;
        padding: 1rem;
        background: rgba(0,0,0,0.3);
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
    ">
        <div style="text-align: center;">
            <div style="font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 700; color: #fff;">54</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 0.65rem; color: rgba(255,255,255,0.5);">Countries</div>
        </div>
        <div style="text-align: center;">
            <div style="font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 700; color: #fff;">~160M</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 0.65rem; color: rgba(255,255,255,0.5);">Housing deficit</div>
        </div>
        <div style="text-align: center;">
            <div style="font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 700; color: #fff;">&lt;20%</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 0.65rem; color: rgba(255,255,255,0.5);">Affordability</div>
        </div>
        <div style="text-align: center;">
            <div style="font-family: 'Inter', sans-serif; font-size: 1.1rem; font-weight: 700; color: #fff;">Live</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 0.65rem; color: rgba(255,255,255,0.5);">World Bank data</div>
        </div>
    </div>
</div>
"""


PAGE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.block-container { padding-top: 1rem !important; }

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
