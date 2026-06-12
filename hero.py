def get_hero_html() -> str:
    return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', sans-serif; background: transparent; }

.hero {
    background: linear-gradient(135deg, #0a1f0d 0%, #122a15 30%, #1a3a1e 60%, #0d2410 100%);
    border-radius: 20px;
    overflow: hidden;
    position: relative;
}

.hero-bg {
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(circle at 30% 40%, rgba(46,125,50,0.1) 0%, transparent 50%),
        radial-gradient(circle at 70% 60%, rgba(255,143,0,0.06) 0%, transparent 40%);
    animation: bgPulse 6s ease-in-out infinite alternate;
}
@keyframes bgPulse { 0% { opacity: 0.6; } 100% { opacity: 1; } }

.hero-top {
    position: relative;
    z-index: 1;
    text-align: center;
    padding: 2.5rem 2rem 1rem 2rem;
}
.hero-title {
    font-size: 2.4rem;
    font-weight: 800;
    background: linear-gradient(135deg, #fff 0%, #a5d6a7 50%, #ffcc80 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.15;
    margin-bottom: 0.5rem;
}
.hero-sub {
    font-size: 1.05rem;
    color: #a5d6a7;
    margin-bottom: 0.5rem;
}
.hero-desc {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.5);
    max-width: 600px;
    margin: 0 auto 1rem auto;
    line-height: 1.6;
}
.badges { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; }
.badge {
    background: rgba(46,125,50,0.25);
    color: #a5d6a7;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 500;
    border: 1px solid rgba(46,125,50,0.3);
}

.map-section {
    position: relative;
    z-index: 1;
    display: flex;
    justify-content: center;
    padding: 0.5rem 1rem;
}
.africa-map {
    width: 100%;
    max-width: 520px;
    height: auto;
}

.continent {
    animation: fadeIn 1.2s ease-out forwards;
    opacity: 0;
}
@keyframes fadeIn { to { opacity: 1; } }

.city-group {
    opacity: 0;
    animation: pop 0.5s ease-out forwards;
}
.city-1  { animation-delay: 0.6s; }
.city-2  { animation-delay: 0.9s; }
.city-3  { animation-delay: 1.2s; }
.city-4  { animation-delay: 1.5s; }
.city-5  { animation-delay: 1.8s; }
.city-6  { animation-delay: 2.1s; }
.city-7  { animation-delay: 2.4s; }
.city-8  { animation-delay: 2.7s; }
.city-9  { animation-delay: 3.0s; }
.city-10 { animation-delay: 3.3s; }
.city-11 { animation-delay: 3.6s; }
.city-12 { animation-delay: 3.9s; }
.city-13 { animation-delay: 4.2s; }
.city-14 { animation-delay: 4.5s; }

@keyframes pop {
    0%   { opacity: 0; transform: scale(0); }
    70%  { transform: scale(1.2); }
    100% { opacity: 1; transform: scale(1); }
}

.house {
    transform-origin: bottom center;
    opacity: 0;
    animation: grow 0.7s ease-out forwards;
}
.city-1  .house { animation-delay: 0.8s; }
.city-2  .house { animation-delay: 1.1s; }
.city-3  .house { animation-delay: 1.4s; }
.city-4  .house { animation-delay: 1.7s; }
.city-5  .house { animation-delay: 2.0s; }
.city-6  .house { animation-delay: 2.3s; }
.city-7  .house { animation-delay: 2.6s; }
.city-8  .house { animation-delay: 2.9s; }
.city-9  .house { animation-delay: 3.2s; }
.city-10 .house { animation-delay: 3.5s; }
.city-11 .house { animation-delay: 3.8s; }
.city-12 .house { animation-delay: 4.1s; }
.city-13 .house { animation-delay: 4.4s; }
.city-14 .house { animation-delay: 4.7s; }

@keyframes grow {
    0%   { opacity: 0; transform: scaleY(0); }
    60%  { transform: scaleY(1.15); }
    100% { opacity: 1; transform: scaleY(1); }
}

.pulse-ring {
    animation: pulse 3s ease-in-out infinite;
    transform-origin: center;
}
@keyframes pulse {
    0%, 100% { opacity: 0.05; }
    50%      { opacity: 0.2; }
}

.city-dot { animation: glow 2s ease-in-out infinite alternate; }
@keyframes glow { 0% { opacity: 0.4; } 100% { opacity: 0.9; } }

.city-label {
    fill: rgba(255,255,255,0.8);
    font-size: 11px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
}

.conn line {
    stroke-dasharray: 4 4;
    stroke-dashoffset: 100;
    animation: draw 2s ease-out forwards;
}
@keyframes draw { to { stroke-dashoffset: 0; } }

.stats {
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 1.1rem 1.5rem;
    background: rgba(0,0,0,0.3);
    border-top: 1px solid rgba(46,125,50,0.15);
}
.stat { text-align: center; }
.stat-num { font-size: 1.4rem; font-weight: 700; color: #fff; }
.stat-label { font-size: 0.7rem; color: rgba(255,255,255,0.45); margin-top: 0.15rem; }
.stat-div { width: 1px; height: 30px; background: rgba(255,255,255,0.1); }
</style>
</head>
<body>
<div class="hero">
  <div class="hero-bg"></div>

  <div class="hero-top">
    <h1 class="hero-title">African Housing Analyst</h1>
    <p class="hero-sub">AI-powered insights on housing markets, policy &amp; investment across Africa</p>
    <p class="hero-desc">Explore housing affordability, mortgage markets, construction costs, urban development and investment opportunities across 54 countries.</p>
    <div class="badges">
      <span class="badge">54 Countries</span>
      <span class="badge">Live World Bank Data</span>
      <span class="badge">CAHF Research</span>
      <span class="badge">Policy Best Practices</span>
    </div>
  </div>

  <div class="map-section">
    <svg viewBox="0 0 500 520" class="africa-map" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="aGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#2e7d32" stop-opacity="0.18"/>
          <stop offset="100%" stop-color="#1b5e20" stop-opacity="0.08"/>
        </linearGradient>
        <filter id="sh"><feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-color="#000" flood-opacity="0.25"/></filter>
      </defs>

      <path class="continent" d="
        M 220,30 C 200,28 180,32 165,38 C 155,42 148,50 140,55
        C 132,60 125,58 118,62 C 108,68 105,78 100,88
        C 95,98 88,105 85,115 C 82,125 80,135 78,145
        C 76,155 72,165 70,175 C 68,185 65,192 63,200
        C 60,210 58,218 57,228 C 56,238 55,248 56,258
        C 57,268 60,278 62,288 C 64,298 68,305 72,312
        C 76,320 80,328 85,335 C 90,342 96,348 100,355
        C 104,362 106,370 110,378 C 114,386 118,392 122,398
        C 126,404 130,410 135,415 C 140,420 148,424 155,430
        C 160,435 162,442 168,448 C 174,454 180,458 185,465
        C 190,472 195,478 202,482 C 208,486 215,488 222,492
        C 228,496 232,502 238,505 C 244,508 252,510 258,512
        C 265,514 272,512 278,510 C 285,508 290,504 295,500
        C 300,496 305,490 310,485 C 316,478 322,472 325,465
        C 328,458 330,450 332,442 C 334,434 338,428 340,420
        C 342,412 340,404 338,396 C 336,388 332,380 330,372
        C 328,365 325,358 325,350 C 325,342 328,334 330,326
        C 332,318 335,310 338,302 C 340,294 342,286 345,278
        C 348,270 352,262 355,255 C 358,248 362,240 365,232
        C 368,224 370,216 372,208 C 374,200 375,192 376,184
        C 377,176 378,168 378,160 C 378,152 376,144 375,136
        C 374,128 372,120 368,112 C 365,105 360,98 356,92
        C 352,86 346,80 342,75 C 338,70 332,66 326,62
        C 318,57 310,55 302,52 C 294,49 286,48 278,46
        C 270,44 262,42 255,40 C 248,38 240,35 232,32 Z
      " fill="url(#aGrad)" stroke="#4caf50" stroke-width="1.5" stroke-opacity="0.3"/>

      <g class="conn" stroke="#4caf50" stroke-opacity="0.15" stroke-width="0.7">
        <line x1="310" y1="82" x2="155" y2="168"/>
        <line x1="155" y1="168" x2="130" y2="155"/>
        <line x1="310" y1="82" x2="325" y2="195"/>
        <line x1="325" y1="195" x2="335" y2="265"/>
        <line x1="335" y1="265" x2="325" y2="320"/>
        <line x1="325" y1="320" x2="280" y2="460"/>
        <line x1="155" y1="168" x2="200" y2="200"/>
        <line x1="200" y1="200" x2="260" y2="280"/>
        <line x1="130" y1="155" x2="100" y2="120"/>
      </g>

      <g class="city-group city-1" transform="translate(310,82)">
        <circle r="18" fill="#4caf50" class="pulse-ring"/>
        <circle r="5" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-10" y="-28" width="20" height="17" rx="2" fill="#ff8f00"/>
          <polygon points="-13,-28 0,-38 13,-28" fill="#e65100"/>
          <rect x="-4" y="-20" width="8" height="7" rx="1" fill="#ffe082"/>
        </g>
        <text x="16" y="-22" class="city-label">Cairo</text>
      </g>

      <g class="city-group city-2" transform="translate(148,68)">
        <circle r="14" fill="#4caf50" class="pulse-ring"/>
        <circle r="4" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-8" y="-24" width="16" height="14" rx="2" fill="#1565c0"/>
          <polygon points="-10,-24 0,-33 10,-24" fill="#0d47a1"/>
          <rect x="-3" y="-18" width="6" height="5" rx="1" fill="#bbdefb"/>
        </g>
        <text x="12" y="-18" class="city-label">Casablanca</text>
      </g>

      <g class="city-group city-3" transform="translate(100,120)">
        <circle r="14" fill="#4caf50" class="pulse-ring"/>
        <circle r="4" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-8" y="-24" width="16" height="14" rx="2" fill="#7b1fa2"/>
          <polygon points="-10,-24 0,-33 10,-24" fill="#4a148c"/>
          <rect x="-3" y="-18" width="6" height="5" rx="1" fill="#e1bee7"/>
        </g>
        <text x="-38" y="-18" class="city-label">Dakar</text>
      </g>

      <g class="city-group city-4" transform="translate(128,152)">
        <circle r="14" fill="#4caf50" class="pulse-ring"/>
        <circle r="4" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-8" y="-24" width="16" height="14" rx="2" fill="#00838f"/>
          <polygon points="-10,-24 0,-33 10,-24" fill="#006064"/>
          <rect x="-3" y="-18" width="6" height="5" rx="1" fill="#b2ebf2"/>
        </g>
        <text x="-36" y="-18" class="city-label">Accra</text>
      </g>

      <g class="city-group city-5" transform="translate(158,170)">
        <circle r="18" fill="#4caf50" class="pulse-ring"/>
        <circle r="5" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-10" y="-28" width="20" height="17" rx="2" fill="#2e7d32"/>
          <polygon points="-13,-28 0,-38 13,-28" fill="#1b5e20"/>
          <rect x="-4" y="-20" width="8" height="7" rx="1" fill="#a5d6a7"/>
        </g>
        <text x="14" y="-22" class="city-label">Lagos</text>
      </g>

      <g class="city-group city-6" transform="translate(202,205)">
        <circle r="12" fill="#4caf50" class="pulse-ring"/>
        <circle r="3.5" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-7" y="-22" width="14" height="12" rx="2" fill="#ef6c00"/>
          <polygon points="-9,-22 0,-30 9,-22" fill="#e65100"/>
          <rect x="-3" y="-17" width="6" height="4" rx="1" fill="#ffe0b2"/>
        </g>
        <text x="12" y="-14" class="city-label">Yaound&#233;</text>
      </g>

      <g class="city-group city-7" transform="translate(328,198)">
        <circle r="16" fill="#4caf50" class="pulse-ring"/>
        <circle r="4.5" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-9" y="-26" width="18" height="15" rx="2" fill="#c62828"/>
          <polygon points="-11,-26 0,-36 11,-26" fill="#b71c1c"/>
          <rect x="-3.5" y="-20" width="7" height="6" rx="1" fill="#ffcdd2"/>
        </g>
        <text x="14" y="-18" class="city-label">Addis Ababa</text>
      </g>

      <g class="city-group city-8" transform="translate(262,282)">
        <circle r="12" fill="#4caf50" class="pulse-ring"/>
        <circle r="3.5" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-7" y="-22" width="14" height="12" rx="2" fill="#1565c0"/>
          <polygon points="-9,-22 0,-30 9,-22" fill="#0d47a1"/>
          <rect x="-3" y="-17" width="6" height="4" rx="1" fill="#bbdefb"/>
        </g>
        <text x="12" y="-14" class="city-label">Kigali</text>
      </g>

      <g class="city-group city-9" transform="translate(338,268)">
        <circle r="18" fill="#4caf50" class="pulse-ring"/>
        <circle r="5" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-10" y="-28" width="20" height="17" rx="2" fill="#d84315"/>
          <polygon points="-13,-28 0,-38 13,-28" fill="#bf360c"/>
          <rect x="-4" y="-20" width="8" height="7" rx="1" fill="#ffccbc"/>
        </g>
        <text x="14" y="-22" class="city-label">Nairobi</text>
      </g>

      <g class="city-group city-10" transform="translate(328,322)">
        <circle r="14" fill="#4caf50" class="pulse-ring"/>
        <circle r="4" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-8" y="-24" width="16" height="14" rx="2" fill="#00695c"/>
          <polygon points="-10,-24 0,-33 10,-24" fill="#004d40"/>
          <rect x="-3" y="-18" width="6" height="5" rx="1" fill="#b2dfdb"/>
        </g>
        <text x="12" y="-16" class="city-label">Dar es Salaam</text>
      </g>

      <g class="city-group city-11" transform="translate(178,312)">
        <circle r="12" fill="#4caf50" class="pulse-ring"/>
        <circle r="3.5" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-7" y="-22" width="14" height="12" rx="2" fill="#f9a825"/>
          <polygon points="-9,-22 0,-30 9,-22" fill="#f57f17"/>
          <rect x="-3" y="-17" width="6" height="4" rx="1" fill="#fff9c4"/>
        </g>
        <text x="-42" y="-14" class="city-label">Luanda</text>
      </g>

      <g class="city-group city-12" transform="translate(272,382)">
        <circle r="12" fill="#4caf50" class="pulse-ring"/>
        <circle r="3.5" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-7" y="-22" width="14" height="12" rx="2" fill="#558b2f"/>
          <polygon points="-9,-22 0,-30 9,-22" fill="#33691e"/>
          <rect x="-3" y="-17" width="6" height="4" rx="1" fill="#dcedc8"/>
        </g>
        <text x="12" y="-14" class="city-label">Lusaka</text>
      </g>

      <g class="city-group city-13" transform="translate(282,462)">
        <circle r="20" fill="#4caf50" class="pulse-ring"/>
        <circle r="5.5" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-11" y="-30" width="22" height="18" rx="2" fill="#1a237e"/>
          <polygon points="-14,-30 0,-42 14,-30" fill="#0d1642"/>
          <rect x="-4.5" y="-24" width="9" height="8" rx="1" fill="#c5cae9"/>
        </g>
        <text x="16" y="-24" class="city-label">Johannesburg</text>
      </g>

      <g class="city-group city-14" transform="translate(312,472)">
        <circle r="10" fill="#4caf50" class="pulse-ring"/>
        <circle r="3" fill="#4caf50" class="city-dot"/>
        <g class="house" filter="url(#sh)">
          <rect x="-7" y="-22" width="14" height="12" rx="2" fill="#ad1457"/>
          <polygon points="-9,-22 0,-30 9,-22" fill="#880e4f"/>
          <rect x="-3" y="-17" width="6" height="4" rx="1" fill="#f8bbd0"/>
        </g>
        <text x="10" y="-14" class="city-label">Maputo</text>
      </g>

    </svg>
  </div>

  <div class="stats">
    <div class="stat">
      <div class="stat-num">~160M</div>
      <div class="stat-label">Unit housing deficit</div>
    </div>
    <div class="stat-div"></div>
    <div class="stat">
      <div class="stat-num">~600M</div>
      <div class="stat-label">New urban residents by 2050</div>
    </div>
    <div class="stat-div"></div>
    <div class="stat">
      <div class="stat-num">&lt;20%</div>
      <div class="stat-label">Can afford cheapest new house</div>
    </div>
    <div class="stat-div"></div>
    <div class="stat">
      <div class="stat-num">54</div>
      <div class="stat-label">Countries covered</div>
    </div>
  </div>
</div>
</body>
</html>"""


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
