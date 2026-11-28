"""`zoom`, `color`, `frames` and `mouth`: views of moments and regions."""

import math
import os
import shutil

from .build import parse_range
from .constants import MAX_PIXELS, MAX_SIDE, PAD
from .details import view_name
from .media import decode_rgb, extract_cells
from .scandir import (
    frames_between,
    label_word,
    load_dir,
    nearest_frame,
    parse_box,
    record_followup,
    scratch_dir,
)
from .sheets import cell_dims, compose, fit_cell, page_times, report_images
from .transcript import join_words, words_at
from .util import _box_px, _hex, die, even, fmt_t


# ----------------------------------------------------------------------------- zoom
def cmd_zoom(a):
    d = os.path.abspath(a.dir)
    idx, pts, words = load_dir(d)
    info = idx["facts"]
    box = parse_box(a.box) if a.box else None
    frames = [nearest_frame(pts, t) for t in (a.at or [])] + list(a.frame or [])
    if not frames:
        die("give --at T (seconds) or --frame N")
    frames = list(dict.fromkeys(frames))
    W, H = info["width"], info["height"]
    if box:
        W, H = (box[2] - box[0]) * W, (box[3] - box[1]) * H
    fs = 22
    label_h = round(fs * 1.25) + 6
    n = len(frames)
    best = None
    for cols in range(1, n + 1):
        rows = math.ceil(n / cols)
        w = fit_cell(
            W / H,
            label_h,
            cap_w=(MAX_SIDE - (cols - 1) * PAD) // cols,
            cap_h=(MAX_SIDE - (rows - 1) * PAD) // rows,
            cap_px=int(MAX_PIXELS * 0.97) // (cols * rows),
        )
        if best is None or w > best[0]:
            best = (w, cols)
    cw = min(best[0], even(int(W * a.max_upscale)))
    ch = round(cw * H / W / 2) * 2
    tmp = scratch_dir(d, "zoom")
    cellmap = extract_cells(idx["video"], frames, box, cw, ch, tmp, "zm", info)
    cells = []
    for i in frames:
        said = label_word(words, pts[i]) if words else ""
        cells.append({"path": cellmap[i], "lines": [f"{fmt_t(pts[i])}  #{i}  {said}"]})
    tag = a.name or (
        "zoom_"
        + "_".join(f"{pts[i]:.2f}" for i in frames[:4])
        + ("_" + "-".join(f"{round(x * 100):02d}" for x in box) if box else "")
    )
    imgs = compose(cells, cw, ch, 1, os.path.join(d, "look", tag), tmp, cols_hint=best[1])
    shutil.rmtree(tmp, ignore_errors=True)
    print(
        f"zoom: {len(frames)} moment(s) "
        + ", ".join(f"{fmt_t(pts[i])} (#{i})" for i in frames)
        + (f", box {a.box}" if box else "")
        + f", each {cw}x{ch} px "
        f"(source pixels {int(W)}x{int(H)}{', upscaled' if cw > W else ''})"
    )
    times = [round(pts[i], 3) for i in frames]
    pages = page_times(imgs, times)
    for im, ts in zip(imgs, pages):
        im["times"] = ts
    mark = []
    for im, ts in zip(imgs, pages):
        nm = view_name(im["path"])
        mark.append(
            f"{{words|{nm}}}"
            if len(ts) == 1
            else " or ".join(f"{{words|{nm}@{fmt_t(t)}}}" for t in ts) + " (the moment the words describe)"
        )
    report_images(imgs, d, mark)
    record_followup(
        d,
        {
            "cmd": "zoom",
            "frames": frames,
            "times": times,
            "box": box,
            "cell": [cw, ch],
            "source_px": [int(W), int(H)],
            "images": [{**im, "path": os.path.relpath(im["path"], d)} for im in imgs],
        },
    )


# ----------------------------------------------------------------------------- color
HUE_NAMES = (
    (15, "red"),
    (40, "orange"),
    (65, "yellow"),
    (160, "green"),
    (195, "teal"),
    (250, "blue"),
    (285, "purple"),
    (330, "magenta-pink"),
    (350, "pink-red"),
    (361, "red"),
)


def color_name(rgb):
    """A plain name from measured RGB, with the numbers it rests on (hue in degrees)."""
    r, g, b = (v / 255 for v in rgb)
    mx, mn = max(r, g, b), min(r, g, b)
    lt, c = (mx + mn) / 2, mx - mn
    sat = 0.0 if c == 0 else c / (1 - abs(2 * lt - 1))
    if c == 0:
        h = 0.0
    elif mx == r:
        h = 60 * (((g - b) / c) % 6)
    elif mx == g:
        h = 60 * ((b - r) / c + 2)
    else:
        h = 60 * ((r - g) / c + 4)
    if sat < 0.12 or c < 0.06:
        name = (
            "black"
            if lt < 0.15
            else "white"
            if lt > 0.9
            else "dark gray"
            if lt < 0.4
            else "light gray"
            if lt > 0.7
            else "gray"
        )
    else:
        name = next(n for top, n in HUE_NAMES if h < top)
        if name in ("orange", "red") and lt < 0.4 and sat < 0.7:
            name = "brown"
        elif name in ("orange", "yellow") and lt > 0.6 and sat < 0.45:
            name = "beige"
        elif name in ("red", "pink-red") and lt > 0.6 and sat < 0.6:
            name = "pink"
        name = ("dark " if lt < 0.3 else "light " if lt > 0.8 else "") + ("grayish " if sat < 0.25 else "") + name
    return name, round(h), round(sat, 2), round(lt, 2)


def light_of_frame(px, n):
    """What the light does to colors in this frame: the color of its brightest surfaces (top 5% by
    luma; a white or light-gray surface takes the light's color) and its median luma."""
    lum = sorted(range(n), key=lambda k: 0.299 * px[3 * k] + 0.587 * px[3 * k + 1] + 0.114 * px[3 * k + 2])
    top = lum[int(0.95 * n) :] or lum[-1:]
    tint = [sum(px[3 * k + c] for k in top) / len(top) for c in range(3)]
    k = lum[n // 2]
    med = (0.299 * px[3 * k] + 0.587 * px[3 * k + 1] + 0.114 * px[3 * k + 2]) / 255
    return tint, med


def cmd_color(a):
    d = os.path.abspath(a.dir)
    idx, pts, _ = load_dir(d)
    info = idx["facts"]
    box = parse_box(a.box)
    W, H = info["width"], info["height"]
    i = nearest_frame(pts, a.at)
    cx, cy, cw, ch = _box_px(box, W, H)
    ow = even(min(cw, 200))
    oh = max(2, round(ow * ch / cw / 2) * 2)
    tmp = scratch_dir(d, "color")
    F = decode_rgb(idx["video"], [i], (cx, cy, cw, ch), ow, oh, tmp)
    fw = 160
    fh = max(2, round(fw * H / W / 2) * 2)
    FF = decode_rgb(idx["video"], [i], (0, 0, even(W), even(H)), fw, fh, os.path.join(tmp, "f"))
    RF = None
    if a.ref:
        ref = parse_box(a.ref)
        rx, ry, rw, rh = _box_px(ref, W, H)
        rw_ = even(min(rw, 200))
        RF = decode_rgb(
            idx["video"], [i], (rx, ry, rw, rh), rw_, max(2, round(rw_ * rh / rw / 2) * 2), os.path.join(tmp, "r")
        )
    shutil.rmtree(tmp, ignore_errors=True)
    if not F:
        die("decode failed")
    px = F[i]
    n = ow * oh
    bins = {}
    for k in range(n):
        bins.setdefault((px[3 * k] >> 5, px[3 * k + 1] >> 5, px[3 * k + 2] >> 5), []).append(k)
    # the inner half of the box (by width and height: a quarter of its area) holds the thing; pixels
    # of the surroundings that a box catches sit mostly at its border
    inner = {k for k in range(n) if ow / 4 <= k % ow < 3 * ow / 4 and oh / 4 <= k // ow < 3 * oh / 4}
    out, used = [], set()
    for b in sorted(bins, key=lambda b: -len(bins[b])):
        if b in used:
            continue
        near = [q for q in bins if q not in used and max(abs(q[0] - b[0]), abs(q[1] - b[1]), abs(q[2] - b[2])) <= 1]
        used.update(near)
        ks = [k for q in near for k in bins[q]]
        col = [sum(px[3 * k + c] for k in ks) / len(ks) for c in range(3)]
        out.append((len(ks) / n, col, sum(1 for k in ks if k in inner) / len(ks)))
    gain = None
    if RF:
        rp = RF[i]
        rn = len(rp) // 3
        rm = [sum(rp[3 * k + c] for k in range(rn)) / rn for c in range(3)]
        g = sum(rm) / 3
        if min(rm) > 8:
            gain = [g / v for v in rm]
    print(
        f"color at {fmt_t(pts[i])} (#{i}), box {a.box} ({cw}x{ch} source px): main colors of the box's "
        f"pixels (share, measured RGB, name with hue in degrees, saturation, lightness; center = share of "
        f"that color's pixels in the box's inner quarter, which is 25% for a color spread evenly)."
    )
    cav = []
    if FF:
        tint, med = light_of_frame(FF[i], fw * fh)
        tn, th, ts, _ = color_name(tint)
        if ts >= 0.15 and max(tint) - min(tint) >= 20:
            cav.append(
                f"tinted light: the brightest surfaces in this frame read {tn} (hue {th}°, sat {ts}); "
                f"under this light a white or gray thing reads tinted toward that hue, and a color "
                f"near that hue can be a neutral one"
            )
        if med < 0.25:
            cav.append(f"dim frame (median lightness {med:.2f}): colors read darker and grayer than they are")
    if cw * ch < 120 * 120:
        cav.append(
            f"small box ({cw}x{ch} px): what surrounds the thing (skin, background) mixes in; "
            f"trust a color with a high center share, not one that sits at the border"
        )
    if cav and not gain:
        print(
            "  CAVEATS (do not name a color from a value these affect; box something known to be white or "
            "gray in the same frame and pass it as --ref to correct for the light):"
        )
        for c in cav:
            print("    - " + c)
    elif cav:
        print(
            "  CAVEATS: " + " | ".join(c for c in cav if not c.startswith("tinted"))
            if any(not c.startswith("tinted") for c in cav)
            else "  (light corrected with --ref)"
        )
    named = []
    for share, col, cen in out[:4]:
        if share < 0.05:
            break
        name, h, sat, lt = color_name(col)
        line = f"  {share:.0%}  {_hex(col)}  {name}  (hue {h}°, sat {sat}, light {lt})  center {cen:.0%}"
        rec = {"name": name, "share": round(share, 3), "center": round(cen, 3)}
        if gain:
            cc = [min(255.0, v * gg) for v, gg in zip(col, gain)]
            n2, h2, s2, l2 = color_name(cc)
            line += f"   with --ref as neutral: {_hex(cc)} {n2} (hue {h2}°, sat {s2}, light {l2})"
            rec["name_ref"] = n2
        named.append(rec)
        print(line)
    if a.ref and not gain:
        print("  --ref box too dark to correct with")
    record_followup(d, {"cmd": "color", "frames": [i], "box": box, "ref": a.ref, "colors": named})


# ----------------------------------------------------------------------------- frames / mouth
def dense(a, mouth):
    d = os.path.abspath(a.dir)
    idx, pts, words = load_dir(d)
    info = idx["facts"]
    box = parse_box(a.box) if a.box else None
    if mouth and not box:
        die("mouth needs --box around the mouth (pick it on a shot frame)")
    if getattr(a, "line", None) is not None:
        lines = (idx.get("transcript_meta") or {}).get("lines") or []
        if not 0 <= a.line < len(lines):
            die(f"--line must be 0..{len(lines) - 1}")
        ln = lines[a.line]
        lw = [w for w in words if w["seg"] == a.line]
        a.start = (lw[0]["start"] if lw else ln["start"]) - 0.15
        a.end = (lw[-1]["end"] if lw else ln["end"]) + 0.15
    if getattr(a, "words", None):
        if not words:
            die("--words needs a transcript (scan --transcript)")
        w0, w1 = parse_range(a.words, len(words), "--words")
        a.start, a.end = words[w0]["start"] - 0.15, words[w1]["end"] + 0.15
    if a.start is None or a.end is None:
        die("give --from S --to E" + (", --words A-B or --line N" if mouth else ""))
    sel = frames_between(pts, a.start, a.end)[:: max(1, a.every)]
    if not sel:
        die("no frames in window")
    per_word = mouth and not getattr(a, "every_frame", False) and words
    if per_word:
        # what tells whether lips move with the words: the mouth in the middle of each word, and in the
        # middle of each pause of 0.15 s or more (open on words, closed in pauses = this person speaks)
        ws = [w for w in words if w["end"] > a.start and w["start"] < a.end]
        want = [nearest_frame(pts, (w["start"] + w["end"]) / 2) for w in ws]
        want += [
            nearest_frame(pts, (ws[k]["end"] + ws[k + 1]["start"]) / 2)
            for k in range(len(ws) - 1)
            if ws[k + 1]["start"] - ws[k]["end"] >= 0.15
        ]
        sel = sorted(set(f for f in want if sel[0] <= f <= sel[-1])) or sel
    long_side = a.size or (160 if per_word else 200 if mouth else 300)
    cw, ch, _ = cell_dims(info, box, long_side)
    if box:  # never more than 2x the source pixels
        W, H = (box[2] - box[0]) * info["width"], (box[3] - box[1]) * info["height"]
        if cw > 2 * W:
            cw, ch, _ = cell_dims(info, box, int(2 * max(W, H)))
    tmp = scratch_dir(d, "dense")
    cellmap = extract_cells(idx["video"], sel, box, cw, ch, tmp, "dn", info)
    cells = []
    prev = None
    for i in sel:
        cur = words_at(words, pts[i]) if words else []
        wtxt = join_words(cur) if cur else "·"
        new = bool(cur) and cur != prev
        prev = cur
        cells.append({"path": cellmap[i], "lines": [f"{fmt_t(pts[i])} #{i}", wtxt], "hi": new})
    tag = a.name or (
        ("mouth_" if mouth else "frames_")
        + f"{a.start:.2f}_{a.end:.2f}"
        + ("_" + "-".join(f"{round(x * 100):02d}" for x in box) if box else "")
    )
    imgs = compose(cells, cw, ch, 2 if words else 1, os.path.join(d, "look", tag), tmp)
    shutil.rmtree(tmp, ignore_errors=True)
    print(
        f"{'mouth' if mouth else 'frames'}: {len(sel)} "
        f"{'frames (one per word and per pause)' if per_word else 'real frames'} "
        f"{fmt_t(pts[sel[0]])}–{fmt_t(pts[sel[-1]])}"
        + (f" (every {a.every})" if a.every > 1 else "")
        + (f", box {a.box}" if box else "")
        + f", cell {cw}x{ch}. Label: time #frame / word being spoken (yellow time = a new word starts)."
    )
    if words:
        ws = [w for w in words if w["end"] > a.start and w["start"] < a.end]
        print("  words: " + "  ".join(f"{w['word']}[{w['start']:.2f}-{w['end']:.2f}]" for w in ws))
    mark = None
    if not mouth:
        pages = page_times(imgs, [pts[i] for i in sel])
        mark = [
            f"{{movement words|{view_name(im['path'])}}} (frames {fmt_t(ts[0])}-{fmt_t(ts[-1])})"
            for im, ts in zip(imgs, pages)
        ]
    report_images(imgs, d, mark)
    record_followup(
        d,
        {
            "cmd": "mouth" if mouth else "frames",
            "window": [a.start, a.end],
            "box": box,
            "images": [{**im, "path": os.path.relpath(im["path"], d)} for im in imgs],
        },
    )
