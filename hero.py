HERO_HTML = """
<div class="hero-container">
  <div class="hero-bg-pattern"></div>
  <div class="hero-content">
    <div class="hero-left">
      <h1 class="hero-title-text">African Housing<br>Analyst</h1>
      <p class="hero-tagline">AI-powered insights on housing markets, policy, and investment across Africa</p>
      <p class="hero-desc-text">
        Explore housing affordability, mortgage markets, construction costs,
        urban development, and investment opportunities across 54 countries.
        Backed by CAHF research and live World Bank data.
      </p>
      <div class="hero-badges">
        <span class="badge-item">54 Countries</span>
        <span class="badge-item">Live World Bank Data</span>
        <span class="badge-item">CAHF Research</span>
        <span class="badge-item">Policy Best Practices</span>
      </div>
    </div>
    <div class="hero-right">
      <svg viewBox="0 0 500 550" class="africa-map" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="africaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2e7d32;stop-opacity:0.15"/>
            <stop offset="100%" style="stop-color:#1b5e20;stop-opacity:0.08"/>
          </linearGradient>
          <linearGradient id="glowGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#4caf50;stop-opacity:0.6"/>
            <stop offset="100%" style="stop-color:#2e7d32;stop-opacity:0.3"/>
          </linearGradient>
          <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="blur"/>
            <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
          </filter>
          <filter id="shadow">
            <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.15"/>
          </filter>
        </defs>

        <!-- Africa continent outline -->
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
          C 270,44 262,42 255,40 C 248,38 240,35 232,32
          Z
        " fill="url(#africaGrad)" stroke="#2e7d32" stroke-width="1.5" stroke-opacity="0.4"/>

        <!-- Subtle grid lines on continent -->
        <line x1="100" y1="200" x2="370" y2="200" stroke="#2e7d32" stroke-opacity="0.06" stroke-width="0.5"/>
        <line x1="90" y1="300" x2="345" y2="300" stroke="#2e7d32" stroke-opacity="0.06" stroke-width="0.5"/>
        <line x1="130" y1="400" x2="330" y2="400" stroke="#2e7d32" stroke-opacity="0.06" stroke-width="0.5"/>
        <line x1="200" y1="30" x2="200" y2="510" stroke="#2e7d32" stroke-opacity="0.06" stroke-width="0.5"/>
        <line x1="300" y1="50" x2="300" y2="500" stroke="#2e7d32" stroke-opacity="0.06" stroke-width="0.5"/>

        <!-- Connection lines between cities -->
        <g class="connections" stroke="#4caf50" stroke-opacity="0.12" stroke-width="0.8" stroke-dasharray="4,4">
          <line x1="310" y1="82" x2="155" y2="168"/>   <!-- Cairo-Lagos -->
          <line x1="155" y1="168" x2="130" y2="155"/>   <!-- Lagos-Accra -->
          <line x1="310" y1="82" x2="325" y2="195"/>    <!-- Cairo-Addis -->
          <line x1="325" y1="195" x2="335" y2="265"/>   <!-- Addis-Nairobi -->
          <line x1="335" y1="265" x2="325" y2="320"/>   <!-- Nairobi-Dar -->
          <line x1="325" y1="320" x2="280" y2="460"/>   <!-- Dar-Joburg -->
          <line x1="155" y1="168" x2="200" y2="200"/>   <!-- Lagos-Yaounde -->
          <line x1="200" y1="200" x2="260" y2="280"/>   <!-- Yaounde-Kigali -->
          <line x1="130" y1="155" x2="100" y2="120"/>   <!-- Accra-Dakar -->
        </g>

        <!-- CAIRO -->
        <g class="city-group city-1" transform="translate(310,82)">
          <circle r="20" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="4" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-8" y="-22" width="16" height="14" rx="1" fill="#ff8f00" class="house-body"/>
            <polygon points="-10,-22 0,-30 10,-22" fill="#e65100" class="house-roof"/>
            <rect x="-3" y="-16" width="6" height="6" rx="0.5" fill="#ffe082"/>
            <rect x="-2" y="-12" width="4" height="4" fill="#fff8e1"/>
          </g>
          <text x="15" y="-18" class="city-label">Cairo</text>
        </g>

        <!-- CASABLANCA -->
        <g class="city-group city-2" transform="translate(148,68)">
          <circle r="16" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="3" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-6" y="-19" width="12" height="11" rx="1" fill="#1565c0" class="house-body"/>
            <polygon points="-8,-19 0,-26 8,-19" fill="#0d47a1" class="house-roof"/>
            <rect x="-2" y="-15" width="4" height="4" rx="0.5" fill="#bbdefb"/>
          </g>
          <text x="10" y="-14" class="city-label">Casablanca</text>
        </g>

        <!-- DAKAR -->
        <g class="city-group city-3" transform="translate(100,120)">
          <circle r="16" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="3" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-6" y="-19" width="12" height="11" rx="1" fill="#6a1b9a" class="house-body"/>
            <polygon points="-8,-19 0,-26 8,-19" fill="#4a148c" class="house-roof"/>
            <rect x="-2" y="-15" width="4" height="4" rx="0.5" fill="#e1bee7"/>
          </g>
          <text x="-35" y="-14" class="city-label">Dakar</text>
        </g>

        <!-- ACCRA -->
        <g class="city-group city-4" transform="translate(130,155)">
          <circle r="16" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="3" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-6" y="-19" width="12" height="11" rx="1" fill="#00838f" class="house-body"/>
            <polygon points="-8,-19 0,-26 8,-19" fill="#006064" class="house-roof"/>
            <rect x="-2" y="-15" width="4" height="4" rx="0.5" fill="#b2ebf2"/>
          </g>
          <text x="-30" y="-14" class="city-label">Accra</text>
        </g>

        <!-- LAGOS -->
        <g class="city-group city-5" transform="translate(155,168)">
          <circle r="20" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="4" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-8" y="-22" width="16" height="14" rx="1" fill="#2e7d32" class="house-body"/>
            <polygon points="-10,-22 0,-30 10,-22" fill="#1b5e20" class="house-roof"/>
            <rect x="-3" y="-16" width="6" height="6" rx="0.5" fill="#a5d6a7"/>
            <rect x="-2" y="-12" width="4" height="4" fill="#e8f5e9"/>
          </g>
          <text x="12" y="-18" class="city-label">Lagos</text>
        </g>

        <!-- YAOUNDE -->
        <g class="city-group city-6" transform="translate(200,200)">
          <circle r="14" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="3" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-5" y="-17" width="10" height="9" rx="1" fill="#ef6c00" class="house-body"/>
            <polygon points="-7,-17 0,-23 7,-17" fill="#e65100" class="house-roof"/>
            <rect x="-2" y="-14" width="4" height="3" rx="0.5" fill="#ffe0b2"/>
          </g>
          <text x="10" y="-10" class="city-label">Yaoundé</text>
        </g>

        <!-- ADDIS ABABA -->
        <g class="city-group city-7" transform="translate(325,195)">
          <circle r="18" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="3.5" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-7" y="-20" width="14" height="12" rx="1" fill="#c62828" class="house-body"/>
            <polygon points="-9,-20 0,-28 9,-20" fill="#b71c1c" class="house-roof"/>
            <rect x="-2.5" y="-16" width="5" height="5" rx="0.5" fill="#ffcdd2"/>
          </g>
          <text x="12" y="-14" class="city-label">Addis Ababa</text>
        </g>

        <!-- KIGALI -->
        <g class="city-group city-8" transform="translate(260,280)">
          <circle r="14" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="3" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-5" y="-17" width="10" height="9" rx="1" fill="#1565c0" class="house-body"/>
            <polygon points="-7,-17 0,-23 7,-17" fill="#0d47a1" class="house-roof"/>
            <rect x="-2" y="-14" width="4" height="3" rx="0.5" fill="#bbdefb"/>
          </g>
          <text x="10" y="-10" class="city-label">Kigali</text>
        </g>

        <!-- NAIROBI -->
        <g class="city-group city-9" transform="translate(335,265)">
          <circle r="20" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="4" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-8" y="-22" width="16" height="14" rx="1" fill="#d84315" class="house-body"/>
            <polygon points="-10,-22 0,-30 10,-22" fill="#bf360c" class="house-roof"/>
            <rect x="-3" y="-16" width="6" height="6" rx="0.5" fill="#ffccbc"/>
            <rect x="-2" y="-12" width="4" height="4" fill="#fbe9e7"/>
          </g>
          <text x="14" y="-18" class="city-label">Nairobi</text>
        </g>

        <!-- DAR ES SALAAM -->
        <g class="city-group city-10" transform="translate(325,320)">
          <circle r="16" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="3" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-6" y="-19" width="12" height="11" rx="1" fill="#00695c" class="house-body"/>
            <polygon points="-8,-19 0,-26 8,-19" fill="#004d40" class="house-roof"/>
            <rect x="-2" y="-15" width="4" height="4" rx="0.5" fill="#b2dfdb"/>
          </g>
          <text x="10" y="-12" class="city-label">Dar es Salaam</text>
        </g>

        <!-- LUANDA -->
        <g class="city-group city-11" transform="translate(175,310)">
          <circle r="14" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="3" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-5" y="-17" width="10" height="9" rx="1" fill="#f9a825" class="house-body"/>
            <polygon points="-7,-17 0,-23 7,-17" fill="#f57f17" class="house-roof"/>
            <rect x="-2" y="-14" width="4" height="3" rx="0.5" fill="#fff9c4"/>
          </g>
          <text x="-38" y="-10" class="city-label">Luanda</text>
        </g>

        <!-- LUSAKA -->
        <g class="city-group city-12" transform="translate(270,380)">
          <circle r="14" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="3" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-5" y="-17" width="10" height="9" rx="1" fill="#558b2f" class="house-body"/>
            <polygon points="-7,-17 0,-23 7,-17" fill="#33691e" class="house-roof"/>
            <rect x="-2" y="-14" width="4" height="3" rx="0.5" fill="#dcedc8"/>
          </g>
          <text x="10" y="-10" class="city-label">Lusaka</text>
        </g>

        <!-- JOHANNESBURG -->
        <g class="city-group city-13" transform="translate(280,460)">
          <circle r="22" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="4.5" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-9" y="-24" width="18" height="15" rx="1" fill="#1a237e" class="house-body"/>
            <polygon points="-11,-24 0,-33 11,-24" fill="#0d1642" class="house-roof"/>
            <rect x="-3.5" y="-18" width="7" height="7" rx="0.5" fill="#c5cae9"/>
            <rect x="-2.5" y="-14" width="5" height="5" fill="#e8eaf6"/>
          </g>
          <text x="16" y="-20" class="city-label">Johannesburg</text>
        </g>

        <!-- MAPUTO -->
        <g class="city-group city-14" transform="translate(310,470)">
          <circle r="12" fill="#4caf50" opacity="0.08" class="pulse-ring"/>
          <circle r="2.5" fill="#4caf50" opacity="0.3" class="city-dot"/>
          <g class="house" filter="url(#shadow)">
            <rect x="-5" y="-17" width="10" height="9" rx="1" fill="#ad1457" class="house-body"/>
            <polygon points="-7,-17 0,-23 7,-17" fill="#880e4f" class="house-roof"/>
            <rect x="-2" y="-14" width="4" height="3" rx="0.5" fill="#f8bbd0"/>
          </g>
          <text x="8" y="-10" class="city-label">Maputo</text>
        </g>

      </svg>
    </div>
  </div>

  <!-- Animated stats bar -->
  <div class="stats-bar">
    <div class="stat-item">
      <div class="stat-number" id="stat1">~160M</div>
      <div class="stat-desc">Unit housing deficit</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
      <div class="stat-number" id="stat2">~600M</div>
      <div class="stat-desc">New urban residents by 2050</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
      <div class="stat-number" id="stat3">&lt;20%</div>
      <div class="stat-desc">Can afford cheapest new house</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
      <div class="stat-number" id="stat4">54</div>
      <div class="stat-desc">Countries covered</div>
    </div>
  </div>
</div>
"""

HERO_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Hero Container */
.hero-container {
    position: relative;
    background: linear-gradient(135deg, #0a1f0d 0%, #122a15 30%, #1a3a1e 60%, #0d2410 100%);
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 2rem;
    box-shadow: 0 20px 60px rgba(0,0,0,0.15), 0 0 40px rgba(46,125,50,0.1);
}

.hero-bg-pattern {
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(circle at 20% 50%, rgba(46,125,50,0.08) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255,143,0,0.05) 0%, transparent 40%),
        radial-gradient(circle at 60% 80%, rgba(46,125,50,0.06) 0%, transparent 40%);
    animation: bgShift 8s ease-in-out infinite alternate;
}
@keyframes bgShift {
    0%   { opacity: 0.7; }
    100% { opacity: 1; }
}

.hero-content {
    position: relative;
    display: flex;
    align-items: center;
    padding: 2.5rem 3rem;
    gap: 2rem;
    z-index: 1;
}
.hero-left {
    flex: 1.1;
    min-width: 0;
}
.hero-right {
    flex: 0.9;
    display: flex;
    justify-content: center;
    min-width: 0;
}

.hero-title-text {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 0%, #a5d6a7 50%, #ffcc80 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.15;
    margin: 0 0 0.75rem 0;
    letter-spacing: -0.02em;
}
.hero-tagline {
    font-size: 1.1rem;
    color: #a5d6a7;
    margin: 0 0 1rem 0;
    font-weight: 400;
    line-height: 1.5;
}
.hero-desc-text {
    font-size: 0.9rem;
    color: rgba(255,255,255,0.6);
    line-height: 1.7;
    margin: 0 0 1.25rem 0;
}
.hero-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.badge-item {
    display: inline-block;
    background: rgba(46,125,50,0.25);
    color: #a5d6a7;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 500;
    border: 1px solid rgba(46,125,50,0.3);
    backdrop-filter: blur(4px);
}

/* Africa Map */
.africa-map {
    width: 100%;
    max-width: 380px;
    height: auto;
    filter: drop-shadow(0 0 30px rgba(46,125,50,0.15));
}
.continent {
    animation: continentFadeIn 1.5s ease-out forwards;
    opacity: 0;
}
@keyframes continentFadeIn {
    0%   { opacity: 0; }
    100% { opacity: 1; }
}

/* City groups - staggered appear */
.city-group {
    opacity: 0;
    animation: cityAppear 0.6s ease-out forwards;
}
.city-1  { animation-delay: 0.8s; }
.city-2  { animation-delay: 1.1s; }
.city-3  { animation-delay: 1.4s; }
.city-4  { animation-delay: 1.7s; }
.city-5  { animation-delay: 2.0s; }
.city-6  { animation-delay: 2.3s; }
.city-7  { animation-delay: 2.6s; }
.city-8  { animation-delay: 2.9s; }
.city-9  { animation-delay: 3.2s; }
.city-10 { animation-delay: 3.5s; }
.city-11 { animation-delay: 3.8s; }
.city-12 { animation-delay: 4.1s; }
.city-13 { animation-delay: 4.4s; }
.city-14 { animation-delay: 4.7s; }

@keyframes cityAppear {
    0%   { opacity: 0; transform: translateY(10px) scale(0.5); }
    60%  { transform: translateY(-3px) scale(1.1); }
    100% { opacity: 1; transform: translateY(0) scale(1); }
}

/* House grow animation */
.house {
    transform-origin: bottom center;
    animation: houseGrow 0.8s ease-out forwards;
    transform: scaleY(0);
}
.city-1  .house { animation-delay: 1.0s; }
.city-2  .house { animation-delay: 1.3s; }
.city-3  .house { animation-delay: 1.6s; }
.city-4  .house { animation-delay: 1.9s; }
.city-5  .house { animation-delay: 2.2s; }
.city-6  .house { animation-delay: 2.5s; }
.city-7  .house { animation-delay: 2.8s; }
.city-8  .house { animation-delay: 3.1s; }
.city-9  .house { animation-delay: 3.4s; }
.city-10 .house { animation-delay: 3.7s; }
.city-11 .house { animation-delay: 4.0s; }
.city-12 .house { animation-delay: 4.3s; }
.city-13 .house { animation-delay: 4.6s; }
.city-14 .house { animation-delay: 4.9s; }

@keyframes houseGrow {
    0%   { transform: scaleY(0) scaleX(0.8); opacity: 0; }
    50%  { transform: scaleY(1.15) scaleX(1.05); }
    70%  { transform: scaleY(0.95) scaleX(0.98); }
    100% { transform: scaleY(1) scaleX(1); opacity: 1; }
}

/* Pulse rings on cities */
.pulse-ring {
    animation: pulse 3s ease-in-out infinite;
    transform-origin: center;
}
.city-1  .pulse-ring { animation-delay: 0s; }
.city-2  .pulse-ring { animation-delay: 0.4s; }
.city-3  .pulse-ring { animation-delay: 0.8s; }
.city-4  .pulse-ring { animation-delay: 1.2s; }
.city-5  .pulse-ring { animation-delay: 0.2s; }
.city-6  .pulse-ring { animation-delay: 1.6s; }
.city-7  .pulse-ring { animation-delay: 0.6s; }
.city-8  .pulse-ring { animation-delay: 1.0s; }
.city-9  .pulse-ring { animation-delay: 0.3s; }
.city-10 .pulse-ring { animation-delay: 1.4s; }
.city-11 .pulse-ring { animation-delay: 0.7s; }
.city-12 .pulse-ring { animation-delay: 1.1s; }
.city-13 .pulse-ring { animation-delay: 0.5s; }
.city-14 .pulse-ring { animation-delay: 1.3s; }

@keyframes pulse {
    0%, 100% { r: 12; opacity: 0.05; }
    50%      { r: 22; opacity: 0.12; }
}

/* City dots glow */
.city-dot {
    animation: dotGlow 2s ease-in-out infinite alternate;
}
@keyframes dotGlow {
    0%   { opacity: 0.3; }
    100% { opacity: 0.7; }
}

/* City labels */
.city-label {
    fill: rgba(255,255,255,0.7);
    font-size: 10px;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
}

/* Connection lines animate */
.connections line {
    stroke-dashoffset: 100;
    animation: drawLine 2s ease-out forwards;
}
@keyframes drawLine {
    0%   { stroke-dashoffset: 100; opacity: 0; }
    100% { stroke-dashoffset: 0; opacity: 0.12; }
}

/* Stats bar */
.stats-bar {
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 1.25rem 2rem;
    background: rgba(0,0,0,0.25);
    border-top: 1px solid rgba(46,125,50,0.15);
}
.stat-item {
    text-align: center;
}
.stat-number {
    font-size: 1.5rem;
    font-weight: 700;
    color: #fff;
    line-height: 1.2;
}
.stat-desc {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.5);
    margin-top: 0.2rem;
}
.stat-divider {
    width: 1px;
    height: 35px;
    background: rgba(255,255,255,0.1);
}

/* Audience cards */
.audience-card-v2 {
    background: #ffffff;
    border-radius: 14px;
    padding: 1.5rem;
    border: 1px solid #e8e8e8;
    height: 100%;
    transition: transform 0.2s, box-shadow 0.2s;
    cursor: default;
}
.audience-card-v2:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}
.audience-card-v2 .card-icon {
    font-size: 2rem;
    margin-bottom: 0.75rem;
}
.audience-card-v2 h4 {
    color: #1a5632;
    margin: 0 0 0.5rem 0;
    font-size: 1.05rem;
    font-weight: 600;
}
.audience-card-v2 p {
    color: #666;
    font-size: 0.88rem;
    margin: 0;
    line-height: 1.55;
}

/* Chat header (during conversation) */
.chat-header {
    font-size: 1.6rem;
    font-weight: 700;
    color: #1a5632;
    margin-bottom: 0.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 2px solid #e8f5e9;
}

/* Sidebar styles */
.sidebar-logo {
    text-align: center;
    padding: 0.5rem 0 0.5rem 0;
}
.sidebar-logo h2 {
    color: #1a5632;
    margin: 0.25rem 0 0 0;
    font-size: 1.2rem;
    font-weight: 700;
}
.sidebar-section {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 0.75rem;
}
.sidebar-section h4 {
    margin-top: 0;
    color: #1a5632;
    font-size: 0.9rem;
}
.sidebar-disclaimer {
    text-align: center;
    padding-top: 0.75rem;
}
.sidebar-disclaimer p {
    font-size: 0.73rem;
    color: #999;
    line-height: 1.4;
}

/* Chat message rounding */
div[data-testid="stChatMessage"] {
    border-radius: 12px;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-content {
        flex-direction: column;
        padding: 1.5rem;
    }
    .hero-title-text {
        font-size: 1.8rem;
    }
    .hero-right {
        max-width: 280px;
    }
    .stats-bar {
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    .stat-divider {
        display: none;
    }
}
</style>
"""
