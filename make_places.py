"""Generate one page per mapped place at places/<slug>.html (served at /places/<slug>).

Content comes from places_content.py; name, photo, region and coordinates from
highlights_content.py. build.py runs it.
"""
import html
import json
import math
import re
from pathlib import Path

from highlights_content import CATEGORIES
from places_all import all_places

ROOT = Path(__file__).parent
SITE = "https://discovericeland.co"
OUT = ROOT / "places"

index = (ROOT / "index.html").read_text(encoding="utf8")
STYLE = re.search(r"<style>(.*?)</style>", index, re.S).group(1)
FONTS = re.search(r'<link href="https://fonts.googleapis.com[^>]+>', index).group(0)
HEADER = re.search(r'<header class="site-header".*?</header>', index, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', index, re.S).group(0)
SCRIPT = re.search(r"<script>(.*?)</script>", index, re.S).group(1)
LEAFLET_CSS = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">'
LEAFLET_JS = ('<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js" defer></script>\n'
              '<script src="/js/iceland-map.js?v=4" defer></script>')


def sitewide(fragment):
    fragment = fragment.replace('href="#top"', 'href="/"')
    return re.sub(r'href="#([a-z-]+)"', r'href="/#\1"', fragment)


HEADER = sitewide(HEADER).replace('href="/highlights"', 'href="/highlights" aria-current="page"')
FOOTER = sitewide(FOOTER)
SCRIPT = SCRIPT.split("// Checklist sign-up")[0] + "\n})();"
LABELS = dict(CATEGORIES)

PAGE_CSS = """
.pl-maphero .bg { opacity: .78; filter: saturate(.85); object-position: 68% 42%; }
.pl-maphero .shade { background: linear-gradient(90deg, rgba(10,17,22,.92) 0%, rgba(10,17,22,.7) 38%, rgba(10,17,22,.1) 70%), linear-gradient(180deg, rgba(10,17,22,.5) 0%, rgba(10,17,22,0) 30%, rgba(10,17,22,.6) 80%, var(--night) 100%) !important; }

.pl-reads a { color: var(--glacier); text-underline-offset: 3px; }
/* Place pages */
.pl-hero { position: relative; min-height: 78svh; display: flex; align-items: flex-end; overflow: hidden; background: var(--night); color: var(--white); }
.pl-hero .bg { -webkit-mask-image: linear-gradient(180deg, #000 60%, transparent 100%); mask-image: linear-gradient(180deg, #000 60%, transparent 100%); }
.pl-hero .shade { background: linear-gradient(180deg, rgba(10, 17, 22, 0.55) 0%, rgba(10, 17, 22, 0.1) 40%, rgba(10, 17, 22, 0.6) 78%, var(--night) 100%); }
.pl-hero .container { position: relative; padding-top: calc(var(--header-h) + 60px); padding-bottom: 46px; }
.pl-hero h1 { font-family: var(--serif); font-weight: 700; font-size: clamp(2.8rem, 8vw, 6rem); letter-spacing: -0.01em; line-height: 0.98; }
.pl-hero .rule { display: block; width: 64px; height: 3px; background: var(--red); margin: 24px 0 16px; }
.pl-crumbs { font-size: 0.78rem; margin-bottom: 18px; opacity: 0.85; }
.pl-crumbs a { text-decoration: none; border-bottom: 1px solid rgba(255, 255, 255, 0.4); }
.pl-tags { display: flex; flex-wrap: wrap; gap: 8px; }
.pl-tags a { font-size: 0.64rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; padding: 6px 10px; border-radius: 2px; background: rgba(10, 17, 22, 0.55); backdrop-filter: blur(6px); text-decoration: none; }
.pl-body { display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: clamp(32px, 6vw, 80px); align-items: start; padding-top: clamp(50px, 7vw, 90px); padding-bottom: clamp(50px, 7vw, 90px); }
.pl-text p { color: rgba(232, 238, 241, 0.86); font-size: clamp(1.06rem, 1.4vw, 1.2rem); line-height: 1.75; }
.pl-text > p:first-child { font-size: clamp(1.18rem, 1.7vw, 1.38rem); color: var(--frost); }
.pl-text h2 { font-size: clamp(1.6rem, 3vw, 2.2rem); margin: 1.6em 0 0.6em; }
.pl-text ul { color: rgba(232, 238, 241, 0.86); font-size: 1.08rem; line-height: 1.75; padding-left: 1.2em; }
.pl-text li { margin-bottom: 6px; }
.pl-facts { position: sticky; top: calc(var(--header-h) + 24px); border: 1px solid var(--line); border-top: 3px solid var(--red); border-radius: var(--radius); padding: 24px 26px; background: rgba(255, 255, 255, 0.02); }
.pl-facts h2 { font-size: 0.74rem; letter-spacing: 0.24em; text-transform: uppercase; color: var(--glacier); font-family: var(--sans); margin-bottom: 14px; }
.pl-facts dl { margin: 0; }
.pl-facts dt { font-size: 0.66rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: var(--mist); margin-top: 14px; }
.pl-facts dd { margin: 4px 0 0; font-weight: 600; }
.pl-facts .btn { margin-top: 22px; width: 100%; text-align: center; }
.pl-map-sec { padding-bottom: clamp(60px, 8vw, 100px); }
.pl-map-sec h2 { font-size: clamp(1.6rem, 3vw, 2.2rem); }
.imap.imap-mini { aspect-ratio: 16 / 9; margin-top: 18px; }
.pl-near { padding-bottom: clamp(70px, 9vw, 120px); }
.pl-near .hx-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 28px; list-style: none; margin: 30px 0 0; padding: 0; }
.pl-near .hx a { text-decoration: none; color: inherit; }
.pl-near .hx-img { display: block; border-radius: var(--radius); overflow: hidden; aspect-ratio: 4 / 3; }
.pl-near .hx-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s; }
.pl-near .hx:hover .hx-img img { transform: scale(1.04); }
.pl-near .hx-region { display: block; margin-top: 14px; font-size: 0.66rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--glacier); }
.pl-near h3 { font-family: var(--serif); font-size: 1.4rem; margin: 6px 0 4px; }
.pl-near .km { color: var(--mist); font-size: 0.85rem; }
.pl-note { color: var(--mist); font-size: 0.85rem; border-top: 1px solid var(--line); padding-top: 18px; margin-top: 40px; }
@media (max-width: 900px) {
  .pl-body { grid-template-columns: 1fr; }
  .pl-facts { position: static; }
  .pl-near .hx-grid { grid-template-columns: 1fr; }
  .imap.imap-mini { aspect-ratio: 4 / 5; }
}
"""


def km(a, b):
    (la1, lo1), (la2, lo2) = a, b
    p = math.pi / 180
    h = math.sin((la2 - la1) * p / 2) ** 2 + math.cos(la1 * p) * math.cos(la2 * p) * math.sin((lo2 - lo1) * p / 2) ** 2
    return 12742 * math.asin(math.sqrt(h))


def main():
    OUT.mkdir(exist_ok=True)
    mapped = all_places()
    for h in mapped:
        p = h["content"]
        slug = h["slug"]
        url = f"{SITE}/places/{slug}"
        img = h["img"]
        near = sorted((x for x in mapped if x is not h), key=lambda x: km(h["ll"], x["ll"]))[:3]
        tags = "".join(f'<a href="/highlights#{c}">{html.escape(LABELS[c])}</a>' for c in h["cats"])
        intro = "".join(f"<p>{html.escape(t)}</p>" for t in p["intro"])
        tips = "".join(f"<li>{html.escape(t)}</li>" for t in p["tips"])
        facts = "".join(f"<dt>{html.escape(k)}</dt><dd>{html.escape(v)}</dd>" for k, v in p["facts"])
        near_html = "".join(
            f"""<li class="hx"><a href="/places/{n['slug']}"><span class="hx-img"><img src="/assets/img/{n['img']}-800.jpg" alt="{html.escape(n['alt'])}" loading="lazy" decoding="async"{' style="object-position: ' + n['pos'] + '"' if n.get('pos') else ''}></span>
            <span class="hx-region">{html.escape(n['region'])}</span><h3>{html.escape(n['name'])}</h3><span class="km">About {round(km(h['ll'], n['ll']))} km away, as the crow flies</span></a></li>"""
            for n in near
        )
        try:
            from make_articles import ARTICLES as ARTS
        except Exception:
            ARTS = []
        reads = [a for a in ARTS if f'/places/{slug}"' in a["body"]]
        reads.sort(key=lambda a: (not a.get("pillar"), a["body"].count(f"/places/{slug}") * -1))
        reads_html = ""
        if reads:
            items = "".join(f'<li><a href="/blog/{a["slug"]}">{html.escape(a["short"])}</a></li>' for a in reads[:5])
            reads_html = f'<h2>Read more in the journal</h2><ul class="pl-reads">{items}</ul>'
        srcs = p.get("sources") or []
        if srcs:
            reads_html += '<p class="pl-note">Sources: ' + ", ".join(f'<a href="{html.escape(u)}" rel="noopener">{html.escape(t)}</a>' for t, u in srcs) + ". Facts checked October 2026.</p>"
        title = f"{h['name']}, Iceland: How to Visit, When to Go and Tips"
        desc = f"{h['text']} How to get to {h['name']}, the best time to visit and practical tips."
        ld = [
            {"@context": "https://schema.org", "@type": "TouristAttraction", "name": h["name"], "description": h["text"],
             "url": url, "image": f"{SITE}/assets/img/{img}-1800.jpg",
             "geo": {"@type": "GeoCoordinates", "latitude": h["ll"][0], "longitude": h["ll"][1]},
             "containedInPlace": {"@type": "Country", "name": "Iceland"}},
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Discover Iceland", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Highlights", "item": SITE + "/highlights"},
                {"@type": "ListItem", "position": 3, "name": h["name"], "item": url}]},
        ]
        pos = f' style="object-position: {h["pos"]}"' if h.get("pos") else ""
        page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)} · Discover Iceland</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Discover Iceland">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/{img}-1800.jpg">
<meta name="twitter:card" content="summary_large_image">
{FONTS}
{LEAFLET_CSS}
{''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)}
<style>{STYLE}{PAGE_CSS}</style>
</head>
<body>
{HEADER}
<main id="top">
  <section class="pl-hero{' pl-maphero' if h.get('maphero') else ''}">
    <img class="bg" src="/assets/img/{img}-1800.jpg" srcset="/assets/img/{img}-800.jpg 800w, /assets/img/{img}-1800.jpg 1800w" sizes="100vw" alt="{html.escape(h['alt'])}"{pos} fetchpriority="high">
    <div class="shade"></div>
    <div class="container">
      <p class="pl-crumbs"><a href="/">Discover Iceland</a> / <a href="/highlights">Highlights</a> / {html.escape(h['name'])}</p>
      <p class="eyebrow light">{html.escape(h['region'])}</p>
      <h1>{html.escape(h['name'])}</h1>
      <span class="rule"></span>
      <div class="pl-tags">{tags}</div>
    </div>
  </section>

  <div class="container pl-body">
    <article class="pl-text">
      {intro}
      <h2>Getting there</h2>
      <p>{html.escape(p['getting'])}</p>
      <h2>When to go</h2>
      <p>{html.escape(p['when'])}</p>
      <h2>Good to know</h2>
      <ul>{tips}</ul>
      {reads_html}
      <p class="pl-note">Drive times are approximate and depend on weather and road conditions. Check road.is and vedur.is before you set off.</p>
    </article>
    <aside class="pl-facts">
      <h2>At a glance</h2>
      <dl>{facts}</dl>
      <a class="btn outline" href="#map">See it on the map</a>
    </aside>
  </div>

  <section class="container pl-map-sec" id="map">
    <p class="eyebrow">On the map</p>
    <h2>Where {html.escape(h['name'])} is.</h2>
    <div class="imap imap-mini" data-map data-focus="{slug}" data-nochips><img class="imap-fallback" src="/assets/img/map-highlights-1800.jpg" alt="Map of Iceland with the main highlights marked" loading="lazy"></div>
  </section>

  <section class="container pl-near">
    <p class="eyebrow">Nearby</p>
    <h2>Also close by.</h2>
    <ul class="hx-grid">{near_html}</ul>
    <div class="btn-row"><a class="btn outline" href="/highlights">All highlights</a><a class="btn outline" href="/#guides">The guides</a></div>
  </section>
</main>
{FOOTER}
<script>{SCRIPT}</script>
{LEAFLET_JS}
</body>
</html>
"""
        (OUT / f"{slug}.html").write_text(page, encoding="utf8")
    print("places", len(mapped))
    return [h["slug"] for h in mapped]


if __name__ == "__main__":
    main()
