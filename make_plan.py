"""Generate plan-your-trip.html (served at /plan-your-trip): one landing page that ties
together the itineraries, the /map trip planner and the Complete Guide with its buy button.
Good page to send ad and social traffic to. build.py runs it after make_articles."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://discovericeland.co"

index = (ROOT / "index.html").read_text(encoding="utf8")
STYLE = re.search(r"<style>(.*?)</style>", index, re.S).group(1)
FONTS = re.search(r'<link href="https://fonts.googleapis.com[^>]+>', index).group(0)
HEADER = re.search(r'<header class="site-header".*?</header>', index, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', index, re.S).group(0)
SCRIPT = re.search(r"<script>(.*?)</script>", index, re.S).group(1)
SCRIPT = SCRIPT.split("// Checklist sign-up")[0] + "\n})();"
# The buy block (price + Apple Pay button) is taken from the homepage, so both always match.
m = re.search(r'<div class="dbook-buy">.*?</p></div>', index, re.S)
BUY = m.group(0) if m else '<a class="btn primary" href="/complete-guide">Get the Complete Guide</a>'


def sitewide(fragment):
    fragment = fragment.replace('href="#top"', 'href="/"')
    return re.sub(r'href="#([a-z-]+)"', r'href="/#\1"', fragment)


HEADER = sitewide(HEADER)
FOOTER = sitewide(FOOTER)

CSS = """
.pt-hero { position: relative; min-height: 86svh; display: flex; align-items: flex-end; overflow: hidden; background: var(--night); }
.pt-hero .bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; -webkit-mask-image: linear-gradient(180deg, #000 60%, transparent 100%); mask-image: linear-gradient(180deg, #000 60%, transparent 100%); }
.pt-hero .shade { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(10,17,22,.55) 0%, rgba(10,17,22,.15) 40%, rgba(10,17,22,.85) 85%, var(--night) 100%); }
.pt-hero .container { position: relative; padding-top: calc(var(--header-h) + 80px); padding-bottom: 56px; }
.pt-hero h1 { font-family: var(--serif); font-size: clamp(2.8rem, 7.5vw, 5.6rem); line-height: .98; margin: 8px 0 18px; max-width: 16ch; }
.pt-hero .lead { color: var(--frost); font-size: clamp(1.05rem, 1.8vw, 1.25rem); max-width: 48ch; }
.pt-steps { display: flex; flex-wrap: wrap; gap: 10px 26px; margin: 30px 0 0; padding: 0; list-style: none; color: var(--mist); font-size: .82rem; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.pt-steps b { color: var(--red); margin-right: 8px; }
.pt-sec { padding: clamp(72px, 9vw, 120px) 0 0; }
.pt-sec > .container > h2 { font-family: var(--serif); font-size: clamp(2rem, 4.4vw, 3.2rem); line-height: 1.05; margin: 6px 0 12px; }
.pt-sec > .container > .lead { color: var(--mist); max-width: 60ch; margin: 0; }
.pt-days { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 22px; margin-top: 40px; }
.pt-day { position: relative; display: flex; flex-direction: column; justify-content: flex-end; min-height: 440px; border-radius: 6px; overflow: hidden; text-decoration: none; color: var(--white); isolation: isolate; }
.pt-day img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: -2; transition: transform .8s; }
.pt-day::after { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(180deg, rgba(10,17,22,.1) 20%, rgba(10,17,22,.92) 78%); }
.pt-day:hover img { transform: scale(1.05); }
.pt-day-body { padding: 22px 20px 22px; }
.pt-num { font-family: var(--sans); font-weight: 800; font-size: 4.2rem; line-height: .85; letter-spacing: -0.05em; }
.pt-num small { font-size: 1rem; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-left: 6px; color: var(--glacier); }
.pt-day h3 { font-family: var(--serif); font-size: 1.15rem; line-height: 1.25; margin: 12px 0 6px; }
.pt-day p { color: var(--frost); opacity: .85; font-size: .88rem; margin: 0 0 12px; }
.pt-day .stat { display: block; font-size: .72rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: var(--glacier); }
.pt-day .go { display: inline-block; margin-top: 14px; font-weight: 700; font-size: .85rem; border-bottom: 2px solid var(--red); }
.pt-note { margin: 22px 0 0; color: var(--mist); }
.pt-note a { color: var(--white); text-underline-offset: 3px; }
.pt-split { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.25fr); gap: clamp(32px, 6vw, 80px); align-items: center; }
.pt-split h2 { font-family: var(--serif); font-size: clamp(2rem, 4.4vw, 3.2rem); line-height: 1.05; margin: 6px 0 14px; }
.pt-split p { color: var(--mist); }
.pt-howto { list-style: none; padding: 0; margin: 24px 0 28px; display: grid; gap: 14px; counter-reset: s; }
.pt-howto li { display: grid; grid-template-columns: 36px 1fr; gap: 12px; align-items: start; color: var(--frost); }
.pt-howto li::before { counter-increment: s; content: counter(s); width: 30px; height: 30px; border-radius: 50%; background: var(--red); color: #fff; display: grid; place-items: center; font-weight: 800; font-size: .85rem; }
.pt-howto strong { color: var(--white); }
.pt-mapimg { display: block; border-radius: 6px; overflow: hidden; box-shadow: 0 30px 70px rgba(0,0,0,.5); }
.pt-mapimg img { display: block; width: 100%; height: auto; transition: transform .8s; }
.pt-mapimg:hover img { transform: scale(1.03); }
.pt-basics { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 22px; margin-top: 40px; }
.pt-basic { display: block; text-decoration: none; color: inherit; }
.pt-basic img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 6px; display: block; }
.pt-basic small { display: block; margin-top: 14px; font-size: .68rem; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: var(--glacier); }
.pt-basic h3 { font-family: var(--serif); font-size: 1.15rem; margin: 6px 0 6px; color: var(--white); }
.pt-basic p { color: var(--mist); font-size: .88rem; margin: 0; }
.pt-book { position: relative; overflow: hidden; isolation: isolate; margin-top: clamp(72px, 9vw, 120px); padding: clamp(72px, 9vw, 120px) 0; }
.pt-book .bgimg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: -2; opacity: .4; filter: blur(3px); transform: scale(1.08); -webkit-mask-image: linear-gradient(180deg, transparent 0%, #000 25%, #000 75%, transparent 100%); mask-image: linear-gradient(180deg, transparent 0%, #000 25%, #000 75%, transparent 100%); }
.pt-book::after { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(90deg, rgba(10,17,22,.35), rgba(10,17,22,.75)); }
.pt-book .wrap { display: grid; grid-template-columns: minmax(0, 360px) 1fr; gap: clamp(36px, 6vw, 88px); align-items: center; }
.pt-book .cov { display: grid; gap: 20px; }
.pt-book .cov a img { display: block; width: 100%; height: auto; transform: rotateY(8deg); box-shadow: -24px 30px 60px rgba(0,0,0,.55); }
.pt-book h2 { font-family: var(--serif); font-size: clamp(2.2rem, 5vw, 3.8rem); line-height: 1; margin: 6px 0 16px; }
.pt-book ul { list-style: none; padding: 0; margin: 22px 0 26px; display: grid; gap: 10px; }
.pt-book li { color: var(--frost); padding-left: 22px; position: relative; }
.pt-book li::before { content: ""; position: absolute; left: 0; top: .7em; width: 10px; height: 2px; background: var(--red); }
.pt-topics { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 30px; }
.pt-topics a { font-size: .74rem; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--frost); text-decoration: none; border: 1px solid rgba(232,238,241,.32); border-radius: 999px; padding: 10px 16px; }
.pt-topics a:hover { background: var(--frost); color: var(--night); }
@media (max-width: 1000px) { .pt-days, .pt-basics { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 760px) {
  .pt-day { min-height: 360px; }
  .pt-split, .pt-book .wrap { grid-template-columns: 1fr; }
  .pt-book .cov { max-width: 260px; }
  .pt-book .cov a img { transform: none; }
}
@media (max-width: 520px) { .pt-days { grid-template-columns: 1fr; } .pt-basics { grid-template-columns: 1fr 1fr; gap: 18px; } }
"""


def main():
    import make_articles
    by = {a["slug"]: a for a in make_articles.ARTICLES}

    days = [(3, "iceland-3-day-itinerary"), (5, "iceland-5-day-itinerary"),
            (7, "iceland-ring-road-7-days"), (10, "iceland-ring-road-10-days")]
    day_cards = ""
    for n, slug in days:
        a = by[slug]
        st = a["stats"][0]
        day_cards += f"""
        <a class="pt-day" href="/blog/{slug}">
          <img src="/assets/img/{a['image']}-800.jpg" alt="{html.escape(a['image_alt'])}" loading="lazy" decoding="async">
          <div class="pt-day-body">
            <div class="pt-num">{n}<small>days</small></div>
            <h3>{html.escape(a['short'])}</h3>
            <p>{html.escape(a['teaser'])}</p>
            <span class="stat">{html.escape(st[0])} · {html.escape(st[1])}</span>
            <span class="go">See the itinerary →</span>
          </div>
        </a>"""

    basics = [("When to go", "best-time-to-visit-iceland"), ("Where to stay", "where-to-stay-in-iceland"),
              ("Getting around", "getting-around-iceland"), ("Winter driving", "iceland-ring-road-winter")]
    basic_cards = "".join(f"""
        <a class="pt-basic" href="/blog/{s}">
          <img src="/assets/img/{by[s]['image']}-800.jpg" alt="{html.escape(by[s]['image_alt'])}" loading="lazy" decoding="async">
          <small>{label}</small><h3>{html.escape(by[s]['short'])}</h3><p>{html.escape(by[s]['teaser'])}</p>
        </a>""" for label, s in basics)

    topics = "".join(f'<a href="/journal#{k}">{html.escape(name)}</a>' for k, name, *_ in make_articles.CLUSTERS)

    title = "Plan Your Iceland Trip: Itineraries, Interactive Map and Complete Guide"
    desc = ("Plan your Iceland trip in three steps: pick a 3, 5, 7 or 10-day itinerary, build your own route on our "
            "interactive map, and take the Complete Guide with you.")
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": SITE + "/plan-your-trip",
          "description": desc,
          "hasPart": [{"@type": "Article", "headline": by[s]["title"], "url": f"{SITE}/blog/{s}"} for _, s in days]}

    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)} · Discover Iceland</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}/plan-your-trip">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Discover Iceland">
<meta property="og:title" content="Plan your Iceland trip">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE}/plan-your-trip">
<meta property="og:image" content="{SITE}/og.jpg">
<meta name="twitter:card" content="summary_large_image">
{FONTS}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{STYLE}{CSS}</style>
</head>
<body>
{HEADER}
<main id="top">
  <section class="pt-hero">
    <img class="bg" src="/assets/img/hero-stokksnes-wide-1800.jpg" srcset="/assets/img/hero-stokksnes-wide-800.jpg 800w, /assets/img/hero-stokksnes-wide-1800.jpg 1800w" sizes="100vw" alt="Vestrahorn rising above the black dunes of Stokksnes" fetchpriority="high">
    <div class="shade"></div>
    <div class="container">
      <p class="eyebrow">Plan your trip</p>
      <h1>Your Iceland trip, start to finish.</h1>
      <p class="lead">Pick how many days you have, build your own route on our map, and take the whole island with you in one book.</p>
      <div class="btn-row"><a class="btn primary" href="#days">Choose your itinerary</a><a class="btn ghost" href="/map">Open the trip planner</a></div>
      <ol class="pt-steps"><li><b>01</b>Pick your days</li><li><b>02</b>Build your route</li><li><b>03</b>Take the guide</li></ol>
    </div>
  </section>

  <section class="pt-sec" id="days">
    <div class="container">
      <p class="eyebrow">Step 1</p>
      <h2>How many days do you have?</h2>
      <p class="lead">Four tested routes, each with daily distances, where to sleep and what to see on the way.</p>
      <div class="pt-days">{day_cards}
      </div>
      <p class="pt-note">Only a few hours? See <a href="/blog/golden-circle-half-day">the Golden Circle in half a day</a>.</p>
    </div>
  </section>

  <section class="pt-sec" id="route">
    <div class="container pt-split">
      <div>
        <p class="eyebrow">Step 2</p>
        <h2>Build your own route.</h2>
        <p>Every waterfall, glacier, canyon and hot spring we cover is on one interactive map. Tap around, collect the places you like and we draw the route.</p>
        <ol class="pt-howto">
          <li><span><strong>Tap a place</strong> to see a photo and a short description.</span></li>
          <li><span><strong>Add it to your trip.</strong> Your stops are numbered and joined on the map.</span></li>
          <li><span><strong>Share the link</strong> with your travel partner, or open it on your phone.</span></li>
        </ol>
        <div class="btn-row"><a class="btn primary" href="/map">Open the trip planner</a><a class="btn outline" href="/highlights">Browse the highlights</a></div>
      </div>
      <a class="pt-mapimg" href="/map" aria-label="Open the interactive trip planner"><img src="/assets/img/map-ring-road-1800.jpg" srcset="/assets/img/map-ring-road-800.jpg 800w, /assets/img/map-ring-road-1800.jpg 1800w" sizes="(min-width: 760px) 55vw, 100vw" alt="Discover Iceland map of a 7-day Ring Road route, day by day" loading="lazy" decoding="async"></a>
    </div>
  </section>

  <section class="pt-book" id="guide">
    <img class="bgimg" src="/assets/img/book-bg-guide-1800.jpg" alt="" loading="lazy" decoding="async" style="object-position:50% 72%">
    <div class="container wrap">
      <div class="cov">
        <a href="/complete-guide"><img src="/assets/img/cover-guide-900.jpg" alt="Cover of Discover Iceland, the Complete Guide" width="900" height="1350" loading="lazy" decoding="async"></a>
        {BUY}
      </div>
      <div>
        <p class="eyebrow">Step 3 · Take the guide</p>
        <h2>Discover Iceland: the Complete Guide.</h2>
        <p class="lead">Everything on this site, and much more, in one book you can read offline on the road: every region, our own maps and practical advice, checked against official sources.</p>
        <ul>
          <li>Region by region, from Reykjavík to the Westfjords and the highlands</li>
          <li>Full-spread maps of the Ring Road, waterfalls, glaciers, hot springs and more</li>
          <li>Weather, daylight and road conditions month by month, plus the aurora calendar</li>
          <li>Instant download: read it on your phone, tablet or laptop</li>
        </ul>
        <div class="btn-row"><a class="btn primary" href="/complete-guide">Look inside the book</a><a class="btn outline" href="/#guides">All four guides</a></div>
      </div>
    </div>
  </section>

  <section class="pt-sec" id="basics">
    <div class="container">
      <p class="eyebrow">Before you go</p>
      <h2>The practical bits.</h2>
      <p class="lead">When to come, where to base yourself and how to get around, including winter driving.</p>
      <div class="pt-basics">{basic_cards}
      </div>
      <p class="eyebrow" style="margin-top:64px">More in the journal</p>
      <div class="pt-topics">{topics}</div>
    </div>
  </section>
  <div style="height:96px"></div>
</main>
{FOOTER}
<script>{SCRIPT}</script>
</body>
</html>
"""
    (ROOT / "plan-your-trip.html").write_text(page, encoding="utf8")
    print("plan-your-trip.html")


if __name__ == "__main__":
    main()
