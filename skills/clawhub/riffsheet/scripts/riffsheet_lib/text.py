"""`text`: each distinct state of a region, once, with on/off times."""

import os
import shutil
import statistics

from .constants import CELL_FLOOR, CELL_JUMP_X, EXACT_T, HOLD_T, STEP_X, STILL_LOCKED
from .layers import LAYER_MAX_W, layer_frames, layer_line, layer_style, trust_styles
from .media import decode_rgb, extract_cells, run
from .scandir import frames_between, load_dir, parse_box, record_followup, scratch_dir
from .sheets import cell_dims, compose, label_fs, report_images, wrap
from .transcript import join_words, words_in
from .util import _box_px, _pc, above, die, even, fmt_t, write_json

# ----------------------------------------------------------------------------- text (region states)
SEG_W = 240  # analysis width (gray) for splitting a region into caption states
CHG_T = 40  # a pixel "changed" across a boundary when its gray level moves more than this
NEW_HOLD = 7  # a new layer on a moving picture must hold exactly for this many frames more
SETTLED = 0.15  # a layer held through motion is believed when it is at most this share of the region
LAYER_CHANGE_SHARE = 0.01  # a layer change moves at least this share of the region (and 8 px)
CELL = 8  # side of the cells (analysis px) whose runs of change find pops, wipes and fades
CELL_RUN_MAX = 15  # a run of changing cells longer than this many frames (half a second) is motion
EDGE_RANGE = 60  # a pixel is on an edge when its 3x3 neighborhood spans this many gray levels: a stroke
EDGE_SHARE = 0.5  # new pixels are drawn strokes when at least this share of them sit on edges
STEP_SHARE = 0.5  # a step: this share of the change held before and after it ...
STEP_SHARE_LARGE = 0.35  # ... or this share when the held part is large (4x the minimum change)
PICTURE_HOLDS = 0.85  # the picture around a change holds when this share of the region holds
SIDED_SHARE = 0.6  # a change mostly of pixels that held on one side: a layer leaving or arriving
LAYER_GONE = 0.5  # a layer changed when this share of its pixels changed
CUT_SURVIVES = 0.85  # a layer comes through a cut when this share of it holds unchanged
CUT_HIT_MAX = 0.15  # at a cut, a drawn layer is untouched when at most this share of its strokes changed
STEP_HIT_MAX = 0.12  # off a cut, a drawn layer held when at most this share of its strokes changed
DRAWN_LOOKBACK = 9  # the drawn layer in hand: edge pixels that held exactly over at most this many frames
MOVING_HELD = 8  # frames a layer must hold through motion before it separates layer from picture
LEFT_SHARE = 0.4  # a state shows no layer when this share of the strokes held before it left ...
NEW_SHARE_MAX = 0.1  # ... and new held strokes are under this share of those that left
INNER_MIN_FRAMES = 6  # a state this long or longer is checked for a layer changing inside it
INNER_HOLDS = 0.5  # ... over a picture where this share of the region holds exactly


def _flags(buf, t):
    """Pixels of a gray difference frame above t, as a big integer with one byte (0/1) per pixel."""
    return int.from_bytes(buf.translate(above(t)), "big")


def _frames_of(path, n, pad):
    """Fixed-size frames from a raw file, with an optional pad frame first (a difference has none)."""
    with open(path, "rb") as f:
        raw = f.read()
    return ([pad] if pad is not None else []) + [raw[i : i + n] for i in range(0, len(raw) - n + 1, n)]


class RegionStates:
    """Split a region into states defined by its own layer's pixels (a caption, a card), not by what
    moves behind it. `states()` returns [(first, last, transition-or-None, unsure, inner, empty)] over
    the frames `sel`.

    Candidates: any frame where >= 1% of the region changes, runs of changing 8x8 cells (a pop,
    wipe or fade), and every cut. A candidate is a layer change when:
    - still picture behind (locked shot, or the region holds around the change): it is a step (the
      pixels that change held for 2-3 frames before and after: a swap) or a one-frame spike of
      change, or it changes most of the layer the state began with. A person who starts or stops
      moving changes pixels that held on one side only, so is not a step.
    - moving picture behind: the layer (pixels that held to within compression noise through the
      state) changes, or new pixels hold that way for 8 frames on drawn edges; until such a layer
      has held for 8 frames, a step, spike or one-sided change also splits (nothing yet separates
      layer from picture), and the state is marked unsure.
    - a cut: the state continues only when >= 85% of the known layer survives it unchanged.
    A layer proven by surviving a cut or holding through motion (a small part of the region) must
    itself change, or gain new edge pixels, for a later step to count."""

    def __init__(self, video, crop_px, sel, N, tmp, cuts=(), moving_frames=frozenset()):
        self.crop_px = crop_px
        self.sel, self.N = sel, N
        self.cutset = set(cuts)
        self.moving_frames = moving_frames
        self.first, self.last = sel[0], sel[-1]
        self.edge_cache = {}
        self.decode(video, tmp)
        self.T = max(8, int(LAYER_CHANGE_SHARE * self.npx))  # the smallest layer change, in pixels
        self.small = max(8, self.T // 4)  # the fewest pixels a layer in hand can have

    def decode(self, video, tmp):
        """The region in gray at analysis size, its frame-to-frame differences, and those differences
        averaged over 8x8 cells; then the masks of pixels that moved more than each threshold."""
        cx, cy, cw, ch = self.crop_px
        aw = even(min(SEG_W, cw))
        ah = max(8, round(aw * ch / cw / 2) * 2)
        gc, gr = max(1, aw // CELL), max(1, ah // CELL)
        self.aw, self.ah, self.npx, self.nc = aw, ah, aw * ah, gc * gr
        gpath, fpath, cpath = (os.path.join(tmp, f"seg_{x}.raw") for x in "gdc")
        fc = (
            f"[0:v]crop={cw}:{ch}:{cx}:{cy},scale={aw}:{ah}:flags=area,format=gray,split[g][t];"
            f"[t]tblend=all_mode=difference,split[d][e];[e]scale={gc}:{gr}:flags=area[c]"
        )
        out = []
        for label, path in (("[g]", gpath), ("[d]", fpath), ("[c]", cpath)):
            out += ["-map", label, "-fps_mode", "passthrough", "-f", "rawvideo", path]
        r = run(
            ["ffmpeg", "-hide_banner", "-nostdin", "-y", "-loglevel", "error", "-i", video, "-an"]
            + ["-filter_complex", fc]
            + out
        )
        if r.returncode != 0:
            die("region decode failed: " + r.stderr.decode()[-400:])
        npx, nc = self.npx, self.nc
        self.G = _frames_of(gpath, npx, None)
        dif = _frames_of(fpath, npx, bytes(npx))
        self.cel = [[v / 255 for v in b] for b in _frames_of(cpath, nc, bytes(nc))]
        if not (len(self.G) == len(dif) == len(self.cel) == self.N):
            die(f"region decode gave {len(self.G)}/{len(dif)}/{len(self.cel)} frames, index has {self.N}")
        self.lo = [_flags(b, HOLD_T) for b in dif]
        self.hi = [_flags(b, CHG_T) for b in dif]
        self.tight = [_flags(b, EXACT_T) for b in dif]
        self.ALL = int.from_bytes(b"\x01" * npx, "big")
        self.tab = above(CHG_T)

    # ---- pixel masks
    def held(self, a_, b_):
        """Pixels that hold from frame a_ through frame b_."""
        x = 0
        for i in range(max(self.first, a_) + 1, min(self.last, b_) + 1):
            x |= self.lo[i]
        return self.ALL & ~x

    def exact(self, a_, b_):
        """Pixels that hold to within compression noise from frame a_ through frame b_."""
        x = 0
        for i in range(max(self.first, a_) + 1, min(self.last, b_) + 1):
            x |= self.tight[i]
        return self.ALL & ~x

    def changed(self, f0, f1):
        """Pixels that differ between two frames."""
        if f1 == f0 + 1:
            return self.hi[f1]
        return int.from_bytes(bytes(abs(p - q) for p, q in zip(self.G[f0], self.G[f1])).translate(self.tab), "big")

    def step(self, t0, t1):
        """Change from frame t0-1 to frame t1 (t1 > t0 means it took several frames), with the pixels
        that held over the frames before and after it."""
        return self.changed(t0 - 1, t1), self.held(t0 - 3, t0 - 1), self.held(t1, t1 + 2)

    def contrasty(self, mask, f):
        """Share of the masked pixels that sit on an edge (3x3 range >= 60 gray levels) in frame f:
        drawn text is edges and strokes; a flat patch the camera settled on is not."""
        aw, ah, npx = self.aw, self.ah, self.npx
        g, mb = self.G[f], mask.to_bytes(npx, "big")
        n = e = 0
        for k in range(npx):
            if not mb[k]:
                continue
            y, x = divmod(k, aw)
            if 0 < y < ah - 1 and 0 < x < aw - 1:
                nb = [g[k + dy * aw + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1)]
                e += max(nb) - min(nb) >= EDGE_RANGE
                n += 1
        return e / n if n else 0.0

    def edges(self, f):
        """Pixels of frame f on an edge (3x3 gray range >= 60): drawn strokes, not flat patches."""
        if f not in self.edge_cache:
            aw, ah = self.aw, self.ah
            g = self.G[f]
            rows = [g[y * aw : (y + 1) * aw] for y in range(ah)]
            hmx = [[max(r[max(0, x - 1) : x + 2]) for x in range(aw)] for r in rows]
            hmn = [[min(r[max(0, x - 1) : x + 2]) for x in range(aw)] for r in rows]
            out = bytearray(self.npx)
            for y in range(ah):
                ys = range(max(0, y - 1), min(ah, y + 2))
                for x in range(aw):
                    if max(hmx[q][x] for q in ys) - min(hmn[q][x] for q in ys) >= EDGE_RANGE:
                        out[y * aw + x] = 1
            self.edge_cache[f] = int.from_bytes(bytes(out), "big")
        return self.edge_cache[f]

    def drawn_before(self, t0, s0):
        """Edge pixels that held to within compression noise since the state began (at most the 9
        frames before t0; at least 2 frames, else the 9 frames before t0 across the state's start).
        A drawn layer (caption, card) sits on top of the picture: nothing passes in front of it, so
        its stroke pixels hold exactly while the picture behind moves, and change only when the
        layer itself changes. Flat patches (blown highlights, black) also hold, so only edges count."""
        b_ = t0 - 1
        a_ = max(self.first, s0, t0 - DRAWN_LOOKBACK)
        if b_ - a_ < 1:
            a_ = max(self.first, t0 - DRAWN_LOOKBACK)
            if b_ - a_ < 3:
                return None
        L_ = self.exact(a_, b_) & self.edges(b_)
        return L_ if _pc(L_) >= self.small else None

    def is_cut(self, t0, t1, nD):
        """A change over most of the region, or one that includes a cut."""
        return nD >= 0.5 * self.npx or any(c in self.cutset for c in range(t0, t1 + 1))

    # ---- candidates
    def cell_runs(self):
        """Per frame of `sel`: does some 8x8 cell step up against its own usual change there? And the
        frames where at least the smallest layer change of pixels changed in one frame."""
        sel, first, last, cel = self.sel, self.first, self.last, self.cel
        single, cells_on = [], []
        for i in sel:
            if i == first:
                cells_on.append(False)
                continue
            on = False
            prv = cel[i - 1] if i - 1 > first else None
            nxt = cel[i + 1] if i + 1 <= last else None
            w = [k for k in range(max(first + 1, i - 15), min(last, i + 15) + 1) if abs(k - i) > 1]
            for c in range(self.nc):
                x = cel[i][c]
                if x < CELL_FLOOR or x < STEP_X * max(prv[c] if prv else 0.0, nxt[c] if nxt else 0.0):
                    continue
                if x >= CELL_JUMP_X * statistics.median([cel[k][c] for k in w] or [0.0]):
                    on = True
                    break
            cells_on.append(on)
            if _pc(self.hi[i]) >= self.T:
                single.append((i, i))
        return single, cells_on

    def candidates(self):
        """Candidate changes (first frame, last frame), and for settle-to-settle changes the frames
        the region holds after it settles."""
        sel = self.sel
        # one-frame changes of pixels (fast swap), or runs of changing 8x8 cells (a pop, wipe or fade
        # over a few frames)
        cand, cells_on = self.cell_runs()
        k = 0
        while k < len(sel):  # multi-frame cell changes: one candidate per run
            if cells_on[k]:
                j = k
                while j + 1 < len(sel) and (cells_on[j + 1] or (j + 2 < len(sel) and cells_on[j + 2])):
                    j += 1
                if 0 < j - k <= CELL_RUN_MAX:  # longer than half a second is motion, not a pop or fade
                    cand.append((sel[k], sel[j]))
                k = j + 1
            else:
                k += 1
        # settle-to-settle changes: the region holds (fewer than T pixels move between frames), then
        # moves for a few frames, then holds again. A word that pops in and scales or bounces into place
        # over several frames is no one-frame step and no run of cell steps, but it is a change from one
        # held picture of the region to another; the tests below decide whether that change is the layer
        settled = [i == self.first or _pc(self.lo[i]) < self.T for i in range(self.N)]
        hold_after = {}
        k = 0
        sl = list(sel)
        while k < len(sl):
            if not (settled[sl[k]] and k + 1 < len(sl) and settled[sl[k + 1]]):
                k += 1
                continue
            j = k + 1
            while j + 1 < len(sl) and settled[sl[j + 1]]:
                j += 1
            t0 = j + 1  # first moving frame after a held run of >= 2 frames
            m = t0
            while m < len(sl) and not settled[sl[m]]:
                m += 1
            # frames m-1, m, m+1 hold: the new picture is in place from frame m-1
            if m + 1 < len(sl) and settled[sl[m + 1]] and 1 <= m - 1 - t0 <= CELL_RUN_MAX:
                r_ = m + 1
                while r_ + 1 < len(sl) and settled[sl[r_ + 1]]:
                    r_ += 1
                cand.append((sl[t0], sl[m - 1]))
                hold_after[(sl[t0], sl[m - 1])] = r_ - (m - 1)  # frames it holds after it settles
            k = max(j + 1, m)
        # a change that includes a cut is the cut: the layer changes on that frame or not at all
        cand = [next(((c, c) for c in range(t0, t1 + 1) if c in self.cutset), (t0, t1)) for t0, t1 in cand]
        cand += [(c, c) for c in self.cutset if self.first < c <= self.last]
        return cand, hold_after

    def measured_steps(self):
        """Each candidate with what the decisions need: the change, its held part, and the step tests."""
        T, npx, hi = self.T, self.npx, self.hi
        cand, hold_after = self.candidates()
        steps = []
        for t0, t1 in sorted(set(cand)):
            if t0 - 2 < self.first or t1 + 2 > self.last:  # needs two frames either side to see what holds
                continue
            D, pre, post = self.step(t0, t1)
            nD = _pc(D)
            if nD < T:
                continue
            A, Bp, Bm = _pc(D & pre & post), _pc(D & post & ~pre), _pc(D & pre & ~post)
            den = A + Bp + Bm
            if t1 > t0:  # over several frames: what changed on the way must be the layer too
                U = 0
                for i in range(t0, t1 + 1):
                    U |= hi[i]
                den = max(den, _pc(U))
            share = A / max(1, den)
            still = (A >= T and share >= STEP_SHARE) or (A >= 4 * T and share >= STEP_SHARE_LARGE)
            if t1 > t0 and min(_pc(pre), _pc(post)) < PICTURE_HOLDS * npx:
                still = False  # a run of changes on a moving picture is motion, not a pop or fade
            spike = t0 == t1 and nD >= 2 * T and nD >= 2 * max(_pc(hi[t0 - 1]), _pc(hi[t0 + 1]))
            if spike:
                still = True  # a one-frame spike of change: a swap, even if what follows keeps moving
            # pixels that held on at least one side make up most of the change: on a moving picture
            # that is a layer leaving or arriving, not the picture moving
            sided = t0 == t1 and A + Bp + Bm >= 2 * T and A + Bp + Bm >= SIDED_SHARE * nD
            locstill = min(_pc(pre), _pc(post)) >= PICTURE_HOLDS * npx  # the picture holds around this change
            steps.append([t0, t1, D, D & pre & post, nD, still, spike or sided, locstill, hold_after.get((t0, t1))])
        return steps

    # ---- decisions
    def decide(self, t0, t1, D, nD, still, spike, locstill, s0, lay, proven, startD, hold=None):
        """Is the change over frames t0..t1 a change of the layer? Returns (keep, layer after, why).
        The picture-based tests below are checked against the drawn layer when one is in hand: a
        drawn layer (caption, card) sits on top of the picture, so nothing passes in front of it;
        its stroke pixels change only when the layer itself changes."""
        T, npx, last, cutset = self.T, self.npx, self.last, self.cutset
        exact, edges = self.exact, self.edges
        keep, lay2, why = self.decide_picture(t0, t1, D, nD, still, spike, locstill, s0, lay, proven)
        L8 = self.drawn_before(t0, s0)
        if not keep and t0 - s0 < 3 and nD < 0.5 * npx and t0 not in cutset:
            # the state began less than three frames ago (a caption left, and the next one arrives a
            # frame or two later): the step test looks at the frames before this change, which then
            # hold the previous change, so it cannot see a step. New strokes that change here and then
            # hold exactly on edges are a new layer (held up to the next cut, at least three frames)
            nxt = min([c for c in cutset if c > t1] + [last + 1])
            end = min(t1 + NEW_HOLD, nxt - 1)
            if end - t1 >= 3:
                Nw = D & exact(t1, end) & edges(min(last, t1 + 3))
                if L8 is not None:
                    Nw &= ~L8
                if _pc(Nw) >= T and self.contrasty(Nw, min(last, t1 + 3)) >= EDGE_SHARE:
                    return (
                        True,
                        lay2,
                        why + f"; a new layer arrives {t0 - s0} frame(s) after the state began: "
                        f"{_pc(Nw)} new px hold exactly on edges",
                    )
        if L8 is None:
            return keep, lay2, why + "; no drawn layer in hand"
        nL, hit = _pc(L8), _pc(D & L8)
        # the held strokes are this state's layer when they are what appeared as the state began (or
        # the state began with the window); on a moving picture, strokes that also held exactly across
        # the state's start are the layer too (nothing filmed holds exactly while the camera moves);
        # otherwise they may be a still part of a locked picture, which says nothing about the caption
        own = (
            startD is None
            or _pc(L8 & startD) >= 0.5 * nL
            or (t0 in self.moving_frames and _pc(L8 & exact(max(self.first, s0 - 3), min(t0 - 1, s0 + 3))) >= 0.5 * nL)
        )
        if self.is_cut(t0, t1, nD):
            # a cut: the drawn layer either comes through it untouched or the state ends
            if keep and nL >= T // 2 and hit <= CUT_HIT_MAX * nL and own:
                return False, L8 & ~D, why + f"; vetoed: {nL - hit}/{nL} of the drawn layer's strokes survive the cut"
            return keep, lay2, why + f"; drawn layer {hit}/{nL} changed at the cut, own {own}"
        # new strokes must then hold exactly: for NEW_HOLD frames, or for as long as the region holds
        # after a settle-to-settle change (a word that bounces into place and is replaced soon after)
        hn = NEW_HOLD if not hold else max(2, min(NEW_HOLD, hold))
        Nw = D & exact(t1, t1 + hn) & ~L8 & edges(min(last, t1 + min(3, hn)))
        if keep and own and hit <= STEP_HIT_MAX * nL and _pc(Nw) < T // 2:
            return False, lay2, why + f"; vetoed: the drawn layer held ({hit}/{nL} strokes changed, {_pc(Nw)} new)"
        if not keep and nL >= T // 2 and hit >= LAYER_GONE * nL:
            return True, lay2, why + f"; overruled: {hit}/{nL} of the drawn layer's strokes changed"
        return keep, lay2, why + f"; drawn layer {hit}/{nL} changed, {_pc(Nw)} new, own {own}"

    def decide_picture(self, t0, t1, D, nD, still, spike, locstill, s0, lay, proven):
        """The decision from the picture alone: what held around the change and in the state's layer."""
        npx, last = self.npx, self.last
        held, exact = self.held, self.exact
        # moving picture behind: the scan measured this shot's camera as not locked, and the
        # region does not hold around this change
        moving = t0 in self.moving_frames and not locstill
        if moving and t0 - 1 > s0:  # what held exactly through the state is the layer
            lay = exact(s0, t0 - 1)
            if _pc(lay) < self.small:
                lay = held(s0, t0 - 1)
        elif lay is not None:
            lay &= held(s0, t0 - 1)
        known = lay is not None and _pc(lay) >= self.small
        if self.is_cut(t0, t1, nD):
            if not known:
                return True, lay, "cut, no layer known before it"
            P = held(t1, t1 + 3) & ~D
            surv = _pc(lay & P) / _pc(lay)
            return surv < CUT_SURVIVES, lay & P, f"cut, layer {_pc(lay)} px, {surv:.2f} of it survives"
        if moving:
            # the layer changed (its own pixels moved), or a new layer appeared: pixels that change
            # here and then hold to within compression noise for 8 frames, on edges (drawn strokes)
            gone = _pc(D & lay) / _pc(lay) if known else 0.0
            if gone >= LAYER_GONE:
                return True, lay, f"moving behind: {gone:.2f} of the layer changed"
            Nw = D & exact(t1, t1 + NEW_HOLD) & (~lay if known else self.ALL)
            new = _pc(Nw)
            edge = self.contrasty(Nw, min(last, t1 + 3)) if new >= self.T else 0.0
            if edge >= EDGE_SHARE:
                return True, lay, f"moving behind: {new} new px hold exactly, edges {edge:.2f}"
            if still and t0 == t1 and not proven:
                return True, lay, "moving behind, but this change is a step (held before and after)"
            # no layer has held through 8+ frames of this motion yet: nothing separates the layer
            # from the picture, so a step splits (a spike of the whole change, or a change made
            # mostly of pixels that held on one side: a layer leaving or arriving)
            settled = known and t0 - s0 >= MOVING_HELD and _pc(lay) <= SETTLED * npx  # held, and only a small part
            return (
                spike and not settled,
                lay,
                f"moving behind: {gone:.2f} of the layer changed, step {spike}, settled layer {settled}",
            )
        if known and not proven:
            # the layer this state began with (pixels that changed at its first frame and then held):
            # most of it changing again is the layer changing, even when the new text keeps moving
            gone = _pc(D & lay) / _pc(lay)
            if gone >= LAYER_GONE:
                return True, lay, f"still behind: {gone:.2f} of the layer it began with changed"
        if still and proven and known:
            # a layer proven by holding through motion or a cut: the change must touch it, or add
            # pixels that sit on edges (drawn strokes), not a smooth change of light or a settling
            gone = _pc(D & lay) / _pc(lay)
            if gone >= LAYER_GONE:
                return True, lay, f"still behind, proven layer: {gone:.2f} of it changed"
            Nw = D & held(t1, t1 + NEW_HOLD) & ~lay
            edge = self.contrasty(Nw, min(last, t1 + 3)) if _pc(Nw) >= self.T else 0.0
            return edge >= EDGE_SHARE, lay, f"still behind, proven layer: {gone:.2f} changed, new px edges {edge:.2f}"
        return still, lay, "still behind: step test"

    # ---- walking the candidates
    def split(self):
        """Walk the candidates in time order with the current state's layer in hand. Returns the states
        as (first, last, transition-or-None)."""
        npx, cutset = self.npx, self.cutset
        # candidates that overlap form one change; a one-frame step inside it wins over the run
        steps = sorted(self.measured_steps(), key=lambda x: (x[0], x[1]))
        groups = []
        for st_ in steps:
            if groups and st_[0] <= max(x[1] for x in groups[-1]):
                groups[-1].append(st_)
            else:
                groups.append([st_])
        out, s0, tr0, lay, proven, startD = [], self.first, None, None, False, None
        for grp in groups:
            singles = sorted((x for x in grp if x[0] == x[1]), key=lambda x: x[0])
            runs = sorted((x for x in grp if x[0] < x[1]), key=lambda x: (x[1] - x[0], x[0]))
            took = False
            for phase in (singles, runs):
                if took:
                    break
                for t0, t1, D, S, nD, still, spike, locstill, hold in phase:
                    if t0 <= s0:
                        continue
                    keep, lay2, _ = self.decide(t0, t1, D, nD, still, spike, locstill, s0, lay, proven, startD, hold)
                    if keep:
                        out.append((s0, t0 - 1, tr0))
                        s0, tr0, startD = t1, ((t0, t1 - 1) if t1 > t0 else None), D
                        lay = S if nD < 0.5 * npx and t0 not in cutset else None
                        took, proven = True, False
                        if phase is runs:
                            break
                        continue
                    if nD >= 0.5 * npx or t0 in cutset:  # the layer survived a cut: it is the layer
                        lay, proven = lay2, True
                    elif (
                        t0 in self.moving_frames
                        and lay2 is not None
                        and t0 - s0 >= MOVING_HELD
                        and self.small <= _pc(lay2) <= SETTLED * npx
                    ):
                        lay, proven = lay2, True
        out.append((s0, self.last, tr0))
        return out

    def empty(self, a_, b_, tr, prev0):
        """A state that shows no drawn layer: the strokes that held to within compression noise in the
        state before change where this one begins, and no new strokes then hold through it. That is the
        layer leaving (a caption gone before the cut), not a new caption; measured only where the change
        is no cut (a cut changes everything, layer or not). Returns (left, held before, new) or None."""
        t0_ = tr[0] if tr else a_
        if prev0 is None or b_ <= a_ or any(c in self.cutset for c in range(t0_, a_ + 1)):
            return None
        L8 = self.drawn_before(t0_, prev0)
        if L8 is None:
            return None
        D = self.changed(t0_ - 1, a_)
        nL, hit = _pc(L8), _pc(D & L8)
        new = _pc(D & self.exact(a_, b_) & ~L8 & self.edges(b_))
        if hit >= max(self.T // 2, LEFT_SHARE * nL) and new < min(self.T // 4, NEW_SHARE_MAX * hit):
            return (hit, nL, new)
        return None

    def unsure(self, a_, b_):
        """A state on a moving picture that no layer held through: a change inside it can have been
        missed, so it is shown by its first and last frames."""
        mv = sum(1 for i in range(a_, b_ + 1) if i in self.moving_frames)
        drawn = _pc(self.exact(a_, b_) & self.edges(b_)) >= self.small  # a drawn layer held through it
        return (
            b_ - a_ + 1 >= 4
            and mv * 2 >= b_ - a_ + 1
            and not drawn
            and not (b_ - a_ + 1 >= MOVING_HELD and _pc(self.held(a_, b_)) >= self.small)
        )

    def inner(self, a_, b_):
        """A layer that keeps changing inside a state over a picture that holds: most of the region
        holds exactly, yet a part of it changes inside the state. That is the layer itself changing
        (a word-by-word reveal or a moving caption) in steps this split did not separate, so what the
        state shows is not one display. Returns the pixel box (source px) of the strokes that changed,
        False or None."""
        if b_ - a_ + 1 < INNER_MIN_FRAMES:
            return None
        hi, tight, npx, aw, ah = self.hi, self.tight, self.npx, self.aw, self.ah
        U = 0
        for i in range(a_ + 2, b_):
            U |= hi[i]
        inner = _pc(self.exact(a_ + 1, b_ - 1)) >= INNER_HOLDS * npx and _pc(U) >= self.T
        if not inner:
            return inner
        # the changing pixels must be drawn strokes: after a change they hold to within compression
        # noise for two frames and sit on an edge (a person moving behind the caption in a locked shot
        # changes pixels that do not settle like that)
        Sx = 0
        for i in range(a_ + 2, b_ - 1):
            Sx |= hi[i] & ~tight[i + 1] & ~tight[i + 2] & self.edges(i + 2)
        if _pc(Sx) < self.T:
            return None
        cx, cy, cw, ch = self.crop_px
        mb = Sx.to_bytes(npx, "big")
        ys = [y for y in range(ah) if b"\x01" in mb[y * aw : (y + 1) * aw]]
        xs = [x for x in range(aw) if any(mb[y * aw + x] for y in ys)]
        return [
            round(cx + xs[0] * cw / aw, 1),
            round(cy + ys[0] * ch / ah, 1),
            round(cx + (xs[-1] + 1) * cw / aw, 1),
            round(cy + (ys[-1] + 1) * ch / ah, 1),
        ]

    def states(self):
        res = []
        prev0 = None  # first frame of the state before
        for a_, b_, tr in self.split():
            if b_ < a_:
                continue
            empty = self.empty(a_, b_, tr, prev0)
            prev0 = a_
            res.append((a_, b_, tr, self.unsure(a_, b_), self.inner(a_, b_), empty))
        return res


def region_states(video, crop_px, sel, N, tmp, cuts=(), moving_frames=frozenset()):
    """The states of a region (RegionStates), as [(first, last, transition, unsure, inner, empty)]."""
    return RegionStates(video, crop_px, sel, N, tmp, cuts, moving_frames).states()


def cmd_text(a):
    d = os.path.abspath(a.dir)
    idx, pts, words = load_dir(d)
    info = idx["facts"]
    box = parse_box(a.box)
    video = idx["video"]
    W, H = info["width"], info["height"]
    bw, bh = (box[2] - box[0]) * W, (box[3] - box[1]) * H
    cx, cy, cw, ch = _box_px(box, W, H)
    a0 = a.start if a.start is not None else 0.0
    a1 = a.end if a.end is not None else pts[-1]
    sel = frames_between(pts, a0, a1)
    if len(sel) < 2:
        die("window holds fewer than 2 frames")
    tmp = scratch_dir(d, "text")
    merged = region_states(
        video,
        (cx, cy, cw, ch),
        sel,
        len(pts),
        tmp,
        cuts=[sh["frames"][0] for sh in idx["shots"][1:]],
        moving_frames={
            i
            for sh in idx["shots"]
            if sh.get("still_share") is not None and sh["still_share"] < STILL_LOCKED
            for i in range(sh["frames"][0], sh["frames"][1] + 1)
        },
    )
    # render: one crop per state (+ a mid-transition crop for changes lasting >= 3 frames)
    long_side = min(int(max(bw, bh)), 320)
    cwr, chr_, _ = cell_dims(info, box, max(64, long_side))
    rows, need = [], set()
    tag = a.name or f"text_{int(box[1] * 100):02d}_{int(box[3] * 100):02d}"
    for si, (s, e, tr, unsure, inner, empty) in enumerate(merged, 1):
        rep = (s + e) // 2
        off = pts[e + 1] if e + 1 < len(pts) else idx["facts"]["duration_video_s"]
        st = {
            "id": f"T{si}",
            "on": round(pts[s], 3),
            "off": round(off, 3),
            "frames": e - s + 1,
            "first_frame": s,
            "rep_frame": rep,
            "rep_t": round(pts[rep], 3),
        }
        if s == sel[0] and s > 0:
            st["on_clipped"] = True  # began before the window: the on time is the window's
        if e == sel[-1] and e < len(pts) - 1:
            st["off_clipped"] = True
        if tr:
            st["appearing_from"] = round(pts[tr[0]], 3)
            st["transition_frames"] = tr[1] - tr[0] + 1
        if unsure:
            st["unsure"] = True
            st["shown_frames"] = [s, e]
            need.update((s, e))
        if empty:
            # the strokes held before this state left as it began and nothing drawn held through it
            st["empty"] = {"strokes_left": empty[0], "strokes_held_before": empty[1], "new_held": empty[2]}
        if inner:
            st["changes_inside"] = [
                round(inner[0] / W, 3),
                round(inner[1] / H, 3),
                round(inner[2] / W, 3),
                round(inner[3] / H, 3),
            ]  # where the strokes changed
            st["shown_frames"] = [s, e]
            need.update((s, e))
        st["spoken_during"] = join_words(words_in(words, pts[s], off)) if words else None
        rows.append(st)
        need.add(rep)
        if tr and tr[1] - tr[0] + 1 >= 3:
            need.add((tr[0] + tr[1]) // 2)
    cellmap = extract_cells(video, sorted(need), box, cwr, chr_, tmp, "tx", info)
    # measure each state's layer: box, text rows, colors (from pixels, not read)
    N = len(pts)
    lw_ = even(min(cw, LAYER_MAX_W))
    lh_ = max(2, round(lw_ * ch / cw / 2) * 2)
    sts = [(s, e, (tr[0] - 1) if tr else None) for s, e, tr, _, _, _ in merged]
    F = decode_rgb(video, layer_frames(sts, N), (cx, cy, cw, ch), lw_, lh_, tmp)
    for st, se in zip(rows, sts):
        st["layer"] = (
            {"measured": False, "why": "no drawn layer is on"}
            if st.get("empty")
            else layer_style(F, [se], N, W, H, (cx, cy, cw, ch), lw_, lh_)
            if F
            else {"measured": False, "why": "decode failed"}
        )
    trust_styles(rows)
    crop_rec = {"crop_px": [cx, cy, cw, ch], "analysis_px": [lw_, lh_]}
    cells = []
    fs = label_fs(cwr)
    for st in rows:
        if st.get("transition_frames", 0) >= 3:
            s0 = int(round(st["first_frame"] - st["transition_frames"]))
            m = (s0 + st["first_frame"] - 1) // 2
            if m in cellmap:
                cells.append(
                    {
                        "path": cellmap[m],
                        "lines": [
                            f"mid-change {fmt_t(st['appearing_from'])}→{fmt_t(st['on'])} "
                            f"({st['transition_frames']} fr)",
                            f"{st['id']} arriving, shown {fmt_t(pts[m])}",
                        ],
                    }
                )
        head = f"{st['id']}  {fmt_t(st['on'])} → {fmt_t(st['off'])}  ({st['frames']} fr)" + (
            "  NO LAYER" if st.get("empty") else ""
        )
        said = wrap("said: " + st["spoken_during"], cwr - 8, fs, 1)[0] if st.get("spoken_during") else ""
        if st.get("unsure") or st.get("changes_inside"):
            f0, f1 = st["shown_frames"]
            cells.append({"path": cellmap[f0], "lines": [head + "  first", said], "hi": True})
            cells.append(
                {
                    "path": cellmap[f1],
                    "lines": [
                        f"{st['id']} last {fmt_t(pts[f1])} "
                        + ("(changes inside)" if st.get("changes_inside") else "(same words?)"),
                        "",
                    ],
                }
            )
        else:
            cells.append({"path": cellmap[st["rep_frame"]], "lines": [head, said], "hi": True})
    imgs = compose(cells, cwr, chr_, 2, os.path.join(d, "look", tag), tmp)
    shutil.rmtree(tmp, ignore_errors=True)
    res = {
        "cmd": "text",
        "box": box,
        "window": [a0, a1],
        **crop_rec,
        "states": rows,
        "images": [{**im, "path": os.path.relpath(im["path"], d)} for im in imgs],
    }
    write_json(os.path.join(d, "look", tag + ".json"), res, indent=1, ensure_ascii=False)
    record_followup(d, {"cmd": "text", "json": f"look/{tag}.json", "images": res["images"]})
    nun = sum(1 for st in rows if st.get("unsure"))
    print(
        f"text region {a.box}: {len(rows)} states in {fmt_t(a0)}–{fmt_t(a1)}. A state changes where the "
        f"layer's own pixels change (a swap, pop, fade, highlight move), not where the picture behind "
        f"moves or cuts. on = first frame showing it, off = first frame not showing it (measured)."
    )
    if nun:
        print(
            f"  {nun} state(s) marked ?: on a moving picture where no layer held still, a change inside "
            f"can be missed; their first and last frames are both shown: if the words differ, read both "
            f"and note the change under tool_gaps"
        )
    nemp = [st["id"] for st in rows if st.get("empty")]
    if nemp:
        print(
            f"  {len(nemp)} state(s) marked NO LAYER ({', '.join(nemp)}): no drawn layer is on. "
            f"The strokes that held in the state "
            f"before left where it begins and nothing drawn held through it (a caption gone, the picture "
            f"behind still moving). Leave it out of every caption; `build` ends a chunk before it"
        )
    nin = sum(1 for st in rows if st.get("changes_inside"))
    if nin:
        print(
            f"  {nin} state(s) marked ~: drawn strokes keep changing inside them while the picture behind "
            f"holds (a word-by-word reveal or a moving caption in steps not separated here). Their first "
            f"and last frames are both shown; read the words with `frames --box` over the state. `build` "
            f"gives no measured words-per-caption for a caption that uses one"
        )
    narr = [st["id"] for st in rows if st.get("transition_frames", 0) >= 3]
    if narr:
        print(
            f"  {len(narr)} state(s) arrive over 3 or more frames ({', '.join(narr)}): the cell before each, "
            f"labeled 'mid-change a→b', shows a frame from inside that arrival (a fade, slide or pop from a "
            f"to b). It is part of the state after it, not a state of its own, and has no id to give in a "
            f"chunk"
        )
    # a box across the seam of a split layout holds two pictures that cut at different times: the
    # layer's style rarely separates from both, so most states come back unmeasured
    for P in idx.get("panes") or []:
        if P["on"] >= a1 or P["off"] <= a0:
            continue
        lo, hi = (box[1], box[3]) if P["axis"].startswith("top") else (box[0], box[2])
        if lo + 0.02 < P["seam"] < hi - 0.02:
            print(
                f"  This box crosses the seam between the panes of {P['id']} (at {P['seam']:.3f}, "
                f"{fmt_t(P['on'])}–{fmt_t(P['off'])}): the two pictures change at different times, so the "
                f"style of many states cannot be separated from them and is left unmeasured. The times are "
                f"measured. A caption lying wholly on one side measures better with a box on that side; one "
                f"that sits across the seam keeps its measured times; where `build` then has no measured "
                f"colors or size for it, give them from your reading, with a `why`"
            )
    print(
        "  layer = colors, box and row height from pixels, kept only when they agree with the "
        "region's other states; '-' = withdrawn, with the reason"
    )
    for st in rows:
        tr = (
            f"  appears from {fmt_t(st['appearing_from'])} over {st['transition_frames']} fr"
            if "appearing_from" in st
            else ""
        )
        clip = (" (began before the window)" if st.get("on_clipped") else "") + (
            " (runs past the window: if it shows a caption, its off time is not measured: give --to a "
            "second later; if it shows none, leave it out)"
            if st.get("off_clipped")
            else ""
        )
        print(
            f"  {st['id']:>4}{'?' if st.get('unsure') else '~' if st.get('changes_inside') else ' '}"
            f"{fmt_t(st['on'])}–{fmt_t(st['off'])} "
            f"{st['frames']:>3} fr{tr}{clip}"
            + ("  NO LAYER" if st.get("empty") else "")
            + (
                f"   said: {st['spoken_during'][:100]}" + ("…" if len(st["spoken_during"]) > 100 else "")
                if st.get("spoken_during")
                else ""
            )
        )
        if st["frames"] >= 4:
            print("       layer: " + layer_line(st["layer"]))
    report_images(imgs, d)
