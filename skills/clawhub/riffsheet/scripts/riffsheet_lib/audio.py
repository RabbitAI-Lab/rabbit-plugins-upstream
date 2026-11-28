"""Audio levels, silences, cliffs and peaks, and what lies under the voice."""

import math
import re
import statistics
import struct

from .media import run

# ----------------------------------------------------------------------------- audio
# Levels are the RMS of the mixed track in 100 ms blocks, in dBFS (0 = full scale).
SILENT_DB = -40  # below this a block is silence (speech and music sit well above it)
LOW_DB = -25  # up to this a block is low; also the floor a peak must rise from
NORMAL_DB = -15  # up to this a block is normal speech or music level; above it, high
SILENCE_MIN_S = 0.3  # a silence lasts at least this long (shorter dips are gaps between words)
CLIFF_DB = 15  # a level change this large within 0.3 s is a cliff (a cut in the sound, a hit, a drop-out)
CLIFF_WINDOW_S = 0.3  # ... measured over this window, and cliffs are at least this far apart
PEAK_HOLD_DB = 3  # a peak runs while the level stays within this of its top
PEAK_MIN_S = 0.1  # ... for at least one more block
PEAK_RISE_DB = 6  # ... and stands this far above the quieter of its two sides
PEAK_SIDE_S = 0.3  # the sides are this long either side of it
MOMENTARY_OVER_DB = 3  # a momentary-loudness peak is this far above the clip's mean loudness
MOMENTARY_GAP_S = 0.8  # ... and at least this far from the one before
SPEECH_SLACK_S = 0.05  # a moment this close to a word counts as during speech
# A sound event's time on the 100 ms curve is only good to a block or more (a peak's time is the middle
# of its loud run), so each event's onset is refined on 10 ms levels of the decoded track (refine_onsets)
ONSET_BLOCK_S = 0.01
ONSET_SAME_S = 0.03  # two refined onsets this close are one moment (a peak and the rise into it)
ONSET_FLOOR_DB = -60  # levels are floored here before steps are measured: a step out of digital silence
# (-120) into the codec's faint smear before an attack (about -60) is not the attack
NEAREST_S = 1.0  # a picture change with no sound event on it names the nearest one this close


def rms_series(video):
    """The RMS level of each 100 ms block of the first audio stream: (times, dB)."""
    r = run(
        [
            "ffmpeg",
            "-nostdin",
            "-hide_banner",
            "-i",
            video,
            "-map",
            "0:a:0",
            "-af",
            "aresample=44100,asetnsamples=4410,astats=metadata=1:reset=1,"
            "ametadata=print:key=lavfi.astats.Overall.RMS_level",
            "-f",
            "null",
            "-",
        ]
    )
    # the exit status is not checked here or for ebur128 below: both print levels as they go, so audio
    # that fails part-way keeps the levels up to the failure, and audio that gives none is measured as
    # no levels rather than stopping the scan
    times, db = [], []
    t = None
    for line in r.stderr.decode("utf-8", "ignore").splitlines():
        m = re.search(r"pts_time:([0-9.]+)", line)
        if m:
            t = float(m.group(1))
        m = re.search(r"RMS_level=(-?[0-9.]+|-inf)", line)
        if m and t is not None:
            times.append(round(t, 2))
            db.append(-120.0 if m.group(1) == "-inf" else float(m.group(1)))
    return times, db


def speech_test(words):
    """A function telling whether time t falls inside a word (with a little slack)."""
    spans = [(w["start"], w["end"]) for w in words]

    def speech(t):
        return any(s - SPEECH_SLACK_S <= t <= e + SPEECH_SLACK_S for s, e in spans)

    return speech


def silences(times, db):
    """Stretches of at least 0.3 s below -40 dB: [start, end]."""
    out, run_start = [], None
    for t, d in zip(times + [times[-1] + 0.1 if times else 0], db + [0.0]):
        if d < SILENT_DB and run_start is None:
            run_start = t
        elif d >= SILENT_DB and run_start is not None:
            if t - run_start >= SILENCE_MIN_S:
                out.append([run_start, round(t, 2)])
            run_start = None
    return out


def cliffs(times, db, speech):
    """Level changes of 15 dB or more within 0.3 s, at least 0.3 s apart."""
    events, last = [], -9
    for i in range(len(db)):
        j = i
        while j > 0 and times[i] - times[j] < CLIFF_WINDOW_S:
            j -= 1
        if j == i or times[i] - last < CLIFF_WINDOW_S:
            continue
        delta = db[i] - db[j]
        if abs(delta) >= CLIFF_DB:
            events.append(
                {
                    "t": times[i],
                    "type": "cliff_rise" if delta > 0 else "cliff_drop",
                    "db": round(db[i], 1),
                    "delta_db": round(delta, 1),
                    "during_speech": speech(times[i]),
                    "_win": (times[j], times[i] + 0.1),
                }
            )
            last = times[i]
    return events


def peaks(times, db, speech):
    """Short loud stretches above -25 dB that stand 6 dB or more above both sides."""
    events = []
    i = 0
    while i < len(db):
        if db[i] < LOW_DB:
            i += 1
            continue
        pv, j = db[i], i
        while j + 1 < len(db) and db[j + 1] >= pv - PEAK_HOLD_DB:
            pv = max(pv, db[j + 1])
            j += 1
        if times[j] - times[i] >= PEAK_MIN_S:

            def side(ks):
                return min([db[k] for k in ks] + [float(LOW_DB)])

            left = side([k for k in range(i) if times[i] - times[k] <= PEAK_SIDE_S])
            right = side([k for k in range(j + 1, len(db)) if times[k] - times[j] <= PEAK_SIDE_S])
            if pv - max(left, right) >= PEAK_RISE_DB:
                tc = round((times[i] + times[j]) / 2, 2)
                events.append(
                    {
                        "t": tc,
                        "type": "peak",
                        "db": round(pv, 1),
                        "delta_db": round(pv - max(left, right), 1),
                        "during_speech": speech(tc),
                        "_win": (times[i], times[j] + 0.1),
                    }
                )
        i = j + 1
    return events


def level_word(d):
    return "silent" if d <= SILENT_DB else "low" if d <= LOW_DB else "normal" if d <= NORMAL_DB else "high"


def energy_segments(times, db):
    """Runs of blocks at one level word, with their mean level."""
    energy = []
    for t, d in zip(times, db):
        if energy and energy[-1]["level"] == level_word(d):
            energy[-1]["end"] = t + 0.1
            energy[-1]["_v"].append(d)
        else:
            energy.append({"start": t, "end": t + 0.1, "level": level_word(d), "_v": [d]})
    for e in energy:
        vals = e.pop("_v")
        e["rms_db"] = round(sum(vals) / len(vals), 1)
        e["end"] = round(e["end"], 2)
    return energy


def momentary_loudness(video):
    """EBU R128 momentary loudness, reported every 100 ms: [(t, LUFS)]."""
    r = run(["ffmpeg", "-nostdin", "-hide_banner", "-i", video, "-map", "0:a:0", "-af", "ebur128", "-f", "null", "-"])
    mom = []
    for line in r.stderr.decode("utf-8", "ignore").splitlines():
        m = re.search(r"t:\s*([0-9.]+)\s+.*M:\s*(-?[0-9.]+)", line)
        if m:
            mom.append((float(m.group(1)), float(m.group(2))))
    return mom


def momentary_peaks(mom):
    """Local maxima of momentary loudness 3 LU above the clip's mean, at least 0.8 s apart."""
    out = []
    vals = [x[1] for x in mom if x[1] > -70]
    if vals:
        mean = sum(vals) / len(vals)
        for k in range(1, len(mom) - 1):
            t, m_ = mom[k]
            if (
                m_ > mean + MOMENTARY_OVER_DB
                and m_ >= mom[k - 1][1]
                and m_ >= mom[k + 1][1]
                and (not out or t - out[-1] > MOMENTARY_GAP_S)
            ):
                out.append(round(t, 2))
    return out


def half_second_levels(times, db):
    """Mean power in dB for every half second (the summary's level line)."""
    if not times:
        return []
    nb = int(times[-1] / 0.5) + 1
    acc = [[] for _ in range(nb)]
    for t, d in zip(times, db):
        acc[min(nb - 1, int(t / 0.5))].append(10 ** (d / 10))
    return [round(10 * math.log10(sum(a) / len(a))) if a and sum(a) > 0 else -120 for a in acc]


def mono_16k(video):
    """The first audio stream as 16 kHz mono samples, or None when it does not decode."""
    r = run(
        [
            "ffmpeg",
            "-nostdin",
            "-v",
            "error",
            "-i",
            video,
            "-map",
            "0:a:0",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-f",
            "s16le",
            "-",
        ]
    )
    raw = r.stdout
    if r.returncode != 0 or len(raw) < 640:
        return None
    return struct.unpack("<%dh" % (len(raw) // 2), raw[: len(raw) // 2 * 2])


def block_levels(s, W):
    """The RMS level in dBFS of each block of W samples."""
    db = []
    for i in range(0, len(s) - W + 1, W):
        e = sum(x * x for x in s[i : i + W]) / W
        db.append(10 * math.log10(e / 32768**2) if e > 0 else -120.0)
    return db


def refine_onsets(events, samples):
    """Each event's `onset_t`, on 10 ms levels: for a peak, the first 10 ms of the unbroken stretch that
    stays within 6 dB of its loudest 10 ms (where it got loud), going back at most to the 100 ms block
    before its run; for a rise or drop, the block inside its
    0.3 s window (through the block after it) where the level steps up (down) the most from one block
    to the next. None when the track does not decode, or the window holds no such step."""
    lv = [max(ONSET_FLOOR_DB, x) for x in block_levels(samples, round(16000 * ONSET_BLOCK_S))] if samples else []
    for e in events:
        a, b = e.pop("_win")
        ka = max(1, int(round(a / ONSET_BLOCK_S)))
        kb = min(len(lv), int(round(b / ONSET_BLOCK_S)) + 1)  # through the block that starts at b
        if kb <= ka:
            e["onset_t"] = None
            continue
        if e["type"] == "peak":  # back from its loudest 10 ms while within 6 dB, at most to a block before the run
            top = max(range(ka, kb), key=lambda k: lv[k])
            k = top
            while k > max(0, ka - 10) and lv[k - 1] >= lv[top] - PEAK_RISE_DB:
                k -= 1
        else:
            sign = -1 if e["type"] == "cliff_drop" else 1
            k = max(range(ka, kb), key=lambda k: sign * (lv[k] - lv[k - 1]))
            if sign * (lv[k] - lv[k - 1]) <= 0:  # no step at all on the 10 ms levels: not refined
                e["onset_t"] = None
                continue
        e["onset_t"] = round(k * ONSET_BLOCK_S, 2)


def measure_audio(video, words):
    times, db = rms_series(video)
    speech = speech_test(words)
    events = sorted(cliffs(times, db, speech) + peaks(times, db, speech), key=lambda e: e["t"])
    samples = mono_16k(video)
    refine_onsets(events, samples)
    return {
        "rms_100ms": {"t": times, "db": db},
        "silences": silences(times, db),
        "events": events,
        "energy_segments": energy_segments(times, db),
        "loudness_peaks_momentary": momentary_peaks(momentary_loudness(video)),
        "rms_db_per_0_5s": half_second_levels(times, db),
        "facts": loudness_facts(times, db, speech, events),
        "under_voice": under_voice(samples, words),
    }


BED_SILENT_DB = 25  # a pause this far below the speech level (or below -55 dBFS) is near silence
BED_UP_DB = 20  # a pause within this of the speech level (and above -50 dBFS) is a sound that continues
BED_SILENT_FLOOR_DB = -55  # a pause floor this low is near silence whatever the speech level
BED_UP_FLOOR_DB = -50  # a pause floor must be above this to count as a sound that continues
PAUSE_EDGE_S = 0.03  # a pause is measured this far in from each word edge (a word's own tail and onset)
PAUSE_MIN_S = 0.12  # pauses shorter than this (after the edges) are not measured


def under_voice(samples, words):
    """Is there continuous sound (music or ambience) under the voice? Measured in the pauses between
    words: with nothing under the voice the level falls to near silence there; a bed keeps it up.
    A music bed is usually mixed 10-20 dB under the voice; a clean recording's pauses fall 30 dB or
    more. Per pause: the quietest 20 ms inside it (0.03 s in from each word edge), against the median
    20 ms level inside words. The tool cannot tell music from room sound or ambience. `samples` is the
    track as 16 kHz mono (mono_16k)."""
    if not words:
        return {"verdict": "no transcript", "pauses": []}
    if samples is None:
        return {"verdict": "no audio decoded", "pauses": []}
    return pause_verdict(block_levels(samples, 320), words)


def pause_verdict(db, words):
    """under_voice on 20 ms levels `db`: each pause's floor against the median level inside words."""
    dur = len(db) * 0.02

    def fr(t):
        return max(0, min(len(db), int(round(t / 0.02))))

    inw = [db[k] for w in words for k in range(fr(w["start"]), fr(w["end"]))]
    if not inw:
        return {"verdict": "no audio under the words", "pauses": []}
    sp = statistics.median(inw)
    spans = [(-1.0, 0.0)] + sorted((w["start"], w["end"]) for w in words) + [(dur, dur + 1)]
    pauses = []
    end_so_far = 0.0
    for (_, a1), (b0, _) in zip(spans, spans[1:]):
        end_so_far = max(end_so_far, a1)
        g0, g1 = end_so_far + PAUSE_EDGE_S, b0 - PAUSE_EDGE_S
        if g1 - g0 >= PAUSE_MIN_S:
            v = db[fr(g0) : fr(g1)]
            if v:
                fl = min(v)
                kind = (
                    "silent"
                    if (fl <= sp - BED_SILENT_DB or fl <= BED_SILENT_FLOOR_DB)
                    else "continues"
                    if (fl >= sp - BED_UP_DB and fl > BED_UP_FLOOR_DB)
                    else "between"
                )
                pauses.append([round(g0, 2), round(g1, 2), round(fl, 1), kind])
    n = len(pauses)
    ns = sum(1 for p in pauses if p[3] == "silent")
    nc = sum(1 for p in pauses if p[3] == "continues")
    res = {"speech_db": round(sp, 1), "pauses": pauses, "silent": ns, "continues": nc}
    if n < 3:
        res["verdict"] = "too_few_pauses"
    elif nc == 0 and ns * 2 >= n:
        res["verdict"] = "no_continuous_bed"
    elif nc * 2 >= n:
        res["verdict"] = "something_continues"
    else:
        res["verdict"] = "unclear"
    fl = [p[2] for p in pauses]
    res["median_pause_floor_db"] = round(statistics.median(fl), 1) if fl else None
    return res


def loudness_facts(times, db, speech, events):
    """The few loudness facts an analysis quotes, stated once so nobody quotes them from memory:
    the level's range, the quietest stretches, the deepest drops, and sound with no word under it."""
    if not times:
        return {}
    pw = [10 ** (d / 10) for d in db]
    lo = min(range(len(db)), key=lambda i: db[i])
    hi = max(range(len(db)), key=lambda i: db[i])
    out = {"min": [times[lo], round(db[lo], 1)], "max": [times[hi], round(db[hi], 1)]}
    # quietest 0.3 s stretches (mean power), not overlapping, lowest three
    win = [(round(10 * math.log10(max(1e-12, sum(pw[i : i + 3]) / 3)), 1), i) for i in range(max(1, len(db) - 2))]
    quiet, used = [], set()
    for v, i in sorted(win):
        if any(j in used for j in range(i - 2, i + 3)):
            continue
        used.update(range(i, i + 3))
        quiet.append(
            [
                times[i],
                round(times[min(len(times) - 1, i + 2)] + 0.1, 2),
                v,
                any(speech(times[k]) for k in range(i, min(len(times), i + 3))),
            ]
        )
        if len(quiet) == 3:
            break
    out["quietest"] = sorted(quiet)
    drops = sorted((e for e in events if e["type"] == "cliff_drop"), key=lambda e: e["db"])[:3]
    out["deepest_drops"] = [[e["t"], e["db"], e["delta_db"], e["during_speech"]] for e in drops]
    # sound with no word under it: >= 0.3 s above -40 dB with no word within 0.05 s
    runs, st = [], None
    for k, (t, d) in enumerate(zip(times + [None], db + [-120.0])):
        on = t is not None and d > SILENT_DB and not speech(t)
        if on and st is None:
            st = k
        elif not on and st is not None:
            if times[k - 1] + 0.1 - times[st] >= 0.3:
                v = db[st:k]
                runs.append(
                    [
                        times[st],
                        round(times[k - 1] + 0.1, 2),
                        round(10 * math.log10(sum(10 ** (x / 10) for x in v) / len(v)), 1),
                    ]
                )
            st = None
    out["sound_without_words"] = runs
    return out


# ----------------------------------------------------------------------------- sound at picture changes
SOUND_WORDS = {"peak": "loudness peak", "cliff_rise": "rise", "cliff_drop": "drop"}
RISES = ("peak", "cliff_rise")


def onsets(events):
    """The events with a refined onset, one per moment: a peak and the rise into it (or two loud runs)
    refine to onsets a block or so apart, and an onset within 30 ms of the one before is the same one."""
    out = []
    for e in sorted((e for e in events if e.get("onset_t") is not None), key=lambda e: e["onset_t"]):
        if not out or e["onset_t"] - out[-1]["onset_t"] > ONSET_SAME_S + 1e-9:
            out.append(e)
    return out


def sound_at(changes, events, tol):
    """For each picture change ({"id", "kind", "span": [first, last]}): the sound events whose onset
    falls within `tol` of its span (`on`), and when none does, the nearest one within NEAREST_S.
    dt = onset minus the change's first frame. Measured times only: it does not say what the sound is."""
    ons = onsets(events)
    out = []
    for c in changes:
        a, b = c["span"]
        gap = [max(a - e["onset_t"], 0.0, e["onset_t"] - b) for e in ons]
        recs = [{"type": e["type"], "t": e["onset_t"], "dt": round(e["onset_t"] - a, 2), "db": e["db"]} for e in ons]
        on = [r for r, g in zip(recs, gap) if g <= tol + 1e-9]
        near = min(range(len(ons)), key=lambda k: gap[k], default=None)
        nearest = recs[near] if not on and near is not None and gap[near] <= NEAREST_S else None
        out.append({**c, "on": on, "nearest": nearest})
    return out


def chance_on(spans, events, tol, dur):
    """How many of these changes would have a peak or rise within `tol` if they fell at random times:
    for each, the share of the clip where its span would reach one, summed."""
    ons = sorted(e["onset_t"] for e in onsets(events) if e["type"] in RISES)
    if dur <= 0:
        return 0.0
    total = 0.0
    for a, b in spans:
        L, covered, end = b - a, 0.0, 0.0
        for o in ons:  # union of the start times that put the span within tol of o
            lo, hi = max(0.0, o - tol - L, end), min(dur, o + tol)
            if hi > lo:
                covered += hi - lo
                end = hi
        total += covered / dur
    return total


def sound_at_picture(changes, events, tol, dur):
    """sound_at for these changes, with what the one-line summary needs: the tolerance, how many peaks
    and rises there are, and how many of the changes would land on one by chance."""
    return {
        "tolerance_s": tol,
        "duration_s": dur,
        "rises": sum(1 for e in onsets(events) if e["type"] in RISES),
        "by_chance": round(chance_on([c["span"] for c in changes], events, tol, dur), 2),
        "changes": sound_at(changes, events, tol),
    }


def sound_at_summary(res, what="cuts"):
    """One line: how many of the changes land on a peak or rise, against chance."""
    n = len(res["changes"])
    if not n:
        return f"no {what} to compare"
    k = sum(1 for c in res["changes"] if any(x["type"] in RISES for x in c["on"]))
    return (
        f"{k} of {n} {what} land on a loudness peak or rise (within {res['tolerance_s']:.3f} s); "
        f"about {res['by_chance']:.1f} would by chance, with {res['rises']} peaks and rises in "
        f"{res['duration_s']:.1f} s"
    )
