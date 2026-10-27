"""Generate northern-lights.html (served at /northern-lights).

Reuses the homepage's styles, header and footer. build.py runs it.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://discovericeland.co"
URL = f"{SITE}/northern-lights"

index = (ROOT / "index.html").read_text(encoding="utf8")
STYLE = re.search(r"<style>(.*?)</style>", index, re.S).group(1)
FONTS = re.search(r'<link href="https://fonts.googleapis.com[^>]+>', index).group(0)
HEADER = re.search(r'<header class="site-header".*?</header>', index, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', index, re.S).group(0)
SCRIPT = re.search(r"<script>(.*?)</script>", index, re.S).group(1)


def sitewide(fragment):
    fragment = fragment.replace('href="#top"', 'href="/"')
    return re.sub(r'href="#([a-z-]+)"', r'href="/#\1"', fragment)


HEADER = sitewide(HEADER).replace('href="/northern-lights"', 'href="/northern-lights" aria-current="page"')
FOOTER = sitewide(FOOTER)
SCRIPT = SCRIPT.split("// Checklist sign-up")[0] + "\n})();"

# Image slots used on this page (build.py resizes them).
SLOTS = {
    "nl-hero-fjord": "76bc3cd2-image.jpg",
    "nl-snow-valley": "d25c89a3-image.jpg",
    "nl-cabins": "d1db2054-image.jpg",
    "nl-winter-arc": "60a4b5c0-image.jpg",
    "nl-kirkjufell": "7ff801e8-image.jpg",
    "nl-lake": "581dc034-image.jpg",
}


def img(slot, alt, sizes="100vw", cls=None, style=None, lazy=True):
    c = f' class="{cls}"' if cls else ""
    s = f' style="{style}"' if style else ""
    load = 'loading="lazy" decoding="async"' if lazy else 'fetchpriority="high"'
    return (f'<img{c} src="/assets/img/{slot}-1800.jpg" srcset="/assets/img/{slot}-800.jpg 800w, '
            f'/assets/img/{slot}-1800.jpg 1800w" sizes="{sizes}" alt="{html.escape(alt)}"{s} {load}>')


FAQ = [
    ("When is the northern lights season in Iceland?",
     "Roughly from late August or September to mid-April, whenever the nights are dark enough. In summer the midnight sun keeps the sky too bright to see them."),
    ("What time of night are the northern lights best?",
     "Most displays happen between about 9 pm and 2 am, but they can appear any time it is dark. Plan to wait, and check the sky every so often."),
    ("Can you see the northern lights from Reykjavík?",
     "Sometimes, during strong displays, but city lights wash out weaker ones. A short drive out of town to somewhere dark makes a big difference."),
    ("Do I need a tour to see the northern lights?",
     "No. With a car, a clear forecast and a dark spot you can go on your own. Tours help in winter if you would rather not drive on icy roads at night, and many offer a free second try if you see nothing."),
    ("How many nights should I plan to see the northern lights?",
     "Give yourself several nights. Cloud is the biggest obstacle, and a stay of three or more nights in the dark season gives you far better odds than one."),
    ("Can I photograph the northern lights with my phone?",
     "Yes. Use night mode, the main lens, no flash, and rest the phone on something steady while the photo is taken."),
]

PAGE_CSS = """
/* Northern lights page */
.nl-hero { position: relative; min-height: 88svh; display: flex; align-items: flex-end; overflow: hidden; background: var(--night); color: var(--white); }
.nl-hero .bg { object-position: 50% 35%; -webkit-mask-image: linear-gradient(180deg, #000 60%, transparent 100%); mask-image: linear-gradient(180deg, #000 60%, transparent 100%); }
.nl-hero .shade { background: linear-gradient(180deg, rgba(10, 17, 22, 0.5) 0%, rgba(10, 17, 22, 0.1) 40%, rgba(10, 17, 22, 0.55) 78%, var(--night) 100%); }
.nl-hero .container { position: relative; padding-top: calc(var(--header-h) + 60px); padding-bottom: 50px; }
.nl-hero h1 { font-family: var(--serif); font-weight: 700; font-size: clamp(2.8rem, 8vw, 6rem); letter-spacing: -0.01em; line-height: 0.98; }
.nl-hero .rule { display: block; width: 64px; height: 3px; background: var(--red); margin: 26px 0 18px; }
.nl-hero .lead { color: rgba(255, 255, 255, 0.88); }
.nl-crumbs { font-size: 0.78rem; margin-bottom: 18px; opacity: 0.85; }
.nl-crumbs a { text-decoration: none; border-bottom: 1px solid rgba(255, 255, 255, 0.4); }
.nl-stats { margin-top: 10px; }
.nl-prose { max-width: 760px; margin: 0 auto; }
.nl-prose p { color: var(--mist); font-size: 1.04rem; line-height: 1.75; }
.nl-prose h2 { margin-bottom: 18px; }
.nl-prose ul { color: var(--mist); padding-left: 1.2em; line-height: 1.75; }
.nl-prose li { margin-bottom: 6px; }
.nl-prose strong { color: var(--frost); }
.nl-prose a { color: var(--frost); }
.nl-two { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; margin-top: 28px; }
.nl-box { border: 1px solid var(--line); border-top: 3px solid var(--glacier); border-radius: var(--radius); padding: 22px 24px; background: rgba(255, 255, 255, 0.02); }
.nl-box h3 { font-size: 1.05rem; margin-bottom: 12px; }
.nl-box ul { margin: 0; padding-left: 1.1em; color: var(--mist); line-height: 1.7; font-size: 0.95rem; }
.nl-gallery { display: grid; grid-template-columns: 1.4fr 1fr 1fr; gap: 6px; -webkit-mask-image: linear-gradient(180deg, transparent 0, #000 10%, #000 80%, transparent 100%); mask-image: linear-gradient(180deg, transparent 0, #000 10%, #000 80%, transparent 100%); }
.nl-gallery img { width: 100%; height: 100%; aspect-ratio: 3 / 4; object-fit: cover; }
.nl-gallery img:first-child { aspect-ratio: auto; }
.nl-graphics { display: grid; gap: 28px; margin-top: 30px; }
.nl-graphic { width: 100%; height: auto; display: block; border-radius: var(--radius); box-shadow: 0 30px 70px rgba(0, 0, 0, 0.45); }
.nl-graphic text { font-family: Montserrat, system-ui, sans-serif; fill: var(--frost); }
.nl-graphic .t-name { font-weight: 800; font-size: 22px; letter-spacing: 0.14em; }
.nl-graphic .t-body { font-size: 19px; }
.nl-graphic .t-strong { font-size: 19px; font-weight: 700; }
.nl-graphic .t-note { font-size: 15px; fill: rgba(232, 238, 241, 0.6); }
.nl-graphic .t-rule { stroke: rgba(232, 238, 241, 0.16); stroke-width: 1; }
.nl-graphic .t-label { font-size: 20px; font-weight: 700; }
.nl-graphic .t-small { font-size: 15px; fill: rgba(232, 238, 241, 0.7); }
.nl-graphic .t-dark { fill: #3a1408; font-weight: 800; }
.nl-graphic-cap { color: var(--mist); font-size: 0.85rem; margin: 10px 0 0; }
.nl-faq details { border-bottom: 1px solid var(--line); padding: 18px 0; }
.nl-faq summary { cursor: pointer; font-weight: 700; font-size: 1.05rem; list-style: none; display: flex; justify-content: space-between; gap: 16px; }
.nl-faq summary::-webkit-details-marker { display: none; }
.nl-faq summary::after { content: "+"; color: var(--glacier); font-weight: 400; font-size: 1.4rem; line-height: 1; }
.nl-faq details[open] summary::after { content: "–"; }
.nl-faq details p { margin: 12px 0 0; color: var(--mist); }
.nl-map a { display: block; border-radius: var(--radius); overflow: hidden; box-shadow: 0 30px 70px rgba(0, 0, 0, 0.5); cursor: zoom-in; margin-top: 28px; }
.nl-map img { width: 100%; }
.nl-map p.fine { text-align: center; }
@media (max-width: 760px) {
  .nl-two { grid-template-columns: 1fr; }
  .nl-gallery { grid-template-columns: 1fr 1fr; }
  .nl-gallery img:first-child { grid-column: 1 / -1; aspect-ratio: 4 / 3; }
}
"""


def main():
    faq_html = "".join(
        f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in FAQ
    )
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": "Northern Lights in Iceland: When, Where and How to See Them",
            "description": "When the aurora season runs, how to read the forecast, the best dark-sky spots, tours or self-drive, and camera settings.",
            "image": [f"{SITE}/assets/img/nl-hero-fjord-1800.jpg"],
            "datePublished": "2026-10-27",
            "dateModified": "2026-10-27",
            "author": {"@type": "Organization", "name": "Discover Iceland", "url": SITE},
            "publisher": {"@type": "Organization", "name": "Discover Iceland", "url": SITE},
            "mainEntityOfPage": URL,
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ
            ],
        },
    ]
    title = "Northern Lights in Iceland: When, Where and How to See Them"
    desc = ("Your guide to the northern lights in Iceland: the season, the best time of night, how to read the "
            "aurora and cloud forecast, dark-sky spots by region, tours or self-drive, and camera settings.")
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Discover Iceland</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Discover Iceland">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{SITE}/assets/img/nl-hero-fjord-1800.jpg">
<meta name="twitter:card" content="summary_large_image">
{FONTS}
{''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)}
<style>{STYLE}{PAGE_CSS}</style>
</head>
<body>
{HEADER}
<main id="top">
  <section class="nl-hero">
    {img("nl-hero-fjord", "Green northern lights swirling over a snowy ridge, reflected in a calm fjord", cls="bg", lazy=False)}
    <div class="shade"></div>
    <div class="container">
      <p class="nl-crumbs"><a href="/">Discover Iceland</a> / Northern lights</p>
      <p class="eyebrow light">The northern lights</p>
      <h1>When the sky<br>comes alive.</h1>
      <span class="rule"></span>
      <p class="lead">When to come, where to stand, how to read the forecast and how to photograph them. Everything you need to see the aurora in Iceland.</p>
    </div>
  </section>

  <section class="section light nl-stats-wrap" style="padding-top: 20px">
    <div class="container stats nl-stats">
      <div><strong>Sep–Apr</strong><span>the aurora season, when the nights are dark</span></div>
      <div><strong>9pm–2am</strong><span>when most displays happen</span></div>
      <div><strong>3+ nights</strong><span>gives you the best odds against cloud</span></div>
    </div>
  </section>

  <section class="section light">
    <div class="nl-prose container">
      <p class="eyebrow">What you need</p>
      <h2>Dark. Clear. Active.</h2>
      <p>The northern lights happen when particles from the sun hit the upper atmosphere and make it glow, mostly green. Iceland sits right under the band where this happens most, so the lights are overhead on many nights. You just need three things to line up:</p>
      <ul>
        <li><strong>Darkness.</strong> From about September to April. In summer the midnight sun hides them completely.</li>
        <li><strong>A clear sky.</strong> Cloud is the most common reason people miss them, far more than a quiet sun.</li>
        <li><strong>Solar activity.</strong> Some nights are quiet, some are spectacular. Even a modest display can be beautiful away from town lights.</li>
      </ul>
    </div>
  </section>

  <section class="section light" id="science">
    <div class="nl-prose container">
      <p class="eyebrow">The science</p>
      <h2>Why the sky glows.</h2>
      <p>The sun sends out a constant stream of charged particles called the solar wind. Earth's magnetic field steers some of them towards the poles, into a ring around each one called the auroral oval. There they collide with oxygen and nitrogen high in the atmosphere, which give off light. The gas and the height decide the colour.</p>
      <div class="nl-graphics">
        <figure style="margin:0"><svg class="nl-graphic" viewBox="0 0 960 440" role="img" aria-labelledby="g2t g2d">
  <title id="g2t">How the northern lights form</title>
  <desc id="g2d">The sun sends out the solar wind, a stream of electrons and protons. Earth's magnetic field guides some of them towards the poles, where they hit the upper atmosphere in a ring called the auroral oval and make it glow.</desc>
  <defs>
    <radialGradient id="sun" cx="0.75" cy="0.5" r="0.8"><stop offset="0" stop-color="#ffb347"/><stop offset="0.6" stop-color="#ff6a2a"/><stop offset="1" stop-color="#d9483b"/></radialGradient>
    <radialGradient id="earth" cx="0.4" cy="0.35" r="0.75"><stop offset="0" stop-color="#4fa3d9"/><stop offset="1" stop-color="#1b4f7a"/></radialGradient>
    <filter id="glow2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#9fd4e2"/></marker>
  </defs>
  <rect width="960" height="440" rx="6" fill="#0d1820"/>
  <circle cx="-40" cy="220" r="230" fill="url(#sun)"/>
  <text x="40" y="215" class="t-label t-dark">The sun</text>
  <g fill="none" stroke="#9fd4e2" stroke-width="2.2" marker-end="url(#arr)" opacity="0.9">
    <path d="M230 90 C420 90 560 110 700 150"/>
    <path d="M240 150 C430 150 560 160 690 180"/>
    <path d="M245 220 C430 220 560 220 660 220"/>
    <path d="M240 290 C430 290 560 280 690 260"/>
    <path d="M230 350 C420 350 560 330 700 290"/>
  </g>
  <g fill="none" stroke="#3cf08c" stroke-width="2.4" filter="url(#glow2)">
    <path d="M250 190 q10 -10 20 0 t20 0 t20 0 t20 0 t20 0 t20 0"/>
    <path d="M250 250 q10 -10 20 0 t20 0 t20 0 t20 0 t20 0 t20 0"/>
  </g>
  <text x="300" y="60" class="t-label">Solar wind</text>
  <text x="270" y="282" class="t-small">Electrons and protons</text>
  <g fill="none" stroke="#d9483b" stroke-width="1.6" stroke-dasharray="3 6" opacity="0.85">
    <ellipse cx="800" cy="220" rx="150" ry="110"/>
    <ellipse cx="830" cy="220" rx="110" ry="80"/>
  </g>
  <circle cx="800" cy="220" r="62" fill="url(#earth)"/>
  <path d="M772 196 c10 -10 30 -8 34 4 c4 12 -10 16 -4 28 c6 10 20 8 22 20 c-4 12 -26 12 -38 2 c-12 -12 -24 -36 -14 -54z" fill="#6fae74" opacity="0.55"/>
  <g filter="url(#glow2)" fill="none" stroke="#3cf08c" stroke-width="5">
    <ellipse cx="800" cy="166" rx="34" ry="8"/>
    <ellipse cx="800" cy="274" rx="34" ry="8" opacity="0.7"/>
  </g>
  <text x="905" y="128" class="t-label" text-anchor="end">Auroral oval</text>
  <text x="925" y="352" class="t-small" text-anchor="end">Magnetic field</text>
  <text x="40" y="410" class="t-small">Iceland sits right under the northern auroral oval, which is why the lights are overhead on so many dark nights.</text>
</svg><figcaption class="nl-graphic-cap">How the northern lights form.</figcaption></figure>
        <figure style="margin:0"><svg class="nl-graphic" viewBox="0 0 960 680" role="img" aria-labelledby="g1t g1d">
  <title id="g1t">Northern lights colours and their altitude</title>
  <desc id="g1d">Red aurora comes from oxygen above about 240 km, green from oxygen between about 100 and 240 km, purple from nitrogen around 100 km and blue from nitrogen below about 100 km.</desc>
  <defs><linearGradient id="g-red" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ff4d5e" stop-opacity="0.95"/><stop offset="0.55" stop-color="#ff4d5e" stop-opacity="0.35"/><stop offset="1" stop-color="#ff4d5e" stop-opacity="0"/></linearGradient><linearGradient id="g-green" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#3cf08c" stop-opacity="0.95"/><stop offset="0.55" stop-color="#3cf08c" stop-opacity="0.35"/><stop offset="1" stop-color="#3cf08c" stop-opacity="0"/></linearGradient><linearGradient id="g-purple" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#c45cff" stop-opacity="0.95"/><stop offset="0.55" stop-color="#c45cff" stop-opacity="0.35"/><stop offset="1" stop-color="#c45cff" stop-opacity="0"/></linearGradient><linearGradient id="g-blue" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#3d8bff" stop-opacity="0.95"/><stop offset="0.55" stop-color="#3d8bff" stop-opacity="0.35"/><stop offset="1" stop-color="#3d8bff" stop-opacity="0"/></linearGradient><mask id="rays" maskUnits="userSpaceOnUse" x="0" y="0" width="960" height="680"><rect width="960" height="680" fill="#fff" opacity="0.55"/><rect x="508" y="0" width="3" height="680" fill="#fff"/><rect x="522" y="0" width="6" height="680" fill="#fff"/><rect x="541" y="0" width="2" height="680" fill="#fff"/><rect x="556" y="0" width="8" height="680" fill="#fff"/><rect x="578" y="0" width="3" height="680" fill="#fff"/><rect x="592" y="0" width="5" height="680" fill="#fff"/><rect x="612" y="0" width="2" height="680" fill="#fff"/><rect x="626" y="0" width="7" height="680" fill="#fff"/><rect x="648" y="0" width="3" height="680" fill="#fff"/><rect x="664" y="0" width="4" height="680" fill="#fff"/><rect x="684" y="0" width="8" height="680" fill="#fff"/><rect x="706" y="0" width="2" height="680" fill="#fff"/><rect x="720" y="0" width="5" height="680" fill="#fff"/><rect x="738" y="0" width="3" height="680" fill="#fff"/><rect x="752" y="0" width="7" height="680" fill="#fff"/><rect x="774" y="0" width="2" height="680" fill="#fff"/><rect x="788" y="0" width="5" height="680" fill="#fff"/><rect x="806" y="0" width="3" height="680" fill="#fff"/><rect x="820" y="0" width="8" height="680" fill="#fff"/><rect x="842" y="0" width="2" height="680" fill="#fff"/><rect x="856" y="0" width="5" height="680" fill="#fff"/><rect x="874" y="0" width="3" height="680" fill="#fff"/><rect x="888" y="0" width="6" height="680" fill="#fff"/><rect x="902" y="0" width="2" height="680" fill="#fff"/></mask><filter id="glow" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
  <rect width="960" height="680" rx="6" fill="#0d1820"/>
  <circle cx="470" cy="60" r="1.4" fill="#fff" opacity="0.6"/><circle cx="880" cy="90" r="1" fill="#fff" opacity="0.5"/><circle cx="640" cy="200" r="1.2" fill="#fff" opacity="0.4"/><circle cx="950" cy="330" r="1.4" fill="#fff" opacity="0.5"/><circle cx="480" cy="470" r="1" fill="#fff" opacity="0.5"/><circle cx="700" cy="520" r="1.3" fill="#fff" opacity="0.4"/><circle cx="930" cy="620" r="1" fill="#fff" opacity="0.5"/><circle cx="560" cy="640" r="1.2" fill="#fff" opacity="0.4"/>
    <text x="40" y="88" class="t-name" fill="#ff4d5e">RED</text>
    <text x="40" y="116" class="t-body">Oxygen, very high up</text>
    <text x="40" y="142" class="t-strong">Above about 240 km (150 mi)</text>
    <text x="40" y="166" class="t-note">Only in strong storms</text>
    <g>
      <path d="M500 120 C560 92 610 142 680 120 C750 98 810 146 910 116 L910 26 C810 56 750 8 680 30 C610 52 560 2 500 30 Z" fill="url(#g-red)" mask="url(#rays)" filter="url(#glow)"/>
      <path d="M500 120 C560 92 610 142 680 120 C750 98 810 146 910 116" fill="none" stroke="#ff4d5e" stroke-width="3.5" stroke-linecap="round" filter="url(#glow)"/>
      <path d="M500 120 C560 92 610 142 680 120 C750 98 810 146 910 116" fill="none" stroke="#fff" stroke-opacity="0.55" stroke-width="1.2" stroke-linecap="round"/>
    </g><line x1="40" y1="200" x2="900" y2="200" class="t-rule"/>
    <text x="40" y="233" class="t-name" fill="#3cf08c">GREEN</text>
    <text x="40" y="261" class="t-body">Oxygen, lower down</text>
    <text x="40" y="287" class="t-strong">About 100–240 km (60–150 mi)</text>
    <text x="40" y="311" class="t-note">The colour you will see most</text>
    <g>
      <path d="M500 265 C560 237 610 287 680 265 C750 243 810 291 910 261 L910 171 C810 201 750 153 680 175 C610 197 560 147 500 175 Z" fill="url(#g-green)" mask="url(#rays)" filter="url(#glow)"/>
      <path d="M500 265 C560 237 610 287 680 265 C750 243 810 291 910 261" fill="none" stroke="#3cf08c" stroke-width="3.5" stroke-linecap="round" filter="url(#glow)"/>
      <path d="M500 265 C560 237 610 287 680 265 C750 243 810 291 910 261" fill="none" stroke="#fff" stroke-opacity="0.55" stroke-width="1.2" stroke-linecap="round"/>
    </g><line x1="40" y1="345" x2="900" y2="345" class="t-rule"/>
    <text x="40" y="378" class="t-name" fill="#c45cff">PURPLE</text>
    <text x="40" y="406" class="t-body">Nitrogen</text>
    <text x="40" y="432" class="t-strong">Around 100 km (60 mi)</text>
    <text x="40" y="456" class="t-note">Often at the lower edge</text>
    <g>
      <path d="M500 410 C560 382 610 432 680 410 C750 388 810 436 910 406 L910 316 C810 346 750 298 680 320 C610 342 560 292 500 320 Z" fill="url(#g-purple)" mask="url(#rays)" filter="url(#glow)"/>
      <path d="M500 410 C560 382 610 432 680 410 C750 388 810 436 910 406" fill="none" stroke="#c45cff" stroke-width="3.5" stroke-linecap="round" filter="url(#glow)"/>
      <path d="M500 410 C560 382 610 432 680 410 C750 388 810 436 910 406" fill="none" stroke="#fff" stroke-opacity="0.55" stroke-width="1.2" stroke-linecap="round"/>
    </g><line x1="40" y1="490" x2="900" y2="490" class="t-rule"/>
    <text x="40" y="523" class="t-name" fill="#3d8bff">BLUE</text>
    <text x="40" y="551" class="t-body">Nitrogen, lowest</text>
    <text x="40" y="577" class="t-strong">Below about 100 km (60 mi)</text>
    <text x="40" y="601" class="t-note">Faint, during strong displays</text>
    <g>
      <path d="M500 555 C560 527 610 577 680 555 C750 533 810 581 910 551 L910 461 C810 491 750 443 680 465 C610 487 560 437 500 465 Z" fill="url(#g-blue)" mask="url(#rays)" filter="url(#glow)"/>
      <path d="M500 555 C560 527 610 577 680 555 C750 533 810 581 910 551" fill="none" stroke="#3d8bff" stroke-width="3.5" stroke-linecap="round" filter="url(#glow)"/>
      <path d="M500 555 C560 527 610 577 680 555 C750 533 810 581 910 551" fill="none" stroke="#fff" stroke-opacity="0.55" stroke-width="1.2" stroke-linecap="round"/>
    </g>
</svg><figcaption class="nl-graphic-cap">Aurora colours by gas and height. Green is by far the most common; red, purple and blue show up in stronger displays.</figcaption></figure>
      </div>
    </div>
  </section>

  <section class="feature" id="when">
    <div class="feature-media">{img("nl-snow-valley", "Green aurora over a snow-covered hillside under a starry sky", style="object-position: 40% 40%")}</div>
    <div class="container feature-body">
      <div class="feature-text">
        <p class="eyebrow light">When to go</p>
        <h2>The season and the hour.</h2>
        <p class="lead">Late August to mid-April, with the longest nights from November to February. September, October and March are good bets: the nights are long enough, and the weather and roads are often kinder than in midwinter.</p>
        <ul class="spots">
          <li><strong>Best hours</strong><span>About 9 pm to 2 am, though they can appear any time it is dark.</span></li>
          <li><strong>Moon</strong><span>A dark, moonless week shows faint displays best; a full moon lights the landscape.</span></li>
          <li><strong>Stay longer</strong><span>Three or more nights in the season gives you far better odds.</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section light" id="forecast">
    <div class="nl-prose container">
      <p class="eyebrow">The forecast</p>
      <h2>How to read the aurora forecast.</h2>
      <p>Check two things every evening, in this order.</p>
      <div class="nl-two">
        <div class="nl-box"><h3>1. Cloud cover</h3><ul><li>The Icelandic Met Office (vedur.is) publishes an aurora forecast with a cloud map for the whole country.</li><li>Look for the white, cloud-free patches and head there.</li><li>Cloud often clears on one side of the island while the other stays covered.</li></ul></div>
        <div class="nl-box"><h3>2. Aurora activity</h3><ul><li>Activity is shown on a scale, often the Kp index from 0 to 9.</li><li>Around 3 or higher is a good night; lower values can still show up in a dark spot.</li><li>Forecasts are a guide, not a promise. Step outside and look.</li></ul></div>
      </div>
      <p style="margin-top: 26px">Apps and alert services can wake you when activity rises. Many hotels in the countryside offer an aurora wake-up call too.</p>
    </div>
  </section>

  <section class="section light nl-map" id="where">
    <div class="container">
      <div class="center narrow">
        <p class="eyebrow">Where to watch</p>
        <h2>Anywhere dark.</h2>
        <p class="lead center">You do not need a special place, just a dark one with a view north and no lights nearby. These are some of the best bases.</p>
      </div>
      <a href="/assets/img/map-highlights-2800.jpg" target="_blank" rel="noopener" aria-label="Open the Iceland highlights map full size"><img src="/assets/img/map-highlights-1800.jpg" srcset="/assets/img/map-highlights-800.jpg 800w, /assets/img/map-highlights-1800.jpg 1800w" sizes="(min-width: 1240px) 1200px, 100vw" alt="Map of Iceland with the main highlights marked" loading="lazy" decoding="async"></a>
      <p class="fine">Tap the map to open it full size.</p>
      <div class="nl-two" style="max-width: 1000px; margin-left: auto; margin-right: auto">
        <div class="nl-box"><h3>Near Reykjavík</h3><ul><li>Þingvellir National Park, 45 minutes away and very dark.</li><li>The Golden Circle countryside around Laugarvatn and Flúðir.</li><li>Grótta lighthouse, at the edge of town, for strong displays.</li></ul></div>
        <div class="nl-box"><h3>South Coast</h3><ul><li>Farm stays around Hella, Hvolsvöllur and Vík.</li><li>Jökulsárlón, with the aurora over the icebergs.</li><li>Black beaches like Reynisfjara, from a safe distance.</li></ul></div>
        <div class="nl-box"><h3>Snæfellsnes</h3><ul><li>Kirkjufell and Kirkjufellsfoss, the classic photo.</li><li>Fishing villages with dark skies all around.</li></ul></div>
        <div class="nl-box"><h3>The north</h3><ul><li>Lake Mývatn and Akureyri, often clearer and colder.</li><li>Fewer people, long winter nights.</li></ul></div>
      </div>
      <div class="btn-row center-row"><a class="btn outline" href="/highlights#aurora">See the aurora highlights</a></div>
    </div>
  </section>

  <section class="feature reverse" id="tours">
    <div class="feature-media">{img("nl-cabins", "Bright green aurora above a dark hillside with two small cabins", style="object-position: 50% 35%")}</div>
    <div class="container feature-body">
      <div class="feature-text">
        <p class="eyebrow light">Tours or on your own</p>
        <h2>Chase them your way.</h2>
        <p class="lead">With a car and a clear forecast you can go on your own: drive somewhere dark, park safely and wait. In winter a tour can be the safer choice, because guides know where the clear skies are and you do not have to drive icy roads at night.</p>
        <ul class="spots">
          <li><strong>Self-drive</strong><span>Free and flexible. Never stop on the road itself; use a proper parking area.</span></li>
          <li><strong>Bus or minibus tours</strong><span>Leave Reykjavík in the evening; many offer a free retry if you see nothing.</span></li>
          <li><strong>Boat tours</strong><span>Sail out of Reykjavík harbour, away from the city lights.</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section light" id="photos">
    <div class="nl-prose container">
      <p class="eyebrow">Photographing the aurora</p>
      <h2>Camera and phone settings.</h2>
      <div class="nl-two">
        <div class="nl-box"><h3>Camera</h3><ul><li>Manual mode, on a tripod.</li><li>Widest aperture, ideally f/2.8.</li><li>ISO 1600, up to 3200 for faint lights.</li><li>Shutter 5–8 s for fast lights, 10–15 s for slow glows.</li><li>Manual focus set to infinity before dark.</li><li>Shoot RAW; white balance around 3500–4000K.</li></ul></div>
        <div class="nl-box"><h3>Phone</h3><ul><li>Night mode on, exposure 10–30 s.</li><li>Use the main lens, not ultra-wide or zoom.</li><li>Flash off.</li><li>Rest the phone on something steady and use the timer.</li><li>Keep still until the photo finishes.</li></ul></div>
      </div>
    </div>
  </section>

  <section class="section light" style="padding-top: 0">
    <div class="nl-gallery">
      {img("nl-lake", "Green northern lights over dark mountains reflected in a lake", sizes="40vw")}
      {img("nl-winter-arc", "A green aurora curving down to a snowy horizon", sizes="30vw")}
      {img("nl-kirkjufell", "Northern lights over Kirkjufell mountain and a frozen waterfall", sizes="30vw")}
    </div>
  </section>

  <section class="section light" id="safety">
    <div class="nl-prose container">
      <p class="eyebrow">Stay safe</p>
      <h2>Winter nights, done right.</h2>
      <ul>
        <li><strong>Dress for standing still.</strong> Warm layers, a hat, gloves, warm boots. You may wait an hour or more.</li>
        <li><strong>Check the roads.</strong> Look at road.is before you drive, and turn back if conditions get worse.</li>
        <li><strong>Park properly.</strong> Never stop on the road to look up. Use a lay-by or car park, with your lights off once parked.</li>
        <li><strong>Mind the coast.</strong> Stay well back from the water on black beaches, day or night.</li>
      </ul>
    </div>
  </section>

  <section class="section light nl-faq" id="faq">
    <div class="nl-prose container">
      <p class="eyebrow">Questions</p>
      <h2>Northern lights FAQ.</h2>
      {faq_html}
    </div>
  </section>

  <section class="section guides">
    <div class="guides-fade"></div>
    <div class="container narrow center">
      <p class="eyebrow center">The aurora guide</p>
      <h2 class="center">Discover Iceland: Northern Lights</h2>
      <p class="lead center">Our full guide to the aurora is coming soon: forecasts, dark-sky spots by region, gear, photography and the best winter routes.</p>
      <div class="btn-row center-row"><a class="btn primary" href="/#checklist">Notify me at launch</a><a class="btn outline" href="/blog/best-time-to-visit-iceland">When to visit Iceland</a></div>
    </div>
  </section>
</main>
{FOOTER}
<script>{SCRIPT}</script>
</body>
</html>
"""
    (ROOT / "northern-lights.html").write_text(page, encoding="utf8")
    print("page northern-lights")


if __name__ == "__main__":
    main()
