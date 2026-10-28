"""Generate map.html (served at /map): a full-screen interactive map of Iceland
where visitors click around the highlights and build their own trip.

The place list is rendered into the HTML (crawlable); js/trip-map.js adds the
map, the preview card and the trip planner. build.py runs it.
"""
import html
import json
import re
from pathlib import Path

from highlights_content import CATEGORIES
from places_all import all_places

ROOT = Path(__file__).parent
SITE = "https://discovericeland.co"

index = (ROOT / "index.html").read_text(encoding="utf8")
STYLE = re.search(r"<style>(.*?)</style>", index, re.S).group(1)
FONTS = re.search(r'<link href="https://fonts.googleapis.com[^>]+>', index).group(0)
HEADER = re.search(r'<header class="site-header".*?</header>', index, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', index, re.S).group(0)
SCRIPT = re.search(r"<script>(.*?)</script>", index, re.S).group(1)
SCRIPT = SCRIPT.split("// Checklist sign-up")[0] + "\n})();"


def sitewide(fragment):
    fragment = fragment.replace('href="#top"', 'href="/"')
    return re.sub(r'href="#([a-z-]+)"', r'href="/#\1"', fragment)


HEADER = sitewide(HEADER)
FOOTER = sitewide(FOOTER)

CSS = """
body.mp-page .site-header { background: rgba(10, 17, 22, 0.96); box-shadow: 0 1px 0 var(--line); }
.mp-app { margin-top: var(--header-h); height: calc(100svh - var(--header-h)); display: grid; grid-template-columns: 400px minmax(0, 1fr); background: var(--night); }
.mp-side { position: relative; display: flex; flex-direction: column; min-height: 0; border-right: 1px solid var(--line); background: var(--night); }
.mp-head { padding: 22px 22px 0; }
.mp-head .eyebrow { margin-bottom: 8px; }
.mp-head h1 { font-family: var(--serif); font-size: 1.9rem; line-height: 1.05; margin: 0 0 6px; }
.mp-head p { color: var(--mist); font-size: .88rem; margin: 0 0 16px; }
.mp-tabs { display: grid; grid-template-columns: 1fr 1fr; border-bottom: 1px solid var(--line); padding: 0 22px; }
.mp-tab { font: 700 .72rem var(--sans); letter-spacing: .16em; text-transform: uppercase; color: var(--mist); background: none; border: 0; border-bottom: 2px solid transparent; padding: 12px 0; cursor: pointer; }
.mp-tab[aria-selected="true"] { color: var(--white); border-bottom-color: var(--red); }
.mp-tab b { display: inline-block; min-width: 20px; margin-left: 6px; padding: 1px 6px; border-radius: 999px; background: var(--red); color: #fff; font-size: .68rem; letter-spacing: 0; }
.mp-panel { flex: 1; min-height: 0; overflow-y: auto; padding: 16px 22px 28px; }
.mp-panel[hidden] { display: none; }
.mp-search { width: 100%; box-sizing: border-box; font: inherit; font-size: .92rem; color: var(--frost); background: var(--night-2); border: 1px solid var(--line); border-radius: 6px; padding: 10px 12px; margin-bottom: 12px; }
.mp-chips { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
.mp-chip { display: inline-flex; align-items: center; gap: 6px; font: 600 .66rem var(--sans); letter-spacing: .1em; text-transform: uppercase; color: var(--frost); background: none; border: 1px solid rgba(232,238,241,.28); border-radius: 999px; padding: 6px 10px; cursor: pointer; }
.mp-chip i { width: 8px; height: 8px; border-radius: 50%; }
.mp-chip[aria-pressed="true"] { background: var(--frost); color: var(--night); border-color: var(--frost); }
.mp-list { list-style: none; margin: 0; padding: 0; }
.mp-item { display: grid; grid-template-columns: 64px minmax(0, 1fr) auto; gap: 12px; align-items: center; padding: 8px; margin: 0 -8px; border-radius: 6px; cursor: pointer; }
.mp-item:hover, .mp-item.on { background: var(--night-2); }
.mp-item img { width: 64px; height: 48px; object-fit: cover; border-radius: 4px; display: block; }
.mp-item a { color: var(--white); font-weight: 700; font-size: .92rem; text-decoration: none; display: block; line-height: 1.25; }
.mp-item small { display: block; color: var(--glacier); font-size: .66rem; letter-spacing: .14em; text-transform: uppercase; font-weight: 700; margin-top: 3px; }
.mp-add { width: 32px; height: 32px; border-radius: 50%; border: 1px solid rgba(232,238,241,.35); background: none; color: var(--frost); font-size: 18px; line-height: 1; cursor: pointer; }
.mp-add[aria-pressed="true"] { background: var(--red); border-color: var(--red); color: #fff; }
.mp-empty { color: var(--mist); font-size: .92rem; }
.mp-trip { list-style: none; margin: 0; padding: 0; counter-reset: stop; }
.mp-stop { display: grid; grid-template-columns: 28px minmax(0, 1fr) auto; gap: 10px; align-items: center; padding: 10px 0; border-bottom: 1px solid var(--line); }
.mp-stop .n { width: 26px; height: 26px; border-radius: 50%; background: var(--red); color: #fff; display: grid; place-items: center; font-weight: 800; font-size: .78rem; }
.mp-stop strong { display: block; color: var(--white); font-size: .92rem; }
.mp-stop small { color: var(--mist); font-size: .74rem; }
.mp-stop .ctl { display: flex; gap: 4px; }
.mp-stop .ctl button { width: 28px; height: 28px; border-radius: 4px; border: 1px solid var(--line); background: none; color: var(--frost); cursor: pointer; font-size: 13px; }
.mp-leg { color: var(--mist); font-size: .72rem; padding: 4px 0 0 38px; }
.mp-total { margin: 16px 0 6px; font-size: .9rem; color: var(--frost); }
.mp-total span { color: var(--mist); font-size: .78rem; display: block; margin-top: 4px; }
.mp-actions { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
.mp-actions .btn { padding: 10px 14px; font-size: .68rem; font-family: var(--sans); cursor: pointer; }
.mp-actions button.btn.outline, .mp-card-btns button.btn.outline { background: transparent; color: var(--frost); border: 1px solid rgba(232,238,241,.45); }
.mp-mapwrap { position: relative; min-width: 0; }
.mp-map { position: absolute; inset: 0; background: #2f6fa6; }
.mp-card { position: absolute; z-index: 600; left: 18px; top: 18px; width: 320px; background: var(--night-2); border-radius: 8px; overflow: hidden; box-shadow: 0 24px 60px rgba(0,0,0,.55); }
.mp-card[hidden] { display: none; }
.mp-card img { display: block; width: 100%; height: 170px; object-fit: cover; }
.mp-card-body { padding: 14px 16px 16px; }
.mp-card-body small { color: var(--glacier); font-size: .64rem; letter-spacing: .18em; text-transform: uppercase; font-weight: 700; }
.mp-card-body h2 { font-family: var(--serif); font-size: 1.45rem; margin: 4px 0 6px; }
.mp-card-body p { color: var(--mist); font-size: .84rem; line-height: 1.5; margin: 0 0 12px; }
.mp-card-btns { display: flex; gap: 8px; flex-wrap: wrap; }
.mp-card-btns .btn { padding: 10px 14px; font-size: .68rem; }
.mp-card-btns .btn.on { background: var(--red); color: #fff; border-color: var(--red); }
.mp-x { position: absolute; top: 8px; right: 8px; width: 32px; height: 32px; border-radius: 50%; border: 0; background: rgba(10,17,22,.72); color: #fff; font-size: 20px; line-height: 1; cursor: pointer; }
.mp-toast { position: fixed; left: 50%; bottom: 24px; transform: translateX(-50%); z-index: 900; background: var(--frost); color: var(--night); font-weight: 700; font-size: .82rem; padding: 10px 16px; border-radius: 6px; box-shadow: 0 10px 30px rgba(0,0,0,.4); }
.mp-toast[hidden] { display: none; }
.mp-pin span { display: block; width: 20px; height: 20px; border-radius: 50%; background: var(--c); border: 3px solid #fff; box-shadow: 0 0 0 2px rgba(10,17,22,.55), 0 4px 10px rgba(0,0,0,.45); transition: transform .15s; }
.mp-pin:hover span, .mp-pin.on span { transform: scale(1.35); }
.mp-pin.on span { box-shadow: 0 0 0 5px rgba(217,72,59,.5), 0 4px 10px rgba(0,0,0,.45); }
.mp-pin.trip span { width: 26px; height: 26px; background: var(--red); color: #fff; display: grid; place-items: center; font: 800 .74rem var(--sans); }
.leaflet-tooltip.mp-tip { background: var(--night); color: var(--frost); border: 0; border-radius: 3px; font: 700 .78rem var(--sans); padding: 6px 10px; box-shadow: 0 6px 18px rgba(0,0,0,.4); }
.leaflet-tooltip.mp-tip::before { border-top-color: var(--night); }
.leaflet-control-zoom a { background: var(--night-2) !important; color: var(--frost) !important; border-color: var(--line) !important; }
.mp-seo { max-width: 900px; margin: 0 auto; padding: 64px 24px; color: var(--mist); }
.mp-seo h2 { font-family: var(--serif); color: var(--white); font-size: 1.8rem; }
@media (max-width: 860px) {
  .mp-app { height: auto; grid-template-columns: 1fr; }
  .mp-mapwrap { order: -1; height: 62svh; }
  .mp-side { border-right: 0; }
  .mp-panel { overflow: visible; }
  .mp-card { position: fixed; left: 0; right: 0; top: auto; bottom: 0; width: auto; border-radius: 12px 12px 0 0; display: grid; grid-template-columns: 38% 1fr; max-height: 46svh; }
  .mp-card[hidden] { display: none; }
  .mp-card img { height: 100%; min-height: 170px; }
  .mp-card-body { padding: 14px 14px 18px; overflow-y: auto; }
  .mp-card-body h2 { font-size: 1.2rem; padding-right: 30px; }
  .mp-card-body p { font-size: .8rem; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; }
}
"""


def main():
    cats = dict(CATEGORIES)
    items = sorted(all_places(), key=lambda p: p["name"])
    lis = "".join(
        f'<li class="mp-item" data-slug="{h["slug"]}"><img src="/assets/img/{h["img"]}-800.jpg" alt="" loading="lazy" decoding="async">'
        f'<div><a href="/places/{h["slug"]}">{html.escape(h["name"])}</a><small>{html.escape(h["region"])} · {html.escape(cats.get(h["cats"][0], ""))}</small></div>'
        f'<button type="button" class="mp-add" aria-pressed="false" aria-label="Add {html.escape(h["name"])} to my trip">+</button></li>'
        for h in items
    )
    title = "Interactive Map of Iceland: Explore the Highlights and Plan Your Trip"
    desc = ("Click around our interactive map of Iceland: waterfalls, glaciers, black beaches, canyons and hot springs. "
            "Preview each place and add it to your own trip.")
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": SITE + "/map", "description": desc,
          "about": [{"@type": "TouristAttraction", "name": h["name"], "url": f"{SITE}/places/{h['slug']}",
                     "geo": {"@type": "GeoCoordinates", "latitude": h["ll"][0], "longitude": h["ll"][1]}} for h in items]}
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)} · Discover Iceland</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}/map">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Discover Iceland">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE}/map">
<meta property="og:image" content="{SITE}/assets/img/map-highlights-1800.jpg">
{FONTS}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{STYLE}{CSS}</style>
</head>
<body class="mp-page">
{HEADER}
<main id="top">
  <div class="mp-app">
    <aside class="mp-side">
      <div class="mp-head">
        <p class="eyebrow">Interactive map</p>
        <h1>Plan your Iceland trip.</h1>
        <p>Tap a place to preview it. Add the ones you like to your trip and we draw the route.</p>
      </div>
      <div class="mp-tabs" role="tablist">
        <button type="button" class="mp-tab" role="tab" aria-selected="true" data-tab="places">Places</button>
        <button type="button" class="mp-tab" role="tab" aria-selected="false" data-tab="trip">My trip<b id="mpCount">0</b></button>
      </div>
      <div class="mp-panel" data-panel="places">
        <input class="mp-search" type="search" placeholder="Search places" aria-label="Search places">
        <div class="mp-chips"></div>
        <ul class="mp-list">{lis}</ul>
      </div>
      <div class="mp-panel" data-panel="trip" hidden>
        <p class="mp-empty">Your trip is empty. Tap <strong>+</strong> next to a place, or <strong>Add to my trip</strong> on its preview.</p>
        <ol class="mp-trip"></ol>
        <p class="mp-total"></p>
        <div class="mp-actions" hidden>
          <button type="button" class="btn primary" data-act="share">Copy trip link</button>
          <a class="btn outline" href="/blog/iceland-ring-road-7-days">Ring Road in 7 days</a>
          <button type="button" class="btn outline" data-act="clear">Clear trip</button>
        </div>
      </div>
    </aside>
    <div class="mp-mapwrap">
      <div class="mp-map" id="mpMap"><img src="/assets/img/map-highlights-1800.jpg" alt="Map of Iceland with the main highlights marked" style="width:100%;height:100%;object-fit:contain"></div>
      <div class="mp-card" hidden></div>
    </div>
  </div>
  <section class="mp-seo">
    <h2>How to use the map</h2>
    <p>Every pin is a place with its own guide. Tap a pin or a name in the list to see a photo and a short description, then open the full guide for directions, the best time to go and practical tips. Add places to <strong>My trip</strong> to see them numbered on the map with a route line and rough distances between them. Distances are straight-line, so allow more on the road, and check <a href="https://umferdin.is/en" rel="noopener">road conditions</a> before each drive.</p>
    <p>Your trip is saved in this browser. Use <strong>Copy trip link</strong> to send it to someone, or to open it on another device. For ready-made routes, see the <a href="/blog/iceland-ring-road-guide">Ring Road guide</a> and the <a href="/journal">journal</a>.</p>
  </section>
  <div class="mp-toast" hidden></div>
</main>
{FOOTER}
<script>{SCRIPT}</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js" defer></script>
<script src="/js/trip-map.js?v=2" defer></script>
</body>
</html>
"""
    (ROOT / "map.html").write_text(page, encoding="utf8")
    print("map.html", len(items), "places")


if __name__ == "__main__":
    main()
