"""`build`: the measured sheet, and riffsheet.json + riffsheet.md from a judgment."""

import json
import os
import re
import sys

from . import FORMAT_VERSION, util
from .audio import sound_at_picture, sound_at_summary
from .capabilities import sound_line, stage_lines, stages_of, untested_lines
from .constants import (
    DESCENDERS,
    EXIT_REFUSED,
    FORMULA_KEYS,
    LINE_PAUSE_S,
    PACE_BANDS,
    PACE_WORDS,
    SENTENCE_ENDS,
    VIDEO_FORMATS,
)
from .details import (
    COLOR_FITS,
    METAL_COLORS,
    check_details,
    color_names_by_garment,
    confirm_views,
    detail_words_note,
    measured_families,
    view_name,
    written_colors,
)
from .hearing import HEARD_ABOUT, hearing_state, listen_clips
from .layers import _near
from .report import fix_articles, report_md
from .scandir import load_dir
from .schema import ANALYSIS_SCHEMA, validate
from .transcript import counts_by_character, is_unspaced_script, join_words
from .util import die, fmt_t, mmss, private, private_doc, read_json, weighted_median, write_json, write_text

PAUSE_LISTED_S = 0.4  # pauses longer than this are listed with a line's pace (a breath, not a word gap)
TREND_MIN_WORDS = 7  # a speed-up or slow-down is judged only on lines this long: halves of 3+ words each
TREND_FASTER = 0.75  # the second half's word spacing under this share of the first's: the line speeds up
TREND_SLOWER = 1.33  # over this share (the inverse of 0.75): it slows down


def pace_of(ws, text=None):
    """Speaking rate of a run of transcript words. Languages written without spaces are counted
    in characters (about one syllable each), others in words; thresholds per unit. `text` is the line
    as corrected (a spelling fix can join two misheard words into one name): the count is taken from
    it, the time from the words' own start and end."""
    if text is None:
        text = " ".join(w["word"] for w in ws)
    letters = [c for c in text if c.isalnum()]
    cjk = sum(1 for c in letters if counts_by_character(c))
    unit = "characters" if letters and cjk / len(letters) > 0.5 else "words"
    n = cjk if unit == "characters" else sum(1 for tok in text.split() if any(c.isalnum() for c in tok))
    dur = max(0.01, ws[-1]["end"] - ws[0]["start"])
    rate = n / dur
    lo, mid, hi = PACE_BANDS[unit]
    band = (
        PACE_WORDS[0] if rate < lo else PACE_WORDS[1] if rate < mid else PACE_WORDS[2] if rate < hi else PACE_WORDS[3]
    )
    gaps = [round(ws[i + 1]["start"] - ws[i]["end"], 2) for i in range(len(ws) - 1)]
    pauses = [[round(ws[i]["end"], 2), g] for i, g in enumerate(gaps) if g > PAUSE_LISTED_S]
    trend = None
    if len(ws) >= TREND_MIN_WORDS:  # word onsets: a word's own length absorbs pauses and line-final drawl
        on = [w["start"] for w in ws]
        h = len(on) // 2
        a = (on[h] - on[0]) / h
        b = (on[-1] - on[h]) / (len(on) - 1 - h)
        trend = "speeds up" if b < TREND_FASTER * a else "slows down" if b > TREND_SLOWER * a else "even"
    return {
        "unit": unit,
        "count": n,
        "per_s": round(rate, 2),
        "band": band,
        "longest_gap_s": max(gaps) if gaps else 0.0,
        "pauses_over_0_4s": pauses,
        "trend": trend,
    }


def parse_range(s, n, what):
    s = str(s).strip()
    a, _, b = s.partition("-")
    try:
        a = int(a)
        b = int(b) if b else a
    except ValueError:
        die(f"{what}: '{s}' must be 'a-b' (integers)")
    if not (0 <= a <= b < n):
        die(f"{what}: '{s}' outside 0..{n - 1}")
    return a, b


class Judgment:
    def __init__(self, d, idx, pts, words):
        self.d, self.idx, self.pts, self.words = d, idx, pts, words
        self.dur = idx["facts"]["duration_video_s"]
        self.shots = {sh["id"]: sh for sh in idx["shots"]}

    def t(self, v, what):
        """A time: seconds, 'Sn' (start of shot n), 'Sn.end' or 'end'."""
        if isinstance(v, (int, float)):
            return float(v)
        v = str(v).strip()
        if v == "end":
            return self.dur
        m = re.fullmatch(r"(S\d+)(\.end)?", v)
        if m and m.group(1) in self.shots:
            sh = self.shots[m.group(1)]
            return sh["end"] if m.group(2) else sh["start"]
        try:
            return float(v)
        except ValueError:
            die(f"{what}: time '{v}' must be seconds, Sn, Sn.end or end")

    def region(self, tag):
        p = os.path.join(self.d, "look", tag + ".json")
        if not os.path.exists(p):
            die(f"text region '{tag}' not found (expected look/{tag}.json from the `text` command)")
        return read_json(p, "region file")

    def states(self, reg, spec, what):
        """'T3' or 'T3-T7' -> list of state dicts from a text-region file."""
        ids = [s["id"] for s in reg["states"]]
        a, _, b = str(spec).partition("-")
        b = b or a
        if a not in ids or b not in ids:
            die(f"{what}: states '{spec}' not in that region (has {ids[0]}..{ids[-1]})")
        return reg["states"][ids.index(a) : ids.index(b) + 1]


def vote_style(styles):
    """Combine per-state layer measurements (weighted by frames): a color wins when states
    holding most of the measured frames agree on it within 40 levels per channel."""
    # a state's fill that agreed with its region's reference color counts as that color
    ok = [({**s, "fill": s.get("agrees_with", s.get("fill"))}, w) for s, w in styles if s.get("measured")]
    total = sum(w for _, w in styles) or 1
    out = {"states_measured": len(ok), "states": len(styles)}
    if not ok:
        out["why"] = sorted({s.get("why", "") for s, _ in styles})
        return out

    def pick(key):
        votes = []
        for s, w in ok:
            if s.get(key):
                for v in votes:
                    if _near(v[0], s[key]):
                        v[1] += w
                        break
                else:
                    votes.append([s[key], w])
        if not votes:
            return None, 0.0
        best = max(votes, key=lambda v: v[1])
        return best[0], best[1] / sum(w for _, w in ok)

    for key in ("fill", "outline_color", "shadow_color", "box_color"):
        v, share = pick(key)
        if v and share >= 0.5:
            out[key] = v
            out[key + "_agree"] = round(share, 2)
    meas_w = sum(w for _, w in ok)
    out["frames_measured_share"] = round(meas_w / total, 2)
    ok = [(s, w) for s, w in ok if s.get("box")]  # size and place: only where they were kept
    if not ok:
        out["size_why"] = sorted({s.get("size_withdrawn", "") for s, _ in styles if s.get("measured")})
        return out
    cy = sorted((s["center"][1], w) for s, w in ok)
    cx = sorted((s["center"][0], w) for s, w in ok)
    out["center"] = [weighted_median(cx), weighted_median(cy)]
    out["box"] = [
        min(s["box"][0] for s, _ in ok),
        min(s["box"][1] for s, _ in ok),
        max(s["box"][2] for s, _ in ok),
        max(s["box"][3] for s, _ in ok),
    ]
    rp = [(s["row_px_1080w"], w) for s, w in ok if s.get("row_px_1080w")]
    out["row_px_1080w"] = weighted_median(sorted(rp)) if rp else None
    out["rows"] = max(s.get("rows", 1) for s, _ in ok)
    return out


def state_layer(st):
    """A text-region state's layer as `build` uses it: the trusted measurement, or why there is none."""
    return st.get("layer") or {"measured": False, "why": "not measured"}


# letter heights (px on a 1080-wide frame) below which a caption is each size; above the last, very_large
SIZE_BANDS = (("very_small", 30), ("small", 55), ("medium", 80), ("large", 120))


def size_class(row_px, text):
    """Letter height from a measured text-row height: a row with descenders is about 1.4 letter
    heights, lower-case without descenders about 1.2, all capitals 1.0. Bands for a 1080-wide frame:
    medium = 55-80 px letters, the usual vertical-video caption."""
    if not row_px:
        return None
    letters = [c for c in text if c.isalpha()]
    if letters and not any(c.islower() for c in letters):
        k = 1.0
    elif any(c in DESCENDERS for c in text):
        k = 1.4
    else:
        k = 1.2
    h = row_px / k
    for name, top in SIZE_BANDS:
        if h < top:
            return name
    return "very_large"


def box_params(b):
    """A graphic's box as the format's params."""
    return {
        "x_ratio": b[0],
        "y_ratio": b[1],
        "width_ratio": round(b[2] - b[0], 3),
        "height_ratio": round(b[3] - b[1], 3),
    }


def count_words(chunk):
    """Words in a caption chunk: space-separated tokens, each Han or kana character counting as one."""
    n = 0
    for tok in chunk.split():
        cj = sum(1 for c in tok if is_unspaced_script(c) and c.isalnum())
        n += cj if cj else 1
    return n


# ----------------------------------------------------------------------------- build stages
# `build` with a judgment file runs in stages on one BuildState: the stages turn the judgment into
# the format's parts (lines, entities, prose, slots), the checks compare them with each other and with
# the measurements, and the last two write the files and print the report. Problems stop the analysis
# from being written; warnings are printed and do not; unconfirmed statements refuse the build.
LOW_PROB = 0.5  # a transcript word below this probability is listed as low-probability (shown '?')
CENTERED_TOL = 0.03  # a caption whose center is within this of the frame's middle is centered: no x
NEAR_WHITE = 0xE6  # a fill with every channel at or above this is white, the default: no color written
BOUNDARY_TOL_S = 0.1  # a cut or panel change this close to a segment boundary is that boundary
NAMED_TIME_STEPS_S = (-0.1, -0.05, 0, 0.05, 0.1)  # a time is named in prose as mm:ss.s within a frame or two
EDGE_TOL_S = 0.05  # a moment counts as inside a segment from this much before its start
END_TOL_S = 0.06  # segment and slot ends match a boundary or the clip's end within this (rounding, a frame)
MAX_SLOTS = 4  # the format's slots are funnel stages: hook, build, payoff, call to action at most
CLOSING_QUOTES = "\"'”’)]»」』"  # stripped from a word before looking for the punctuation that ends it
SPEAKING_MODES = ("on_camera_dialogue", "voiceover", "no_dialogue")
MEANING_KEYS = {"attention_contract", "payoff_meaning", "proof_surface"}


class BuildState:
    """What the build stages share: the scan, the judgment, and what the stages find."""

    def __init__(self, idx, pts, words, J, jj=None, views=None):
        self.idx, self.pts, self.words, self.J = idx, pts, words, J
        self.jj, self.views = jj, views or {}
        self.dur = idx["facts"]["duration_video_s"]
        self.cuts = [sh["start"] for sh in idx["shots"][1:]]
        self.problems, self.warnings = [], []
        self.confirmed, self.unconfirmed = [], []  # unconfirmed: statements without a confirming view
        self.vsegs, self.line_facts = [], []
        self.speaking = "none"
        self.ents, self.ids = [], set()
        self.cap_report = []
        self.psegs, self.prose = [], ""
        self.slots = []
        self.meta = None
        self.own_means, self.tool_gaps = [], []
        self.hearing, self.heard, self.unheard = None, [], []  # unheard: statements of sound without a pass

    def add(self, e):
        if e["id"] in self.ids:
            self.problems.append(f"entity id '{e['id']}' used twice")
        self.ids.add(e["id"])
        self.ents.append(e)

    def details(self, text, window, where, uncertain):
        """Take the {words|view} marks out of a piece of judgment text, checking each (check_details)."""
        return check_details(text, window, where, self.views, self.unconfirmed, self.confirmed, uncertain)

    def segment_at(self, t, before=0.0):
        """The prose segment holding time t (counted from `before` seconds ahead of its start)."""
        return next((p for p in self.psegs if p["window"][0] - before <= t < p["window"][1]), None)

    def boundaries(self):
        return [p["window"][0] for p in self.psegs[1:]]

    def person_ids(self):
        return {e["id"] for e in self.ents if e["kind"] in ("person", "source_image")}


def sentence_pause_warnings(k, a_, ws):
    """One line is one sentence (references/METHOD.md, section 5): a sentence end with a pause after it
    inside a line is two lines in one; a comma with a pause after it may be one too (recognizers often
    join two sentences with a comma)."""
    out = []
    for j in range(len(ws) - 1):
        gap = ws[j + 1]["start"] - ws[j]["end"]
        end = ws[j]["word"].strip().rstrip(CLOSING_QUOTES)
        if gap >= LINE_PAUSE_S and end.endswith(SENTENCE_ENDS):
            out.append(
                f"vs{k}: '{ws[j]['word'].strip()}' (word {a_ + j}) ends a sentence and a {gap:.2f} s "
                f"pause follows; one line is one sentence: end the line at word {a_ + j}"
            )
        elif gap >= LINE_PAUSE_S and end.endswith((",", "，", "、", ";", "；")):
            out.append(
                f"vs{k}: '{ws[j]['word'].strip()}' (word {a_ + j}) is followed by a {gap:.2f} s pause; "
                f"if the words up to it make a complete sentence, end the line at word {a_ + j}"
            )
    return out


def line_fact(k, ws, pace, crosses, low, text):
    """The LINES row `build` prints for one spoken line."""
    return (
        f"  vs{k} {fmt_t(ws[0]['start'])}–{fmt_t(ws[-1]['end'])} {pace['per_s']} {pace['unit']}/s "
        f"= {pace['band']}"
        + (f", {pace['trend']}" if pace["trend"] and pace["trend"] != "even" else "")
        + (f", pauses {pace['pauses_over_0_4s']}" if pace["pauses_over_0_4s"] else "")
        + (
            f", crosses cut {', '.join(fmt_t(c) for c in crosses)}: its [voice:vs{k}] goes in the "
            f"segment holding {fmt_t(ws[0]['start'])}, where it starts"
            if crosses
            else ""
        )
        + (f", low-prob: {' '.join(low)}" if low else "")
        + f"  | {text}"
    )


def build_lines(s):
    """Spoken lines: voice segments with measured times and pace, and the facts printed under LINES."""
    words = s.words
    for k, ln in enumerate(s.J.get("lines", []), 1):
        a_, b_ = parse_range(ln.get("words", ""), len(words), f"lines[{k - 1}].words")
        ws = words[a_ : b_ + 1]
        text = join_words([w["word"] for w in ws])
        src, notes = {"time_range": "measured", "text": "measured"}, []
        for old, new in (ln.get("fix") or {}).items():
            if old not in text:
                s.problems.append(f"vs{k}: fix '{old}' not found in transcript text '{text}'")
            text = text.replace(old, new, 1)
            notes.append(f"transcript '{old}' -> '{new}' (seen in a word-for-word caption)")
        if ln.get("text"):
            text = ln["text"]
            src["text"] = "seen"
        low = [w["word"] for w in ws if w.get("prob") is not None and w["prob"] < LOW_PROB]
        crosses = [c for c in s.cuts if ws[0]["start"] < c < ws[-1]["end"]]
        pace = pace_of(ws, text)  # counted on the line as corrected, timed on its words
        s.warnings += sentence_pause_warnings(k, a_, ws)
        seg = {
            "id": f"vs{k}",
            "time_range": [round(ws[0]["start"], 2), round(ws[-1]["end"], 2)],
            "text": text.strip(),
            "mode": ln.get("mode", "on_camera_dialogue"),
            "speaker": ln.get("speaker"),
        }
        for f in ("mode", "speaker"):
            if f in (ln.get("inferred") or []):
                src[f] = "inferred"
            if f in (ln.get("cannot_judge") or []):
                src[f] = "cannot_judge_locally"
        seg["_src"] = src
        seg["_pace"] = pace
        if low:
            notes.append("low-probability words: " + ", ".join(low))
        if crosses:
            notes.append("line runs across cut(s) at " + ", ".join(fmt_t(c) for c in crosses))
        if ln.get("uncertain"):
            notes.append("uncertain: " + "; ".join(ln["uncertain"]))
        if notes:
            seg["_notes"] = notes
        if seg["mode"] not in SPEAKING_MODES:
            s.problems.append(f"vs{k}: mode '{seg['mode']}' is not on_camera_dialogue / voiceover / no_dialogue")
        if seg["mode"] != "no_dialogue" and not seg["speaker"]:
            s.problems.append(f"vs{k}: speaker missing")
        s.vsegs.append(seg)
        s.line_facts.append(line_fact(k, ws, pace, crosses, low, seg["text"]))
    s.speaking = speaking_mode(s.vsegs)


def check_words_used_once(s):
    """A transcript word belongs to one spoken line, and a word of a line is not also music."""
    used = {}
    for k, ln in enumerate(s.J.get("lines", []), 1):
        a_, b_ = parse_range(ln.get("words", ""), len(s.words), "lines")
        for i in range(a_, b_ + 1):
            if i in used:
                s.problems.append(f"word {i} is in both {used[i]} and vs{k}")
            used[i] = f"vs{k}"
    for m in s.J.get("music_words", []):
        a_, b_ = parse_range(m.get("words", ""), len(s.words), "music_words")
        for i in range(a_, b_ + 1):
            if i in used:
                s.problems.append(f"word {i} is both a spoken line ({used[i]}) and music")
                break


def speaking_mode(vsegs):
    modes = {v["mode"] for v in vsegs if v["mode"] != "no_dialogue"}
    if not modes:
        return "none"
    if modes == {"on_camera_dialogue"}:
        return "on_camera"
    if modes == {"voiceover"}:
        return "voiceover"
    return "mixed"


def build_people(s):
    for p in s.J.get("people", []):
        tr_ = [round(s.jj.t(x, p["id"]), 3) for x in p.get("time", [0, "end"])]
        unc = list(p.get("uncertain") or [])
        sem = s.details(p.get("semantic", ""), tr_, f"person {p['id']}", unc)
        e = {
            "id": p["id"],
            "kind": "person",
            "semantic": sem,
            "time_range": tr_,
            "attributes": p.get("attributes", {}),
            "params": {},
        }
        src = {f"attributes.{x}": "inferred" for x in p.get("inferred", [])}
        if src:
            e["_src"] = src
        if unc:
            e["_notes"] = unc
        s.add(e)


def caption_chunks(s, c, reg):
    """A caption's chunks [text, on, off] from the region states it reads, the styles of those states
    weighted by frames, and notes on chunks trimmed to the states that show its layer."""
    chunks, styles, trim = [], [], []
    for spec, txt in c.get("read", []):
        sts = s.jj.states(reg, spec, f"caption {c['id']}")
        # a state measured as showing no drawn layer (the strokes held before it left as it began,
        # nothing drawn held through it) is not part of the caption: a chunk ends before it.
        # Trimmed at either end, with a note; inside a chunk it splits two displays
        gone = [x["id"] for x in sts if x.get("empty")]
        if gone:
            while sts and sts[-1].get("empty"):
                sts = sts[:-1]
            while sts and sts[0].get("empty"):
                sts = sts[1:]
            if not sts or any(x.get("empty") for x in sts):
                s.problems.append(
                    f"caption {c['id']}: chunk {spec} includes {', '.join(gone)}, measured as showing "
                    f"no drawn layer; read the states on either side as separate chunks"
                )
                if not sts:
                    continue
            else:
                trim.append(
                    f"chunk {spec} taken as {sts[0]['id']}-{sts[-1]['id']} "
                    f"({fmt_t(sts[0].get('appearing_from', sts[0]['on']))}–{fmt_t(sts[-1]['off'])}): "
                    f"{', '.join(gone)} shows no drawn layer (measured)"
                )
        # times are the states' own edges: the frames where the layer's pixels changed
        chunks.append([txt, sts[0].get("appearing_from", sts[0]["on"]), sts[-1]["off"]])
        styles += [(state_layer(x), x["frames"]) for x in sts]
        if any(x.get("on_clipped") for x in sts[:1]) or any(x.get("off_clipped") for x in sts[-1:]):
            s.problems.append(
                f"caption {c['id']}: a chunk touches the edge of the `text` window; "
                "re-run `text` over a window that contains the whole caption (end it a second past "
                "where the caption leaves, never on a cut: a caption can stay into the next shot)"
            )
    return chunks, styles, trim


def caption_moving_states(s, c, reg, sty):
    """States of a caption in which the layer kept changing across the caption's own text line.

    Words per caption is measured only when every chunk is one display: a state in which the layer
    kept changing where this caption sits (a word-by-word reveal not separated) shows several displays,
    and its words-per-caption would be too high. Only changes reaching across the caption's own text
    line count: a recorded screen changing beside the caption in the same region says nothing about it."""
    cb = sty.get("box")
    cy_ = c.get("position_y_ratio")
    if cb:
        mid, half = (cb[1] + cb[3]) / 2, 0.25 * (cb[3] - cb[1])
    elif isinstance(cy_, (int, float)):
        mid, half = cy_, 0.005
    else:
        mid, half = None, 0
    return [
        x["id"]
        for spec, _ in c.get("read", [])
        for x in s.jj.states(reg, spec, c["id"])
        if x.get("changes_inside")
        and (mid is None or (x["changes_inside"][1] <= mid - half and x["changes_inside"][3] >= mid + half))
    ]


CAPTION_READ_KEYS = (
    "color",
    "outline_color",
    "box_color",
    "approximate_size",
    "position_y_ratio",
    "position_x_ratio",
    "cue_max_words",
)


def build_caption(s, c):
    """One caption entity: its text and times from the states it reads, its style from their pixels,
    with the agent's own reading replacing a measurement where it gives one."""
    reg = s.jj.region(c["region"])
    chunks, styles, trim = caption_chunks(s, c, reg)
    if not chunks:
        s.problems.append(f"caption {c['id']}: no 'read' chunks")
        return
    sty = vote_style(styles)
    text = " ".join(t for t, _, _ in chunks if t)
    params = {"text": text}
    src = {"time_range": "measured", "params.cue_max_words": "measured"}
    if sty.get("center"):
        params["position_y_ratio"] = round(sty["center"][1], 3)
        src["params.position_y_ratio"] = "measured"
        if abs(sty["center"][0] - 0.5) >= CENTERED_TOL:
            params["position_x_ratio"] = round(sty["center"][0], 3)
            src["params.position_x_ratio"] = "measured"
    size = size_class(sty.get("row_px_1080w"), text)
    if size:
        params["approximate_size"] = size
        src["params.approximate_size"] = "measured"
    fill = sty.get("fill")
    if fill and not all(int(fill[i : i + 2], 16) >= NEAR_WHITE for i in (1, 3, 5)):
        params["color"] = fill
        src["params.color"] = "measured"
    for key in ("outline_color", "box_color"):
        if sty.get(key):
            params[key] = sty[key]
            src["params." + key] = "measured"
    moving = caption_moving_states(s, c, reg, sty)
    if moving:
        notes_cue = (
            f"cue_max_words not measured: the layer kept changing inside {', '.join(moving)} (a "
            f"reveal the `text` split did not separate)"
        )
        src.pop("params.cue_max_words", None)
    else:
        notes_cue = None
        params["cue_max_words"] = max(count_words(t) for t, _, _ in chunks)
    for key in ("voice_anchor", "visual_anchor", "highlight_words", "highlight_color"):
        if c.get(key):
            params[key] = c[key]
    notes = trim + ([notes_cue] if notes_cue else [])
    for key in CAPTION_READ_KEYS:
        if key in c:  # the agent's own reading replaces a measurement
            if key in params and params[key] != c[key]:
                notes.append(f"{key}: measured {params[key]}, set to {c[key]} by reading ({c.get('why', 'see notes')})")
            params[key] = c[key]
            src["params." + key] = "seen"
            if c[key] is None:
                params.pop(key)
    if sty.get("shadow_color") and "outline_color" not in params:
        notes.append(f"measured a shadow {sty['shadow_color']}, not an outline")
    if not sty.get("states_measured"):
        notes.append("style not measured: " + "; ".join(sty.get("why", [])))
    elif sty.get("size_why"):
        notes.append("size and position not measured: " + "; ".join(sty["size_why"]))
    if c.get("uncertain"):
        notes += c["uncertain"]
    e = {
        "id": c["id"],
        "kind": "subtitle",
        "semantic": c.get("semantic", ""),
        "time_range": [round(chunks[0][1], 3), round(chunks[-1][2], 3)],
        "attributes": {},
        "params": params,
        "_src": src,
        "_measured_style": sty,
    }
    if notes:
        e["_notes"] = notes
    e["_region"] = c["region"]
    e["_trim"] = trim
    s.add(e)


SIBLING_KEYS = ("position_y_ratio", "approximate_size", "color", "outline_color", "box_color")


def fill_captions_from_siblings(caps):
    """A caption whose states all change on the same frames as the picture behind it (or whose
    measurement was withdrawn) takes what it lacks from a measured caption of the same region."""
    for e in caps:
        ms = e["_measured_style"]
        lack = [
            k
            for k in SIBLING_KEYS
            if k not in e["params"]
            and not e["_src"].get("params." + k)
            and (
                k in ("position_y_ratio", "approximate_size")
                and not ms.get("box")
                or k not in ("position_y_ratio", "approximate_size")
                and not ms.get("states_measured")
            )
        ]
        sib = next(
            (
                x
                for x in caps
                if x is not e
                and x["_region"] == e["_region"]
                and x["_measured_style"].get("states_measured")
                and x["_measured_style"].get("box")
            ),
            None,
        )
        if not lack or not sib:
            continue
        got = [k for k in lack if k in sib["params"] and sib["_src"].get("params." + k) == "measured"]
        for k in got:
            e["params"][k] = sib["params"][k]
            e["_src"]["params." + k] = "inferred"
        if got:
            e.setdefault("_notes", []).append(f"{', '.join(got)} taken from {sib['id']} (same region, measured)")


def caption_lines(e, trim):
    """The CAPTIONS rows `build` prints for one caption: values read or inferred are tagged so."""
    p_, ms, sr = e["params"], e["_measured_style"], e["_src"]

    def val(k):
        tag = {"seen": " (read)", "inferred": " (inferred)"}.get(sr.get("params." + k), "")
        return f"{p_.get(k)}{tag}" if k in p_ else "-"

    fill = val("color") if "color" in p_ else ("white" if ms.get("fill") else "-")
    return [
        f"  {e['id']}: {e['time_range'][0]:.3f}–{e['time_range'][1]:.3f} y {val('position_y_ratio')} "
        f"size {val('approximate_size')} fill {fill} outline {val('outline_color')} "
        f"box {val('box_color')} cue {val('cue_max_words')} "
        f"[{ms.get('states_measured')}/{ms.get('states')} states measured"
        f"{'; shadow ' + ms['shadow_color'] if ms.get('shadow_color') else ''}]  {p_['text']}"
    ] + ["      " + x for x in trim]


def build_captions(s):
    for c in s.J.get("captions", []):
        build_caption(s, c)
    caps = [e for e in s.ents if e["kind"] == "subtitle"]
    fill_captions_from_siblings(caps)
    for e in caps:
        e.pop("_region", None)
        s.cap_report += caption_lines(e, e.pop("_trim", []))


def build_graphics(s):
    jj = s.jj
    for g in s.J.get("graphics", []):
        params = {"description": g.get("description", "")}
        if g.get("inline_text"):
            params["inline_text"] = g["inline_text"]
        src = {}
        if g.get("region") and not jj.region(g["region"]).get("states"):
            s.problems.append(
                f"graphic {g['id']}: region {g['region']} was not measured "
                f"({jj.region(g['region']).get('why', '')}); give a tighter box to `element`, or 'box' and 'time'"
            )
            tr = [jj.t(x, g["id"]) for x in g.get("time", [0, "end"])]
        elif g.get("region"):
            reg = jj.region(g["region"])
            sts = jj.states(
                reg, g.get("states", reg["states"][0]["id"] + "-" + reg["states"][-1]["id"]), f"graphic {g['id']}"
            )
            tr = [sts[0].get("appearing_from", sts[0]["on"]), sts[-1]["off"]]
            src["time_range"] = "measured"
            sty = vote_style([(state_layer(x), x["frames"]) for x in sts])
            if sty.get("box") and "box" not in g:
                params.update(box_params(sty["box"]))
                for f in ("x_ratio", "y_ratio", "width_ratio", "height_ratio"):
                    src["params." + f] = "measured"
        else:
            tr = [jj.t(x, g["id"]) for x in g.get("time", [0, "end"])]
        if g.get("box"):
            params.update(box_params(g["box"]))
        elif "x_ratio" not in params:
            why_ = ""
            if g.get("region"):
                sts_ = jj.region(g["region"]).get("states") or []
                why_ = next(
                    (
                        x["layer"].get("why", "")
                        for x in sts_
                        if not (x.get("layer") or {}).get("measured") and x.get("layer")
                    ),
                    "",
                )
            s.problems.append(
                f"graphic {g['id']}: no box: "
                + (f"region {g['region']} measured its times but not its box ({why_}); " if g.get("region") else "")
                + "give 'box': [x0, y0, x1, y1] drawn by eye, with a 'why'"
            )
        params["split"] = bool(g.get("split", False))
        e = {
            "id": g["id"],
            "kind": "graphic",
            "semantic": g.get("semantic", ""),
            "time_range": [round(x, 3) for x in tr],
            "attributes": {},
            "params": params,
        }
        if src:
            e["_src"] = src
        if g.get("uncertain"):
            e["_notes"] = g["uncertain"]
        s.add(e)


def build_objects(s):
    for o in s.J.get("objects", []):
        tr_ = [round(s.jj.t(x, o["id"]), 3) for x in o.get("time", [0, "end"])]
        unc = list(o.get("uncertain") or [])
        desc = s.details(o.get("description", ""), tr_, f"object {o['id']}", unc)
        sem = s.details(o.get("semantic", ""), tr_, f"object {o['id']} semantic", unc)
        e = {
            "id": o["id"],
            "kind": "source_image",
            "semantic": sem,
            "time_range": tr_,
            "attributes": {},
            "params": {"description": desc},
        }
        if unc:
            e["_notes"] = unc
        s.add(e)


# `to` is where a segment or slot ends; Sn is the start of shot n, so one over shot n ends at S(n+1) or Sn.end
TO_HINT = " (`to` is where it ends: Sn is the start of shot n, so one over shot n alone ends at S(n+1) or Sn.end)"


def build_prose(s):
    """Prose segments: each judgment segment's text with its marks checked and taken out, headed by its
    window, with the claims it makes and the measurements that fall inside it."""
    t0 = 0.0
    for k, sg in enumerate(s.J.get("segments", [])):
        t1 = s.jj.t(sg.get("to", "end"), f"segments[{k}].to")
        if t1 <= t0 + 1e-6:
            s.problems.append(f"segments[{k}]: ends at {t1} which is not after its start {t0}{TO_HINT}")
        head = f"[{mmss(t0)}-{mmss(t1)}]"
        unc = list(sg.get("uncertain") or [])
        body = s.details(sg.get("text", "").strip(), [t0, t1], f"segment {k + 1} [{mmss(t0)}-{mmss(t1)}]", unc)
        body = fix_articles(re.sub(r"  +", " ", body))
        ps = {"window": [round(t0, 3), round(t1, 3)], "text": f"{head} {body}"}
        tags = {}
        for lab, val in (
            ("inferred", sg.get("inferred")),
            ("uncertain", unc),
            ("cannot_judge_locally", sg.get("cannot_judge")),
        ):
            if val:
                tags[lab] = val
        meas = [f"cut at {mmss(c)}" for c in s.cuts if t0 - EDGE_TOL_S <= c <= t1 + EDGE_TOL_S]
        meas += [
            f"{e['type']} {e['db']} dB at {mmss(e['t'])}"
            for e in (s.idx.get("audio") or {}).get("events", [])
            if t0 <= e["t"] < t1 and mmss(e["t"]) in body
        ]
        if meas:
            tags["measured"] = meas
        if tags:
            ps["claims"] = tags
        s.psegs.append(ps)
        t0 = t1
    if s.psegs and abs(t0 - s.dur) > END_TOL_S:
        s.problems.append(f"segments end at {t0:.2f}, clip ends at {s.dur:.2f} (last 'to' should be 'end')")
    s.prose = "\n\n".join(p["text"] for p in s.psegs)


def check_garment_color_names(s):
    """One garment or product keeps one color name everywhere."""
    J = s.J
    texts = [(f"segment {k + 1}", sg.get("text", "")) for k, sg in enumerate(J.get("segments", []))]
    texts += [(f"person {p.get('id')}", p.get("semantic", "")) for p in J.get("people", [])]
    texts += [
        (f"object {o.get('id')}", (o.get("semantic", "") + " " + o.get("description", "")))
        for o in J.get("objects", [])
    ]
    for gar, by in sorted(color_names_by_garment(texts).items()):
        if len(by) > 1:
            s.warnings.append(
                f"'{gar}' is called "
                + "; ".join(f"{' and '.join(c)} ({', '.join(sorted(set(w)))})" for c, w in sorted(by.items()))
                + ": one garment or product keeps one color name everywhere (from `color`); for "
                "different ones, say what tells them apart"
            )


VOICEOVER_WORDS = re.compile(
    r"voice[\s-]?over|off[\s-]?(?:camera|screen|frame)|narrat|unseen|not (?:on|in) (?:camera|frame|shot)", re.I
)


def check_voiceover_in_summary(s):
    """The report's summary of who speaks how: with lines both on camera and in voiceover, a summary
    that never mentions the voiceover reads as all on camera."""
    lines = s.J.get("lines") or []
    vo = [f"vs{k}" for k, ln in enumerate(lines, 1) if ln.get("mode") == "voiceover"]
    oc = any(ln.get("mode", "on_camera_dialogue") == "on_camera_dialogue" for ln in lines)
    wh = str((s.J.get("report") or {}).get("what_happens") or "")
    if vo and oc and wh and not VOICEOVER_WORDS.search(wh):
        s.warnings.append(
            f"report what_happens: {', '.join(vo)} {'is' if len(vo) == 1 else 'are'} voiceover and the "
            f"other lines on camera; say which part is which, or it reads as all on camera"
        )


NO_SPEECH_WORDS = re.compile(
    r"\b(?:no (?:speech|dialogue|talking|narration|voice(?:[\s-]?over)?|spoken (?:words?|lines?))|"
    r"(?:nobody|no[\s-]one) (?:speaks|talks|says)|(?:never|does not|doesn't|do not|don't) (?:speak|talk)s?|"
    r"wordless|without (?:any )?(?:speech|words|dialogue|speaking|talking))\b",
    re.I,
)


def speech_unknown(s):
    """Why the speech is not known (speech recognition failed or did not run on a video with sound), or
    None when it is known."""
    st = stages_of(s.idx)["speech_recognition"]
    return st["why"] if st["state"] != "ran" and s.idx["facts"].get("has_audio") else None


def check_no_speech_claims(s):
    """With the speech not transcribed, nothing has measured whether anyone speaks: text saying that
    nobody does would state as fact what was never measured."""
    why = speech_unknown(s)
    if not why:
        return
    R = s.J.get("report") or {}
    for where, text in [("prose", s.prose)] + [
        (f"report {k}", str(R.get(k) or "")) for k in ("what_happens", "why_it_holds")
    ]:
        for m in NO_SPEECH_WORDS.finditer(text):
            s.problems.append(
                f"{where}: '{m.group(0)}', but the speech was not transcribed ({why}): whether anyone speaks is "
                f"not known. Say that the speech was not transcribed, and describe only what the pictures show "
                f"(a mouth that moves or stays closed)"
            )


def time_pair(tm):
    """Whether a judgment's 'time' is [start, end], each seconds, Sn, Sn.end or end."""
    return isinstance(tm, list) and len(tm) == 2 and all(isinstance(v, (str, int, float)) for v in tm)


# words that say what a sound is, which only hearing settles (`references/TOOL.md`, Sound words)
SOUND_WORDS = re.compile(
    r"\b(?:music(?:al)?|songs?|sung|sings?|singing|singers?|melod(?:y|ies|ic)|instrumentals?|lyrics?|"
    r"bass(?:lines?)?|drums?|percussion|beat drops?|whoosh(?:es)?|swoosh(?:es)?|sound effects?|sfx|"
    r"jingles?|chimes?|applause|tone of (?:\w+ )?voice)\b",
    re.I,
)
# a sentence holding one of these says the sound is not known, rather than what it is
SOUND_NOT_KNOWN = re.compile(
    r"\b(?:whether|unknown|unclear|(?:cannot|can't|can not) be (?:judged|told|known|heard)|"
    r"(?:is|are|was|were|stays?) not (?:known|judged|heard|told apart))\b",
    re.I,
)
# fields whose text is not the agent's statement of what the sound is: what it says it cannot judge, the
# heard statements (after a pass), and words taken from the transcript or the screen
SOUND_FREE_KEYS = ("cannot_judge", "heard", "fix", "inline_text", "highlight_words")


def judgment_texts(x, where=""):
    """(where, text) of every string the agent wrote in the judgment, outside SOUND_FREE_KEYS."""
    if isinstance(x, dict):
        for k, v in x.items():
            if k not in SOUND_FREE_KEYS:
                yield from judgment_texts(v, f"{where}.{k}" if where else str(k))
    elif isinstance(x, list):
        for k, v in enumerate(x):
            yield from judgment_texts(v, f"{where}[{k}]")
    elif isinstance(x, str):
        yield where, x


def check_sound_claims(s):
    """Without a passed hearing check, nothing has heard the sound: a statement anywhere in the judgment of
    what it is (music, a song, a sound effect, a tone of voice) would state as fact what nobody heard. Found
    by the words of SOUND_WORDS, as check_no_speech_claims finds claims that nobody speaks."""
    st = hearing_state(s.jj.d)["state"] if s.idx["facts"].get("has_audio") else "no_audio_track"
    if st == "passed":
        return
    why = {
        "failed": "this agent's hearing check failed",
        "cannot_hear": "this agent said it cannot open sound",
        "not_taken": "no hearing check was answered for this analysis",
        "no_audio_track": "the video has no audio track",
    }[st]
    for where, text in judgment_texts(s.J):
        for sent in re.split(r"(?<=[.;!?])\s+", text):
            if SOUND_NOT_KNOWN.search(sent):
                continue
            for m in SOUND_WORDS.finditer(sent):
                s.problems.append(
                    f"{where}: '{m.group(0)}' says what the sound is, and nothing heard it ({why}). Say only what "
                    f"the tool measured (loudness, times) and put what the sound is under cannot_judge; after a "
                    f"passed hearing check, write it under heard"
                )


def build_own_means(s):
    """Facts the agent established by means the tool does not provide (another program, a service, a source
    of its own), each with what it used: they go out marked as such, never as measured or seen."""
    s.own_means = []
    given = s.J.get("own_means") or []
    if not isinstance(given, list):
        s.problems.append('own_means: give a list, [{"fact": "...", "used": "what you used"}, ...]')
        given = []
    for k, x in enumerate(given):
        if not (
            isinstance(x, dict)
            and isinstance(x.get("fact"), str)
            and x["fact"].strip()
            and isinstance(x.get("used"), str)
            and x["used"].strip()
        ):
            s.problems.append(f'own_means[{k}]: give each as {{"fact": "...", "used": "what you used"}}')
            continue
        e = {"fact": x["fact"].strip(), "used": x["used"].strip()}
        if x.get("time") is not None and not time_pair(x["time"]):
            s.problems.append(f"own_means[{k}]: 'time' is [start, end]")
        elif x.get("time") is not None:
            e["time_range"] = [round(s.jj.t(v, f"own_means[{k}]"), 3) for v in x["time"]]
        s.own_means.append(e)
    gaps = s.J.get("tool_gaps")
    if gaps is not None and not isinstance(gaps, list):
        s.problems.append('tool_gaps: give a list, ["what the tool lacked, and what you did instead", ...]')
    s.tool_gaps = gaps if isinstance(gaps, list) else []


def build_heard(s):
    """What the sound is, as the agent heard it: only after it passed the hearing check for this analysis,
    and each from a sound file `listen` cut. Without a pass every such statement refuses the build."""
    if not s.idx["facts"].get("has_audio"):
        s.hearing = {"state": "no_audio_track"}
    else:
        s.hearing = hearing_state(s.jj.d)
    given = s.J.get("heard") or []
    if not isinstance(given, list):
        s.problems.append('heard: give a list of statements, [{"clip": NAME, "about": ..., "text": "..."}, ...]')
        return
    if not given:
        return
    if s.hearing["state"] != "passed":
        why = {
            "failed": "this agent's hearing check failed",
            "cannot_hear": "this agent said it cannot open sound",
            "not_taken": "no hearing check was answered for this analysis",
            "no_audio_track": "the video has no audio track",
        }[s.hearing["state"]]
        for k, x in enumerate(given):
            text = str(x.get("text") if isinstance(x, dict) else x)
            s.unheard.append(f"heard[{k}] ({text[:60]}): {why}")
        return
    clips = listen_clips(s.jj.d)
    for k, x in enumerate(given):
        if not (isinstance(x, dict) and isinstance(x.get("text"), str) and x["text"].strip()):
            s.problems.append(f'heard[{k}]: give each as {{"clip": NAME, "about": ..., "text": "..."}}')
            continue
        clip = x.get("clip")
        span = clips.get(clip) if isinstance(clip, str) else None
        if not span:
            s.problems.append(
                f"heard[{k}]: clip {json.dumps(clip, ensure_ascii=False)} is not a sound file `listen` cut in this "
                f"scan folder ({', '.join(sorted(clips)) or 'none yet: run listen'})"
            )
            continue
        if not (isinstance(x.get("about"), str) and x["about"] in HEARD_ABOUT):
            s.problems.append(f"heard[{k}]: 'about' is one of {', '.join(HEARD_ABOUT)}")
            continue
        tm = x.get("time")
        if tm is not None and not time_pair(tm):
            s.problems.append(f"heard[{k}]: 'time' is [start, end] (seconds, Sn, Sn.end or end)")
            continue
        tr = [round(s.jj.t(v, f"heard[{k}]"), 3) for v in tm or span]
        if tr[0] < span[0] - EDGE_TOL_S or tr[1] > span[1] + EDGE_TOL_S or tr[1] <= tr[0]:
            s.problems.append(f"heard[{k}]: time {tr} lies outside the clip it was heard in ({span[0]}–{span[1]} s)")
            continue
        # kept inside the clip and inside this video
        tr = [max(tr[0], span[0], 0.0), min(tr[1], span[1], s.jj.dur)]
        if tr[1] <= tr[0]:
            s.problems.append(f"heard[{k}]: time {tr} lies outside this video (0–{s.jj.dur} s)")
            continue
        s.heard.append(
            {
                "id": f"h{len(s.heard) + 1}",
                "time_range": tr,
                "about": x["about"],
                "text": x["text"].strip(),
                "clip": clip,
                "_src": {"text": "heard"},
            }
        )


def check_measured_colors(s):
    """A color written in a confirmed statement that no `color` measurement of that moment could be:
    the cheap mismatch the tool can see (the reading itself stays the agent's)."""
    idx, pts = s.idx, s.pts
    runs = [f for f in idx.get("followups", []) if f.get("cmd") == "color" and f.get("colors") and f.get("frames")]

    def shot_of(t):
        return next((sh["id"] for sh in idx["shots"] if sh["start"] - 1e-6 <= t < sh["end"] + 1e-6), None)

    for c in s.confirmed:
        said = written_colors(c["words"])
        if not said or (s.views.get(view_name(c["view"])) or {}).get("frames"):
            continue
        near = []
        for f in runs:
            ft = pts[f["frames"][0]] if f["frames"][0] < len(pts) else None
            if ft is None or shot_of(ft) != shot_of(c["t"]):
                continue
            fb = f.get("box") or [0, 0, 1, 1]
            mx, my = (fb[0] + fb[2]) / 2, (fb[1] + fb[3]) / 2
            if c.get("box") and not (c["box"][0] <= mx <= c["box"][2] and c["box"][1] <= my <= c["box"][3]):
                continue
            near.append((ft, fb, [x.get("name_ref") or x["name"] for x in f["colors"]]))
        if not near:
            continue
        # each color word on its own: a statement naming two things (a pink and green can) passes only
        # when every one of its colors fits some measurement. A metal's color is its shine, which a
        # box's main colors do not show: gold and silver are not checked
        fams = {q for _, _, ns in near for n in ns for q in measured_families(n)}
        bad = [w for w in said if w not in METAL_COLORS and not COLOR_FITS[w] & fams]
        if bad:
            s.warnings.append(
                f"{c['where']}: '{c['words']}' says {', '.join(bad)}, but no `color` measurement in the "
                f"same shot could be {' or '.join(bad)}: it measured "
                + "; ".join(
                    f"{', '.join(ns)} at {ft:.2f} s (box {','.join(f'{v:.2f}' for v in fb)})" for ft, fb, ns in near
                )
                + f": if one of those boxes was on the thing called {' or '.join(bad)}, look again and "
                f"name the color `color` gives; if none was, measure that thing with `color`"
            )


def build_slots(s):
    t0 = 0.0
    for k, sl in enumerate(s.J.get("slots", []), 1):
        t1 = s.jj.t(sl.get("to", "end"), f"slots[{k - 1}].to")
        f = sl.get("formula", {})
        miss = [x for x in FORMULA_KEYS if x not in f]
        if miss:
            s.problems.append(f"s{k}: formula missing {', '.join(miss)}")
        mc = f.get("meaning_contract")
        if isinstance(mc, dict) and set(mc) != MEANING_KEYS:
            s.problems.append(f"s{k}: meaning_contract needs attention_contract, payoff_meaning, proof_surface")
        if t1 <= t0 + 1e-6:
            s.problems.append(f"s{k}: ends at {t1} which is not after its start {t0}{TO_HINT}")
        slot = {
            "id": f"s{k}",
            "time_range": [round(t0, 3), round(t1, 3)],
            "formula": f,
            "_src": {"time_range": "inferred", "formula": "inferred"},
        }
        if sl.get("cannot_judge"):
            slot["_src"].update({f"formula.{x}": "cannot_judge_locally" for x in sl["cannot_judge"]})
        s.slots.append(slot)
        t0 = t1


# ---- checks: the format's rules, and consistency with the measurements
def named_in(t, text):
    """Is time t written (as mm:ss.s, within a frame or two) in text?"""
    return any(mmss(t + dt) in text for dt in NAMED_TIME_STEPS_S)


def check_cuts_named(s):
    """Every cut is a segment boundary or is named in its segment."""
    bounds = s.boundaries()
    for c in s.cuts:
        if any(abs(c - b) <= BOUNDARY_TOL_S for b in bounds):
            continue
        seg = s.segment_at(c)
        if seg and not named_in(c, seg["text"]):
            s.problems.append(f"cut at {fmt_t(c)} is neither a segment boundary nor named ({mmss(c)}) in its segment")


def check_panel_changes_named(s):
    """A panel change (a cut inside one pane) is a segment boundary or is named in its segment."""
    bounds = s.boundaries()
    for ev in s.idx["events"]:
        if ev["kind"] == "panel":
            seg = s.segment_at(ev["t"])
            if (
                seg
                and not any(abs(ev["t"] - b) <= BOUNDARY_TOL_S for b in bounds)
                and not named_in(ev["t"], seg["text"])
            ):
                s.problems.append(
                    f"{ev['id']} panel change at {fmt_t(ev['t'])} (a cut inside one pane?) is not named in its segment"
                )


def check_prose_quotes(s):
    if '"' in s.prose:
        s.problems.append("prose contains the ASCII double-quote character")


def check_image_markers(s):
    pid = s.person_ids()
    for m in re.finditer(r"\[image:([^\]]+)\]", s.prose):
        if m.group(1) not in pid:
            s.problems.append(f"[image:{m.group(1)}] names no person or source_image entity")


def check_entities(s):
    """Objects are labeled by a caption, people and objects appear in prose, caption anchors exist."""
    labeled = {e["params"].get("visual_anchor") for e in s.ents if e["kind"] == "subtitle"}
    for e in s.ents:
        if e["kind"] == "source_image" and e["id"] not in labeled:
            s.problems.append(
                f"object {e['id']}: no caption names it as visual_anchor. 'objects' holds only a filmed "
                f"object some caption labels (marked [image:{e['id']}] in prose, named by that caption's "
                f"visual_anchor); any other filmed thing is described in prose only, with no entry"
            )
        elif e["kind"] in ("person", "source_image") and f"[image:{e['id']}]" not in s.prose:
            s.problems.append(f"{e['kind']} {e['id']} never appears as [image:{e['id']}] in prose")
        if e["kind"] == "subtitle":
            va = e["params"].get("voice_anchor")
            if va and va not in {v["id"] for v in s.vsegs}:
                s.problems.append(f"{e['id']}: voice_anchor {va} is not a voice segment")
            vis = e["params"].get("visual_anchor")
            if vis and vis not in s.ids:
                s.problems.append(f"{e['id']}: visual_anchor {vis} is not an entity")


def check_voice_markers(s):
    """Each spoken line's [voice:X] marker: once in prose, in the segment where the line starts, after
    the marker of the person speaking it."""
    pid = s.person_ids()
    for v in s.vsegs:
        if v["speaker"] and v["speaker"] not in ("protagonist", "narrator") and v["speaker"] not in pid:
            s.problems.append(f"{v['id']}: speaker {v['speaker']} is not protagonist, narrator or a person entity")
        mark = f"[voice:{v['id']}]"
        n = s.prose.count(mark)
        if v["mode"] == "no_dialogue":
            if n:
                s.problems.append(f"{mark} in prose but the line is no_dialogue")
            continue
        if n != 1:
            s.problems.append(f"{mark} appears {n} times in prose (must be once)")
            continue
        st = v["time_range"][0]
        seg = s.segment_at(st, before=EDGE_TOL_S)
        if seg and mark not in seg["text"]:
            k_ = s.psegs.index(seg)
            at = next((j for j, p in enumerate(s.psegs) if mark in p["text"]), None)
            s.problems.append(
                f"{mark} is in segment {at + 1}, but the line starts at {fmt_t(st)}, inside "
                f"segment {k_ + 1} [{mmss(seg['window'][0])}-{mmss(seg['window'][1])}]: put its marker "
                f"there, after the speaker's marker; a line that runs on across the cut is not marked again "
                f"(the next segment says the speaker is still talking)"
            )
            continue  # the speaker check below reads the segment the marker belongs in
        # a speaker who is no person entity (a narrator, or the featured person seen only as hands or
        # from below the face: protagonist with no protagonist entity) has no marker to stand next to
        if seg and v["speaker"] and v["speaker"] in pid:
            left = seg["text"].split(mark)[0]
            mk = re.findall(r"\[image:([^\]]+)\]", left)
            if not mk:
                s.problems.append(f"{mark}: no [image:X] marker before it in its segment")
            elif mk[-1] != v["speaker"]:
                s.problems.append(f"{mark}: nearest marker to its left is {mk[-1]}, speaker is {v['speaker']}")


def check_pace_words(s):
    """The pace word next to a line is the measured band (one source)."""
    for v in s.vsegs:
        for sent in re.split(r"(?<=[.;!?])\s+", s.prose):
            if f"[voice:{v['id']}]" not in sent:
                continue
            said = [w for w in PACE_WORDS if re.search(r"\b" + re.escape(w) + r"\b", sent)]
            band = v["_pace"]["band"]
            if said and band not in said:
                s.problems.append(f"[voice:{v['id']}]: its sentence says {', '.join(said)}; measured pace is {band}")


def check_ids_as_words(s):
    """An entity id is a marker or nothing: written as a plain word it reaches the person's report as
    jargon ("the protagonist"); markers become plain words there ("the main person")."""
    plain = re.sub(r"\[(image|voice):[^\]]*\]", " ", s.prose)
    report = s.J.get("report") or {}
    rep = (
        " ".join(str(x) for x in report.values() if isinstance(x, str))
        + " "
        + " ".join(str(x) for x in report.get("swappable") or [])
    )
    for name in sorted({x for x in s.person_ids() if re.search(r"[_\d]", x)} | {"protagonist"}):  # id-like
        for where, txt in (("prose", plain), ("report", rep)):
            if re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", txt, re.I):
                s.problems.append(
                    f"{where}: the id '{name}' is written as a plain word; "
                    + (
                        f"write the marker [image:{name}] or plain words"
                        if where == "prose"
                        else "write plain words (the report is read by people, who never see ids)"
                    )
                )


def check_voice_ids(s):
    vids = {v["id"] for v in s.vsegs}
    for m in re.finditer(r"\[voice:([^\]]+)\]", s.prose):
        if m.group(1) not in vids:
            s.problems.append(f"[voice:{m.group(1)}] names no voice segment")
    if s.speaking == "none" and "[voice:" in s.prose:
        s.problems.append("speaking_mode none but prose has [voice:X]")


def check_slots(s):
    """At most four slots, one per funnel stage, each ending on a prose boundary, the last at the end."""
    stages = [x["formula"].get("funnel_stage") for x in s.slots]
    if len(s.slots) > MAX_SLOTS:
        s.problems.append(f"{len(s.slots)} slots (at most {MAX_SLOTS})")
    if len(set(stages)) != len(stages):
        s.problems.append("two slots share a funnel_stage")
    bounds = s.boundaries()
    for x in s.slots[:-1]:
        if not any(abs(x["time_range"][1] - b) <= END_TOL_S for b in bounds):
            s.problems.append(f"{x['id']} ends at {x['time_range'][1]} which is not a prose segment boundary")
    if s.slots and abs(s.slots[-1]["time_range"][1] - s.dur) > END_TOL_S:
        s.problems.append("last slot must end at 'end'")
    for need in ("segments", "slots"):
        if not s.J.get(need):
            s.problems.append(f"no {need} yet")


def check_video_format(s):
    """video_format = how the camera picture is partitioned at one moment, never how many shots. A
    measured split layout must be accounted for: two camera pictures at once is a split video_format;
    a recording, card or screenshot in one pane beside camera footage is a split graphic on single_shot."""
    J = s.J
    vf = J.get("video_format") or "single_shot"
    if vf not in VIDEO_FORMATS:
        s.problems.append(f"video_format '{vf}' is not one of {', '.join(VIDEO_FORMATS)}")
    if vf != "single_shot" and any(g.get("split") for g in J.get("graphics", [])):
        s.problems.append(
            f"video_format {vf} with a split graphic: a recording or card beside camera footage is "
            "a split graphic on single_shot; a split video_format needs two camera pictures at once"
        )
    for P in s.idx.get("panes") or []:
        sg = [g for g in J.get("graphics", []) if g.get("split")]
        if vf == "single_shot" and not sg:
            s.problems.append(
                f"{P['id']}: the frame is split {P['axis']} at {P['seam']:.3f} from {fmt_t(P['on'])} to "
                f"{fmt_t(P['off'])} (measured), but video_format is single_shot and no graphic has split: "
                f"true. Two camera pictures at once: video_format "
                f"{'split_screen_top_bottom' if P['axis'] == 'top/bottom' else 'split_screen_left_right'}; "
                f"a recording, card or screenshot in one pane: a graphic with split: true (region {P['id']} "
                f"via `element`)"
            )


def build_metadata(s):
    J = s.J
    vf = J.get("video_format") or "single_shot"
    lang = J.get("language") or (s.idx.get("transcript_meta") or {}).get("language")
    s.meta = {
        "duration_seconds": s.dur,
        "video_format": vf,
        "language": lang,
        "speaking_mode": s.speaking,
        "_src": {
            "duration_seconds": "measured",
            # with the speech not transcribed nothing measured whether anyone speaks: "none" only means
            # that the analysis has no spoken lines
            "speaking_mode": "cannot_judge_locally" if speech_unknown(s) else "measured",
            "video_format": "seen" if J.get("video_format") else "default",
            "language": "seen" if J.get("language") else "measured",
        },
    }
    if not lang:
        s.problems.append("language unknown: no transcript language; give 'language' (on-screen text language)")


STAGES = (
    build_lines,
    check_words_used_once,
    build_people,
    build_captions,
    build_graphics,
    build_objects,
    build_prose,
    check_garment_color_names,
    check_voiceover_in_summary,
    check_no_speech_claims,
    check_sound_claims,
    build_own_means,
    build_heard,
    check_measured_colors,
    build_slots,
    check_cuts_named,
    check_panel_changes_named,
    check_prose_quotes,
    check_image_markers,
    check_entities,
    check_voice_markers,
    check_pace_words,
    check_ids_as_words,
    check_voice_ids,
    check_slots,
    check_video_format,
    build_metadata,
)  # in this order: problems are printed in the order the stages find them


def music_words(s):
    out = []
    for m in s.J.get("music_words", []):
        a_, b_ = parse_range(m["words"], len(s.words), "music_words")
        out.append(
            {
                "words": m["words"],
                "text": join_words([w["word"] for w in s.words[a_ : b_ + 1]]),
                "why": m.get("why", ""),
            }
        )
    return out


def sound_at_picture_doc(s):
    """Which cuts and caption appearances a sound event falls on, as scan measured for the cuts and the
    same way for each caption's measured on time (tool-measured: times only, not what the sound is)."""
    sc, au = s.idx.get("sound_at_cuts"), s.idx.get("audio")
    if not sc or not au:
        return None
    caps = [
        {"id": e["id"], "kind": "caption", "span": [e["time_range"][0]] * 2}
        for e in s.ents
        if e["kind"] == "subtitle" and e.get("_src", {}).get("time_range") == "measured"
    ]
    cap = sound_at_picture(caps, au["events"], sc["tolerance_s"], sc["duration_s"])
    return {
        "tolerance_s": sc["tolerance_s"],
        "peaks_and_rises": sc["rises"],
        "cuts": {"summary": sound_at_summary(sc), "by_chance": sc["by_chance"], "changes": sc["changes"]},
        "captions": {
            "summary": sound_at_summary(cap, "caption appearances"),
            "by_chance": cap["by_chance"],
            "changes": cap["changes"],
        },
    }


def analysis_of(s, d, out_dir):
    """The riffsheet.json document."""
    idx, J = s.idx, s.J
    return {
        "format_version": FORMAT_VERSION,
        "prose": s.prose,
        "audio": {"voice_segments": s.vsegs, "heard": s.heard},
        "scene_entities": s.ents,
        "slots": s.slots,
        "metadata": s.meta,
        "_prose_segments": s.psegs,
        "_local": {
            "method": "riffsheet build",
            "scan": os.path.relpath(d, out_dir),
            "stages": stages_of(idx),
            "hearing": s.hearing,
            "tags": "untagged = seen; _src lists measured fields and exceptions only",
            "cuts": s.cuts,
            "non_cut_changes": [
                {k: e[k] for k in ("id", "t", "kind", "box")} for e in idx["events"] if e["kind"] != "cut"
            ],
            "camera_still_share": {sh["id"]: sh.get("still_share") for sh in idx["shots"]},
            "sound_at_picture": sound_at_picture_doc(s),
            "dropped_as_music": music_words(s),
            "cannot_judge_locally": J.get("cannot_judge", []),
            "tool_gaps": s.tool_gaps,
            "own_means": s.own_means,
            "followups": [
                {k: f.get(k) for k in ("cmd", "json", "window", "box", "frames")} for f in idx.get("followups", [])
            ],
            "images_viewed": J.get("images_viewed"),
            "checks": s.problems or "all passed",
            "confirmations": s.confirmed,
        },
    }


def write_outputs(s, analysis, out_dir):
    """Write riffsheet.json and riffsheet.md, or, when the build is refused or the document does not fit
    the format, remove any earlier ones (never leave an earlier, unchecked analysis behind)."""
    outs = [os.path.join(out_dir, f) for f in ("riffsheet.json", "riffsheet.md")]

    def remove_earlier():
        for f in outs:
            if os.path.exists(f):
                os.remove(f)

    if s.unheard:
        remove_earlier()
        print(
            f"build: REFUSED, nothing written to {out_dir}: {len(s.unheard)} statement(s) of what the sound is, "
            f"and this agent has not passed the hearing check for this analysis. Take it ({util.CMD} hear-check "
            f"DIR), or remove them: without a pass, what the sound is stays not judged."
        )
        return
    if s.unconfirmed:
        remove_earlier()
        print(
            f"build: REFUSED, nothing written to {out_dir}: {len(s.unconfirmed)} statement(s) about people, "
            f"products, supports or the place have no confirming view. Open a large view of each (`zoom` at "
            f"a moment inside its stretch, a box on it; several moments in one command) and wrap the words "
            f"as {{words|zoom_image_name}}, or as {{words|?}} to send them out tagged uncertain."
        )
        return
    # files meant to be shared: no home folder in them (it names the person)
    analysis = private_doc(analysis)
    # the file goes out only in the documented format: check it as it will be read back
    bad = validate(json.loads(json.dumps(analysis)), ANALYSIS_SCHEMA)
    if bad:
        remove_earlier()
        die(
            f"build: nothing written: the analysis does not fit the format (schema/riffsheet.schema.json), "
            f"{len(bad)} problem(s): " + "; ".join(bad[:8]) + (" ..." if len(bad) > 8 else "")
        )
    write_json(outs[0], analysis, indent=1, ensure_ascii=False)
    write_text(outs[1], private(report_md(s.idx, analysis, s.J)))
    print(f"build: {out_dir}/riffsheet.json and riffsheet.md ({len(s.confirmed)} detail statement(s) confirmed)")


def checks_line(n_problems, n_unconfirmed):
    nprob = n_problems + n_unconfirmed
    if not nprob:
        return "CHECKS: all passed"
    if n_unconfirmed and n_problems:
        return f"CHECKS: {nprob} problem(s): {n_problems} listed here, {n_unconfirmed} under UNCONFIRMED below"
    if n_unconfirmed:
        return f"CHECKS: {nprob} problem(s), all under UNCONFIRMED below"
    return f"CHECKS: {nprob} problem(s)"


def print_report(s):
    unknown = speech_unknown(s)
    print(
        f"  {s.dur} s, {len(s.idx['shots'])} shot(s), speaking {s.speaking}"
        + (" (speech not transcribed)" if unknown else "")
        + f", {len(s.vsegs)} line(s), "
        f"{len(s.ents)} entit(ies), {len(s.psegs)} prose segment(s), {len(s.slots)} slot(s)"
    )
    for line in stage_lines(stages_of(s.idx), s.idx["facts"]):
        print("NOT IN THIS ANALYSIS: " + line + " riffsheet.md says so under its first line.")
    for line in untested_lines(stages_of(s.idx)):
        print("OUTSIDE THE TESTED PATH: " + line + " riffsheet.md says so under its first line.")
    if s.hearing and s.hearing["state"] != "no_audio_track":
        print(f"SOUND: {sound_line(s.hearing)} riffsheet.md says so near the top.")
    if s.line_facts:
        print("LINES (measured: pace band to use in prose; cut crossings; low-probability words)")
        print("\n".join(s.line_facts))
    if s.cap_report:
        print("CAPTIONS (measured from pixels; override a value in the judgment file only after looking)")
        print("\n".join(s.cap_report))
    sp = sound_at_picture_doc(s)
    if sp and sp["captions"]["changes"]:
        print("SOUND AT CAPTION APPEARANCES (measured times, not what the sound is): " + sp["captions"]["summary"])
    print(checks_line(len(s.problems), len(s.unconfirmed)))
    for p in s.problems:
        print("  - " + p)
    named = sorted({c["view"] for c in s.confirmed})
    if named:
        print(
            f"VIEWS NAMED in detail marks ({len(named)}): " + ", ".join(named) + ". A mark is a confirmation only "
            "if you compared its words with that image: open any of these you have not opened, in one step"
        )
    if s.warnings:
        print(f"WARNINGS ({len(s.warnings)}): look at each; they do not stop the build")
        for w in s.warnings:
            print("  - " + w)
    if s.unheard:
        print(f"NOT HEARD ({len(s.unheard)}): statements of what the sound is need a passed hearing check")
        for p in s.unheard:
            print("  - " + p)
    if s.unconfirmed:
        print(f"UNCONFIRMED ({len(s.unconfirmed)}): the analysis is not written until each is confirmed or marked ?")
        for p in s.unconfirmed:
            print("  - " + p)


def cmd_build(a):
    d = os.path.abspath(a.dir)
    idx, pts, words = load_dir(d)
    if not a.judgment:
        return build_sheet(d, idx, words, [sh["start"] for sh in idx["shots"][1:]])
    J = read_json(a.judgment, "judgment file")
    if not isinstance(J, dict):
        die(f"judgment file {a.judgment}: expected a JSON object (format in references/METHOD.md, section 9)")
    s = BuildState(idx, pts, words, J, jj=Judgment(d, idx, pts, words), views=confirm_views(idx, pts))
    out_dir = os.path.abspath(a.out or os.path.join(d, "out"))
    os.makedirs(out_dir, exist_ok=True)
    for stage in STAGES:
        stage(s)
    write_outputs(s, analysis_of(s, d, out_dir), out_dir)
    print_report(s)
    if s.unconfirmed or s.unheard:
        sys.exit(EXIT_REFUSED)


def build_sheet(d, idx, words, cuts):
    """Without a judgment file: the measured facts the judgment is written against."""
    tm = idx.get("transcript_meta") or {}
    print(f"build sheet for {d} (no judgment file given: nothing written)")
    print(f"duration {idx['facts']['duration_video_s']} s; cuts at " + (", ".join(fmt_t(c) for c in cuts) or "none"))
    if not words:
        st = stages_of(idx)["speech_recognition"]
        if st["state"] == "ran":
            print(f"no transcript words: speech recognition ({st['by']}) heard none")
        else:
            verb = "failed" if st["state"] == "failed" else "did not run"
            print(
                f"no transcript words: speech recognition {verb}: {st['why']}. The judgment has no lines; "
                f"never write that nobody speaks: whether anyone does is not known"
            )
    else:
        for line in untested_lines(stages_of(idx)):
            print("TRANSCRIPT: " + line)
        print(
            f"WORDS language {tm.get('language')}: index:word@start (seconds), '?' = probability < 0.5, "
            f"'|gap|' = pause of {LINE_PAUSE_S} s or more, '✂' = cut (a line of yours that crosses one: its "
            f"[voice:X] goes in the segment where its first word starts). Lines L0, L1 ... are the transcriber's, "
            f"not yours (`mouth --line N` takes N; `mouth --words A-B` takes one of your own lines). PACE "
            f"below gives the measured band for each sentence as the transcript punctuates it"
        )
        for ln in tm.get("lines", []):
            idxs = [i for i, w in enumerate(words) if w["seg"] == ln["i"]]
            if not idxs:
                continue
            parts = []
            for j, i in enumerate(idxs):
                w = words[i]
                if j:
                    g = w["start"] - words[idxs[j - 1]]["end"]
                    if g >= LINE_PAUSE_S:
                        parts.append(f"|{g:.2f}|")
                for c in cuts:
                    if (words[idxs[j - 1]]["end"] if j else w["start"]) <= c < w["end"] and (j or c > w["start"]):
                        parts.append(f"✂{fmt_t(c)}")
                q = "?" if w.get("prob") is not None and w["prob"] < LOW_PROB else ""
                parts.append(f"{i}:{w['word']}{q}@{w['start']:.2f}")
            print(f" L{ln['i']} {fmt_t(words[idxs[0]]['start'])}–{fmt_t(words[idxs[-1]]['end'])}  " + " ".join(parts))
    if words:
        # pace per sentence as the transcript punctuates it: a line is one sentence, so these are usually
        # the lines the judgment gives, and the first judgment can use the measured band word
        sents, start = [], 0
        for i, w in enumerate(words):
            end = w["word"].strip().rstrip(CLOSING_QUOTES)
            if end.endswith(SENTENCE_ENDS) or i == len(words) - 1:
                sents.append((start, i))
                start = i + 1
        print(
            "PACE (measured, per sentence as the transcript punctuates it; words A-B: band, rate). Use the "
            "band word of the sentence a line covers; a line split differently gets its own band, printed "
            "under LINES by build with the judgment file, which is the one that counts (it is counted on "
            "the line as corrected: a spelling fix that joins two misheard words into one changes it)"
        )
        for a_, b_ in sents:
            pc = pace_of(words[a_ : b_ + 1])
            txt = join_words([w["word"].strip() for w in words[a_ : b_ + 1]])
            print(
                f"  {a_}-{b_}: {pc['band']}, {pc['per_s']} {pc['unit']}/s  | {txt[:70]}{'…' if len(txt) > 70 else ''}"
            )
    regs = sorted(f[:-5] for f in os.listdir(os.path.join(d, "look")) if f.endswith(".json"))
    print("TEXT REGIONS read so far (use the name in the judgment file): " + (", ".join(regs) or "none"))
    for sh in idx["shots"]:
        if sh.get("still_share") is not None:
            print(
                f"  {sh['id']} {fmt_t(sh['start'])}–{fmt_t(sh['end'])} "
                f"still {sh['still_share']} ({sh['camera_measure']})"
            )
    print(detail_words_note())
