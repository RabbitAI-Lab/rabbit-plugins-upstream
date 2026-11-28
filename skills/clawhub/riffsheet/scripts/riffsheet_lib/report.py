"""riffsheet.md: the plain-words report."""

import json
import os
import re

from .capabilities import sound_line, stage_lines, untested_lines
from .util import mmss

FORMAT_WORDS = {
    "single_shot": "one picture at a time",
    "split_screen_left_right": "split screen, left and right",
    "split_screen_top_bottom": "split screen, top and bottom",
    "picture_in_picture": "picture in picture",
    "multi_grid_2x2": "grid of four pictures",
    "multi_grid_other": "grid of pictures",
}
SPEAKING_WORDS = {
    "none": "no speech",
    "on_camera": "spoken on camera",
    "voiceover": "spoken as voiceover",
    "mixed": "spoken on camera and as voiceover",
}
STAGE_WORDS = {"cta": "call to action", "call to action": "call to action"}
ORDINALS = ("second", "third", "fourth", "fifth", "sixth", "seventh", "eighth")


def _sentence(x, cap=True):
    """A formula value as a sentence: closing full stop, and a capital first letter unless it
    continues a sentence of the report."""
    x = str(x or "").strip()
    if not x:
        return ""
    if cap:
        x = x[0].upper() + x[1:]
    return x if x[-1] in ".!?" else x + "."


def fix_articles(text):
    """'a' before a word said with a vowel sound becomes 'an' ("a oatmeal sweater" -> "an oatmeal
    sweater"). Lower-case words only, and not the ones said with a consonant sound (one, unit, euro)."""

    def an(m):
        w = m.group(2)
        if re.match(r"(one|once|eu|ewe|uni|use|usu|uti|ura|ure|uri|uro|u-)", w):
            return m.group(0)
        return m.group(1) + "n " + w

    return re.sub(r"(?<![\w'’-])([Aa]) ([aeiou][\w'’-]*)", an, text)


def _readable(text, names, lines, seen=None):
    """Prose for a person: markers become plain words, [voice:vsN] becomes the line in quotes. `names`
    maps an id to (first mention, later mentions); `seen` holds the ids already named in the document."""
    seen = set() if seen is None else seen

    def person(m):
        nm = names.get(m.group(1))
        if not nm:
            return "someone"
        first = m.group(1) not in seen
        seen.add(m.group(1))
        return nm[0] if first else nm[1]

    def voice(m):
        t = lines.get(m.group(1))
        return f"“{t}”" if t else ""

    text = re.sub(r"\[image:([^\]]+)\]", person, text)
    text = fix_articles(text)
    # a quoted line straight after the words that introduce it ("says, smiling [voice:vs2]") gets a colon
    text = re.sub(r"([\w)])\s*(\[voice:[^\]]+\])", r"\1: \2", text)
    text = re.sub(r"\[voice:([^\]]+)\]", voice, text)
    # a quoted line keeps its own closing mark: no second full stop after it, and the sentence after it
    # starts with a capital (the full stop that ended the quoting sentence is gone)
    text = re.sub(r"([.!?…。？！])”\.(\s+)([a-z])", lambda m: m.group(1) + "”" + m.group(2) + m.group(3).upper(), text)
    text = re.sub(r"([.!?…。？！])”\.", r"\1”", text)
    # a sentence that now starts with a lower-case name gets its capital back
    text = re.sub(r"(^|[.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), text)
    return re.sub(r"  +", " ", text).strip()


def merge_items(items, keep_order=False):
    """A list for the report with each point once: an item whose words all appear in a longer item
    ("tone of voice and pitch" beside "tone of voice, pitch and energy of every line") is dropped."""

    def words(x):
        return set(re.findall(r"[\w'’-]+", str(x).lower()))

    out = []
    uniq = list(dict.fromkeys(str(x).strip() for x in items if str(x).strip()))
    for x in uniq:
        wx = words(x)
        if any(y != x and wx <= words(y) and (len(words(y)) > len(wx) or uniq.index(y) < uniq.index(x)) for y in uniq):
            continue
        out.append(x)
    return out if keep_order else sorted(out)


def headline(m, n_shots, n_lines):
    """The line under the title: length, shots, layout, speech and its language. With no speech the
    agent gives the on-screen text's language (METHOD: metadata), named as that; a language only the
    transcript gave is then a guess on sound without speech, and is left out. With the speech not
    transcribed, whether anyone speaks is not known, and the line says so instead of "no speech"."""
    lang = m.get("language")
    speech = SPEAKING_WORDS.get(m["speaking_mode"], m["speaking_mode"])
    if m["speaking_mode"] == "none" and (m.get("_src") or {}).get("speaking_mode") == "cannot_judge_locally":
        speech = "speech not transcribed"
    if m["speaking_mode"] != "none":
        speech += f" ({lang})" if lang else ""
    elif lang and (m.get("_src") or {}).get("language") == "seen":
        speech += f" · on-screen text in {lang}"
    return (
        f"{m['duration_seconds']} s · {n_shots} shot{'s' if n_shots != 1 else ''} · "
        f"{FORMAT_WORDS.get(m['video_format'], m['video_format'])} · {speech}"
        + (f" · {n_lines} spoken line{'s' if n_lines != 1 else ''}" if n_lines else "")
    )


def report_md(idx, A, J):
    """riffsheet.md: an account of the video, beat by beat, for a person who has not seen it."""
    R = J.get("report", {})
    m = A["metadata"]
    ents = A["scene_entities"]
    names, k = {}, 0  # id -> (first mention in the document, every later mention)
    for e in ents:
        if e["kind"] == "person":
            if e["id"] == "protagonist":
                nm = ("the video's main person", "the main person")
            else:
                o = ORDINALS[min(k, len(ORDINALS) - 1)]
                nm = (f"a {o} person", f"the {o} person")
                k += 1
            # what the agent tagged uncertain about the person itself (whether every clip shows the same
            # one) is said where the person is first named, so the account does not state it as settled
            own = [x for x in e.get("_notes") or [] if not str(x).startswith("not confirmed on a large view")]
            names[e["id"]] = ((nm[0] + " (uncertain: " + "; ".join(own) + ")") if own else nm[0], nm[1])
        elif e["kind"] == "source_image":
            sem = re.sub(r"^(a|an|the)\s+", "", e["semantic"].strip().rstrip("."), flags=re.I)
            nm = ("the " + sem[0].lower() + sem[1:]) if sem and len(sem.split()) <= 6 else "the labeled object"
            names[e["id"]] = (nm, nm)
    seen = set()
    lines = {v["id"]: v["text"] for v in A["audio"]["voice_segments"]}
    title = os.path.splitext(os.path.basename(idx["video"]))[0]
    n_lines = len(A["audio"]["voice_segments"])
    L = [f"# {title}", "", headline(m, len(idx["shots"]), n_lines)]
    hearing = A["_local"].get("hearing")
    if hearing and hearing["state"] != "no_audio_track":  # what the sound is: heard, or not judged and why
        L += ["", "**Sound.** " + sound_line(hearing)]
    gaps = stage_lines(A["_local"].get("stages") or {}, idx["facts"])
    if gaps:  # an optional stage that failed or did not run, said where the reader starts
        L += ["", "**Not in this analysis.** " + " ".join(gaps)]
    other = untested_lines(A["_local"].get("stages") or {})
    if other:  # a stage that ran by the agent's choice of means, not the tool's tested path
        L += ["", "**Outside the tool's tested path.** " + " ".join(other)]
    sp = A["_local"].get("sound_at_picture")
    if sp:  # measured coincidence of sound events with cuts and caption appearances (times, not hearing)
        parts = [g["summary"] for g in (sp["cuts"], sp["captions"]) if g["changes"]]
        if parts:
            L += ["", "Sound and picture (measured times, not what the sound is): " + "; ".join(parts) + "."]
    if R.get("what_happens"):
        L += ["", "## What happens", "", fix_articles(R["what_happens"].strip())]
    if R.get("why_it_holds"):
        L += ["", "## Why it holds a viewer", "", fix_articles(R["why_it_holds"].strip())]
    # beats: the slots, each with the prose segments that start inside it; without slots, each segment
    segs = A["_prose_segments"]
    beats = [(s["time_range"], s["formula"]) for s in A["slots"]] if A["slots"] else [(p["window"], None) for p in segs]
    if beats:
        L += ["", "## Beat by beat"]
    for n, ((t0, t1), f) in enumerate(beats, 1):
        stage = str((f or {}).get("funnel_stage") or "").strip().replace("_", " ")
        stage = STAGE_WORDS.get(stage.lower(), stage)
        L += [
            "",
            f"### {n}. " + (stage[:1].upper() + stage[1:] + " · " if stage else "") + f"{mmss(t0)}–{mmss(t1)}",
            "",
        ]
        for p in segs:
            if t0 - 0.05 <= p["window"][0] < t1 - 0.05:
                body = re.sub(r"^\[[0-9:.]+-[0-9:.]+\]\s*", "", p["text"])
                L += [f"**{mmss(p['window'][0])}–{mmss(p['window'][1])}** " + _readable(body, names, lines, seen), ""]
        shown, spoken = [], []
        for e in ents:
            a_, b_ = e["time_range"]
            if not (a_ < t1 and b_ > t0):
                continue
            if e["kind"] == "subtitle" and e["params"].get("voice_anchor"):
                spoken.append(f"“{e['params']['text']}” ({mmss(a_)}–{mmss(b_)})")
            elif e["kind"] == "subtitle":
                shown.append(f"“{e['params']['text']}” ({mmss(a_)}–{mmss(b_)})")
            elif e["kind"] == "graphic":
                what = (e["semantic"] or e["params"].get("description") or "").strip().rstrip(".")
                said = [str(v).strip() for v in (e["params"].get("inline_text") or {}).values() if str(v).strip()]
                if said:  # the words on a card or graphic, as read
                    what = (what + ": " if what else "") + ", ".join(f"“{x}”" for x in said)
                if what:
                    shown.append(f"{what} ({mmss(a_)}–{mmss(b_)})")
        heard = [h for h in A["audio"].get("heard") or [] if t0 - 0.05 <= h["time_range"][0] < t1 - 0.05]
        if heard:  # what the agent heard, after it passed the hearing check
            L += [
                "**Heard by the agent.** "
                + "; ".join(
                    f"{mmss(h['time_range'][0])}–{mmss(h['time_range'][1])}, {h['about']}: {h['text'].rstrip('.')}"
                    for h in heard
                )
                + ".",
                "",
            ]
        if shown:
            L += ["Also on screen: " + "; ".join(shown) + ".", ""]
        if spoken:
            L += ["Captions of the spoken words: " + "; ".join(spoken) + ".", ""]
        if f:
            does = " ".join(x for x in (_sentence(f.get("function")), _sentence(f.get("mechanism"))) if x)
            before = _sentence(f.get("viewer_state_before"), cap=False)
            after = _sentence(f.get("viewer_state_after"), cap=False)
            if before and after:
                does += f" Before this beat: {before} After it: {after}"
            if does.strip():
                L += ["**What it does for the viewer.** " + does.strip(), ""]
            if f.get("constraint"):
                L += ["**Keep when remaking.** " + _sentence(f["constraint"]), ""]
        while L and L[-1] == "":
            L.pop()
    if R.get("swappable"):
        L += ["", "## What you can change when remaking", ""] + [f"- {fix_articles(str(x))}" for x in R["swappable"]]
    cj = merge_items(
        list(A["_local"].get("cannot_judge_locally", []))
        + [x for p in segs for x in p.get("claims", {}).get("cannot_judge_locally", [])]
    )
    if cj:
        L += ["", "## Not judged (needs hearing, or motion the still pictures do not settle)", ""] + [
            f"- {x}" for x in cj
        ]
    unc = []
    for e in ents:
        if e["kind"] == "person" and e.get("_notes"):
            unc += [f"{names[e['id']][1]}: {x}" for x in e["_notes"]]
    for v in A["audio"]["voice_segments"]:
        unc += [
            f"“{v['text']}” ({mmss(v['time_range'][0])}): {x[len('uncertain: ') :]}"
            for x in v.get("_notes") or []
            if str(x).startswith("uncertain: ")
        ]
    for p in segs:
        unc += [f"{mmss(p['window'][0])}–{mmss(p['window'][1])}: {x}" for x in p.get("claims", {}).get("uncertain", [])]
    if unc:
        L += ["", "## Marked uncertain", ""] + [f"- {x}" for x in merge_items(unc, keep_order=True)]
    own = A["_local"].get("own_means") or []
    if own:
        L += ["", "## Established by the agent's own means, outside the tool", ""] + [
            f"- {fix_articles(x['fact'].rstrip('.'))} (used: {x['used'].rstrip('.')}"
            + (f"; {mmss(x['time_range'][0])}–{mmss(x['time_range'][1])}" if x.get("time_range") else "")
            + ")."
            for x in own
        ]
    gaps_ = [x if isinstance(x, str) else json.dumps(x, ensure_ascii=False) for x in A["_local"].get("tool_gaps") or []]
    if gaps_:
        L += ["", "## What the tool lacked here (recorded by the agent)", ""] + [f"- {x}" for x in gaps_]
    if A["_local"]["checks"] != "all passed":
        L += ["", "## Open checks", ""] + [f"- {_readable(x, names, lines, set(names))}" for x in A["_local"]["checks"]]
    return "\n".join(L) + "\n"
