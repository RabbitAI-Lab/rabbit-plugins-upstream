"""Change measurement over the whole picture: frame index, change grid, events, shots, layers."""

import bisect
import math
import os
import re
import statistics
import struct

from .constants import (
    BASELINE_S,
    CELL_FLOOR,
    CELL_JUMP_X,
    EXACT_T,
    GRID_N,
    HOLD_T,
    SCDET_THRESHOLD,
    SPIKE_FLOOR,
    SPIKE_LOCAL_X,
    SPIKE_NEIGHBOR_X,
    SPIKE_WINDOW_S,
    STILL_CELL,
    STILL_LOCKED,
    STILL_MOVING,
)
from .media import decode_rgb, run
from .util import _box_px, _pc, above, die, even, fmt_t


# ----------------------------------------------------------------------------- frame index + change grid
def grid_shape(w, h, n=GRID_N):
    if w <= h:
        return n, max(1, round(n * h / w))
    return max(1, round(n * w / h)), n


def measure_picture(video, info, cache):
    """One decode: every frame's true timestamp, per-cell change maps, the 32x32 global
    change (the spike rule's input) and ffmpeg scdet scores."""
    C, R = grid_shape(info["width"], info["height"])
    os.makedirs(cache, exist_ok=True)
    gpath, spath = os.path.join(cache, "grid.raw"), os.path.join(cache, "g32.raw")
    fc = (
        f"[0:v]showinfo,split=3[a][b][c];"
        f"[a]scale={C * 8}:{R * 8}:flags=area,format=gray16le,tblend=all_mode=difference,"
        f"scale={C}:{R}:flags=area[ga];"
        f"[b]scale=32:32:flags=area,format=gray16le,tblend=all_mode=difference,"
        f"scale=1:1:flags=area[gb];"
        f"[c]scdet=threshold={SCDET_THRESHOLD},nullsink"
    )
    r = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-y",
            "-i",
            video,
            "-an",
            "-filter_complex",
            fc,
            "-map",
            "[ga]",
            "-fps_mode",
            "passthrough",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "gray16le",
            gpath,
            "-map",
            "[gb]",
            "-fps_mode",
            "passthrough",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "gray16le",
            spath,
        ]
    )
    err = r.stderr.decode("utf-8", "ignore")
    if r.returncode != 0:
        die("ffmpeg decode failed: " + err[-400:])
    pts, means = [], []
    for line in err.splitlines():
        if "Parsed_showinfo_0" in line:
            m = re.search(r"pts_time:\s*(-?[0-9.]+)", line)
            if m:
                pts.append(round(float(m.group(1)) - info["start_time"], 6))
                # the frame's mean per plane; kept for YUV and gray frames (plane 0 = luma)
                q = re.search(r"fmt:(\w+).*?mean:\[([0-9 .]+)\]", line)
                means.append(
                    [float(x) for x in q.group(2).split()]
                    if q and q.group(1).startswith(("yuv", "yuvj", "nv", "gray"))
                    else None
                )
    scd = []
    for m in re.finditer(r"lavfi\.scd\.score:\s*([0-9.]+),\s*lavfi\.scd\.time:\s*([0-9.]+)", err):
        scd.append((round(float(m.group(2)) - info["start_time"], 6), float(m.group(1))))
    n = C * R
    with open(gpath, "rb") as f:
        raw = f.read()
    vals = struct.unpack("<%dH" % (len(raw) // 2), raw)
    grid = [[x / 65535 for x in vals[i * n : (i + 1) * n]] for i in range(len(vals) // n)]
    with open(spath, "rb") as f:
        raw = f.read()
    g = [x / 65535 for x in struct.unpack("<%dH" % (len(raw) // 2), raw)]
    if len(pts) < 2:
        die(f"{video} decodes to {len(pts)} frame(s): a still image or an empty stream, not a video")
    if len(grid) != len(pts) - 1 or len(g) != len(pts) - 1:
        die(f"frame count mismatch (pts {len(pts)}, diffs {len(grid)}/{len(g)}); cannot trust timestamps")
    # index 0 of diff lists = change INTO frame 1; pad so diff[i] = change into frame i
    grid.insert(0, [0.0] * n)
    g.insert(0, 0.0)
    return {"pts": pts, "cols": C, "rows": R, "grid": grid, "g": g, "scdet": scd, "means": means}


def spike_frames(pts, g):
    """Hard cuts: a frame whose whole-picture change is an isolated one-frame spike, well above both
    neighbors and above the usual change around it (motion rises and falls over several frames)."""
    out = []
    for i in range(2, len(g) - 1):
        x = g[i]
        if x < SPIKE_FLOOR or x < SPIKE_NEIGHBOR_X * g[i - 1] or x < SPIKE_NEIGHBOR_X * g[i + 1]:
            continue
        lo = bisect.bisect_left(pts, pts[i] - SPIKE_WINDOW_S)
        hi = bisect.bisect_right(pts, pts[i] + SPIKE_WINDOW_S)
        others = [g[k] for k in range(max(1, lo), hi) if k != i]
        if others and x < SPIKE_LOCAL_X * statistics.median(others):
            continue
        out.append(i)
    return out


class Baseline:
    """Per-cell 'usual change' (median over +-BASELINE_S), computed on 0.25 s blocks."""

    def __init__(self, pts, grid, ncell):
        self.pts, self.grid = pts, grid
        self.blk = 0.25
        nb = int(pts[-1] / self.blk) + 1
        members = [[] for _ in range(nb)]
        for i in range(1, len(pts)):
            members[min(nb - 1, int(pts[i] / self.blk))].append(i)
        reach = int(round(BASELINE_S / self.blk))
        self.med = []
        for b in range(nb):
            idx = [i for bb in range(max(0, b - reach), min(nb, b + reach + 1)) for i in members[bb]]
            self.med.append([statistics.median([grid[i][c] for i in idx]) if idx else 0.0 for c in range(ncell)])

    def at(self, i):
        return self.med[min(len(self.med) - 1, int(self.pts[i] / self.blk))]


def changed_mask(grid, i, base):
    return [d >= CELL_FLOOR and d >= CELL_JUMP_X * b for d, b in zip(grid[i], base)]


def components(mask, C, R):
    seen = [False] * len(mask)
    comps = []
    for s in range(len(mask)):
        if not mask[s] or seen[s]:
            continue
        stack, comp = [s], []
        seen[s] = True
        while stack:
            k = stack.pop()
            comp.append(k)
            r, c = divmod(k, C)
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < R and 0 <= cc < C:
                        q = rr * C + cc
                        if mask[q] and not seen[q]:
                            seen[q] = True
                            stack.append(q)
        comps.append(comp)
    comps.sort(key=len, reverse=True)
    return comps


def classify(mask, C, R, W, H):
    """Where in the frame did the picture change? Shape rules, not tuned magnitudes:
    cut    = more than half of the picture changes, or the change spans the whole frame in
             both directions and covers at least a third of it (new take on a held background);
    panel  = a filled rectangle covering >= 1/5 of the frame changes, the rest holds
             (a cut or page change inside one panel of a split screen / inset);
    band   = a rectangle at least twice as wide as tall changes (caption, title, graphic line);
    local  = anything smaller (sticker, small graphic, or something jumping inside a still frame)."""
    total = C * R
    comps = [c for c in components(mask, C, R) if len(c) >= 2]
    count = sum(len(c) for c in comps)
    if count == 0:
        return "none", 0.0, None
    frac = count / total
    main = comps[0]
    rs = [k // C for k in main]
    cs = [k % C for k in main]
    r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
    allr = [k // C for c in comps for k in c]
    allc = [k % C for c in comps for k in c]
    span_w = (max(allc) - min(allc) + 1) / C
    span_h = (max(allr) - min(allr) + 1) / R
    box = [round(c0 / C, 3), round(r0 / R, 3), round((c1 + 1) / C, 3), round((r1 + 1) / R, 3)]
    if frac >= 0.5 or (span_w >= 0.9 and span_h >= 0.9 and frac >= 1 / 3):
        return "cut", frac, None
    barea = (r1 - r0 + 1) * (c1 - c0 + 1)
    fill = len(main) / barea
    bw_px = (box[2] - box[0]) * W
    bh_px = (box[3] - box[1]) * H
    if fill >= 0.6 and barea / total >= 0.2:
        return "panel", frac, box
    if bw_px >= 2 * bh_px:
        return "band", frac, box
    return "local", frac, box


def find_events(M, info):
    pts, g, grid, C, R = M["pts"], M["g"], M["grid"], M["cols"], M["rows"]
    N = len(pts)
    spikes = set(spike_frames(pts, g))
    cand = {}
    for i in spikes:
        cand.setdefault(i, set()).add("spike")
    scd_score = {}
    for t, s in M["scdet"]:
        i = min(range(N), key=lambda k: abs(pts[k] - t))
        cand.setdefault(i, set()).add("scdet")
        scd_score[i] = max(scd_score.get(i, 0), s)
    base = Baseline(pts, grid, C * R)
    evs = []
    for i in sorted(cand):
        # peak of the global change near the candidate, then the span where it stays high
        lo, hi = max(1, i - 3), min(N - 1, i + 3)
        p = i if "spike" in cand[i] else max(range(lo, hi + 1), key=lambda k: g[k])
        lvl = max(SPIKE_FLOOR, g[p] / 4)
        s = p
        while s - 1 >= 1 and g[s - 1] >= lvl and p - s < 12:
            s -= 1
        e = p
        while e + 1 < N and g[e + 1] >= lvl and e - p < 12:
            e += 1
        evs.append({"s": s, "e": e, "p": p, "by": set(cand[i]), "scd": scd_score.get(i)})
    # merge overlapping spans
    merged = []
    for ev in sorted(evs, key=lambda x: x["s"]):
        if merged and ev["s"] <= merged[-1]["e"] + 1:
            m = merged[-1]
            m["e"] = max(m["e"], ev["e"])
            m["by"] |= ev["by"]
            if g[ev["p"]] > g[m["p"]]:
                m["p"] = ev["p"]
            m["scd"] = max([x for x in (m["scd"], ev["scd"]) if x is not None], default=None)
        else:
            merged.append(ev)
    out = []
    for ev in merged:
        s, e, p = ev["s"], ev["e"], ev["p"]
        mask = [False] * (C * R)
        # usual change measured outside the event span
        lo = bisect.bisect_left(pts, pts[p] - BASELINE_S)
        hi = bisect.bisect_right(pts, pts[p] + BASELINE_S)
        idx = [k for k in range(max(1, lo), hi) if k < s - 1 or k > e + 1]
        bl = [statistics.median([grid[k][c] for k in idx]) if idx else 0.0 for c in range(C * R)]
        for k in range(s, e + 1):
            mask = [a or b for a, b in zip(mask, changed_mask(grid, k, bl))]
        kind, frac, box = classify(mask, C, R, info["width"], info["height"])
        if kind == "none":
            kind = "cut" if g[p] >= 0.05 else "local"  # change too diffuse to localize
        abrupt = e == s
        out.append(
            {
                "t": round(pts[s], 3),
                "frame": s,
                "kind": kind,
                "onset": "abrupt" if abrupt else "gradual",
                "span": [round(pts[s], 3), round(pts[e], 3)],
                "span_frames": [s, e],
                "peak_t": round(pts[p], 3),
                "peak_frame": p,
                "changed_fraction": round(frac, 2),
                "box": box,
                "found_by": sorted(ev["by"]),
                "scdet_score": ev["scd"],
                "global_change": round(g[p], 4),
            }
        )
    for k, ev in enumerate(out, 1):
        ev["id"] = f"E{k}"
    return out, base


# A jump cut inside one framing: the camera and background hold while the person jumps to a new pose in
# one frame, so the change is local. It is a cut when the change is abrupt, covers at least a tenth of
# the frame (a person, not a sticker or a word), and the colors in its box are nearly the same before and
# after (the same person, clothes and light, rearranged). A graphic, picture or caption that pops on
# brings colors that were not there. On the test videos the jump cuts measured 0.19-0.43 of the frame and
# 0.93-0.96 alike; the graphics that popped on, 0.02-0.06 and 0.62-0.81.
JUMP_MIN_FRAC = 0.10
JUMP_SAME_COLORS = 0.90  # overlap of 64-bin color histograms (4 levels per channel) across the change


def color_overlap(a, b):
    """How alike the colors of two RGB frames are: the overlap of their 64-bin histograms, 0 to 1."""
    ha, hb = [0] * 64, [0] * 64
    for buf, h in ((a, ha), (b, hb)):
        for i in range(0, len(buf) - 2, 3):
            h[(buf[i] >> 6) * 16 + (buf[i + 1] >> 6) * 4 + (buf[i + 2] >> 6)] += 1
    return sum(min(x, y) for x, y in zip(ha, hb)) / max(1, sum(ha))


def jump_cuts(video, info, events, tmp):
    """Turn each local change that is a jump cut inside one framing (see JUMP_MIN_FRAC) into a cut, with
    `jump_cut` = how alike the colors in its box stayed; it keeps its box."""
    want = [
        ev
        for ev in events
        if ev["kind"] == "local" and ev["onset"] == "abrupt" and ev["box"] and ev["changed_fraction"] >= JUMP_MIN_FRAC
    ]
    for ev in want:
        p = ev["peak_frame"]
        F = decode_rgb(video, [p - 1, p], _box_px(ev["box"], info["width"], info["height"]), 64, 64, tmp)
        if not F:
            continue
        same = color_overlap(F[p - 1], F[p])
        if same >= JUMP_SAME_COLORS:
            ev["kind"] = "cut"
            ev["jump_cut"] = {"same_colors": round(same, 2)}


BETWEEN_LUMA = 4  # mean luma levels (0-255) that count as darker or lighter
BETWEEN_TINT = 6  # change of mean V-U (0-255 chroma) that counts as warmer or cooler
BETWEEN_MIX = 0.25  # a frame within this share of the change from a mix of its neighbors is a mix


def between_frames(video, info, M, events, tmp):
    """The one or two frames inside a change that takes two or three frames (a flash, a dip, a tinted
    or blended frame between two pictures): each one's mean brightness and tint against the frame
    before the change and the frame after it, measured, and whether it is a mix of those two
    (a dissolve step) or not. Written onto each such event as `between`."""
    means = M.get("means") or []
    want = [ev for ev in events if 1 <= ev["span_frames"][1] - ev["span_frames"][0] <= 2 and ev["span_frames"][0] >= 1]
    if not want or len(means) != len(M["pts"]):
        return
    fr = sorted({k for ev in want for k in range(ev["span_frames"][0] - 1, ev["span_frames"][1] + 1)})
    if any(means[k] is None for k in fr):
        return
    F = decode_rgb(video, fr, (0, 0, even(info["width"]), even(info["height"])), 32, 32, tmp)
    for ev in want:
        s, e = ev["span_frames"]
        b, a = s - 1, e
        rows = []
        for k in range(s, e):
            yb, yk, ya = means[b][0], means[k][0], means[a][0]
            row = {
                "t": round(M["pts"][k], 3),
                "frame": k,
                "luma": [round(yb), round(yk), round(ya)],
                "vs_before": "darker" if yk <= yb - BETWEEN_LUMA else "lighter" if yk >= yb + BETWEEN_LUMA else "same",
                "vs_after": "darker" if yk <= ya - BETWEEN_LUMA else "lighter" if yk >= ya + BETWEEN_LUMA else "same",
            }
            if len(means[k]) >= 3:
                tb, tk = means[b][2] - means[b][1], means[k][2] - means[k][1]
                row["tint_vs_before"] = (
                    "warmer" if tk - tb >= BETWEEN_TINT else "cooler" if tb - tk >= BETWEEN_TINT else "same"
                )
            if F and all(x in F for x in (b, k, a)):
                pb, pk, pa = F[b], F[k], F[a]
                dd = sum((x - y) ** 2 for x, y in zip(pa, pb))
                if dd:
                    al = min(1.0, max(0.0, sum((z - y) * (x - y) for x, y, z in zip(pa, pb, pk)) / dd))
                    res = sum((z - (1 - al) * y - al * x) ** 2 for x, y, z in zip(pa, pb, pk))
                    row["mix_of_neighbors"] = (res / dd) ** 0.5 <= BETWEEN_MIX
                    row["mix_residual"] = round((res / dd) ** 0.5, 2)
            rows.append(row)
        ev["between"] = rows


def between_line(r):
    """One measured sentence about a frame inside a change, for the summary."""
    yb, yk, ya = r["luma"]

    def than(v):
        return "as bright as" if v == "same" else v + " than"

    shape = (
        "darker than both neighbors (a dip)"
        if r["vs_before"] == r["vs_after"] == "darker"
        else "lighter than both neighbors (a flash)"
        if r["vs_before"] == r["vs_after"] == "lighter"
        else f"{than(r['vs_before'])} the frame before, {than(r['vs_after'])} the frame after"
    )
    out = f"frame {fmt_t(r['t'])} #{r['frame']} is {shape}: mean luma {yb} -> {yk} -> {ya}"
    if r.get("tint_vs_before") and r["tint_vs_before"] != "same":
        out += f"; {r['tint_vs_before']} than the frame before"
    if "mix_of_neighbors" in r:
        out += (
            "; a mix of the frames either side (a dissolve step)"
            if r["mix_of_neighbors"]
            else "; not a mix of the frames either side"
        )
    return out


def still_share(grid, frames):
    n = len(grid[0])
    meds = [statistics.median([grid[i][c] for i in frames]) for c in range(n)]
    return round(sum(1 for m in meds if m < STILL_CELL) / n, 2)


def still_of_shot(M, a, b):
    """Share of the picture whose pixels stay still through the shot (whole shot, and per
    1-second block). Locked camera: the background holds, so a large share is still. Handheld
    or moving camera: every part of the picture changes every frame, so almost none is."""
    pts, grid = M["pts"], M["grid"]
    fr = list(range(max(1, a), b + 1))
    if len(fr) < 4:
        return {"still_share": None, "still_per_s": [], "camera_measure": "too short to measure"}
    blocks, k = [], 0
    while k < len(fr):
        j = k
        while j + 1 < len(fr) and pts[fr[j + 1]] - pts[fr[k]] < 1.0:
            j += 1
        if j - k + 1 >= 4:
            blocks.append(still_share(grid, fr[k : j + 1]))
        k = j + 1
    sh = still_share(grid, fr)
    word = "locked" if sh >= STILL_LOCKED else "moving" if sh <= STILL_MOVING else "mixed"
    return {"still_share": sh, "still_per_s": blocks, "camera_measure": word}


def text_regions(M, events, base, info):
    """Cells that keep changing on their own (not during cuts) -> likely caption / text bands."""
    pts, grid, C, R = M["pts"], M["grid"], M["cols"], M["rows"]
    skip = set()
    for ev in events:
        if ev["kind"] in ("cut", "panel"):
            a, b = ev["span_frames"]
            skip.update(range(a - 1, b + 2))
    counts = [0] * (C * R)
    hits = []
    for i in range(1, len(pts)):
        if i in skip:
            continue
        m = changed_mask(grid, i, base.at(i))
        if sum(m) > 0.5 * C * R:
            continue
        # text swaps are one-frame steps per cell; motion changes a cell over several frames
        prv = grid[i - 1]
        nxt = grid[i + 1] if i + 1 < len(grid) else [0.0] * len(m)
        m = [v and grid[i][c] >= 2 * max(prv[c], nxt[c]) for c, v in enumerate(m)]
        hits.append((i, m))
        for c, v in enumerate(m):
            if v:
                counts[c] += 1
    top = max(counts) if counts else 0
    if top < 3:
        return []
    keep = [x >= max(3, 0.3 * top) for x in counts]
    regs = []
    for comp in components(keep, C, R):
        if len(comp) < 2:
            continue
        rs = [k // C for k in comp]
        cs = [k % C for k in comp]
        r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
        # the core holds the most frequent changes; text reaches further out (long lines, words
        # at the line ends change less often), so widen along the core's rows to every cell that
        # stepped there repeatedly
        weak = max(2, 0.1 * top)
        while c0 > 0 and any(counts[r * C + c0 - 1] >= weak for r in range(r0, r1 + 1)):
            c0 -= 1
        while c1 < C - 1 and any(counts[r * C + c1 + 1] >= weak for r in range(r0, r1 + 1)):
            c1 += 1
        cells = {r * C + c for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)} & {
            k for k in range(C * R) if counts[k]
        }
        frames = [i for i, m in hits if any(m[c] for c in cells)]
        # count change moments (consecutive frames = one moment)
        moments = sum(1 for k, i in enumerate(frames) if k == 0 or i - frames[k - 1] > 1)
        mx = 0.5 / C
        my = 1.0 / R  # a text row's top or bottom often sits in a cell that rarely steps
        box = [max(0.0, c0 / C - mx), max(0.0, r0 / R - my), min(1.0, (c1 + 1) / C + mx), min(1.0, (r1 + 1) / R + my)]
        w_px = (box[2] - box[0]) * info["width"]
        h_px = (box[3] - box[1]) * info["height"]
        if abs((box[0] + box[2]) / 2 - 0.5) < 0.1:
            # centered text: its longest line can reach far wider than its usual words
            box[0], box[2] = 0.02, 0.98
            w_px = 0.96 * info["width"]
        starts = [i for k, i in enumerate(frames) if k == 0 or i - frames[k - 1] > 1]
        regs.append(
            {
                "box": [round(x, 2) for x in box],
                "change_moments": moments,
                "shape": "band" if w_px >= 2 * h_px else "block",
                "_steps": starts,
            }
        )
    regs.sort(key=lambda r: -r["change_moments"])
    seen_boxes, uniq = set(), []
    for r in regs:
        if tuple(r["box"]) not in seen_boxes:
            seen_boxes.add(tuple(r["box"]))
            uniq.append(r)
    regs = uniq
    for k, r in enumerate(regs[:4], 1):
        r["id"] = f"R{k}"
    return regs[:4]


def region_settles(video, info, regs, N):
    """How text-like a suggested region is: at each of its change moments, the share of the pixels that
    changed which then hold to within compression noise for the next three frames. Drawn text swaps in
    and then sits still; a moving person or object keeps changing. Median over the moments."""
    W, H = info["width"], info["height"]
    for r_ in regs:
        steps = r_.pop("_steps", [])
        cx, cy, cw, ch = _box_px(r_["box"], W, H)
        ow = even(min(160, cw))
        oh = max(4, round(ow * ch / cw / 2) * 2)
        n = ow * oh
        rr = run(
            [
                "ffmpeg",
                "-hide_banner",
                "-nostdin",
                "-loglevel",
                "error",
                "-i",
                video,
                "-an",
                "-vf",
                f"crop={cw}:{ch}:{cx}:{cy},scale={ow}:{oh}:flags=area,format=gray,tblend=all_mode=difference",
                "-fps_mode",
                "passthrough",
                "-f",
                "rawvideo",
                "-",
            ]
        )
        raw = rr.stdout
        difs = [b""] + [raw[i : i + n] for i in range(0, len(raw) - n + 1, n)]
        # the exit status is not needed: a failed decode gives the wrong frame count, and the region is
        # then left without a "settles" value
        if len(difs) != N or not steps:
            continue
        tc = above(24)
        tm = above(EXACT_T)
        vals = []
        for i in steps:
            if i + 3 >= N:
                continue
            C_ = int.from_bytes(difs[i].translate(tc), "big")
            if not C_:
                continue
            later = 0
            for k in (1, 2, 3):
                later |= int.from_bytes(difs[i + k].translate(tm), "big")
            vals.append(_pc(C_ & ~later) / _pc(C_))
        if vals:
            r_["settles"] = round(statistics.median(vals), 2)
    regs.sort(key=lambda r_: -(r_.get("settles", 0.5)))
    for k, r_ in enumerate(regs, 1):
        r_["id"] = f"R{k}"
    return regs


FIX_W = 360  # analysis width for finding layers that hold while the picture moves
FIX_MOVING = 0.85  # a 1 s block counts when this share of the picture changes in it (camera move or cut)
FIX_HELD = 0.75  # a pixel is part of a fixed layer when it holds in this share of such blocks


def fixed_layers(video, info, pts, tmp):
    """Layers that never change while the picture behind them moves: a caption, title, logo or
    watermark that stays up. Such a layer never steps, so text_regions cannot find it. A drawn layer
    sits on top of the picture, so its stroke pixels hold to within compression noise while the
    camera moves or the shot cuts; filmed things do not. Only 1 s blocks where nearly the whole
    picture changes (camera move, cut) separate the two; a locked shot says nothing."""
    W, H = info["width"], info["height"]
    aw = even(min(FIX_W, W))
    ah = max(8, round(aw * H / W / 2) * 2)
    npx = aw * ah
    dpath, gpath = os.path.join(tmp, "fix_d.raw"), os.path.join(tmp, "fix_g.raw")
    fc = f"[0:v]scale={aw}:{ah}:flags=area,format=gray,split[g][t];[t]tblend=all_mode=difference[d]"
    r = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-y",
            "-loglevel",
            "error",
            "-i",
            video,
            "-an",
            "-filter_complex",
            fc,
            "-map",
            "[d]",
            "-fps_mode",
            "passthrough",
            "-f",
            "rawvideo",
            dpath,
            "-map",
            "[g]",
            "-fps_mode",
            "passthrough",
            "-f",
            "rawvideo",
            gpath,
        ]
    )
    if r.returncode != 0:
        return {"blocks_used": 0, "layers": [], "note": "decode failed"}
    tab = above(HOLD_T)  # moved: a layer does not
    tabm = above(EXACT_T)  # changed at all: the picture moves
    ALL = int.from_bytes(b"\x01" * npx, "big")
    blocks, cur, curm, t0 = [], 0, 0, 0.0
    with open(dpath, "rb") as f:
        k = 0
        while True:
            buf = f.read(npx)
            if len(buf) < npx:
                break
            k += 1  # diff k = change into frame k
            if k >= len(pts):
                break
            cur |= int.from_bytes(buf.translate(tab), "big")
            curm |= int.from_bytes(buf.translate(tabm), "big")
            if pts[k] - t0 >= 1.0 or k == len(pts) - 1:
                blocks.append((t0, pts[k], cur, curm))
                cur, curm, t0 = 0, 0, pts[k]
    moving = [(a_, b_, m) for a_, b_, m, mm in blocks if _pc(mm) >= FIX_MOVING * npx]
    res = {"blocks_used": len(moving), "blocks": len(blocks), "layers": []}
    if len(moving) < 2:
        res["note"] = "the picture never moved enough to separate a fixed layer from it"
        return res
    counts = bytearray(npx)
    for _, _, m in moving:
        held = (ALL & ~m).to_bytes(npx, "big")
        counts = bytearray(a_ + b_ for a_, b_ in zip(counts, held))
    need = math.ceil(FIX_HELD * len(moving))
    cand = [k for k in range(npx) if counts[k] >= need]
    if not cand:
        return res
    # keep candidates on drawn strokes: 3x3 gray range >= 40 in a frame from the middle
    gsz = os.path.getsize(gpath) // npx
    with open(gpath, "rb") as f:
        f.seek((gsz // 2) * npx)
        g = f.read(npx)
    cell = 8
    gc, gr = math.ceil(aw / cell), math.ceil(ah / cell)
    cnt = [0] * (gc * gr)
    for k in cand:
        y, x = divmod(k, aw)
        if 0 < y < ah - 1 and 0 < x < aw - 1:
            nb = [g[k + dy * aw + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1)]
            if max(nb) - min(nb) >= 40:
                cnt[(y // cell) * gc + x // cell] += 1
    mask = [c >= 3 for c in cnt]
    parts = []
    for comp in components(mask, gc, gr):
        rs = [q // gc for q in comp]
        cs = [q % gc for q in comp]
        parts.append(
            [
                min(cs) * cell / aw,
                min(rs) * cell / ah,
                min(1.0, (max(cs) + 1) * cell / aw),
                min(1.0, (max(rs) + 1) * cell / ah),
                sum(cnt[q] for q in comp),
            ]
        )
    # pieces of one line of text (words, thin letters) sit on the same rows: join pieces whose
    # rows overlap and that lie within a fifth of the frame width of each other, and stacked lines
    merged = True
    while merged:
        merged = False
        for i in range(len(parts)):
            for j in range(i + 1, len(parts)):
                a_, b_ = parts[i], parts[j]
                ov = min(a_[3], b_[3]) - max(a_[1], b_[1])
                gap = max(a_[0], b_[0]) - min(a_[2], b_[2])
                vgap = max(a_[1], b_[1]) - min(a_[3], b_[3])
                same_line = ov > 0.5 * min(a_[3] - a_[1], b_[3] - b_[1]) and gap < 0.2
                next_line = vgap < max(a_[3] - a_[1], b_[3] - b_[1]) and gap < 0  # stacked lines
                if same_line or next_line:
                    parts[i] = [
                        min(a_[0], b_[0]),
                        min(a_[1], b_[1]),
                        max(a_[2], b_[2]),
                        max(a_[3], b_[3]),
                        a_[4] + b_[4],
                    ]
                    del parts[j]
                    merged = True
                    break
            if merged:
                break
    for x0, y0, x1, y1, px in parts:
        if px < 40:
            continue
        mx, my = 0.02, 0.01
        box = [
            round(max(0.0, x0 - mx), 2),
            round(max(0.0, y0 - my), 2),
            round(min(1.0, x1 + mx), 2),
            round(min(1.0, y1 + my), 2),
        ]
        res["layers"].append({"box": box, "stroke_px": px})
    res["layers"].sort(key=lambda L_: -L_["stroke_px"])
    res["layers"] = res["layers"][:4]
    for k, L_ in enumerate(res["layers"], 1):
        L_["id"] = f"F{k}"
    return res
