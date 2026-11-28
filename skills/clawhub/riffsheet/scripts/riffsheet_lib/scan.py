"""`scan`: everything up front, and summary.txt."""

import math
import os
import shlex
import shutil
import statistics
import time

from . import VERSION, util
from .audio import (
    BED_SILENT_DB,
    BED_UP_DB,
    ONSET_BLOCK_S,
    SOUND_WORDS,
    measure_audio,
    sound_at_picture,
    sound_at_summary,
)
from .capabilities import STAGE_RECORDS, stage_lines, stages_of, untested_lines
from .constants import LONG_VIDEO_S, REGION_SETTLE_MIN, STILL_LOCKED, STILL_MOVING
from .elements import element_candidates, element_line, element_record, find_panes
from .hearing import forget
from .media import extract_cells, probe, run, run_timeout_for, set_timeout
from .picture import (
    between_frames,
    between_line,
    find_events,
    fixed_layers,
    jump_cuts,
    measure_picture,
    region_settles,
    still_of_shot,
    text_regions,
)
from .scandir import label_word, nearest_frame, scratch_dir
from .sheets import cell_dims, compose, fit_cell, label_fs, wrap
from .transcript import join_words, load_words, words_in
from .util import die, even, fmt_t, warn, write_json, write_text

# ----------------------------------------------------------------------------- scan
OVERVIEW_STEP_S = 0.5  # the overview shows a frame every half second ...
OVERVIEW_CELLS = 54  # ... up to this many cells (27 s); longer clips step further, in quarter seconds
OVERVIEW_LONG_SIDE = (427, 400)  # overview cell long side, portrait and landscape: 3 sheets of 18 fit the cap
REP_FROM, REP_TO = 0.2, 0.8  # a shot's frame is picked from this part of it, away from its edges
SHOT_FONT = 22  # label font size on the one large frame per shot
EVENT_LONG_SIDE = 256  # cell long side on the change-events sheet
EVENT_CELLS_MAX = 6  # a change over more frames is shown by the frame before, 4 across it, and the frame after
JUMP_LONG_SIDE = 560  # cell long side on the possible-jump-cuts sheet (before and after side by side)
# scan time, roughly: this many seconds per second of 720x1280 video (used only to warn on long clips)
SCAN_S_PER_S = 0.35


def overview_step(dur):
    return OVERVIEW_STEP_S if dur <= OVERVIEW_STEP_S * OVERVIEW_CELLS else math.ceil(dur / OVERVIEW_CELLS / 0.25) * 0.25


def long_video_warning(info):
    dur = info["duration_s"]
    est = max(1, round(dur * SCAN_S_PER_S * info["width"] * info["height"] / (720 * 1280) / 60))
    warn(
        f"{dur:.0f} s video; riffsheet is made for short clips (up to about a minute). scan decodes "
        f"every frame several times (expect roughly {est} min or more); the overview samples every "
        f"{overview_step(dur):g} s instead of 0.5 s; `text`, `element`, `frames` and "
        f"`mouth` hold every frame of their area in memory (give `text` and `frames` --from/--to to "
        f"cover only the part you need)"
    )


def frame_facts(info, pts):
    """Frame count, interval range, variable frame rate and the video's duration from the true timestamps."""
    N = len(pts)
    info["frames"] = N
    ints = [round(pts[i] - pts[i - 1], 4) for i in range(1, N)]
    info["frame_interval_s"] = {"min": min(ints), "max": max(ints)} if ints else None
    info["variable_frame_rate"] = bool(ints) and (max(ints) - min(ints) > 0.002)
    info["duration_video_s"] = round(pts[-1] + (statistics.median(ints) if ints else 0), 3)


def find_shots(M, events, info):
    """Shots = spans between whole-picture changes, each with a representative frame (the stillest one
    in its middle part) and how still its camera is."""
    pts, g = M["pts"], M["g"]
    N = len(pts)
    cuts = [e for e in events if e["kind"] == "cut"]
    bounds = [0] + [e["frame"] for e in cuts] + [N]
    shots = []
    for k in range(len(bounds) - 1):
        s, e = bounds[k], bounds[k + 1]  # frames s .. e-1
        if k > 0:
            ce = cuts[k - 1]
            s_eff = ce["span_frames"][1] + 1 if ce["onset"] == "gradual" else s
        else:
            s_eff = s
        s_eff = min(s_eff, e - 1)
        L = e - s_eff
        lo, hi = s_eff + int(L * REP_FROM), s_eff + max(1, int(L * REP_TO))
        rng = range(lo, max(lo + 1, hi))
        rep = min(rng, key=lambda i: g[i] + (g[i + 1] if i + 1 < N else 0) + (abs(i - (lo + hi) / 2) * 1e-6))
        end_t = pts[e] if e < N else info["duration_video_s"]
        shots.append(
            {
                "id": f"S{k + 1}",
                "start": round(pts[s], 3),
                "end": round(end_t, 3),
                "frames": [s, e - 1],
                "rep_frame": rep,
                "rep_t": round(pts[rep], 3),
                "inner_events": [x["id"] for x in events if x["kind"] != "cut" and s <= x["frame"] < e],
                **still_of_shot(M, s_eff + 2, e - 1),
            }
        )
    return shots


def jump_words(e):
    """How a jump cut inside one framing is described in the summary."""
    b = ",".join(f"{x:.2f}" for x in e["box"])
    return (
        f"jump cut (only box {b} changed, {e['changed_fraction']:.2f} of the frame, its colors "
        f"{e['jump_cut']['same_colors']:.2f} alike: the same scene rearranged, check on events.jpg)"
    )


def sound_at_cuts(audio, events, info, pts):
    """Which cuts a sound event falls on (audio.sound_at), within one frame interval plus the 10 ms the
    onsets are refined to: a cut is known to the frame, an onset to 10 ms."""
    if not audio:
        return None
    fi = statistics.median(pts[i] - pts[i - 1] for i in range(1, len(pts)))
    cuts = [{"id": e["id"], "kind": "cut", "span": e["span"]} for e in events if e["kind"] == "cut"]
    return sound_at_picture(cuts, audio["events"], round(fi + ONSET_BLOCK_S, 3), info["duration_video_s"])


def sound_at_lines(res):
    """The scan summary's lines for sound_at_cuts."""
    L = [
        "SOUND AT THE CUTS (measured: a sound event's onset, refined to 10 ms, within one frame interval plus "
        "10 ms of the cut; times only, not what the sound is)",
        "  " + sound_at_summary(res),
    ]
    for c in res["changes"]:
        a, b = c["span"]
        when = fmt_t(a) if a == b else f"{fmt_t(a)}–{fmt_t(b)}"
        if c["on"]:
            what = "on " + ", ".join(f"{SOUND_WORDS[x['type']]} {x['t']:.2f} ({x['dt']:+.2f} s)" for x in c["on"])
        elif c["nearest"]:
            x = c["nearest"]
            what = f"no sound event on it; nearest {SOUND_WORDS[x['type']]} {x['t']:.2f} ({x['dt']:+.2f} s)"
        else:
            what = "no sound event within 1 s"
        L.append(f"  {c['id']} cut {when}: {what}")
    return L


def overview_sheets(video, info, pts, shots, words, out, tmp, step):
    """A frame every `step` seconds (and one per shot shorter than that), labeled with the words said."""
    dur = info["duration_video_s"]
    targets, k = [], 0
    while k * step < dur - 1e-6:
        targets.append(k * step)
        k += 1
    ov = set(nearest_frame(pts, t) for t in targets)
    for sh in shots:  # a shot shorter than the step still gets one cell
        if not any(sh["frames"][0] <= i <= sh["frames"][1] for i in ov):
            ov.add(sh["frames"][0])
    ov = sorted(ov)
    cw, ch, _ = cell_dims(
        info, None, OVERVIEW_LONG_SIDE[0] if info["height"] >= info["width"] else OVERVIEW_LONG_SIDE[1]
    )
    cellmap = extract_cells(video, ov, None, cw, ch, tmp, "ov", info)
    shot_of = {}
    for sh in shots:
        for i in range(sh["frames"][0], sh["frames"][1] + 1):
            shot_of[i] = sh["id"]
    cells = []
    for j, i in enumerate(ov):
        nxt = pts[ov[j + 1]] if j + 1 < len(ov) else dur
        said = join_words(words_in(words, pts[i], nxt)) if words else ""
        first = shot_of.get(i) if any(sh["frames"][0] == i for sh in shots) else None
        head = f"{fmt_t(pts[i])}  #{i}  {shot_of.get(i, '')}" + ("  ◀new shot" if first and i > 0 else "")
        cells.append(
            {"path": cellmap[i], "lines": [head] + wrap(said, cw - 8, label_fs(cw), 2), "hi": bool(first and i > 0)}
        )
    imgs = compose(cells, cw, ch, 3, os.path.join(out, "overview"), tmp, grid=True)
    for im in imgs:
        im["kind"] = "overview"
    return imgs


def shot_frames(video, info, pts, shots, words, out, tmp):
    """One large frame per shot (never upscaled), at shots/shot_NN.jpg."""
    label_big = 2 * round(SHOT_FONT * 1.25) + 6
    cwb = min(fit_cell(info["width"] / info["height"], label_big), even(info["width"]))  # never upscale
    chb = round(cwb * info["height"] / info["width"] / 2) * 2
    cellmap = extract_cells(video, [sh["rep_frame"] for sh in shots], None, cwb, chb, tmp, "shot", info)
    images = []
    for sh in shots:
        i = sh["rep_frame"]
        said = label_word(words, pts[i]) if words else ""
        lines = [f"{sh['id']}  {fmt_t(sh['start'])}–{fmt_t(sh['end'])}   frame {fmt_t(pts[i])}  #{i}   {said}"]
        im = compose(
            [{"path": cellmap[i], "lines": lines}],
            cwb,
            chb,
            1,
            os.path.join(out, "shots", f"shot_{sh['id'][1:].zfill(2)}"),
            tmp,
        )[0]
        im["kind"] = "shot"
        im["shot"] = sh["id"]
        sh["image"] = os.path.relpath(im["path"], out)
        images.append(im)
    return images


def event_frames(ev, N):
    """The frames shown for one change: two before to one after; a long gradual change is shown by the
    frame before, four frames across it (its peak kept) and the frame after."""
    s, e = ev["span_frames"]
    fr = list(range(max(0, s - 2), min(N, e + 2)))
    if len(fr) <= EVENT_CELLS_MAX:
        return fr
    inside = list(range(s, e + 1))
    pick = {inside[round(x * (len(inside) - 1) / 3)] for x in range(4)} | {ev["peak_frame"]}
    pick = sorted(pick)
    while len(pick) > 4:
        pick.remove(
            min(
                (x for x in pick if x != ev["peak_frame"]),
                key=lambda x: min(abs(x - y) for y in pick if y != x),
            )
        )
    return [max(0, s - 1)] + pick + [min(N - 1, e + 1)]


def blank_cell(ew, eh, tmp):
    """A gray cell that pads short rows of the events sheet."""
    blank = os.path.join(tmp, "blank.png")
    r = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-y",
            "-loglevel",
            "error",
            "-f",
            "lavfi",
            "-i",
            f"color=c=0x3a3a3a:s={ew}x{eh}",
            "-frames:v",
            "1",
            blank,
        ]
    )
    if r.returncode != 0:
        die("blank cell failed: " + r.stderr.decode()[-400:])
    return blank


def event_sheets(video, info, pts, events, words, out, tmp):
    """Change events: one row of frames around each, the change box outlined on its peak frame."""
    if not events:
        return []
    N = len(pts)
    ew, eh, _ = cell_dims(info, None, EVENT_LONG_SIDE)
    rows_cells, need = [], set()
    for ev in events:
        fr = event_frames(ev, N)
        rows_cells.append((ev, fr))
        need.update(fr)
    cellmap = extract_cells(video, sorted(need), None, ew, eh, tmp, "ev", info)
    width = max(len(fr) for _, fr in rows_cells)
    blank = blank_cell(ew, eh, tmp)
    cells = []
    for ev, fr in rows_cells:
        for i in fr:
            mark = i == ev["peak_frame"]
            l1 = f"{fmt_t(pts[i])} #{i}"
            l2 = f"{ev['id']} {ev['kind']}" if mark else (label_word(words, pts[i]) if words else "")
            cells.append(
                {
                    "path": cellmap[i],
                    "lines": [l1, l2],
                    "hi": mark,
                    "box": ev["box"] if (mark and ev["box"]) else None,
                }
            )
        for _ in range(width - len(fr)):
            cells.append({"path": blank, "lines": []})
    imgs = compose(cells, ew, eh, 2, os.path.join(out, "events"), tmp, cols_hint=width)
    for im in imgs:
        im["kind"] = "events"
    return imgs


def jump_sheets(video, info, pts, events, words, out, tmp):
    """Possible jump cuts: a small area changes in one frame (a hand or object jumps) while the rest of
    the picture holds. Not classified: the agent compares the frame before and after."""
    jumps = [ev for ev in events if ev["kind"] == "local" and ev["onset"] == "abrupt"]
    for ev in jumps:
        ev["possible_jump_cut"] = True
    if not jumps:
        return []
    jw, jh, _ = cell_dims(info, None, JUMP_LONG_SIDE)
    need = sorted({i for ev in jumps for i in (max(0, ev["peak_frame"] - 1), ev["peak_frame"])})
    cellmap = extract_cells(video, need, None, jw, jh, tmp, "jc", info)
    cells = []
    for ev in jumps:
        p = ev["peak_frame"]
        for i, tag in ((max(0, p - 1), "before"), (p, "after")):
            cells.append(
                {
                    "path": cellmap[i],
                    "box": ev["box"],
                    "hi": tag == "after",
                    "lines": [
                        f"{ev['id']} {tag}  {fmt_t(pts[i])} #{i}",
                        label_word(words, pts[i]) if words else "",
                    ],
                }
            )
    imgs = compose(cells, jw, jh, 2, os.path.join(out, "jumps"), tmp, cols_hint=2)
    for im in imgs:
        im["kind"] = "jumps"
    return imgs


def cmd_scan(a):
    t0 = time.time()
    video = os.path.abspath(a.video)
    # inputs are checked before the output folder is made, so a bad input leaves nothing behind
    info = probe(video)
    words, tmeta = load_words(a.transcript)
    if a.transcript_by and not a.transcript:
        die("--transcript-by says what made the transcript given with --transcript; there is none")
    stages = {k: record(info, tmeta, a.transcript_by) for k, record in STAGE_RECORDS.items()}
    if tmeta and tmeta.get("stage"):  # transcribe's record of why it made no transcript: no words in it
        tmeta = None
    set_timeout(run_timeout_for(info["duration_s"]))
    if info["duration_s"] > LONG_VIDEO_S:
        long_video_warning(info)
    out = os.path.abspath(a.out)
    os.makedirs(out, exist_ok=True)
    for sub in ("shots", "look"):
        os.makedirs(os.path.join(out, sub), exist_ok=True)
    tmp = scratch_dir(out, "scan")
    # ---- measure: the picture's changes, then what holds and what sounds
    M = measure_picture(video, info, tmp)
    pts = M["pts"]
    N = len(pts)
    frame_facts(info, pts)
    events, base = find_events(M, info)
    jump_cuts(video, info, events, tmp)
    between_frames(video, info, M, events, tmp)
    regions = region_settles(video, info, text_regions(M, events, base, info), N)
    fixed = fixed_layers(video, info, M["pts"], tmp)
    audio = measure_audio(video, words) if info["has_audio"] else None
    shots = find_shots(M, events, info)
    # ---- split layouts and drawn elements, measured (offered to the agent as ready regions)
    panes = find_panes(video, info, pts, events, shots, tmp)
    elements = element_candidates(video, info, pts, shots, events, fixed, tmp, regions=regions, panes=panes)
    for m in elements:
        write_json(
            os.path.join(out, "look", m["id"] + ".json"), element_record(m, m["id"]), indent=1, ensure_ascii=False
        )
    # ---- the default pictures
    step = overview_step(info["duration_video_s"])
    images = overview_sheets(video, info, pts, shots, words, out, tmp, step)
    images += shot_frames(video, info, pts, shots, words, out, tmp)
    images += event_sheets(video, info, pts, events, words, out, tmp)
    images += jump_sheets(video, info, pts, events, words, out, tmp)
    for im in images:
        im["path"] = os.path.relpath(im["path"], out)
    index = {
        "tool": "riffsheet",
        "version": VERSION,
        "video": video,
        "transcript": os.path.abspath(a.transcript) if a.transcript else None,
        "facts": info,
        "transcript_meta": (
            {"language": tmeta["language"], "words": len(words), "lines": tmeta["lines"]} if tmeta else None
        ),
        "stages": stages,
        "shots": shots,
        "events": events,
        "text_regions": regions,
        "fixed_layers": fixed,
        "panes": panes,
        "elements": elements,
        "scdet": [{"t": round(t, 3), "score": s} for t, s in M["scdet"]],
        "audio": audio,
        "sound_at_cuts": sound_at_cuts(audio, events, info, pts),
        "images": images,
        "default_image_tokens": sum(im["tokens"] for im in images),
        "overview_step_s": step,
        "_words": words,
    }
    forget(out)  # a hearing record and cut sound files belong to the video they were made for
    write_json(os.path.join(out, "frames.json"), {"pts": pts})
    index["scan_seconds"] = round(time.time() - t0, 2)
    write_json(os.path.join(out, "index.json"), index, indent=1, ensure_ascii=False)
    summ = summary_text(index, out)
    write_text(os.path.join(out, "summary.txt"), summ)
    shutil.rmtree(tmp, ignore_errors=True)
    print(summ)


def summary_text(ix, out):
    CMD = util.CMD  # read when called: the entry script sets it after this module is imported
    f = ix["facts"]
    L = []
    L.append(f"riffsheet  {os.path.basename(ix['video'])}  -> {out}")
    vfr = "VARIABLE frame rate" if f["variable_frame_rate"] else "constant frame rate"
    L.append(
        f"{f['duration_video_s']} s, {f['width']}x{f['height']}, {f['frames']} frames, {vfr} "
        f"(avg {f['fps_avg']} fps), audio {'yes' if f['has_audio'] else 'no'}"
    )
    tm = ix.get("transcript_meta")
    if tm:
        L.append(f"transcript: {tm['words']} words, {len(tm['lines'])} lines, language {tm['language']}")
    for line in untested_lines(stages_of(ix)):
        L.append("TRANSCRIPT: " + line)
    heard = stages_of(ix)["speech_recognition"]["state"] == "ran"  # words known: sound is set against them
    for line in stage_lines(stages_of(ix), f):
        L.append("NOT IN THIS SCAN: " + line + " `check VIDEO` says what it needs.")
    L.append("Times are true frame timestamps in seconds; #n = decoder frame number (0-based).")
    L.append("")
    L.append(
        "SHOTS (a cut = the whole picture changes, or a jump cut: in one frame a tenth of the picture or more "
        "changes while the rest holds, and its colors stay alike). still = share of the picture whose pixels hold "
        f"through the shot: >= {STILL_LOCKED} locked camera or frozen picture, <= {STILL_MOVING} the whole "
        "picture moves every frame (handheld or a camera move), between = mixed: look"
    )
    evid = {e["id"]: e for e in ix["events"]}
    for k, sh in enumerate(ix["shots"]):
        how = ""
        if k > 0:
            ce = [e for e in ix["events"] if e["kind"] == "cut" and e["frame"] == sh["frames"][0]]
            if ce:
                e = ce[0]
                came = (
                    jump_words(e)
                    if e.get("jump_cut")
                    else "cut"
                    if e["onset"] == "abrupt"
                    else f"gradual change {fmt_t(e['span'][0])}–{fmt_t(e['span'][1])}, peak {fmt_t(e['peak_t'])}"
                )
                how = f"  in by {came} [{'+'.join(e['found_by'])}]"
                for r in e.get("between", []):
                    how += "; " + between_line(r) + " (measured)"
        inner = ""
        if sh["inner_events"]:
            inner = "  inner: " + ", ".join(f"{x} {evid[x]['kind']}@{fmt_t(evid[x]['t'])}" for x in sh["inner_events"])
        cam = ""
        if sh.get("still_share") is not None:
            cam = f"  still {sh['still_share']:.2f} ({sh['camera_measure']})"
            if len(sh["still_per_s"]) > 1:
                cam += " per s: " + " ".join(f"{x:.2f}" for x in sh["still_per_s"])
        L.append(
            f" {sh['id']:>3} {fmt_t(sh['start'])}–{fmt_t(sh['end'])} ({sh['end'] - sh['start']:.2f}s)"
            f"  {sh['image']}{how}{inner}{cam}"
        )
    L.append("")
    other = [e for e in ix["events"] if e["kind"] != "cut"]
    L.append("CHANGES THAT ARE NOT WHOLE-PICTURE CUTS (red box on events sheet)")
    meaning = {
        "panel": "a filled rectangle changes, rest holds: cut or page change inside a panel/inset",
        "band": "a wide strip changes: caption, title or graphic line",
        "local": "a small area changes: sticker/graphic, or something jumping inside a still frame",
    }
    if not other:
        L.append("  none")
    for e in other:
        b = e["box"]
        bs = f"box {b[0]:.2f},{b[1]:.2f},{b[2]:.2f},{b[3]:.2f}" if b else ""
        flag = "  POSSIBLE JUMP CUT, check on jumps.jpg" if e.get("possible_jump_cut") else ""
        L.append(f"  {e['id']} {fmt_t(e['t'])} {e['kind']:<5} {bs}  ({meaning[e['kind']]}){flag}")
        L += [f"      {between_line(r)} (measured)" for r in e.get("between", [])]
    if any(e.get("possible_jump_cut") for e in other):
        L.append(
            "A POSSIBLE JUMP CUT is a small area that changes completely in one frame while the rest holds: an "
            "edit inside a still frame (a hand or object jumps) or a sticker popping. Not classified: compare "
            "the frames before and after on jumps.jpg (red box = the change) and decide."
        )
    L.append("Not found = not proven absent: same-background outfit swaps, composites and slow dissolves can slip.")
    L.append("")
    L.append("TEXT-LIKE REGIONS (areas that keep changing on their own; read them with `text`)")
    if not ix["text_regions"]:
        L.append("  none found")
    for r in ix["text_regions"]:
        b = ",".join(f"{x:.2f}" for x in r["box"])
        st = r.get("settles")
        tag = (
            ""
            if st is None
            else (
                f"  settles {st:.2f}"
                + (
                    "  MOTION ONLY? (what changes here keeps moving; skip unless the overview shows text in it)"
                    if st < REGION_SETTLE_MIN
                    else ""
                )
            )
        )
        L.append(
            f"  {r['id']} {r['shape']:<5} box {b}  ~{r['change_moments']} changes{tag}   "
            f"-> {CMD} text {shlex.quote(out)} --box {b}"
        )
    fl = ix.get("fixed_layers") or {}
    L.append(
        "FIXED LAYERS (strokes that hold while the picture behind moves or cuts: a caption, title, logo "
        "or watermark that stays up; text-like regions above miss these because they never change)"
    )
    if fl.get("note"):
        L.append("  not measurable: " + fl["note"])
    elif not fl.get("layers"):
        L.append(
            f"  none found ({fl.get('blocks_used', 0)} of {fl.get('blocks', 0)} one-second blocks "
            f"had a moving picture to test against)"
        )
    for r in fl.get("layers", []):
        b = ",".join(f"{x:.2f}" for x in r["box"])
        L.append(f"  {r['id']} box {b}  ({r['stroke_px']} held stroke px)   -> {CMD} text {shlex.quote(out)} --box {b}")
    if fl.get("layers"):
        L.append(
            "  Skip one whose box shows no lettering, logo or drawn shape on the overview (leaves, an edge of "
            "furniture, a still object): say so under tool_gaps"
        )
    L.append("SPLIT LAYOUTS (a straight seam with one side changing while the other holds; boxes measured)")
    if not ix.get("panes"):
        L.append("  none found")
    for P in ix.get("panes") or []:
        L.append(
            f"  {P['id']} {P['axis']} seam at {P['seam']:.4f} ({P['seam_px']} px), {fmt_t(P['on'])}–{fmt_t(P['off'])}; "
            f"panes "
            + "; ".join(",".join(f"{v:.3f}" for v in b) for b in P["panes"])
            + f"  (evidence: {', '.join(P['evidence'])})"
        )
    if ix.get("panes"):
        L.append(
            "  Decide per pane: camera footage (two camera pictures at once = a split video_format) or a recording, "
            "card or screenshot (a graphic with split: true on single_shot). `element` with a box on a pane "
            "returns the pane."
        )
    L.append(
        "DRAWN ELEMENTS (measured: pixels that appear together, hold while the picture moves or cuts, and "
        'leave together; give a graphic "region": "Gn" to use the box and times)'
    )
    if not ix.get("elements"):
        L.append("  none found (a card, icon or logo the overview shows: `element DIR --box ROUGH --at T` measures it)")
    for m in ix.get("elements") or []:
        L.append("  " + element_line(m, m["id"]).replace("element ", "", 1))
    L.append("")
    au = ix.get("audio")
    if au:
        L.append("SOUND (mixed track; cannot tell voice from music)")
        L.append(
            "  silences < -40 dB, >= 0.3 s: " + (", ".join(f"{a:.1f}–{b:.1f}" for a, b in au["silences"]) or "none")
        )
        ev = [f"{e['t']:.1f} {e['type']} {e['db']:.0f}dB" for e in au["events"] if not e["during_speech"]]
        ns = sum(1 for e in au["events"] if e["during_speech"])
        if heard:
            L.append(
                "  loudness events with no word under them: "
                + (", ".join(ev) or "none")
                + f"  (+{ns} during speech, in index.json)"
            )
        else:
            L.append(
                "  loudness events (speech not transcribed: none is set against words): " + (", ".join(ev) or "none")
            )
        L.append(
            "  momentary loudness peaks: " + (", ".join(f"{t:.1f}" for t in au["loudness_peaks_momentary"]) or "none")
        )
        fx = au.get("facts") or {}
        if fx:
            L.append("  LOUDNESS FACTS (quote these, not memory; 100 ms RMS of the mixed track):")
            L.append(
                f"    level ranges from {fx['min'][1]:.0f} dB at {fx['min'][0]:.1f} s to {fx['max'][1]:.0f} dB "
                f"at {fx['max'][0]:.1f} s"
            )
            L.append(
                "    quietest 0.3 s stretches: "
                + "; ".join(
                    f"{a:.1f}–{b:.1f} {v:.0f} dB" + ((" (a word overlaps it)" if sp else " (no word)") if heard else "")
                    for a, b, v, sp in fx["quietest"]
                )
            )
            L.append(
                "    deepest drops: "
                + (
                    "; ".join(
                        f"{t:.1f} to {d:.0f} dB ({dd:+.0f} dB in 0.3 s"
                        + ((", under a word" if sp else ", no word") if heard else "")
                        + ")"
                        for t, d, dd, sp in fx["deepest_drops"]
                    )
                    or "none"
                )
            )
            L.append(
                (
                    "    sound with no word under it (>= 0.3 s above -40 dB): "
                    if heard
                    else "    sound (>= 0.3 s above -40 dB; speech not transcribed, so words are not known): "
                )
                + ("; ".join(f"{a:.1f}–{b:.1f} {v:.0f} dB" for a, b, v in fx["sound_without_words"]) or "none")
            )
        uv = au.get("under_voice") or {}
        if uv.get("pauses") is not None and "speech_db" in uv:
            n = len(uv["pauses"])
            head = {
                "no_continuous_bed": f"NO CONTINUOUS BED: in {uv['silent']} of {n} pauses the level falls to near "
                f"silence and none stays up",
                "something_continues": f"SOMETHING CONTINUES under the voice (music or ambience; the tool cannot "
                f"tell which): in {uv['continues']} of {n} pauses the level stays up",
                "unclear": f"UNCLEAR: {uv['continues']} of {n} pauses stay up, {uv['silent']} fall to near silence",
                "too_few_pauses": f"NOT MEASURABLE: only {n} pause(s) of 0.12 s or more between words",
            }[uv["verdict"]]
            L.append(
                f"  UNDER THE VOICE (measured; quote this): {head}. Speech median {uv['speech_db']:.0f} dB; "
                f"quietest 20 ms in each pause (near silence = {BED_SILENT_DB} dB under speech or below -55; "
                f"stays up = "
                f"within {BED_UP_DB} dB and above -50): "
                + (", ".join(f"{a:.1f}-{b:.1f} {f:.0f}" for a, b, f, _ in uv["pauses"]) or "none")
            )
        L.append("  RMS dB per 0.5 s from 0.0: " + " ".join(str(x) for x in au["rms_db_per_0_5s"]))
        L.append("")
    if ix.get("sound_at_cuts"):
        L += sound_at_lines(ix["sound_at_cuts"])
        L.append("")
    L.append("IMAGES (pixel size, estimated tokens = ceil(w/28) x ceil(h/28))")
    tot = 0
    for im in ix["images"]:
        tot += im["tokens"]
        L.append(f"  {im['path']:<22} {im['w']}x{im['h']}  ~{im['tokens']} tok  [{im['kind']}]")
    L.append(
        f"  total ~{tot} tokens. Read overview first (labels: time, #frame, shot, words spoken "
        f"in that {ix['overview_step_s']} s slot; 10% grid for boxes); shot frames when you need "
        f"detail; events sheets only to check a change."
    )
    L.append("")
    L.append("NEXT (each line is one complete command; write it out in full, never from a shell variable)")
    q = shlex.quote(out)
    L.append(f"  {CMD} text {q} --box x0,y0,x1,y1          each caption/region state once, with on/off times")
    L.append(f"  {CMD} element {q} --box x0,y0,x1,y1 --at T  measured box and times of a card, icon, logo, pane")
    L.append(f"  {CMD} zoom {q} --at T [--at T] [--box ...]  sharp large view (clothes, shoes, objects, colors)")
    L.append(f"  {CMD} mouth {q} --box ... --words A-B       the mouth at each word and pause of words A-B (one line)")
    L.append(f"  {CMD} frames {q} --from S --to E [--box ...] every real frame in a window, tiled")
    L.append(f"  {CMD} color {q} --at T --box x0,y0,x1,y1    measured colors of one thing, with plain names")
    return "\n".join(L) + "\n"
