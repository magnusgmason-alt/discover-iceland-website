"""One list of every place that has its own page (/places/<slug>) and a pin on the maps.

- Highlights with coordinates and an entry in places_content.PLACES (our own photo).
- Extra places from places_extra_a/b.EXTRA. Until we have a photo of them, their
  header image is a crop of our branded highlights map centred on the place.
Highlight cards that are only a variation of a place (a season, a detail) point
to that place's page through PARENT.
"""
import importlib
import math

from highlights_content import HIGHLIGHTS
from places_content import PLACES

# Extra-place photos we have (slug -> file in photos/). Add one here to replace the map crop.
EXTRA_PHOTOS = {}

# Highlight card -> page it belongs to.
PARENT = {
    "jokulsarlon-winter": "/places/jokulsarlon",
    "blue-icebergs": "/places/jokulsarlon",
    "black-ice": "/places/jokulsarlon",
    "glacier-kayaking": "/places/fjallsarlon",
    "crevasses": "/places/vatnajokull",
    "frozen-lagoon": "/places/fjallsarlon",
    "seljalandsfoss-winter": "/places/seljalandsfoss",
    "black-beaches": "/places/reynisfjara",
    "stokksnes-shore": "/places/stokksnes",
    "vestrahorn-mist": "/places/vestrahorn",
    "braided-rivers": "/places/maelifell",
    "highland-rivers": "/places/landmannalaugar",
    "northern-lights": "/northern-lights",
    "aurora-fjord": "/northern-lights",
    "aurora-countryside": "/northern-lights",
    "aurora-winter": "/northern-lights",
}


def _extras():
    out = {}
    for mod in ("places_extra_a", "places_extra_b"):
        try:
            out.update(importlib.import_module(mod).EXTRA)
        except ModuleNotFoundError:
            pass
    return out


EXTRA = _extras()


def all_places():
    items = []
    for h in HIGHLIGHTS:
        if h.get("ll") and h["slug"] in PLACES:
            items.append({
                "slug": h["slug"], "name": h["name"], "region": h["region"], "cats": h["cats"], "ll": h["ll"],
                "alt": h["alt"], "text": h["text"], "pos": h.get("pos"), "img": "hx-" + h["slug"],
                "content": PLACES[h["slug"]], "maphero": False,
            })
    have = {i["slug"] for i in items}
    for slug, e in EXTRA.items():
        if slug in have:
            continue
        photo = EXTRA_PHOTOS.get(slug)
        items.append({
            "slug": slug, "name": e["name"], "region": e["region"], "cats": e["cats"], "ll": e["ll"],
            "alt": f"Discover Iceland map showing where {e['name']} is" if not photo else e.get("photo_alt", e["name"]),
            "text": e["text"], "pos": None, "img": ("px-" if photo else "pl-") + slug,
            "content": e, "maphero": not photo,
        })
    return items


def parent_url(slug):
    if slug in PARENT:
        url = PARENT[slug]
        if url.startswith("/places/") and url[8:] not in {p["slug"] for p in all_places()}:
            return None
        return url
    return None


# Pixel position on the 3000 px branded maps (Web Mercator fit from 15 towns, rms ~1 px).
def map_px(lat, lon):
    x = 254.0247 * lon + 6313.1704
    m = math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))
    y = -14561.4507 * m + 23024.9191
    return x, y


def map_crop(img, lat, lon, w=1150, h=650):
    """Crop of the branded map centred on a place, with a soft red ring on it."""
    from PIL import ImageDraw
    x, y = map_px(lat, lon)
    # the place sits right of centre, so the page title on the left covers open map, not the pin
    left = int(min(max(x - w * 0.68, 0), img.width - w))
    top = int(min(max(y - h * 0.42, 0), img.height - h))
    crop = img.convert("RGB").crop((left, top, left + w, top + h))
    d = ImageDraw.Draw(crop)
    cx, cy = x - left, y - top
    for r, a in ((46, 5), (60, 2)):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(217, 72, 59), width=a)
    return crop.resize((1800, round(1800 * h / w)))
