"""`element`: drawn elements and panes, measured box and on/off times."""

import os
import shutil
import statistics

from .constants import EXACT_T, STILL_MOVING
from .layers import state_samples
from .media import _bbox, _grow, _open, decode_gray_all, decode_rgb, run
from .picture import components
from .scandir import load_dir, nearest_frame, parse_box, record_followup, scratch_dir
from .util import _box_px, _overlap, _pc, above, at_most, even, write_json

# ----------------------------------------------------------------------------- drawn elements and panes
EL_W = 360  # analysis width for timing an element (the search area, not the frame)
EL_TOL = 10  # an element pixel "still shows it" when its gray level is within this of the reference
EL_EXACT = 12  # on native pixels a drawn element holds to within this (a still person does not)
EL_NATIVE_MAX = 1280  # box refinement decodes the search area at native pixels up to this width


EL_FAR = 4 * EL_TOL  # a pixel this far from its held value shows something else: the element is not there
EL_MIN_PX = 20  # fewer pixels than this holding together is no element (specks of the picture)
EL_INSIDE_MIN = 0.05  # the pixels that come and go together must cover this share of the rough box
EL_FADE_FRAMES = 20  # a fade or slide is looked for over this many frames before it settles (after it leaves)
EL_FADE_NEAR = 0.8  # a frame of a fade lies this share or less of the picture's distance from the element
EL_SUPPORT = 0.08  # an edge row (column) of the box holds at least this share of the widest row (column)
EL_BOX_INSIDE = 0.7  # what was measured must lie this much inside the box pointed at, else it is another layer
EL_FULL_FRAME = 0.6  # what came and went with it covering this share of the frame is a full-frame card


class _Found:
    """Where one pass of measure_element found the element: in time (the frames it settles on and starts
    leaving), and in the search area (its mask and box in analysis pixels)."""


def _search_area(rough, grow):
    """The rough box widened by `grow` times its size each side (and 2% of the frame), as fractions."""
    bw, bh = rough[2] - rough[0], rough[3] - rough[1]
    return (
        max(0.0, rough[0] - grow * bw - 0.02),
        max(0.0, rough[1] - grow * bh - 0.02),
        min(1.0, rough[2] + grow * bw + 0.02),
        min(1.0, rough[3] + grow * bh + 0.02),
    )


def _still_masks(D, n):
    """Per frame: pixels that still show the reference (every color plane within EL_TOL of it; gray
    alone would join a red mark to the dark red cloth behind it), and pixels far from it (the element
    is not there at all)."""
    tab = at_most(EL_TOL)
    tabj = above(EL_FAR)
    Mk, Jf = [], []
    for b in D:
        t3 = b.translate(tab)
        Mk.append(
            int.from_bytes(t3[:n], "big") & int.from_bytes(t3[n : 2 * n], "big") & int.from_bytes(t3[2 * n :], "big")
        )
        j3 = b.translate(tabj)
        Jf.append(
            int.from_bytes(j3[:n], "big") | int.from_bytes(j3[n : 2 * n], "big") | int.from_bytes(j3[2 * n :], "big")
        )
    return Mk, Jf


def _rough_inside(rough, area_px, ow, oh, W, H):
    """The rough box inside the search area, as one byte (0/1) per analysis pixel."""
    cx, cy, cw, ch = area_px
    inb = bytearray(ow * oh)
    for y in range(oh):
        fy = (cy + (y + 0.5) * ch / oh) / H
        if rough[1] <= fy <= rough[3]:
            for x in range(ow):
                fx = (cx + (x + 0.5) * cw / ow) / W
                if rough[0] <= fx <= rough[2]:
                    inb[y * ow + x] = 1
    return inb


def _hold_ends(Mk, r, N, ONE):
    """Follow every pixel forward and back from the reference frame r while it holds: dead[f] = pixels
    that stop holding at frame f (dead[N]: hold to the end); born[f] = pixels that hold from frame f."""
    alive, dead = ONE, {}
    for i in range(r + 1, N):
        nxt = alive & Mk[i]
        if nxt != alive:
            dead[i] = alive & ~nxt
        alive = nxt
    dead[N] = alive
    alive, born = ONE, {}
    for i in range(r - 1, -1, -1):
        nxt = alive & Mk[i]
        if nxt != alive:
            born[i + 1] = alive & ~nxt
        alive = nxt
    born[0] = alive
    return dead, born


def _find_once(video, W, H, N, r, rough, grow, tmp):
    """One pass over the search area `grow` makes: returns (why, None) when the evidence does not
    settle where the element is, else (None, found)."""
    f = _Found()
    f.area = _search_area(rough, grow)
    cx, cy, cw, ch = f.px = _box_px(list(f.area), W, H)
    ow = f.ow = even(min(EL_W, cw))
    oh = f.oh = max(8, round(ow * ch / cw / 2) * 2)
    n = ow * oh
    D = decode_gray_all(video, (cx, cy, cw, ch), ow, oh, tmp, ref_frame=r)
    if not D or len(D) != N:
        return "decode failed", None
    Mk, Jf = _still_masks(D, n)
    f.Mk = Mk
    ONE = int.from_bytes(b"\x01" * n, "big")
    inb = _rough_inside(rough, f.px, ow, oh, W, H)
    INB = int.from_bytes(bytes(inb), "big")
    dead, born = _hold_ends(Mk, r, N, ONE)

    # the element's edges in time: the frames (+ the next two) where most rough-box pixels stop
    # holding; pixels that stop within two frames of the reference are the picture moving
    def edge(table, lo, hi):
        # a drawn element appears and leaves on one frame, jumping between its color and the
        # picture's: count, per frame alone, the pixels that start (stop) holding and were (are then)
        # far from their held color. A still part of the picture comes to rest, and starts moving,
        # pixel by pixel over several frames and in small steps
        best = None
        for fr in sorted(table):
            if not lo <= fr <= hi:
                continue
            c = _pc(table[fr] & INB & (Jf[fr] if fr < N else -1))
            if best is None or c > best[1]:
                best = (fr, c)
        return best

    b_ = edge(dead, r + 3, N)
    if not b_:
        return "nothing holds past the reference frame", None
    EB = 0
    for k in range(3):
        EB |= dead.get(b_[0] + k, 0)
    a_ = None
    best = 0
    for fr in sorted(born):
        if fr > r - 2:
            continue
        c = _pc(born[fr] & EB & INB & (Jf[fr - 1] if fr > 0 else -1))
        if c > best:
            a_, best = fr, c
    if a_ is None:
        return "nothing holds before the reference frame", None
    BA = 0
    for k in range(3):
        BA |= born.get(a_ - k, 0)
    E = EB & BA
    if _pc(E) < EL_MIN_PX or _pc(E & INB) < EL_INSIDE_MIN * _pc(INB):
        return (
            f"no group of pixels inside the box appears and disappears together ({_pc(E & INB)} px of {_pc(INB)})",
            None,
        )
    eb = E.to_bytes(n, "big")
    # the element is the connected group with most pixels inside the rough box (specks of the
    # picture that happened to hold over the same frames lie apart from it)
    comps = components(list(eb), ow, oh)
    # a drawn element appears on one frame (or fades in together); a still part of the picture
    # comes to rest pixel by pixel: prefer the group whose pixels began holding on the same frame
    b1 = born.get(a_, 0).to_bytes(n, "big")
    d1 = dead.get(b_[0], 0).to_bytes(n, "big")

    def score(c):
        sync = sum(1 for q in c if b1[q] or d1[q]) / len(c)
        return sum(inb[q] for q in c) * sync * sync

    group = max(comps, key=score) if comps else []
    keep = bytearray(n)
    for q in group:
        keep[q] = 1
    if len(group) < EL_MIN_PX:
        return "the pixels that hold together are scattered", None
    f.eb = bytes(keep)
    f.E = int.from_bytes(f.eb, "big")
    f.ne = _pc(f.E)
    f.bb = _bbox(f.eb, ow, oh, min_px=1)
    if not f.bb:
        return "the pixels that hold together are scattered", None
    f.a_, f.b_ = a_, b_[0]
    return None, f


def _touches(f):
    """Does the element reach a side of the search area that could still grow?"""
    bb, (sx0, sy0, sx1, sy1) = f.bb, f.area
    return (
        (bb[0] == 0 and sx0 > 0)
        or (bb[1] == 0 and sy0 > 0)
        or (bb[2] == f.ow and sx1 < 1)
        or (bb[3] == f.oh and sy1 < 1)
    )


def _visible_edges(video, f, W, H, N, cuts, tmp):
    """The element holds from frame a_ (in place) until frame b_. A fade or slide shows as frames before
    a_ (after b_) whose colors already lie part of the way to the element's: its first visible frame
    is the first one clearly nearer to the element than the picture was before it came. Returns the
    first frame showing it and the first frame not showing it."""
    a_, b_ = f.a_, f.b_
    cx, cy, cw, ch = f.px
    eb_ = _bbox(f.eb, f.ow, f.oh, min_px=1)
    ex = (cx + eb_[0] * cw / f.ow, cy + eb_[1] * ch / f.oh, cx + eb_[2] * cw / f.ow, cy + eb_[3] * ch / f.oh)
    a0, b0 = a_, b_
    ew = max(2, even(min(120, int(ex[2] - ex[0]))))
    eh_ = max(2, round(ew * (ex[3] - ex[1]) / max(1, ex[2] - ex[0]) / 2) * 2)
    epx = _box_px([ex[0] / W, ex[1] / H, ex[2] / W, ex[3] / H], W, H)
    near = list(range(max(0, a_ - EL_FADE_FRAMES), a_ + 1)) + list(
        range(max(0, b_ - 1), min(N, b_ + EL_FADE_FRAMES + 1))
    )
    R_ = decode_rgb(video, near, epx, ew, eh_, tmp)
    if not R_:
        return a0, b0

    def dist(fr, ref):
        A_, B_ = R_[fr], R_[ref]
        return sum(abs(A_[k] - B_[k]) for k in range(0, len(A_), 3)) / (len(A_) / 3)

    cset = set(cuts)
    prev_cut = max([c for c in cuts if c <= a_] or [0])
    next_cut = min([c for c in cuts if c >= b_] or [N])
    # a cut is a hard edge: an element that starts (ends) on a cut is not faded across it
    before = [] if a_ in cset else [fr for fr in range(max(prev_cut, a_ - EL_FADE_FRAMES), a_)]
    # the picture without the element: the typical distance well before it came (after it left)
    if before:
        dv = {fr: dist(fr, a_) for fr in before}
        far = [dv[fr] for fr in before if fr <= a_ - 6] or list(dv.values())
        base = statistics.median(far)
        fr = a_
        while fr - 1 in dv and dv[fr - 1] <= EL_FADE_NEAR * base and base > 2 * EL_TOL:
            fr -= 1
        a0 = fr
    if b_ < N and b_ not in cset:
        after = [fr for fr in range(b_, min(next_cut, b_ + EL_FADE_FRAMES + 1))]
        dv = {fr: dist(fr, b_ - 1) for fr in after}
        far = [dv[fr] for fr in after if fr >= b_ + 5] or list(dv.values())
        base = statistics.median(far)
        fr = b_
        while fr in dv and dv[fr] <= EL_FADE_NEAR * base and base > 2 * EL_TOL:
            fr += 1
        b0 = min(fr, next_cut)
    return a0, b0


def _native_mask(F, life, pre, post, sw, sh):
    """Pixels that hold through the element's life and differ from the frame before it appeared and
    the frame after it left."""
    m = bytearray(sw * sh)
    L0 = F[life[0]]
    for k in range(sw * sh):
        g = [sum(F[i][3 * k : 3 * k + 3]) / 3 for i in life]
        if max(g) - min(g) > EL_EXACT:
            continue
        v = g[0]
        if (
            pre is not None
            and abs(sum(F[pre][3 * k : 3 * k + 3]) / 3 - v) <= 2 * EL_TOL
            and max(abs(F[pre][3 * k + c] - L0[3 * k + c]) for c in range(3)) <= 2 * EL_TOL
        ):
            continue
        if post is not None and max(abs(F[post][3 * k + c] - F[life[-1]][3 * k + c]) for c in range(3)) <= 2 * EL_TOL:
            continue
        m[k] = 1
    return m


def _refine_box(video, W, H, coarse, f, life, pre, post, tmp):
    """The element's box on native pixels: what holds through its life, changed from before it appeared
    and after it left. The analysis pass can miss parts of the element: refine over the coarse box
    widened by half its size each side (more on a side the element reaches), keeping the part connected
    to the coarse core. Returns (box, measured fields) or (None, {})."""
    cw, ch = f.px[2], f.px[3]
    gw, gh = (coarse[2] - coarse[0]) * W, (coarse[3] - coarse[1]) * H
    pads = [max(4 * cw / f.ow, 0.5 * gw), max(4 * ch / f.oh, 0.5 * gh)] * 2  # left, top, right, bottom
    box, fields = None, {}
    for _ in range(4):
        rx0, ry0 = max(0, int(coarse[0] * W - pads[0])), max(0, int(coarse[1] * H - pads[1]))
        rx1, ry1 = min(W, int(coarse[2] * W + pads[2]) + 1), min(H, int(coarse[3] * H + pads[3]) + 1)
        nx, ny, nw, nh = _box_px([rx0 / W, ry0 / H, rx1 / W, ry1 / H], W, H)
        sw = even(min(nw, EL_NATIVE_MAX))
        sh = max(2, round(sw * nh / nw / 2) * 2)
        F = decode_rgb(video, life + [x for x in (pre, post) if x is not None], (nx, ny, nw, nh), sw, sh, tmp)
        if not F:
            break
        # an opening (erode, then grow back) cuts thin threads of the picture that happened to hold and
        # touch the element; parts of the element a pixel or two apart (thin strokes the opening broke)
        # are joined by taking connectivity on the mask grown by two pixels, the box on the mask itself
        m = _open(_native_mask(F, life, pre, post, sw, sh), sw, sh)
        comps = components(list(_grow(_grow(m, sw, sh), sw, sh)), sw, sh)
        core = (
            int((coarse[0] * W - nx) * sw / nw),
            int((coarse[1] * H - ny) * sh / nh),
            int((coarse[2] * W - nx) * sw / nw) + 1,
            int((coarse[3] * H - ny) * sh / nh) + 1,
        )
        if not comps:
            break

        def in_core(c, m=m, sw=sw, core=core):
            return sum(1 for q in c if m[q] and core[0] <= q % sw < core[2] and core[1] <= q // sw < core[3])

        best = [q for q in max(comps, key=in_core) if m[q]]
        if len(best) < EL_MIN_PX:
            break
        # edges where the element has real support: rows and columns holding at least 8% of its widest
        # row (column), so a speck the growth joined on does not stretch the box
        rc, cc = {}, {}
        for q in best:
            rc[q // sw] = rc.get(q // sw, 0) + 1
            cc[q % sw] = cc.get(q % sw, 0) + 1
        ys = [y for y, v in rc.items() if v >= max(2, EL_SUPPORT * max(rc.values()))]
        xs = [x for x, v in cc.items() if v >= max(2, EL_SUPPORT * max(cc.values()))]
        box = [
            (nx + min(xs) * nw / sw) / W,
            (ny + min(ys) * nh / sh) / H,
            (nx + (max(xs) + 1) * nw / sw) / W,
            (ny + (max(ys) + 1) * nh / sh) / H,
        ]
        fields = {
            "box_px": [round(box[0] * W, 1), round(box[1] * H, 1), round(box[2] * W, 1), round(box[3] * H, 1)],
            "precision_px": round(max(nw / sw, 1.0), 1),
            "fill": round(len(best) / max(1, (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)), 2),
        }
        # it reaches the edge of the window on a side that can still grow: widen that side, again
        reach = [
            min(xs) <= 1 and rx0 > 0,
            min(ys) <= 1 and ry0 > 0,
            max(xs) >= sw - 2 and rx1 < W,
            max(ys) >= sh - 2 and ry1 < H,
        ]
        if not any(reach):
            break
        pads = [p_ + (gw if k % 2 == 0 else gh) if reach[k] else p_ for k, p_ in enumerate(pads)]
    return box, fields


def measure_element(video, info, pts, rough, t, tmp, cuts=()):
    """Measure a drawn element (card, icon, logo, end card, fixed text) the agent pointed at with a
    rough box and a moment. An element is drawn over the picture: its pixels hold their value through
    its life, while the picture around or behind it moves or cuts, and they all start and stop holding
    on the same frames. So: take the frame at t as reference; follow every pixel forward and back while
    it keeps that value; the frames on which most pixels inside the rough box stop holding are the
    element's edges in time, and the pixels that stop on both those frames are the element. Its box is
    then refined on native pixels: what holds through its life and differs from the frame before it
    appeared and the frame after it left. Returns a dict; values that the evidence does not settle are
    left out with the reason."""
    W, H, N = info["width"], info["height"], len(pts)
    r = nearest_frame(pts, t)
    bw, bh = rough[2] - rough[0], rough[3] - rough[1]
    grow = 0.5
    out = {"rough_box": rough, "at": round(pts[r], 3)}
    for attempt in range(4):
        why, f = _find_once(video, W, H, N, r, rough, grow, tmp)
        if why:
            out["why"] = why
            return out
        if _touches(f) and attempt < 3:
            grow = grow * 2 + 0.5
            continue
        break
    a_, b_ = f.a_, f.b_
    a0, b0 = _visible_edges(video, f, W, H, N, cuts, tmp)
    # a drawn element shows something new; a still part of the picture uncovered by something moving
    # away showed the same pixels before (or again after)
    again = [fr for fr in range(N) if fr < a0 - 2 or fr > b0 + 2]
    out["seen_elsewhere"] = round(max([_pc(f.Mk[fr] & f.E) / f.ne for fr in again] or [0.0]), 2)
    out.update(
        {
            "on": round(pts[a0], 3),
            "settled": round(pts[a_], 3),
            "off": round(pts[b0], 3) if b0 < N else info["duration_video_s"],
            "on_frame": a0,
            "settled_frame": a_,
            "off_frame": b0,
            "leaving_from": round(pts[b_], 3) if b_ < N and b_ != b0 else None,
            "until_end": b0 >= N,
            "from_start": a0 == 0,
            "crosses_cuts": [round(pts[c], 3) for c in cuts if a0 < c < b0],
        }
    )
    # coarse box (analysis pixels) in frame fractions
    cx, cy, cw, ch = f.px
    bb = f.bb
    coarse = [
        (cx + bb[0] * cw / f.ow) / W,
        (cy + bb[1] * ch / f.oh) / H,
        (cx + bb[2] * cw / f.ow) / W,
        (cy + bb[3] * ch / f.oh) / H,
    ]
    coarse_area = (coarse[2] - coarse[0]) * (coarse[3] - coarse[1])
    if coarse_area > 4 * max(1e-6, bw * bh) and coarse_area > 0.25:
        out["box_why"] = (
            "what holds with it covers far more than the box pointed at (the picture around it "
            "holds too), so its edges are not separable here"
        )
        return out
    life = state_samples(a_ + (b_ - a_) // 4, max(a_, b_ - 1), 8)  # after any entrance animation
    pre = a0 - 1 if a0 > 0 else None
    post = b0 if b0 < N else None
    box, fields = _refine_box(video, W, H, coarse, f, life, pre, post, tmp)
    out.update(fields)
    if box is None:
        box = coarse
        out["precision_px"] = round(cw / f.ow, 1)
        out["box_note"] = "native refinement found no pixels; box from the analysis pass"
    # the element pointed at lies inside the box pointed at; what was measured must too (else the box
    # caught another layer, a caption beside it, or the picture): absent rather than wrong
    inside = _overlap(box, rough) * min(
        1.0, (rough[2] - rough[0]) * (rough[3] - rough[1]) / max(1e-9, (box[2] - box[0]) * (box[3] - box[1]))
    )
    area = (box[2] - box[0]) * (box[3] - box[1])
    if inside < EL_BOX_INSIDE and rough != [0.0, 0.0, 1.0, 1.0] and area >= EL_FULL_FRAME:
        # what came and went with it fills most of the frame: a full-frame card over a still picture (or a
        # whole new picture). Its times are measured; no box around the element alone can be
        for k in ("box_px", "precision_px", "fill"):
            out.pop(k, None)
        out["box_why"] = (
            f"what appears and leaves with it fills {area:.0%} of the frame: a full-frame card (or a "
            f"new picture, which is no element); nothing separates the element from the card"
        )
        return out
    if inside < EL_BOX_INSIDE and rough != [0.0, 0.0, 1.0, 1.0]:
        for k in ("on", "settled", "off", "leaving_from", "box_px", "precision_px", "fill"):
            out.pop(k, None)
        out["why"] = (
            f"what appears and leaves together here reaches beyond the box pointed at ({inside:.0%} of it "
            f"inside): another layer or the picture was caught; give a box around the element alone"
        )
        return out
    out["box"] = [round(v, 4) for v in box]
    out["evidence"] = (
        "held while the picture around it moved"
        if not out["crosses_cuts"]
        else "held across cut(s) " + ", ".join(f"{c:.3f}" for c in out["crosses_cuts"])
    )
    return out


def find_panes(video, info, pts, events, shots, tmp):
    """Split layouts. A pane border is a straight line across the whole frame at a fixed place (a seam
    where two pictures meet), and the two sides change independently: at some change inside its life
    one side changes far more than the other. Evidence: in the middle frame of each shot, lines along
    which nearly every pixel steps sharply from its neighbor across the line; such a line kept through
    consecutive shots, with at least one cut or panel change inside that stretch changing one side three
    times as much as the other. The seam is then placed on native pixels in each shot's middle frame."""
    W, H, N = info["width"], info["height"], len(pts)
    aw = even(min(240, W))
    ah = max(8, round(aw * H / W / 2) * 2)
    mids = [(sh["frames"][0] + sh["frames"][1]) // 2 for sh in shots]
    evs = [e for e in events if e["kind"] in ("panel", "cut") and e["onset"] == "abrupt"]
    need = set(mids) | {f for e in evs for f in (e["peak_frame"] - 1, e["peak_frame"]) if f >= 0}
    fr = decode_rgb(video, sorted(need), (0, 0, even(W), even(H)), aw, ah, tmp)
    if not fr:
        return []
    G = {
        k: bytes((v[3 * i] * 299 + v[3 * i + 1] * 587 + v[3 * i + 2] * 114) // 1000 for i in range(aw * ah))
        for k, v in fr.items()
    }

    def lines(g, axis):
        """Positions (line index = first row/column of the second side) of straight full-length steps."""
        if axis == "y":
            prof = [
                sum(1 for x in range(aw) if abs(g[y * aw + x] - g[(y - 1) * aw + x]) > 12) / aw for y in range(1, ah)
            ]
        else:
            prof = [sum(1 for y in range(ah) if abs(g[y * aw + x] - g[y * aw + x - 1]) > 12) / ah for x in range(1, aw)]
        med = statistics.median(prof)
        L = len(prof) + 1
        return {q + 1 for q, v in enumerate(prof) if v >= 0.6 and v >= 4 * med and 0.05 * L <= q + 1 <= 0.95 * L}

    def sides(e, axis, s):
        p = e["peak_frame"]
        a, b = G.get(p - 1), G.get(p)
        if a is None or b is None:
            return None
        ch = [abs(x - y) > 30 for x, y in zip(a, b)]
        if axis == "y":
            A_ = sum(ch[: s * aw]) / (s * aw)
            B_ = sum(ch[s * aw :]) / ((ah - s) * aw)
        else:
            A_ = sum(ch[y * aw + x] for y in range(ah) for x in range(s)) / (s * ah)
            B_ = sum(ch[y * aw + x] for y in range(ah) for x in range(s, aw)) / ((aw - s) * ah)
        return A_, B_

    panes = []
    for axis in ("y", "x"):
        per = [lines(G[m], axis) if m in G else set() for m in mids]
        k = 0
        while k < len(shots):
            for s in sorted(per[k]):
                # keep the line through consecutive shots
                k1 = k
                while k1 + 1 < len(shots) and any(abs(s - q) <= 2 for q in per[k1 + 1]):
                    k1 += 1
                a_f, b_f = shots[k]["frames"][0], shots[k1]["frames"][1] + 1
                ev = [e for e in evs if a_f < e["peak_frame"] < b_f]
                proof = []
                for e in ev:
                    sd = sides(e, axis, s)
                    if sd and max(sd) >= 0.1 and max(sd) >= 3 * min(sd):
                        proof.append(
                            f"{e['id']} {e['kind']} @{e['t']:.3f} changes one side {max(sd):.2f}, "
                            f"the other {min(sd):.2f}"
                        )
                if not proof:
                    continue
                # native position: the line itself in each shot's middle frame (median over shots)
                L = H if axis == "y" else W
                La = ah if axis == "y" else aw
                pos_n = []
                for kk in range(k, k1 + 1):
                    band = max(6, int(3 * L / La))
                    lo_ = even(max(1, int(s * L / La) - band))
                    hi_ = min(L, int(s * L / La) + band)
                    crop = (
                        (0, lo_ - 2, even(W), max(4, even(hi_ - lo_ + 2)))
                        if axis == "y"
                        else (lo_ - 2, 0, max(4, even(hi_ - lo_ + 2)), even(H))
                    )
                    nat = decode_rgb(video, [mids[kk]], crop, crop[2], crop[3], tmp)
                    if not nat:
                        continue
                    A_ = nat[mids[kk]]
                    cw_, ch_ = crop[2], crop[3]
                    if axis == "y":
                        pr = [
                            sum(
                                1
                                for x in range(cw_)
                                if max(
                                    abs(A_[3 * (y * cw_ + x) + c] - A_[3 * ((y - 1) * cw_ + x) + c]) for c in range(3)
                                )
                                > 12
                            )
                            / cw_
                            for y in range(1, ch_)
                        ]
                    else:
                        pr = [
                            sum(
                                1
                                for y in range(ch_)
                                if max(abs(A_[3 * (y * cw_ + x) + c] - A_[3 * (y * cw_ + x - 1) + c]) for c in range(3))
                                > 12
                            )
                            / ch_
                            for x in range(1, cw_)
                        ]
                    q = max(range(len(pr)), key=lambda i: pr[i])
                    if pr[q] >= 0.6:
                        pos_n.append((crop[1] if axis == "y" else crop[0]) + q + 1)
                seam_px = int(statistics.median(pos_n)) if pos_n else round(s * L / La)
                sf = round(seam_px / L, 4)
                boxes = (
                    [[0.0, 0.0, 1.0, sf], [0.0, sf, 1.0, 1.0]]
                    if axis == "y"
                    else [[0.0, 0.0, sf, 1.0], [sf, 0.0, 1.0, 1.0]]
                )
                if any(
                    P["axis"] == ("top/bottom" if axis == "y" else "left/right")
                    and abs(P["seam"] - sf) < 0.02
                    and P["on"] <= pts[a_f] < P["off"]
                    for P in panes
                ):
                    continue
                panes.append(
                    {
                        "axis": "top/bottom" if axis == "y" else "left/right",
                        "seam": sf,
                        "seam_px": seam_px,
                        "on": round(pts[a_f], 3),
                        "off": round(pts[b_f], 3) if b_f < N else info["duration_video_s"],
                        "panes": boxes,
                        "evidence": proof,
                        "seam_found_in": f"{len(pos_n)} of {k1 - k + 1} shot middle frame(s)",
                    }
                )
            k += 1
    # lines inside one pane (rules of a recorded app screen) also pass for a while; per axis keep the
    # line that lasts longest (then has most evidence) wherever lives overlap
    kept = []
    for P in sorted(panes, key=lambda P: (-(P["off"] - P["on"]), -len(P["evidence"]))):
        if not any(
            Q["axis"] == P["axis"] and min(P["off"], Q["off"]) - max(P["on"], Q["on"]) > 0.5 * (P["off"] - P["on"])
            for Q in kept
        ):
            kept.append(P)
    panes = sorted(kept, key=lambda P: P["on"])
    for k, P in enumerate(panes, 1):
        P["id"] = f"P{k}"
    return panes


def element_candidates(video, info, pts, shots, events, fixed, tmp, regions=(), panes=(), max_n=6):
    """Drawn elements the scan offers without being pointed at, only where the evidence is clear: a
    layer that holds while the picture behind it moves (a fixed layer, or what holds through every
    frame of a shot whose whole picture moves), and a small area that changes on its own (a `local`
    change: a sticker, icon or card popping on). Each is measured like an `element` request
    and offered only when that measurement succeeds, the shape is solid (a caption's letters are read
    with `text`), it lives at least 8 frames and it shows something new (a part of the picture
    uncovered by something moving away showed the same pixels before)."""
    W, H, N = info["width"], info["height"], len(pts)
    cuts = sorted(sh["frames"][0] for sh in shots[1:])
    cands = []
    for L_ in (fixed or {}).get("layers", []):
        cands.append((None, L_["box"]))
    for e in events:  # (a `band` change is a caption line: read with `text`)
        if e["kind"] == "local" and e.get("box"):
            cands.append((min(N - 1, e["span_frames"][1] + 4), e["box"]))
    aw = even(min(180, W))
    ah = max(8, round(aw * H / W / 2) * 2)
    n = aw * ah
    moving = [
        sh
        for sh in shots
        if sh.get("still_share") is not None
        and sh["still_share"] <= STILL_MOVING
        and sh["frames"][1] - sh["frames"][0] >= 15
    ]
    if moving:
        r = run(
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
                f"scale={aw}:{ah}:flags=area,format=gray,tblend=all_mode=difference",
                "-fps_mode",
                "passthrough",
                "-f",
                "rawvideo",
                "-",
            ]
        )
        raw = r.stdout
        difs = [raw[i : i + n] for i in range(0, len(raw) - n + 1, n)]
        if len(difs) == N - 1:
            tabm = above(EXACT_T)
            for sh in moving:
                acc = 0
                for i in range(sh["frames"][0] + 2, sh["frames"][1] + 1):
                    acc |= int.from_bytes(difs[i - 1].translate(tabm), "big")
                held = int.from_bytes(b"\x01" * n, "big") & ~acc
                for comp in components(list(held.to_bytes(n, "big")), aw, ah):
                    if max(20, 0.001 * n) <= len(comp) <= 0.5 * n:
                        ys = [q // aw for q in comp]
                        xs = [q % aw for q in comp]
                        cands.append(
                            (
                                (sh["frames"][0] + sh["frames"][1]) // 2,
                                [min(xs) / aw, min(ys) / ah, (max(xs) + 1) / aw, (max(ys) + 1) / ah],
                            )
                        )

    def texty(box):
        return (box[2] - box[0]) * W >= 3 * (box[3] - box[1]) * H and any(
            _overlap(r_["box"], box) > 0.8 for r_ in regions
        )

    out, tried = [], 0
    for i, box in cands:
        if len(out) >= max_n or tried >= 2 * max_n:
            break
        if i is None:  # a fixed layer: measure it in the middle of the clip
            i = N // 2
        if any(o["on_frame"] <= i < o["off_frame"] and _overlap(o["box"], box) > 0.3 for o in out):
            continue
        if any(P["on"] <= pts[i] < P["off"] for P in panes):
            continue
        tried += 1
        m = measure_element(video, info, pts, box, pts[i], tmp, cuts=cuts)
        if "box" not in m or "on" not in m:
            continue
        if (
            m["off_frame"] - m["on_frame"] < 8
            or texty(m["box"])
            or m.get("fill", 0) < 0.5
            or m.get("seen_elsewhere", 1) >= 0.5
        ):
            continue
        if any(abs(o["on_frame"] - m["on_frame"]) <= 2 and _overlap(o["box"], m["box"]) > 0.5 for o in out):
            continue
        out.append(m)
    out.sort(key=lambda m: (m["on"], m["box"][1]))
    for k, m in enumerate(out, 1):
        m["id"] = f"G{k}"
    return out


def element_record(m, name):
    """An element measurement as a region file `build` reads (`"region": name` on a graphic)."""
    if "on" not in m:
        return {"cmd": "element", "name": name, "measured": m, "states": [], "why": m.get("why", "")}
    st = {
        "id": "T1",
        "on": m["on"],
        "off": m["off"],
        "frames": m["off_frame"] - m["on_frame"],
        "first_frame": m["on_frame"],
    }
    if m.get("box"):
        b = m["box"]
        st["layer"] = {
            "measured": True,
            "box": b,
            "center": [round((b[0] + b[2]) / 2, 4), round((b[1] + b[3]) / 2, 4)],
            "evidence": m.get("evidence", ""),
        }
    else:
        st["layer"] = {"measured": False, "why": m.get("box_why") or m.get("why", "")}
    return {"cmd": "element", "name": name, "measured": m, "states": [st]}


def cmd_element(a):
    d = os.path.abspath(a.dir)
    idx, pts, _ = load_dir(d)
    info = idx["facts"]
    box = parse_box(a.box)
    tmp = scratch_dir(d, "element")
    name = a.name or f"element_{a.at:.2f}_" + "-".join(f"{round(x * 100):02d}" for x in box)
    # a box that mostly covers a measured pane at this moment is that pane
    i = nearest_frame(pts, a.at)
    for P in idx.get("panes") or []:
        if P["on"] - 1e-6 <= pts[i] < P["off"]:
            for pb in P["panes"]:
                if _overlap(pb, box) >= 0.6 and (box[2] - box[0]) * (box[3] - box[1]) >= 0.3 * (pb[2] - pb[0]) * (
                    pb[3] - pb[1]
                ):
                    m = {
                        "rough_box": box,
                        "at": round(pts[i], 3),
                        "on": P["on"],
                        "off": P["off"],
                        "on_frame": nearest_frame(pts, P["on"]),
                        "off_frame": nearest_frame(pts, P["off"]) if P["off"] < info["duration_video_s"] else len(pts),
                        "box": pb,
                        "evidence": f"pane {P['id']} ({P['axis']} seam at {P['seam']}: {', '.join(P['evidence'])})",
                        "until_end": P["off"] >= info["duration_video_s"],
                        "from_start": P["on"] == 0,
                    }
                    rec = element_record(m, name)
                    break
            else:
                continue
            break
    else:
        cuts = [sh["frames"][0] for sh in idx["shots"][1:]]
        m = measure_element(idx["video"], info, pts, box, a.at, tmp, cuts=cuts)
        rec = element_record(m, name)
    shutil.rmtree(tmp, ignore_errors=True)
    write_json(os.path.join(d, "look", name + ".json"), rec, indent=1, ensure_ascii=False)
    record_followup(d, {"cmd": "element", "json": f"look/{name}.json", "box": box, "frames": [i]})
    print(element_line(m, name))
    if "on" in m and m.get("box"):
        print(
            f'  saved as look/{name}.json: give a graphic "region": "{name}" and `build` takes its box and '
            f"times from it"
        )
    elif "on" in m:
        print(
            f'  saved as look/{name}.json with its times only: give the graphic "region": "{name}" (`build` '
            f'takes its times from it) plus "box": [x0, y0, x1, y1] drawn by eye on the overview or a zoom, '
            f'and a "why"'
        )
    else:
        print(
            '  nothing measured: give the graphic "box": [x0, y0, x1, y1] and "time": [on, off] by eye, '
            'with a "why" (or try a tighter box around the element alone)'
        )


def element_line(m, name):
    if "on" not in m:
        return f"element {name}: not measured ({m.get('why', '')})"
    s = f"element {name}: on {m['on']:.3f}"
    if m.get("settled") is not None and abs(m["settled"] - m["on"]) > 1e-6:
        s += f" (in place from {m['settled']:.3f})"
    s += f", off {m['off']:.3f}" + (" (to the end)" if m.get("until_end") else "")
    if m.get("leaving_from") is not None:
        s += f" (leaving from {m['leaving_from']:.3f})"
    if m.get("box"):
        b = m["box"]
        s += (
            f"; box {b[0]:.3f},{b[1]:.3f},{b[2]:.3f},{b[3]:.3f} (x {b[0]:.3f}, y {b[1]:.3f}, w {b[2] - b[0]:.3f}, "
            f"h {b[3] - b[1]:.3f})"
        )
        if m.get("precision_px"):
            s += f" to about {m['precision_px']} px"
    else:
        s += "; box not measured: " + m.get("box_why", "")
    if m.get("evidence"):
        s += f"; {m['evidence']}"
    return s
