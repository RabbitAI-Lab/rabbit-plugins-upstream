"""Measuring a caption state's drawn layer: mask, box, rows and colors."""

import statistics

from .util import _hex, _rgb, weighted_median

# ----------------------------------------------------------------------------- layer measurement (text states)
LAYER_MAX_W = 720  # analysis width for color measurement (native pixels up to this)
LAYER_CHANGE = 48  # a pixel "changed" when a channel moves by more than this (0-255)
LAYER_STABLE = 24  # a pixel is "stable" in a state when no channel strays more than this


def state_samples(s, e, k=8):
    """Up to k frames spread evenly over a state (always its first and last)."""
    if e - s + 1 <= k:
        return list(range(s, e + 1))
    return sorted({s + round(j * (e - s) / (k - 1)) for j in range(k)})


def layer_frames(states, N):
    want = set()
    for st_ in states:
        s, e = st_[0], st_[1]
        pre = st_[2] if len(st_) > 2 and st_[2] is not None else s - 1
        want.update(state_samples(s, e))
        want.update(x for x in (pre, e + 1) if 0 <= x < N)
    return sorted(want)


def layer_mask(F, s, e, N, npx, ow, oh, pre=None):
    """Pixels of the layer a state shows. Two kinds of evidence:
    motion: the picture behind moved through the state (most of the region does not hold), so the
            pixels that hold are the layer;
    edges:  on a still picture, the pixels that hold through the state AND change where it starts
            and where it ends. With only one usable edge, what changed there may be the picture the
            next layer covers, so that evidence is weak.
    Returns (mask or None, note, evidence)."""
    inside = state_samples(s, e)
    if any(i not in F for i in inside):
        return None, "frames not decoded", None
    base = F[inside[0]]
    stable = bytearray(b"\x01") * npx
    for i in inside[1:]:
        fb = F[i]
        for k in range(npx):
            if (
                stable[k]
                and max(
                    abs(base[3 * k] - fb[3 * k]),
                    abs(base[3 * k + 1] - fb[3 * k + 1]),
                    abs(base[3 * k + 2] - fb[3 * k + 2]),
                )
                > LAYER_STABLE
            ):
                stable[k] = 0
    if len(inside) >= 4 and sum(stable) <= 0.35 * npx:
        return _despeck(stable, npx, ow, oh), "", "motion"
    edges, notes = [], []
    for a, b, lab in ((s - 1 if pre is None else pre, s, "appeared"), (e + 1, e, "left")):
        if not (0 <= a < N) or a not in F:
            continue
        fa, fb = F[a], F[b]
        m = bytearray(npx)
        for k in range(npx):
            if (
                max(abs(fa[3 * k] - fb[3 * k]), abs(fa[3 * k + 1] - fb[3 * k + 1]), abs(fa[3 * k + 2] - fb[3 * k + 2]))
                > LAYER_CHANGE
            ):
                m[k] = 1
        n = sum(m)
        held = sum(1 for k in range(npx) if m[k] and stable[k])
        # usable edge: what changed there is mostly the layer itself (it then holds still);
        # a cut or a moving subject behind changes far more than the layer and does not hold
        if n > 0.6 * npx or held < 0.4 * n:
            notes.append(f"picture behind changed when it {lab}")
        else:
            edges.append(m)
    if not edges:
        return None, "; ".join(notes) or "no frame before or after it", None
    mask = bytearray(npx)
    for k in range(npx):
        if stable[k] and all(m[k] for m in edges):
            mask[k] = 1
    return _despeck(mask, npx, ow, oh), "; ".join(notes), "two edges" if len(edges) == 2 else "one edge"


def _despeck(mask, npx, ow, oh):
    clean = bytearray(npx)  # drop specks: keep pixels with >= 2 masked 8-neighbors
    for k in range(npx):
        if mask[k]:
            y, x = divmod(k, ow)
            c = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if (dy or dx) and 0 <= y + dy < oh and 0 <= x + dx < ow and mask[(y + dy) * ow + x + dx]:
                        c += 1
            clean[k] = 1 if c >= 2 else 0
    return clean


ROW_MIN_SHARE = 0.01  # a text row has layer pixels on at least this share of the region's width (and 2)
ROW_MIN_WEIGHT = 0.15  # a row holds at least this share of the heaviest row's pixels; lighter ones are specks
ROW_MIN_PX = 3  # rows lower than this many analysis px are specks, not text
WORD_GAP_ROWS = 1.5  # column runs closer than this many row heights are one line (word spaces are far smaller)
CLUSTER_TOL = 40  # a pixel belongs to a color cluster within this many levels per channel of its mean
CLUSTER_MIN_SHARE = 0.08  # a cluster holds at least this share of the layer's pixels ...
CLUSTER_MAX = 4  # ... and the largest few are kept: fill, outline or shadow, box, one more
BOX_FILLS = 0.6  # the layer fills this share of its rows' boxes: a solid box behind the text ...
BOX_SHARE = 0.45  # ... when its largest color also holds this share of the pixels
MAIN_SHARE = 0.15  # the fill is chosen among clusters holding at least this share
EDGE_COLOR_SHARE = 0.12  # a second color holding this share can be an outline or shadow
EDGE_REACH = 0.15  # an outline or shadow is looked for this share of a row height out from the fill
OUTLINE_HITS = 0.5  # the second color hugs the fill on this share of its edge on every side: an outline
SHADOW_HITS = 0.35  # on at least this share on one or two sides: a shadow


def _layer_items(F, states, N, npx, ow, oh):
    """Each state's layer mask (with the middle sample frame and the state's length), the notes on
    states with none, and the kinds of evidence the masks rest on."""
    items, notes, evid = [], [], []
    for st_ in states:
        s, e = st_[0], st_[1]
        m, note, ev = layer_mask(F, s, e, N, npx, ow, oh, st_[2] if len(st_) > 2 else None)
        if note:
            notes.append(note)
        if ev:
            evid.append(ev)
        if m is not None and sum(m) >= 20:
            items.append((m, F[state_samples(s, e)[len(state_samples(s, e)) // 2]], e - s + 1))
    return items, notes, evid


def _text_rows(m, npx, ow, oh):
    """The text rows of one layer mask, and the mask kept to those rows and to its heaviest group of
    columns (a speck far to one side is not part of the line). Returns (kept mask, box, rows) or None."""
    prof = [0] * oh
    for k in range(npx):
        if m[k]:
            prof[k // ow] += 1
    lim = max(2, ROW_MIN_SHARE * ow)
    runs, r0 = [], None
    for y in range(oh + 1):
        on = y < oh and prof[y] >= lim
        if on and r0 is None:
            r0 = y
        elif not on and r0 is not None:
            runs.append((r0, y, sum(prof[r0:y])))
            r0 = None
    if not runs:
        return None
    big = max(r[2] for r in runs)
    rows = [(a, b) for a, b, w in runs if w >= ROW_MIN_WEIGHT * big and b - a >= ROW_MIN_PX]  # specks are not rows
    if not rows:
        return None
    keep = bytearray(npx)
    for a, b in rows:
        for k in range(a * ow, b * ow):
            keep[k] = m[k]
    # columns: group runs closer than 1.5 row heights (word spaces are far smaller), keep the
    # heaviest group; a speck far to one side is not part of the line
    colp = [0] * ow
    for k in range(npx):
        if keep[k]:
            colp[k % ow] += 1
    rh = statistics.median([b - a for a, b in rows])
    groups, g0, last, mass = [], None, None, 0
    for x in range(ow):
        if colp[x]:
            if g0 is None or x - last > WORD_GAP_ROWS * rh:
                if g0 is not None:
                    groups.append((g0, last + 1, mass))
                g0, mass = x, 0
            last = x
            mass += colp[x]
    if g0 is not None:
        groups.append((g0, last + 1, mass))
    gx0, gx1, _ = max(groups, key=lambda g: g[2])
    for k in range(npx):
        if keep[k] and not gx0 <= k % ow < gx1:
            keep[k] = 0
    return keep, (gx0, rows[0][0], gx1, rows[-1][1]), rows


def _color_clusters(items, npx, cnt):
    """The layer's main colors: pooled 8-level bins; each cluster = a peak bin plus neighboring bins
    near its color. Clusters holding a fair share of the pixels, largest first."""
    bins = {}
    for ii, (m, img, _) in enumerate(items):
        for k in range(npx):
            if m[k]:
                bins.setdefault((img[3 * k] >> 5, img[3 * k + 1] >> 5, img[3 * k + 2] >> 5), []).append((ii, k))
    order = sorted(bins, key=lambda b: -len(bins[b]))
    clusters, used = [], set()
    for b in order:
        if b in used:
            continue
        near = [q for q in order if q not in used and max(abs(q[0] - b[0]), abs(q[1] - b[1]), abs(q[2] - b[2])) <= 1]
        used.update(near)
        pk = bins[b]
        col = [sum(items[i][1][3 * k + c] for i, k in pk) / len(pk) for c in range(3)]
        px = [
            (i, k)
            for q in near
            for (i, k) in bins[q]
            if max(abs(items[i][1][3 * k + c] - col[c]) for c in range(3)) <= CLUSTER_TOL
        ]
        col = [sum(items[i][1][3 * k + c] for i, k in px) / len(px) for c in range(3)]
        clusters.append({"rgb": col, "px": set(px), "share": len(px) / cnt})
    return [c for c in clusters if c["share"] >= CLUSTER_MIN_SHARE][:CLUSTER_MAX]


def _outside_contact(clusters, items, ow, oh):
    """Each cluster's share of pixels touching the outside of the layer."""

    def inmask(i, y, x):
        return 0 <= y < oh and 0 <= x < ow and items[i][0][y * ow + x]

    for c in clusters:
        t = 0
        for i, k in c["px"]:
            y, x = divmod(k, ow)
            if not all(inmask(i, y + dy, x + dx) for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1))):
                t += 1
        c["contact"] = t / len(c["px"])


def _edge_hits(fill, d, ow, oh, row_h):
    """Per side (up, down, left, right): the share of the fill's edge pixels with color d within a short
    reach outward."""
    reach = max(2, round(EDGE_REACH * (row_h or 12)))
    hits = {}
    for name, (dy, dx) in (("up", (-1, 0)), ("down", (1, 0)), ("left", (0, -1)), ("right", (0, 1))):
        ed = h = 0
        for i, k in fill["px"]:
            y, x = divmod(k, ow)
            yy, xx = y + dy, x + dx
            if not (0 <= yy < oh and 0 <= xx < ow) or (i, yy * ow + xx) in fill["px"]:
                continue
            ed += 1
            for r_ in range(1, reach + 1):
                yy, xx = y + dy * r_, x + dx * r_
                if 0 <= yy < oh and 0 <= xx < ow and (i, yy * ow + xx) in d["px"]:
                    h += 1
                    break
        hits[name] = round(h / ed, 2) if ed else 0.0
    return hits


def layer_style(F, states, N, W, H, crop_px, ow, oh):
    """Measure the layer shown by a list of states (one caption chunk, or every chunk of one
    caption): its box, text rows and colors, pooled over the states. Colors come from pixels:
    fill = the main color of the layer away from its outer edge; a second color hugging the fill
    on all four sides = outline, on one or two sides = shadow; a color filling most of the box
    behind = box. Returns a dict with measured=False and the reason when it cannot measure."""
    npx = ow * oh
    sx, sy = crop_px[2] / ow, crop_px[3] / oh
    items, notes, evid = _layer_items(F, states, N, npx, ow, oh)
    if not items:
        return {"measured": False, "why": "; ".join(sorted(set(notes))) or "no layer pixels"}
    # box and rows: from each item's text rows, and the union box
    boxes, rowsets = [], []
    for ii, (m, img, nfr) in enumerate(items):
        found = _text_rows(m, npx, ow, oh)
        if not found:
            continue
        keep, box, rows = found
        items[ii] = (keep, img, nfr)
        boxes.append(box)
        rowsets.append(rows)
    items = [it for it in items if sum(it[0])]
    if not boxes:
        return {"measured": False, "why": "no text rows in the layer"}
    cnt = sum(sum(m) for m, _, _ in items)
    X0, Y0 = min(b[0] for b in boxes), min(b[1] for b in boxes)
    X1, Y1 = max(b[2] for b in boxes), max(b[3] for b in boxes)
    cys = sorted(((b[1] + b[3]) / 2) for b in boxes)
    cxs = sorted(((b[0] + b[2]) / 2) for b in boxes)
    nrows = statistics.median([len(r) for r in rowsets])
    heights = sorted(b - a for r in rowsets for a, b in r)
    row_h = statistics.median(heights) if heights else 0

    def fx(x):
        return (crop_px[0] + x * sx) / W

    def fy(y):
        return (crop_px[1] + y * sy) / H

    clusters = _color_clusters(items, npx, cnt)
    if not clusters:
        return {"measured": False, "why": "no dominant color in the layer"}
    _outside_contact(clusters, items, ow, oh)
    st = {
        "measured": True,
        "layer_px": cnt,
        "states_used": len(items),
        "evidence": "motion" if "motion" in evid else "two edges" if "two edges" in evid else "one edge",
    }
    area = cnt / max(1, sum((b[2] - b[0]) * (b[3] - b[1]) for b in boxes))
    rest = list(clusters)
    if area >= BOX_FILLS and clusters[0]["share"] >= BOX_SHARE and len(clusters) > 1:
        st["box_color"] = _hex(clusters[0]["rgb"])
        rest = clusters[1:]
    # the fill sits inside the layer; an outline or shadow is what touches the outside
    main = [c for c in rest if c["share"] >= MAIN_SHARE] or rest[:1]
    fill = min(main, key=lambda c: c["contact"])
    rest = [fill] + sorted((c for c in rest if c is not fill), key=lambda c: -c["share"])
    st["fill"] = _hex(fill["rgb"])
    st["fill_share"] = round(fill["share"], 2)
    edge = [c for c in rest[1:] if c["share"] >= EDGE_COLOR_SHARE]
    if edge:
        d = edge[0]
        hits = _edge_hits(fill, d, ow, oh, row_h)
        mx, mn = max(hits.values()), min(hits.values())
        if mx >= OUTLINE_HITS and mn >= 0.5 * mx:
            st["outline_color"] = _hex(d["rgb"])
        elif mx >= SHADOW_HITS:
            st["shadow_color"] = _hex(d["rgb"])
            st["shadow_side"] = "+".join(k for k, v in hits.items() if v >= 0.5 * mx)
        else:
            st["second_color"] = _hex(d["rgb"])
        st["edge_hits"] = hits
    others = [c for c in rest[1:] if not (edge and c is edge[0])]
    if others:
        st["other_colors"] = [_hex(c["rgb"]) + f" {c['share']:.2f}" for c in others]
    if notes:
        st["note"] = "; ".join(sorted(set(notes)))
    # a caption read with a box that holds it with a margin never reaches two opposite edges of that
    # box. A layer that does is not separated from the picture (still parts of a locked shot held
    # with it) or the box cuts the text: its rows, size and place say nothing about the text. Held
    # through motion, the whole mask is the picture's as much as the layer's, so its colors go too
    reach = [n for n, hit in (("top", Y0 <= 0), ("bottom", Y1 >= oh), ("left", X0 <= 0), ("right", X1 >= ow)) if hit]
    if {"top", "bottom"} <= set(reach) or {"left", "right"} <= set(reach):
        why = (
            f"the measured layer reaches the {' and '.join(reach)} edges of the box: the picture got in "
            f"or the box cuts the text (a box holding the text with a margin can measure it)"
        )
        if st["evidence"] == "motion":
            return {"measured": False, "why": why}
        st["size_withdrawn"] = why
        return st
    st["box"] = [round(fx(X0), 3), round(fy(Y0), 3), round(fx(X1), 3), round(fy(Y1), 3)]
    st["center"] = [round(fx(statistics.median(cxs)), 3), round(fy(statistics.median(cys)), 3)]
    st["rows"] = int(round(nrows))
    st["row_px_1080w"] = round(row_h * sy * 1080 / W)
    return st


TRUST_TOL = 24  # two measured fills are the same color within this many levels per channel


def _near(a, b, tol=40):
    return max(abs(x - y) for x, y in zip(_rgb(a), _rgb(b))) <= tol


def trust_styles(rows):
    """A layer measured from pixels is kept only when other evidence agrees with it. Edges on a still
    picture can pick up the picture where the neighboring state's text sat or will sit, and a hold
    through motion can pick up a part of the picture that happened to stay still; neither is the
    same color across states with different pictures behind, while the layer is. So the region's
    reference fill is the best-supported color over all measured states (frame-weighted), needing
    >= 25% of the weight, two states showing it (unless only one state was measured) and 1.5x the
    best color unlike it; a state whose fill disagrees with it, or any state when there is no
    reference, has its values withdrawn with the reason (absent rather than wrong)."""
    meas = [(st["layer"]["fill"], st["frames"]) for st in rows if st["layer"].get("measured")]
    tot = sum(w for _, w in meas)
    # each measured fill's support: the weight of fills within TRUST_TOL of it; the best-supported
    # fill is the reference (a drawn fill repeats exactly; a light picture behind is near, not equal)
    sup = sorted(((sum(w2 for f2, w2 in meas if _near(f, f2, TRUST_TOL // 2)), f) for f, _ in meas), reverse=True)
    ref = None
    single = sum(1 for st in rows if st["layer"].get("measured")) == 1
    # agreement needs two states showing that color; a lone measured state stands only on its own
    # (it then must not come from one edge, where the picture the next layer covers can get in)
    if sup and not single and sum(1 for f, _ in meas if _near(f, sup[0][1], TRUST_TOL // 2)) < 2:
        sup = []
    if sup and sup[0][0] >= 0.25 * tot:
        rest = [x for x in sup if not _near(x[1], sup[0][1], TRUST_TOL)]
        if not rest or sup[0][0] >= 1.5 * rest[0][0]:
            ref = sup[0][1]
    for st in rows:
        ly = st["layer"]
        if not ly.get("measured"):
            continue
        if ref and _near(ly["fill"], ref, TRUST_TOL) and (not single or ly.get("evidence") != "one edge"):
            ly["agrees_with"] = ref
            continue
        why = (
            f"fill {ly['fill']} (from {ly['evidence']}) differs from this region's color {ref}"
            if ref
            else f"fill {ly['fill']} (from {ly['evidence']}) has no other state to agree with"
        )
        st["layer"] = {"measured": False, "untrusted": ly, "why": why + ": it may be the picture behind"}
    # text size and place: a mask that picked up the picture, or two text lines merged into one row,
    # gives a taller row. Reference = frame-weighted median row height of the kept states, from edge
    # evidence when there is any (a hold through motion keeps still bits of the picture too)
    kept = [st for st in rows if st["layer"].get("measured") and st["layer"].get("row_px_1080w")]
    pool = [st for st in kept if st["layer"]["evidence"] != "motion"] or kept
    if pool:
        ref_row = weighted_median(sorted((st["layer"]["row_px_1080w"], st["frames"]) for st in pool))
        for st in kept:
            ly = st["layer"]
            if abs(ly["row_px_1080w"] - ref_row) > 0.4 * ref_row:
                ly["size_withdrawn"] = (
                    f"row height {ly['row_px_1080w']} px differs from this region's "
                    f"{ref_row} px: rows merged or the picture got in"
                )
                for k in ("row_px_1080w", "rows", "box", "center"):
                    ly.pop(k, None)


def layer_line(ly):
    if not ly.get("measured"):
        return "not measured (" + ly.get("why", "") + ")"
    parts = [f"[{ly.get('evidence')}] fill {ly['fill']}"]
    for k, lab in (
        ("outline_color", "outline"),
        ("shadow_color", "shadow"),
        ("box_color", "box"),
        ("second_color", "edge color (neither outline nor shadow)"),
    ):
        if k in ly:
            parts.append(f"{lab} {ly[k]}" + (f" ({ly['shadow_side']})" if k == "shadow_color" else ""))
    if ly.get("other_colors"):
        parts.append("also " + ", ".join(ly["other_colors"]))
    if ly.get("box"):
        b = ly["box"]
        parts.append(f"box {b[0]:.3f},{b[1]:.3f},{b[2]:.3f},{b[3]:.3f}")
        parts.append(f"{ly['rows']} row(s), row height {ly['row_px_1080w']} px at 1080 wide")
    else:
        parts.append("size and place not given: " + ly.get("size_withdrawn", ""))
    if ly.get("note"):
        parts.append(ly["note"])
    return "; ".join(parts)
