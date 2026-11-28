"""Laying out cells into contact sheets within the image budget."""

import math
import os
import re

from .constants import FONT_CANDIDATES, MAX_PIXELS, MAX_SIDE, PAD
from .media import concat_q, fq, run
from .transcript import is_wide
from .util import die, write_text


def tokens_of(w, h):
    return math.ceil(w / 28) * math.ceil(h / 28)


def image_size(path):
    r = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height",
            "-of",
            "csv=p=0",
            path,
        ]
    )
    w, h = r.stdout.decode().strip().split(",")[:2]
    return int(w), int(h)


def font_path():
    for f in FONT_CANDIDATES:
        if f and os.path.exists(f):
            return f
    return None


# ----------------------------------------------------------------------------- rendering
def fit_cell(aspect, label_h, cap_w=MAX_SIDE, cap_h=MAX_SIDE, cap_px=MAX_PIXELS):
    """Largest even cell width w (height w/aspect + label) inside the image caps."""
    w = min(cap_w, int((cap_h - label_h) * aspect))
    while w > 16:
        h = round(w / aspect / 2) * 2 + label_h
        if h <= cap_h and w * h <= cap_px:
            break
        w -= 2
    return w - (w % 2)


def plan_grid(cell_w, cell_h, n):
    """cols x rows that hold the most cells within the caps (ties: squarer sheet)."""
    best = None
    for cols in range(1, 41):
        W = cols * cell_w + (cols - 1) * PAD
        if W > MAX_SIDE:
            break
        for rows in range(1, 41):
            H = rows * cell_h + (rows - 1) * PAD
            if H > MAX_SIDE or W * H > MAX_PIXELS:
                break
            key = (min(cols * rows, n), -abs(W - H))
            if best is None or key > best[0]:
                best = (key, cols, rows)
    if best is None:
        die("cell too large for one image")
    return best[1], best[2]


def label_fs(cell_w):
    """Font size of the labels under a cell this wide."""
    return max(12, min(22, round(cell_w / 15)))


def wrap(text, width_px, fs, max_lines):
    def cw(ch):
        return fs * (1.0 if is_wide(ch) else 0.56)

    lines, cur, curw = [], "", 0.0
    tokens = re.findall(r"[\u2e80-\uffff]|[^\s\u2e80-\uffff]+|\s+", text)
    for tok in tokens:
        if tok.isspace():
            if cur:
                cur += " "
                curw += cw(" ")
            continue
        tw = sum(cw(c) for c in tok)
        if curw + tw > width_px and cur.strip():
            lines.append(cur.rstrip())
            cur, curw = "", 0.0
        cur += tok
        curw += tw
    if cur.strip():
        lines.append(cur.rstrip())
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: max(1, len(lines[-1]) - 1)] + "…"
    return lines


def compose(cells, cell_w, cell_h, n_lines, out_prefix, tmp, grid=False, cols_hint=None):
    """cells: list of dict(path, lines[list], box(optional fractions), dim(bool)).
    Writes sheet(s) <out_prefix>_NN.jpg (or <out_prefix>.jpg when one) within the caps."""
    font = font_path()
    fs = label_fs(cell_w)
    lh = round(fs * 1.25)
    label_h = n_lines * lh + 6 if n_lines else 0
    total_h = cell_h + label_h
    cols, rows = plan_grid(cell_w, total_h, len(cells))
    if cols_hint:
        cols = min(cols_hint, cols)
        rows = min(rows, max(1, (MAX_PIXELS // ((cols * cell_w) or 1)) // (total_h + PAD)))
        rows = min(rows, (MAX_SIDE + PAD) // (total_h + PAD))
    per = cols * rows
    outs = []
    nsheets = math.ceil(len(cells) / per)
    for si in range(nsheets):
        chunk = cells[si * per : (si + 1) * per]
        c_ = min(cols, len(chunk)) if not cols_hint else cols
        r_ = math.ceil(len(chunk) / c_)
        lst = os.path.join(tmp, f"concat_{os.path.basename(out_prefix)}_{si}.txt")
        with open(lst, "w", encoding="utf-8") as f:
            f.write("ffconcat version 1.0\n")
            for c in chunk:
                f.write(f"file {concat_q(c['path'])}\nduration 0.04\n")
        parts = ["[0:v]setpts=N/25/TB"]
        if grid:
            parts.append("drawgrid=w=iw/10:h=ih/10:t=1:c=white@0.28")
        if label_h:
            parts.append(f"pad=iw:ih+{label_h}:0:0:color=black")
        for k, c in enumerate(chunk):
            if c.get("box"):
                x0, y0, x1, y1 = c["box"]
                parts.append(
                    f"drawbox=x={int(x0 * cell_w)}:y={int(y0 * cell_h)}:w={max(4, int((x1 - x0) * cell_w))}:"
                    f"h={max(4, int((y1 - y0) * cell_h))}:color=red@0.9:t=3:enable='eq(n\\,{k})'"
                )
            for li, text in enumerate(c["lines"][:n_lines]):
                if not text:
                    continue
                tf = os.path.join(tmp, f"lbl_{os.path.basename(out_prefix)}_{si}_{k}_{li}.txt")
                write_text(tf, text)
                color = "yellow" if (li == 0 and c.get("hi")) else "white"
                fo = f"fontfile={fq(font)}:" if font else ""
                parts.append(
                    f"drawtext={fo}textfile={fq(tf)}:expansion=none:fontsize={fs}:"
                    f"fontcolor={color}:x=4:y=h-{label_h}+3+{li * lh}:enable='eq(n\\,{k})'"
                )
        parts.append(f"tile={c_}x{r_}:padding={PAD}:color=0x3a3a3a")
        script = os.path.join(tmp, f"compose_{os.path.basename(out_prefix)}_{si}.txt")
        write_text(script, ",\n".join(parts) + "[o]")
        out = f"{out_prefix}_{si + 1:02d}.jpg" if nsheets > 1 else f"{out_prefix}.jpg"
        r = run(
            [
                "ffmpeg",
                "-hide_banner",
                "-nostdin",
                "-y",
                "-loglevel",
                "error",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                lst,
                "-/filter_complex",
                script,
                "-map",
                "[o]",
                "-frames:v",
                "1",
                "-q:v",
                "2",
                out,
            ]
        )
        if r.returncode != 0:
            die("compose failed: " + r.stderr.decode()[-600:])
        w, h = image_size(out)
        if w > MAX_SIDE or h > MAX_SIDE or w * h > MAX_PIXELS:
            die(f"internal: {out} is {w}x{h}, over the cap")
        outs.append({"path": out, "w": w, "h": h, "tokens": tokens_of(w, h), "cells": len(chunk)})
    return outs


def cell_dims(info, crop, long_side):
    W, H = info["width"], info["height"]
    if crop:
        W, H = (crop[2] - crop[0]) * W, (crop[3] - crop[1]) * H
    a = W / H
    if a >= 1:
        w = long_side
        h = round(long_side / a / 2) * 2
    else:
        h = long_side
        w = round(long_side * a / 2) * 2
    return max(16, w), max(16, h), a


def report_images(imgs, d, mark=None):
    """Each image with its size and token cost. `mark`, for a view a detail mark may name, gives per
    image the text after the bar ({words|NAME}) and what it shows, printed as the name to use."""
    tot = 0
    for k, im in enumerate(imgs):
        rel = os.path.relpath(im["path"], d)
        print(f"  {rel}  {im['w']}x{im['h']}  ~{im['tokens']} tok")
        if mark:
            print(f"      in a mark: {mark[k]}")
        tot += im["tokens"]
    print(f"  total ~{tot} image tokens")
    return tot


def page_times(imgs, times):
    """The moments each page of a sheet shows: pages hold their cells in order."""
    out, k = [], 0
    for im in imgs:
        out.append(times[k : k + im["cells"]])
        k += im["cells"]
    return out
