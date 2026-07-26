"""Tiny dependency-free SVG chart helpers. Pure string building, no libs."""
import math

PALETTE = {
    "accent": "#5ec8f8",
    "accent2": "#f8b95e",
    "grid": "#2a2f3a",
    "text": "#aab2c0",
    "bg": "#171a21",
}

# Apple Fitness activity ring colors.
RING_COLORS = {
    "move": ("#fa114f", "#ff5e8f"),        # (base, overflow-lap tint)
    "exercise": ("#92e82a", "#c3ff7a"),
    "stand": ("#1eeaef", "#7ff5f8"),
}
RING_TRACK = "#3a2230"


def _ring_point(cx, cy, r, frac):
    theta = math.radians(360 * frac - 90)
    return cx + r * math.cos(theta), cy + r * math.sin(theta)


def _ring_arc_path(cx, cy, r, frac):
    """Path for a clockwise arc from the top (12 o'clock), covering `frac` of
    a full circle (0..1). frac >= ~1 is drawn as a full loop (two half-arcs,
    since an SVG arc command can't express a 360-degree sweep in one span)."""
    if frac <= 0:
        return None
    if frac >= 0.9995:
        x0, y0 = _ring_point(cx, cy, r, 0)
        x1, y1 = _ring_point(cx, cy, r, 0.5)
        return (f"M {x0:.2f} {y0:.2f} A {r:.2f} {r:.2f} 0 1 1 {x1:.2f} {y1:.2f} "
                f"A {r:.2f} {r:.2f} 0 1 1 {x0:.2f} {y0:.2f}")
    x0, y0 = _ring_point(cx, cy, r, 0)
    x1, y1 = _ring_point(cx, cy, r, frac)
    large = 1 if frac > 0.5 else 0
    return f"M {x0:.2f} {y0:.2f} A {r:.2f} {r:.2f} 0 {large} 1 {x1:.2f} {y1:.2f}"


def ring_progress(cx, cy, r, stroke, frac, color, overflow_color, track_color=RING_TRACK):
    """One Apple-style activity ring: dim track + progress arc with rounded
    caps. frac > 1 draws a full base lap plus a brighter overlay arc for the
    extra amount, mimicking how Apple shows rings that exceed their goal."""
    parts = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{track_color}" '
             f'stroke-width="{stroke}"/>']
    base_frac = min(frac, 1.0)
    path = _ring_arc_path(cx, cy, r, base_frac)
    if path:
        parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="{stroke}" '
                     f'stroke-linecap="round"/>')
    if frac > 1.0:
        over_path = _ring_arc_path(cx, cy, r, frac - 1.0)
        if over_path:
            parts.append(f'<path d="{over_path}" fill="none" stroke="{overflow_color}" '
                         f'stroke-width="{stroke}" stroke-linecap="round"/>')
    return "".join(parts)


def activity_rings(move_frac, exercise_frac, stand_frac, size=280, stroke=22, gap=6):
    """Three concentric Apple-style rings: Move (outer, red), Exercise
    (middle, green), Stand (inner, cyan)."""
    cx = cy = size / 2
    r_move = size / 2 - stroke / 2 - 2
    r_ex = r_move - stroke - gap
    r_stand = r_ex - stroke - gap
    parts = [f'<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">']
    move_c, move_o = RING_COLORS["move"]
    ex_c, ex_o = RING_COLORS["exercise"]
    stand_c, stand_o = RING_COLORS["stand"]
    parts.append(ring_progress(cx, cy, r_move, stroke, move_frac, move_c, move_o))
    parts.append(ring_progress(cx, cy, r_ex, stroke, exercise_frac, ex_c, ex_o))
    parts.append(ring_progress(cx, cy, r_stand, stroke, stand_frac, stand_c, stand_o))
    parts.append("</svg>")
    return "".join(parts)


def mini_rings(move_frac, exercise_frac, stand_frac, size=44, stroke=5, gap=2):
    return activity_rings(move_frac, exercise_frac, stand_frac, size=size, stroke=stroke, gap=gap)


def zone_gauge(value, zones, width=560, height=64, vmax=2.0):
    """Horizontal banded gauge (e.g. training-load zones) with a pointer.
    zones: list of (lo, hi, label, color) covering [0, vmax]."""
    pad_l, pad_r, bar_y, bar_h = 10, 10, 20, 18
    plot_w = width - pad_l - pad_r

    def x(v):
        return pad_l + plot_w * max(0.0, min(v, vmax)) / vmax

    parts = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
             f'font-family="ui-monospace,monospace" font-size="10">']
    for lo, hi, label, color in zones:
        x0, x1 = x(lo), x(hi)
        parts.append(f'<rect x="{x0:.1f}" y="{bar_y}" width="{(x1-x0):.1f}" height="{bar_h}" '
                     f'rx="3" fill="{color}" opacity="0.85"/>')
        parts.append(f'<text x="{(x0+x1)/2:.1f}" y="{bar_y+bar_h+14}" fill="{PALETTE["text"]}" '
                     f'text-anchor="middle">{label}</text>')
    px = x(value)
    parts.append(f'<polygon points="{px-6:.1f},{bar_y-8} {px+6:.1f},{bar_y-8} {px:.1f},{bar_y-1}" fill="#fff"/>')
    parts.append(f'<text x="{px:.1f}" y="{bar_y-11}" fill="#fff" text-anchor="middle" '
                 f'font-size="11" font-weight="bold">{value:.2f}</text>')
    parts.append("</svg>")
    return "".join(parts)


def _scale(values, lo=None, hi=None):
    vals = [v for v in values if v is not None]
    if not vals:
        return 0, 1
    lo = min(vals) if lo is None else lo
    hi = max(vals) if hi is None else hi
    if lo == hi:
        lo, hi = lo - 1, hi + 1
    return lo, hi


def line_chart(values, width=560, height=140, color=PALETTE["accent"],
               baseline=None, baseline_band=None, y_fmt=lambda v: f"{v:.0f}"):
    """values: list of (label, value|None). baseline: horizontal reference value.
    baseline_band: (lo, hi) shaded band, e.g. rolling mean +/- stddev."""
    pad_l, pad_r, pad_t, pad_b = 36, 10, 10, 20
    plot_w, plot_h = width - pad_l - pad_r, height - pad_t - pad_b
    nums = [v for _, v in values]
    lo, hi = _scale(nums + ([baseline] if baseline is not None else []) +
                     (list(baseline_band) if baseline_band else []))
    n = len(values)

    def x(i):
        return pad_l + (plot_w * i / max(n - 1, 1))

    def y(v):
        return pad_t + plot_h - (plot_h * (v - lo) / (hi - lo))

    parts = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
             f'font-family="ui-monospace,monospace" font-size="10">']
    parts.append(f'<rect width="{width}" height="{height}" fill="{PALETTE["bg"]}"/>')

    for frac in (0, 0.5, 1):
        gy = pad_t + plot_h * (1 - frac)
        gv = lo + (hi - lo) * frac
        parts.append(f'<line x1="{pad_l}" y1="{gy:.1f}" x2="{width-pad_r}" y2="{gy:.1f}" '
                     f'stroke="{PALETTE["grid"]}" stroke-width="1"/>')
        parts.append(f'<text x="2" y="{gy+3:.1f}" fill="{PALETTE["text"]}">{y_fmt(gv)}</text>')

    if baseline_band:
        blo, bhi = baseline_band
        parts.append(f'<rect x="{pad_l}" y="{y(bhi):.1f}" width="{plot_w:.1f}" '
                     f'height="{(y(blo)-y(bhi)):.1f}" fill="{color}" opacity="0.12"/>')
    if baseline is not None:
        parts.append(f'<line x1="{pad_l}" y1="{y(baseline):.1f}" x2="{width-pad_r}" y2="{y(baseline):.1f}" '
                     f'stroke="{color}" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>')

    points = [(x(i), y(v)) for i, (_, v) in enumerate(values) if v is not None]
    if len(points) >= 2:
        path = "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in points)
        parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="2"/>')
    for px, py in points:
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2.5" fill="{color}"/>')

    step = max(1, n // 7)
    for i, (label, _) in enumerate(values):
        if i % step == 0 or i == n - 1:
            parts.append(f'<text x="{x(i):.1f}" y="{height-4}" fill="{PALETTE["text"]}" '
                         f'text-anchor="middle">{label}</text>')
    parts.append("</svg>")
    return "".join(parts)


def sparkline(values, width=140, height=36, color=PALETTE["accent"]):
    lo, hi = _scale(values)
    n = len(values)
    if n == 0:
        return f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg"></svg>'

    def x(i):
        return 2 + (width - 4) * i / max(n - 1, 1)

    def y(v):
        return height - 2 - (height - 4) * (v - lo) / (hi - lo)

    points = [(x(i), y(v)) for i, v in enumerate(values) if v is not None]
    path = "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in points) if len(points) >= 2 else ""
    circle = ""
    if points:
        lx, ly = points[-1]
        circle = f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="2" fill="{color}"/>'
    return (f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{path}" fill="none" stroke="{color}" stroke-width="1.5"/>{circle}</svg>')


def stacked_bar(days, series, colors, width=560, height=160):
    """days: list of labels. series: dict[name] -> list of values aligned with days."""
    pad_l, pad_r, pad_t, pad_b = 36, 10, 10, 20
    plot_w, plot_h = width - pad_l - pad_r, height - pad_t - pad_b
    n = len(days)
    totals = [sum(series[k][i] or 0 for k in series) for i in range(n)]
    hi = max(totals) if totals else 1
    hi = hi or 1
    bar_w = plot_w / max(n, 1) * 0.6
    gap = plot_w / max(n, 1)

    parts = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
             f'font-family="ui-monospace,monospace" font-size="10">']
    parts.append(f'<rect width="{width}" height="{height}" fill="{PALETTE["bg"]}"/>')
    for i, day in enumerate(days):
        cx = pad_l + gap * i + (gap - bar_w) / 2
        cy = pad_t + plot_h
        for name in series:
            v = series[name][i] or 0
            bh = plot_h * v / hi
            cy -= bh
            parts.append(f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{bar_w:.1f}" height="{bh:.1f}" '
                         f'fill="{colors[name]}"/>')
        parts.append(f'<text x="{cx+bar_w/2:.1f}" y="{height-4}" fill="{PALETTE["text"]}" '
                     f'text-anchor="middle">{day}</text>')
    legend_x = width - pad_r
    for j, name in enumerate(series):
        ly = pad_t + j * 12
        parts.append(f'<rect x="{legend_x-70}" y="{ly}" width="8" height="8" fill="{colors[name]}"/>')
        parts.append(f'<text x="{legend_x-58}" y="{ly+8}" fill="{PALETTE["text"]}">{name}</text>')
    parts.append("</svg>")
    return "".join(parts)


def calendar_heatmap(day_values, all_days, color=PALETTE["accent"], cell=16, cols=7):
    """day_values: dict[date_str]->value (None/missing = no data). all_days: ordered list of date_str."""
    vals = [v for v in day_values.values() if v is not None]
    hi = max(vals) if vals else 1
    hi = hi or 1
    rows = (len(all_days) + cols - 1) // cols
    width, height = cols * (cell + 3) + 4, rows * (cell + 3) + 4
    parts = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
             f'font-family="ui-monospace,monospace" font-size="8">']
    parts.append(f'<rect width="{width}" height="{height}" fill="{PALETTE["bg"]}"/>')
    for i, day in enumerate(all_days):
        col, row = i % cols, i // cols
        x, y = 4 + col * (cell + 3), 4 + row * (cell + 3)
        v = day_values.get(day)
        if v is None:
            fill, opacity = PALETTE["grid"], "1"
        else:
            opacity = f"{0.15 + 0.85 * (v / hi):.2f}"
            fill = color
        parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" '
                     f'fill="{fill}" opacity="{opacity}"><title>{day}: '
                     f'{"no data" if v is None else round(v, 1)}</title></rect>')
    parts.append("</svg>")
    return "".join(parts)
