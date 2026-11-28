"""Detail words, movement words and color words, and the views that confirm them."""

import os
import re

# ----------------------------------------------------------------------------- confirmation of details
# Statements about a person's clothing, footwear, jewelry, hands and marks, a product, what an object
# rests on or holds, and the place are the ones that drift between runs when written from small sheet
# cells. Each is written once, wrapped as {words|VIEW}: VIEW names the large view it was checked on (a
# `zoom` image or a shot frame, optionally @T for one moment of a several-moment zoom), or `?` when no
# view confirmed it (it then goes out tagged uncertain). `build` refuses to write the analysis while a
# sentence holds a detail word outside such a mark, or a mark names a view that does not exist, is not
# large, or does not show a moment inside the stretch the statement describes.
DETAIL_WORDS = (
    # clothing and footwear
    "shirt",
    "t-shirt",
    "tee",
    "tank top",
    "crop top",
    "blouse",
    "hoodie",
    "sweater",
    "sweatshirt",
    "jumper",
    "cardigan",
    "jacket",
    "coat",
    "blazer",
    "vest",
    "dress",
    "skirt",
    "jeans",
    "denim",
    "trousers",
    "pants",
    "shorts",
    "leggings",
    "joggers",
    "suit",
    "uniform",
    "apron",
    "overalls",
    "sleeve",
    "collar",
    "hood",
    "sneaker",
    "shoe",
    "boot",
    "heel",
    "sandal",
    "slipper",
    "clog",
    "loafer",
    "sock",
    "hat",
    "cap",
    "beanie",
    "bandana",
    "headband",
    "scarf",
    "glove",
    "belt",
    "bag",
    "handbag",
    "purse",
    "tote",
    "backpack",
    "glasses",
    "sunglasses",
    "outfit",
    # jewelry, hair accessories, marks
    "bracelet",
    "bangle",
    "ring",
    "necklace",
    "chain",
    "pendant",
    "earring",
    "hoop",
    "stud",
    "wristwatch",
    "anklet",
    "piercing",
    "hair clip",
    "hairclip",
    "scrunchie",
    "hairband",
    "hair bow",
    "tattoo",
    "scar",
    "nail",
    "manicure",
    "lipstick",
    "makeup",
    "lanyard",
    "badge",
    # hands and what is held or rests on something
    "left hand",
    "right hand",
    "both hands",
    "grips",
    "gripping",
    "rests on",
    "resting on",
    "placed on",
    "propped",
    # products and props
    "product",
    "bottle",
    "jar",
    "tube",
    "packet",
    "package",
    "packaging",
    "pouch",
    "sachet",
    "carton",
    "cup",
    "mug",
    "tumbler",
    "phone",
    "laptop",
    "tablet",
    "microphone",
    "mic",
    # support surfaces and the place
    "table",
    "desk",
    "counter",
    "countertop",
    "worktop",
    "shelf",
    "ledge",
    "windowsill",
    "bench",
    "nightstand",
    "dresser",
    "tray",
    "plate",
    "bed",
    "sofa",
    "couch",
    "chair",
    "stool",
    "floor",
    "rug",
    "carpet",
    "cushion",
    "pillow",
    "room",
    "kitchen",
    "bedroom",
    "bathroom",
    "office",
    "studio",
    "street",
    "sidewalk",
    "pavement",
    "park",
    "store",
    "shop",
    "car",
    "gym",
    "cafe",
    "café",
    "restaurant",
    "wall",
    "window",
    "door",
    "doorway",
    "mirror",
    "curtain",
    "blinds",
    "plant",
    "tree",
    "lamp",
)
_DETAIL_RE = re.compile(
    r"(?<![\w-])("
    + "|".join(sorted((re.escape(w) for w in DETAIL_WORDS), key=len, reverse=True))
    + r")(?:s|es)?(?![\w-])",
    re.I,
)
# "hold" is a detail only when a thing is held: "holds a mug", "holding it up"; "the top pane holds"
# and "the shot holds still" say nothing about hands, nor does holding something abstract ("holds that
# gaze", "holds the pose", "holds the viewer's attention", "holds a note")
HOLD_ABSTRACT = (
    "gaze",
    "stare",
    "look",
    "glance",
    "eye contact",
    "eyeline",
    "pose",
    "position",
    "posture",
    "stance",
    "expression",
    "smile",
    "grin",
    "frown",
    "attention",
    "focus",
    "interest",
    "note",
    "breath",
    "silence",
    "pause",
    "beat",
    "moment",
    "shot",
    "frame",
    "view",
    "tension",
    "gesture",
)
_HOLD_RE = re.compile(
    r"(?<![\w-])(hold(?:s|ing)?|held)\s+(?:a|an|the|her|his|their|its|my|your|it|them|one|two|"
    r"three|both|each|up|out|onto|some|this|that|these|those)(?![\w-])"
    r"(?!\s+(?:[\w-]+(?:'s|’s)\s+)?(?:" + "|".join(HOLD_ABSTRACT) + r")s?(?![\w-]))",
    re.I,
)


def detail_hits(text):
    """The detail words in a piece of text, ordinary phrases taken out first (sorted, lower case)."""
    t = NOT_DETAIL_RE.sub(" ", text)
    return sorted(
        {m.group(1).lower() for m in _DETAIL_RE.finditer(t)} | {m.group(1).lower() for m in _HOLD_RE.finditer(t)}
    )


# ordinary phrases that hold a detail word but state nothing about a person, product, support or place:
# taken out before the detail words are looked for (a sound "bed", the quality of light, room tone)
NOT_DETAIL_RE = re.compile(
    r"(?<![\w-])(?:(?:music|sound|audio|background|continuous|ambient)\s+bed|"
    r"window[\s-]light|ring[\s-]light|room\s+(?:tone|sound)|(?:app|play)\s+store)s?(?![\w-])",
    re.I,
)
# movements a single still cannot show: written only from a `frames` view over the moment
MOTION_RE = re.compile(
    r"(?<![\w-])(?:nod(?:s|ded|ding)?|shrug(?:s|ged|ging)?|wink(?:s|ed|ing)?|"
    r"head\s+(?:tilt|shake|turn)s?|(?:tilt|shake|shook|turn)(?:s|ed|ing)?\s+(?:her|his|their|the)\s+head)"
    r"(?![\w-])",
    re.I,
)
_MARK_RE = re.compile(r"\{([^{}|]+)\|([^{}]*)\}")
CLOTHING_WORDS = DETAIL_WORDS[: DETAIL_WORDS.index("bracelet")]
PRODUCT_WORDS = DETAIL_WORDS[DETAIL_WORDS.index("product") : DETAIL_WORDS.index("table")]
# things that keep one color through a video: a garment, a product or prop
_CLOTHING_RE = re.compile(
    r"(?<![\w-])("
    + "|".join(sorted((re.escape(w) for w in CLOTHING_WORDS + PRODUCT_WORDS), key=len, reverse=True))
    + r")(?:s|es)?(?![\w-])",
    re.I,
)
COLOR_WORDS = (
    "red",
    "orange",
    "yellow",
    "green",
    "teal",
    "blue",
    "navy",
    "purple",
    "violet",
    "pink",
    "magenta",
    "brown",
    "tan",
    "beige",
    "cream",
    "ivory",
    "oatmeal",
    "camel",
    "khaki",
    "olive",
    "white",
    "black",
    "gray",
    "grey",  # read as gray: a judgment may spell it either way
    "charcoal",
    "silver",
    "gold",
    "rust",
    "burgundy",
    "maroon",
    "mustard",
    "lilac",
    "lavender",
    "mint",
    "coral",
    "peach",
    "taupe",
    "ecru",
    "sand",
    "off-white",
)


def color_names_by_garment(texts):
    """{garment: {color words: [where, ...]}} from the words before each garment word (same clause).
    One garment named with different color words in different places reads as several garments."""
    out = {}
    for where, text in texts:
        plain = _MARK_RE.sub(lambda m: m.group(1), text or "")
        for m in _CLOTHING_RE.finditer(plain):
            before = re.split(r"[.;,:()]|\band\b|\bwith\b", plain[max(0, m.start() - 60) : m.start()])[-1]
            cols = tuple(
                sorted(
                    {("gray" if w == "grey" else w) for w in re.findall(r"[a-z-]+", before.lower()) if w in COLOR_WORDS}
                )
            )
            if cols:
                out.setdefault(m.group(1).lower(), {}).setdefault(cols, []).append(where)
    return out


# a written color word against the plain names `color` prints. Coarse on purpose: light, shade and
# compression move a measured color a long way, so only a written color that no measured color could
# be is a mismatch (a blue sweater measured red), never a near one (cream measured beige or light gray)
_LIGHT_NEUTRAL = {"white", "gray", "beige", "yellow", "orange", "brown", "pink"}
COLOR_FITS = {
    "white": _LIGHT_NEUTRAL | {"blue"},
    "gray": {"gray", "white", "black", "beige", "blue", "teal", "brown"},
    "silver": {"gray", "white", "black", "beige", "blue", "teal"},
    "charcoal": {"black", "gray", "brown", "blue", "purple"},
    "black": {"black", "gray", "brown", "blue", "purple"},
    "cream": _LIGHT_NEUTRAL,
    "ivory": _LIGHT_NEUTRAL,
    "oatmeal": _LIGHT_NEUTRAL,
    "beige": _LIGHT_NEUTRAL,
    "ecru": _LIGHT_NEUTRAL,
    "sand": _LIGHT_NEUTRAL,
    "taupe": _LIGHT_NEUTRAL,
    "khaki": _LIGHT_NEUTRAL | {"green"},
    "camel": _LIGHT_NEUTRAL | {"red"},
    "tan": _LIGHT_NEUTRAL | {"red"},
    "brown": {"brown", "orange", "red", "beige", "yellow", "black"},
    "red": {"red", "pink-red", "pink", "magenta-pink", "brown", "orange"},
    "burgundy": {"red", "pink-red", "magenta-pink", "brown", "purple", "black"},
    "maroon": {"red", "pink-red", "magenta-pink", "brown", "purple", "black"},
    "rust": {"orange", "red", "brown", "pink-red"},
    "coral": {"orange", "red", "pink", "pink-red", "beige"},
    "peach": {"orange", "pink", "beige", "pink-red", "yellow"},
    "orange": {"orange", "red", "brown", "yellow", "beige"},
    "mustard": {"yellow", "orange", "brown", "beige", "green"},
    "gold": {"yellow", "orange", "brown", "beige", "green"},
    "yellow": {"yellow", "orange", "beige", "green", "brown"},
    "olive": {"green", "yellow", "brown"},
    "green": {"green", "teal", "yellow"},
    "mint": {"green", "teal", "white"},
    "teal": {"teal", "green", "blue"},
    "blue": {"blue", "teal", "purple"},
    "navy": {"blue", "teal", "purple", "black"},
    "purple": {"purple", "blue", "magenta-pink", "pink"},
    "violet": {"purple", "blue", "magenta-pink", "pink"},
    "lilac": {"purple", "blue", "magenta-pink", "pink", "white"},
    "lavender": {"purple", "blue", "magenta-pink", "pink", "white"},
    "pink": {"pink", "magenta-pink", "pink-red", "red", "purple", "beige", "orange"},
    "magenta": {"magenta-pink", "pink", "pink-red", "purple", "red"},
}


METAL_COLORS = {"gold", "silver"}


def measured_families(name):
    """The base colors a plain name from `color` stands for ("dark grayish blue" -> blue, gray, black)."""
    fam = set()
    base = name
    for pre, extra in (("dark ", "black"), ("light ", "white"), ("grayish ", "gray")):
        if base.startswith(pre):
            fam.add(extra)
            base = base[len(pre) :]
    fam.add("gray" if base.endswith("gray") else base)
    return fam


def written_colors(text):
    """Color words in a statement ("mint-green" gives mint and green; grey is gray)."""
    words = (("gray" if w == "grey" else w) for w in re.findall(r"[a-z]+", text.lower()))
    return sorted({w for w in words if w in COLOR_FITS})


CONFIRM_MIN_SIDE = 480  # a confirming view shows the moment with a long side of at least this many px


def view_name(path):
    """A view's name: its file name without a trailing `.jpg`. Not os.path.splitext: the name carries times
    and boxes (`zoom_3.80_30-70-60-100`), so its last dot is not an extension."""
    name = os.path.basename(path.strip())
    return name[:-4] if name.lower().endswith(".jpg") else name


def confirm_views(idx, pts):
    """Large views this scan folder holds: zoom images (per moment) and shot frames."""
    views = {}
    for f in idx.get("followups", []):
        if f.get("cmd") != "zoom":
            continue
        cell = f.get("cell")
        times = f.get("times") or [pts[i] for i in f.get("frames", []) if 0 <= i < len(pts)]
        for im in f.get("images", []):  # a page shows only its own moments (older scans: all of them)
            views[view_name(im["path"])] = {
                "image": im["path"],
                "times": im.get("times") or times,
                "box": f.get("box"),
                "long_side": max(cell) if cell else None,
            }
    for sh in idx.get("shots", []):
        if sh.get("image"):
            views[view_name(sh["image"])] = {
                "image": sh["image"],
                "times": [sh["rep_t"]],
                "box": None,
                "long_side": None,
            }
    for f in idx.get("followups", []):  # every frame of a window: the only view that shows a movement
        if f.get("cmd") == "frames" and f.get("window"):
            for im in f.get("images", []):
                views[view_name(im["path"])] = {
                    "image": im["path"],
                    "span": [round(x, 3) for x in f["window"]],
                    "box": f.get("box"),
                    "frames": True,
                }
    return views


def check_details(text, window, where, views, problems, confirmed, uncertain):
    """Check one piece of judgment text; return it with the marks taken out."""
    plain = []
    pos = 0
    for m in _MARK_RE.finditer(text):
        plain.append(text[pos : m.start()])
        pos = m.end()
        words, ref = m.group(1).strip(), m.group(2).strip()
        plain.append(words)
        if ref == "?":
            uncertain.append(f"not confirmed on a large view: {words}")
            continue
        at = None
        if "@" in ref:
            ref, _, at_s = ref.partition("@")
            try:
                at = float(at_s)
            except ValueError:
                problems.append(f"UNCONFIRMED {where}: '{words}': '@{at_s}' is not a time")
                continue
        if len(words.split()) > 40:
            problems.append(
                f"UNCONFIRMED {where}: a mark of {len(words.split())} words ('{words[:40]}…'): wrap each "
                f"statement on its own, with the view that shows it"
            )
            continue
        v = views.get(view_name(ref))
        moves = bool(MOTION_RE.search(words))
        if not v:
            problems.append(
                f"UNCONFIRMED {where}: '{words}': no view '{ref}' in this scan folder (a `zoom` image "
                f"or shots/shot_NN; for a movement, a `frames` sheet; overview sheets are not views)"
            )
            continue
        if v.get("frames"):
            # a frames sheet shows how something moves, in small cells: it confirms any movement, never a
            # detail (clothing, what is held, the place)
            hit = detail_hits(words)
            if hit:
                problems.append(
                    f"UNCONFIRMED {where}: '{words}': {v['image']} is a `frames` sheet, whose cells are "
                    f"too small for {', '.join(hit)}; confirm that on a `zoom` image or shot frame "
                    f"(wrap the movement and the detail separately)"
                )
                continue
            a_, b_ = v["span"]
            if b_ < window[0] - 0.05 or a_ > window[1] + 0.05:
                problems.append(
                    f"UNCONFIRMED {where}: '{words}': {v['image']} shows {a_:.2f}-{b_:.2f} s, outside "
                    f"{window[0]:.2f}-{window[1]:.2f} s"
                )
                continue
            confirmed.append(
                {"where": where, "words": words, "view": v["image"], "t": round(max(a_, window[0]), 3), "box": v["box"]}
            )
            continue
        if moves:
            problems.append(
                f"UNCONFIRMED {where}: '{words}': a single still ({v['image']}) cannot show a movement; "
                f"run `frames` over the moment and name that sheet, or write only what the still shows"
            )
            continue
        if v["long_side"] is not None and v["long_side"] < CONFIRM_MIN_SIDE:
            problems.append(
                f"UNCONFIRMED {where}: '{words}': {v['image']} shows each moment at {v['long_side']} px "
                f"(needs {CONFIRM_MIN_SIDE}); zoom fewer moments or a box"
            )
            continue
        ts = [t for t in v["times"] if (at is None or abs(t - at) <= 0.05)]
        inside = [t for t in ts if window[0] - 0.05 <= t <= window[1] + 0.05]
        if not inside:
            problems.append(
                f"UNCONFIRMED {where}: '{words}': {v['image']} shows "
                f"{', '.join(f'{t:.2f}' for t in v['times'])} s, outside {window[0]:.2f}-{window[1]:.2f} s"
            )
            continue
        confirmed.append(
            {"where": where, "words": words, "view": v["image"], "t": round(inside[0], 3), "box": v["box"]}
        )
    plain.append(text[pos:])
    out = "".join(plain)
    bare = _MARK_RE.sub(" ", text)
    bare = NOT_DETAIL_RE.sub(" ", re.sub(r"\[(image|voice):[^\]]*\]", " ", bare))
    hit = detail_hits(bare)
    if hit:
        problems.append(f"UNCONFIRMED {where}: detail words outside a {{words|view}} mark: {', '.join(hit)}")
    mv = sorted({m.group(0).lower() for m in MOTION_RE.finditer(bare)})
    if mv:
        problems.append(
            f"UNCONFIRMED {where}: movement words outside a {{words|view}} mark: {', '.join(mv)} (a "
            f"movement is written only from a `frames` sheet over the moment: name it after the bar)"
        )
    return out


def detail_words_note():
    """The words that make a statement a detail, as `build` finds them (also in references/TOOL.md)."""
    return (
        "DETAIL WORDS (references/TOOL.md, section 'Detail words'): a statement using one of these, or a "
        "plural of one, is a detail and goes in a {words|VIEW} mark; outside a mark `build` refuses it. "
        + ", ".join(DETAIL_WORDS)
        + "; hold, holds, holding and held with something held after them "
        "(holds a mug, not holds that gaze). Movements a still cannot show, which need a `frames` sheet: nod, "
        "shrug, wink, head tilt, head shake, head turn (and tilts, shakes or turns her head). Not details: "
        "a music, sound, audio, background, continuous or ambient bed, window light, ring light, room tone "
        "or sound, app store, play store."
    )
