"""Generate 404.html. Cloudflare Pages serves it with a real 404 status for any missing
URL (without it, missing URLs fall back to the homepage with status 200).
build.py runs it after make_plan, reusing that page's header, footer and styles."""
import html
from pathlib import Path

import make_plan as mp

ROOT = Path(__file__).parent

CSS = """
.nf { position: relative; min-height: 100svh; display: flex; align-items: center; overflow: hidden; background: var(--night); }
.nf .bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: .35; -webkit-mask-image: linear-gradient(180deg, #000 50%, transparent 100%); mask-image: linear-gradient(180deg, #000 50%, transparent 100%); }
.nf .container { position: relative; padding-top: calc(var(--header-h) + 60px); padding-bottom: 80px; }
.nf h1 { font-family: var(--serif); font-size: clamp(2.6rem, 7vw, 5rem); line-height: 1; margin: 8px 0 16px; max-width: 14ch; }
.nf .lead { color: var(--frost); max-width: 46ch; }
.nf-links { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 30px; }
"""

LINKS = [
    ("/", "Home", "primary"),
    ("/journal", "Journal", "ghost"),
    ("/map", "Trip map", "ghost"),
    ("/highlights", "Highlights", "ghost"),
    ("/plan-your-trip", "Plan your trip", "ghost"),
]


def main():
    links = "\n        ".join(f'<a class="btn {c}" href="{u}">{html.escape(t)}</a>' for u, t, c in LINKS)
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Page not found · Discover Iceland</title>
<meta name="robots" content="noindex">
{mp.FONTS}
<style>{mp.STYLE}{CSS}</style>
</head>
<body>
{mp.HEADER}
<main id="top">
  <section class="nf">
    <img class="bg" src="/assets/img/hero-stokksnes-wide-1800.jpg" alt="">
    <div class="container">
      <p class="eyebrow">404</p>
      <h1>This road is closed.</h1>
      <p class="lead">The page you were looking for does not exist or has moved. Try one of these instead.</p>
      <div class="nf-links">
        {links}
      </div>
    </div>
  </section>
</main>
{mp.FOOTER}
<script>{mp.SCRIPT}</script>
</body>
</html>
"""
    (ROOT / "404.html").write_text(page, encoding="utf8")
    print("404.html")


if __name__ == "__main__":
    main()
