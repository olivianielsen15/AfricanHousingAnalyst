import base64
import os

def get_hero_image_base64() -> str:
    img_path = os.path.join(os.path.dirname(__file__), "assets", "hero.jpg")
    if not os.path.exists(img_path):
        return ""
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def get_hero_html() -> str:
    b64 = get_hero_image_base64()
    if not b64:
        bg_style = "background: linear-gradient(135deg, #0a1f0d, #1a3a1e);"
    else:
        bg_style = f"background: url('data:image/jpeg;base64,{b64}') center/cover no-repeat;"

    return f"""
<div style="
    {bg_style}
    border-radius: 18px;
    overflow: hidden;
    position: relative;
    min-height: 420px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
">
    <div style="
        position: absolute; inset: 0;
        background: linear-gradient(
            to bottom,
            rgba(0,0,0,0.1) 0%,
            rgba(0,0,0,0.2) 40%,
            rgba(0,0,0,0.7) 75%,
            rgba(0,0,0,0.85) 100%
        );
        border-radius: 18px;
    "></div>
    <div style="
        position: relative; z-index: 1;
        padding: 2rem 2.5rem 1.5rem 2.5rem;
    ">
        <h1 style="
            font-family: 'Inter', sans-serif;
            font-size: 2.4rem; font-weight: 800;
            color: #ffffff;
            margin: 0 0 0.4rem 0;
            line-height: 1.15;
            text-shadow: 0 2px 8px rgba(0,0,0,0.4);
        ">African Housing Analyst</h1>
        <p style="
            font-family: 'Inter', sans-serif;
            font-size: 1.05rem; color: #c8e6c9;
            margin: 0 0 1rem 0;
            text-shadow: 0 1px 4px rgba(0,0,0,0.5);
        ">AI-powered insights on housing markets, policy &amp; investment across Africa</p>
        <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
            <span style="background: rgba(46,125,50,0.35); color: #a5d6a7; padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.75rem; font-weight: 500; font-family: 'Inter', sans-serif; border: 1px solid rgba(46,125,50,0.4);">54 Countries</span>
            <span style="background: rgba(46,125,50,0.35); color: #a5d6a7; padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.75rem; font-weight: 500; font-family: 'Inter', sans-serif; border: 1px solid rgba(46,125,50,0.4);">Live World Bank Data</span>
            <span style="background: rgba(46,125,50,0.35); color: #a5d6a7; padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.75rem; font-weight: 500; font-family: 'Inter', sans-serif; border: 1px solid rgba(46,125,50,0.4);">CAHF Research</span>
            <span style="background: rgba(46,125,50,0.35); color: #a5d6a7; padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.75rem; font-weight: 500; font-family: 'Inter', sans-serif; border: 1px solid rgba(46,125,50,0.4);">Policy Best Practices</span>
        </div>
    </div>
    <div style="
        position: relative; z-index: 1;
        display: flex; justify-content: space-around; align-items: center;
        padding: 1rem 1.5rem;
        background: rgba(0,0,0,0.4);
        backdrop-filter: blur(8px);
        border-top: 1px solid rgba(255,255,255,0.08);
    ">
        <div style="text-align: center;">
            <div style="font-family: 'Inter', sans-serif; font-size: 1.3rem; font-weight: 700; color: #fff;">~160M</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 0.68rem; color: rgba(255,255,255,0.5);">Unit housing deficit</div>
        </div>
        <div style="width: 1px; height: 28px; background: rgba(255,255,255,0.12);"></div>
        <div style="text-align: center;">
            <div style="font-family: 'Inter', sans-serif; font-size: 1.3rem; font-weight: 700; color: #fff;">~600M</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 0.68rem; color: rgba(255,255,255,0.5);">New urban residents by 2050</div>
        </div>
        <div style="width: 1px; height: 28px; background: rgba(255,255,255,0.12);"></div>
        <div style="text-align: center;">
            <div style="font-family: 'Inter', sans-serif; font-size: 1.3rem; font-weight: 700; color: #fff;">&lt;20%</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 0.68rem; color: rgba(255,255,255,0.5);">Can afford cheapest new house</div>
        </div>
        <div style="width: 1px; height: 28px; background: rgba(255,255,255,0.12);"></div>
        <div style="text-align: center;">
            <div style="font-family: 'Inter', sans-serif; font-size: 1.3rem; font-weight: 700; color: #fff;">54</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 0.68rem; color: rgba(255,255,255,0.5);">Countries covered</div>
        </div>
    </div>
</div>
"""


PAGE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.audience-card-v2 {
    background: #ffffff;
    border-radius: 14px;
    padding: 1.5rem;
    border: 1px solid #e8e8e8;
    height: 100%;
    transition: transform 0.2s, box-shadow 0.2s;
}
.audience-card-v2:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}
.audience-card-v2 .card-icon { font-size: 2rem; margin-bottom: 0.75rem; }
.audience-card-v2 h4 { color: #1a5632; margin: 0 0 0.5rem 0; font-size: 1.05rem; font-weight: 600; }
.audience-card-v2 p { color: #666; font-size: 0.88rem; margin: 0; line-height: 1.55; }

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
