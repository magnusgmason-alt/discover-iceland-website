"""Build the Discover Iceland site into dist/.

Resizes the original photos in photos/ into dist/assets/img/ (800 px and
1800 px wide versions) and copies the page files. Cloudflare Pages runs:
    pip install pillow && python3 build.py
with build output directory: dist
"""
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
PHOTOS = ROOT / "photos"
DIST = ROOT / "dist"
IMG = DIST / "assets" / "img"

# Image slot used in index.html -> original photo in photos/
SLOTS = {
    "hero-vestrahorn": "fef618d7-image.jpg",
    "strip-maelifell": "b52705a6-image.jpg",
    "strip-braided-river": "750ddcac-image.jpg",
    "strip-studlagil": "f066c020-image.jpg",
    "strip-jokulsarlon": "d1daec0e-image.jpg",
    "editions-flag": "945438f5-image.jpg",
    "guide-seljalandsfoss-winter": "7cd62cb9-image.jpg",
    "fire-ice-river": "c875a826-image.jpg",
    "journal-aurora-lake": "581dc034-image.jpg",
    "journal-reykjavik": "b83d9893-image.jpg",
    "journal-ring-road": "e16ddbb6-image.jpg",
    "seasons-coast": "95ba1c86-image.jpg",
    "quiet-maelifell-snow": "26985221-image.jpg",
    "checklist-black-beach": "059be267-image.jpg",
    "guides-braided-river": "f1655396-image.jpg",
    "hl-gullfoss": "6c6db642-image.jpg",
    "hl-geysir": "ad4609b3-image.jpg",
    "hl-seljalandsfoss": "156976c6-image.jpg",
    "hl-reynisfjara": "6fe08f5e-image.jpg",
    "hl-solheimajokull": "e3538fb7-image.jpg",
    "hl-jokulsarlon": "50fff888-image.jpg",
    "hl-hengifoss": "f6649b39-image.jpg",
    "hl-crater-lake": "984d7c30-image.jpg",
    "hl-maelifell": "734b6fc9-image.jpg",
    "hl-reykjadalur": "bc8dfc46-image.jpg",
    "hl-northern-lights": "581dc034-image.jpg",
    "hl-kirkjufell": "7ff801e8-image.jpg",
}

# Book covers: add photos/cover-guide.jpg, cover-summer.jpg, cover-winter.jpg and
# cover-aurora.jpg (or .png) to replace the placeholders.
COVERS = {
    "cover-guide": "THE COMPLETE TRAVEL GUIDE",
    "cover-summer": "SUMMER EDITION",
    "cover-winter": "WINTER EDITION",
    "cover-aurora": "NORTHERN LIGHTS",
}

PAGE_FILES = ["index.html", "highlights.html", "robots.txt", "sitemap.xml"]
PAGE_DIRS = ["blog"]


def save_sizes(im, name, widths):
    im = im.convert("RGB")
    for w in widths:
        r = min(1, w / im.width)
        out = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
        out.save(IMG / f"{name}-{w}.jpg", quality=80, optimize=True, progressive=True)


def font(size):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def placeholder_cover(subtitle):
    im = Image.new("RGB", (900, 1350), (14, 19, 23))
    d = ImageDraw.Draw(im)
    d.rectangle([90, 560, 190, 570], fill=(200, 32, 47))
    d.text((90, 600), "DISCOVER", font=font(64), fill=(255, 255, 255))
    d.text((90, 680), "ICELAND", font=font(64), fill=(255, 255, 255))
    d.text((90, 790), subtitle, font=font(32), fill=(170, 180, 186))
    return im


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    IMG.mkdir(parents=True)

    import make_articles
    make_articles.main()
    import make_highlights
    make_highlights.main()
    from highlights_content import HIGHLIGHTS
    for h in HIGHLIGHTS:
        SLOTS["hx-" + h["slug"]] = h["photo"]

    for f in PAGE_FILES:
        shutil.copy(ROOT / f, DIST / f)
    for d in PAGE_DIRS:
        shutil.copytree(ROOT / d, DIST / d)

    for slot, photo in SLOTS.items():
        with Image.open(PHOTOS / photo) as im:
            save_sizes(im, slot, (800, 1800))
        print("photo", slot)

    for name, subtitle in COVERS.items():
        found = [p for p in (PHOTOS / f"{name}.jpg", PHOTOS / f"{name}.png") if p.exists()]
        if found:
            with Image.open(found[0]) as im:
                save_sizes(im, name, (500, 900))
            print("cover", name)
        else:
            save_sizes(placeholder_cover(subtitle), name, (500, 900))
            print("cover placeholder", name)


if __name__ == "__main__":
    main()
