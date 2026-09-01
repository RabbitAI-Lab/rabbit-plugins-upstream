# -*- coding: utf-8 -*-
"""Render front+back ENGLISH flashcard PNGs.
Front = pastel rounded card: emoji/illustration (top ~35%) + big WORD (bottom).
Back  = white rounded card: big WORD only (for recall / tracing).
Aspect W:H == on-page cell aspect (95:135 ≈ 1150:1634) => no distortion.
No pinyin for English. Big word auto-fits so long words never clip.
"""
import os, sys, json, shutil
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from words100 import WORDS

FONT = os.environ.get("EN_FONT", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
if not os.path.exists(FONT):
    FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def F(sz):
    sz = max(8, int(sz))
    try: return ImageFont.truetype(FONT, sz)
    except Exception: return ImageFont.load_default(sz)

W, H, SS = 1150, 1634, 2
WORD_COLOR = "#20242B"
PALETTE = [
    ("#FFF6DB","#E08A12","#F0A93C"),("#E9EEFF","#3B52A6","#7C8CD6"),
    ("#DCF3FA","#1565C0","#5BB8E8"),("#D8ECFF","#1B6FB0","#69A9DB"),
    ("#FDE9E9","#C0392B","#E08A86"),("#EAF7E3","#3B7A2B","#8CCB78"),
    ("#FFF1E0","#C86A1E","#EBA76C"),
]
EMOJI = os.environ.get("EMOJI_OUT", os.path.join(HERE, "emoji"))
EMOJI_MAP = json.load(open(os.path.join(EMOJI, "_final.json")))
FR_DIR = os.path.join(HERE, "all_front"); BK_DIR = os.path.join(HERE, "all_back")
os.makedirs(FR_DIR, exist_ok=True); os.makedirs(BK_DIR, exist_ok=True)

def ctext(d, cx, cy, s, font, fill):
    b = d.textbbox((0, 0), s, font=font); w, h = b[2]-b[0], b[3]-b[1]
    d.text((cx - w/2 - b[0], cy - h/2 - b[1]), s, font=font, fill=fill)

def frame(d, bg, border, bw):
    pd, rp = int(58*SS), int(46*SS)
    d.rounded_rectangle([pd, pd, W*SS-pd, H*SS-pd], radius=rp, fill=bg, outline=border, width=int(bw*SS))

_cache = {}
def get_image(word):
    if word in _cache: return _cache[word]
    p = f"{EMOJI}/{EMOJI_MAP[word]}.png"
    img = Image.open(p).convert("RGBA")
    _cache[word] = img; return img

def fit_font(word, max_w, start_sz, min_sz):
    """Shrink font until the word fits within max_w pixels (min floor)."""
    sz = start_sz
    probe = ImageDraw.Draw(Image.new("RGB", (8,8)))
    while sz > min_sz:
        f = F(sz)
        b = probe.textbbox((0,0), word, font=f)
        if (b[2]-b[0]) <= max_w: return f
        sz -= 8
    return F(min_sz)

def make_front(word, idx, path):
    bg, pin, border = PALETTE[idx % len(PALETTE)]
    img = Image.new("RGBA", (W*SS, H*SS), (0,0,0,0)); d = ImageDraw.Draw(img)
    frame(d, bg, border, 12)
    src = get_image(word)
    ew, eh = src.size
    sc = min((W*SS*0.46)/ew, (H*SS*0.40)/eh)
    nw, nh = int(ew*sc), int(eh*sc)
    esrc = src.resize((nw, nh), Image.LANCZOS)
    img.paste(esrc, (int(W*SS/2 - nw/2), int(H*SS*0.33 - nh/2)), esrc)
    f = fit_font(word, int(W*SS*0.72), int(W*SS*0.24), int(W*SS*0.10))
    ctext(d, W*SS/2, int(H*SS*0.66), word, f, "#16191F")
    img.resize((W, H), Image.LANCZOS).convert("RGB").save(path)

def make_back(word, path):
    img = Image.new("RGBA", (W*SS, H*SS), (0,0,0,0)); d = ImageDraw.Draw(img)
    frame(d, "#FFFFFF", "#D7DDE6", 4)
    f = fit_font(word, int(W*SS*0.80), int(W*SS*0.34), int(W*SS*0.14))
    ctext(d, W*SS/2, int(H*SS*0.50), word, f, "#16191F")
    img.resize((W, H), Image.LANCZOS).convert("RGB").save(path)

for i, (word, _py, em) in enumerate(WORDS):
    s = f"c{i:03d}_{word}"
    make_front(word, i, os.path.join(FR_DIR, s + ".png"))
    make_back(word, os.path.join(BK_DIR, s + ".png"))
print("generated", len(WORDS), "front + back cards ->", FR_DIR, "/", BK_DIR)
