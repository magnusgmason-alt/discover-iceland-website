"""Sanity checks for journal articles: fields, links, images, maps."""
import re
import sys

import build
from highlights_content import HIGHLIGHTS
from places_content import PLACES
import make_articles

slots = set(build.SLOTS) | {"hx-" + h["slug"] for h in HIGHLIGHTS}
arts = make_articles.ARTICLES
slugs = {a["slug"] for a in arts}
ok = True


def bad(a, msg):
    global ok
    ok = False
    print(f"  {a['slug']}: {msg}")


only = set(sys.argv[1:])
for a in arts:
    if only and a["cluster"] not in only:
        continue
    for k in ("slug", "cluster", "short", "title", "description", "category", "teaser", "image", "image_alt", "stats", "body", "checked_note", "sources"):
        if not a.get(k):
            bad(a, f"missing {k}")
    if a["image"] not in slots:
        bad(a, f"unknown image {a['image']}")
    b = a["body"]
    if b.count("<!--TOC-->") != 1:
        bad(a, "TOC marker count")
    for s in re.findall(r"/assets/img/([a-z0-9-]+?)-(?:800|1800|2800)\.jpg", b):
        if s not in slots:
            bad(a, f"unknown img slot {s}")
    if "a-map" not in b and a["cluster"] != "planning":
        bad(a, "no map")
    for s in re.findall(r'href="/places/([a-z0-9-]+)"', b):
        if s not in PLACES:
            bad(a, f"bad place link {s}")
    for s in re.findall(r'href="/blog/([a-z0-9-]+)"', b):
        if s not in slugs:
            print(f"  (pending) {a['slug']} -> /blog/{s}")
    for s in re.findall(r'href="(/[^"#]*)', b):
        if not re.match(r"^/(places|blog|assets)/|^/(highlights|northern-lights|journal)?$", s):
            bad(a, f"odd link {s}")
    words = len(re.sub(r"<[^>]+>", " ", b).split())
    print(f"{a['cluster']:14} {a['slug']:40} {words:5}w  title {len(a['title'])}  desc {len(a['description'])}")
print("OK" if ok else "PROBLEMS")
