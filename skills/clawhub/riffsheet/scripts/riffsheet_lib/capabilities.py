"""What this machine can do for an analysis, and what each optional stage did.

`check` reports ffmpeg (required) and each optional capability: ready, missing or partly there, what it
adds, what getting it costs and the commands that prepare it. `scan` records, for each optional stage,
whether it ran (and by what means), failed (and why) or did not run (and why); `build` carries that
record into riffsheet.json (`_local.stages`) and says it in riffsheet.md. Nothing here uses the network,
imports an optional package or changes the machine.

A second optional capability is one more entry in CAPABILITIES (its check, cost and commands) and one
more function in STAGE_RECORDS (what scan writes about it)."""

import glob
import importlib.util
import json
import os
import re
import shlex
import shutil
import subprocess
import sys

from . import VERSION, util
from .constants import FFMPEG_MIN_MAJOR
from .hearing import SYNTHESIZERS, synthesizer
from .media import probe
from .transcript import TRANSCRIBE_MODEL
from .util import this_python

# Every ffmpeg filter (and the one lavfi source, color) the tool's commands use. A build of ffmpeg without
# one of them fails on the command that needs it, so `check` names any that are missing. drawtext is the
# one most often missing: it needs ffmpeg built with freetype.
FFMPEG_FILTERS = (
    "ametadata",
    "aresample",
    "asetnsamples",
    "astats",
    "blend",
    "color",
    "crop",
    "drawbox",
    "drawgrid",
    "drawtext",
    "ebur128",
    "format",
    "interleave",
    "nullsink",
    "pad",
    "scale",
    "scdet",
    "select",
    "setpts",
    "setsar",
    "showinfo",
    "split",
    "tblend",
    "tile",
)

# Where `check` suggests installing faster-whisper: a virtual environment of its own in the user's home,
# so the system Python is never changed. `check` also looks there, so a package installed there is found
# even when the tool runs under another Python.
VENV = os.path.join("~", ".riffsheet", "venv")
# What getting speech recognition costs, measured on 2026-11-28 by installing faster-whisper 1.2.1 into a
# fresh virtual environment (Python 3.9, macOS on Apple silicon): 64.3 MB of wheels downloaded, 206.6 MB
# added on disk (214.7 MB environment minus 8.1 MB when empty). Other systems and versions differ somewhat.
SPEECH_PACKAGE_DOWNLOAD_MB = 64
SPEECH_PACKAGE_DISK_MB = 207
# The model faster-whisper fetches for the default size, and its size: model.bin 483.5 MB, tokenizer.json
# 2.2 MB, vocabulary.txt 0.5 MB, config.json 2 KB, as stored in the Hugging Face cache (the same on disk).
# Installing the downloaded wheels into a fresh environment took 4.5 s (the same system, from a local
# folder, so without the download); the download itself takes what the person's connection takes.
SPEECH_PACKAGE_INSTALL_S = 5
SPEECH_MODEL_REPO = {"small": "Systran/faster-whisper-small"}
SPEECH_MODEL_MB = {"small": 486}

SPEECH_ADDS = (
    "the spoken words, each with its start and end time, so the riffsheet quotes every line, says who says "
    "it and at what pace, and sets the sound measures against the words"
)
# run time of `transcribe` with the default model, from the model comparison in references/TOOL.md
SPEECH_RUN_TIME = (
    "transcribing takes about 2.4 to 4.6 s for a clip of 8 to 30 s (small model, CPU, int8; references/TOOL.md)"
)
SPEECH_OTHER_WAYS = (
    "any recognizer that gives a word-timed transcript in the format `transcribe` writes (references/TOOL.md), "
    "or a transcript the person supplies in it; `scan --transcript-by` records what made it"
)
HEARING_ADDS = (
    "if the agent's model takes sound as input and passes the check: what the sound is (music or not and what "
    "kind, tone of voice, what a sound effect is), each statement marked heard by the agent"
)
HEARING_LACKS = "what the sound is stays not judged; times and loudness are measured either way"
SPEECH_LACKS = (
    "the riffsheet quotes no spoken line and cannot say whether anyone speaks; it says that the speech was not "
    "transcribed, and why"
)


def _q(path):
    return shlex.quote(path)


def _mb(n_bytes):
    return round(n_bytes / 1e6)


# ----------------------------------------------------------------------------- ffmpeg
def ffmpeg_status():
    """ffmpeg and ffprobe: where, which version, and which of the filters the tool uses are missing."""
    ff, fp = shutil.which("ffmpeg"), shutil.which("ffprobe")
    out = {"ffmpeg": ff, "ffprobe": fp, "version": None, "filters_missing": [], "needs": f"{FFMPEG_MIN_MAJOR}.0"}
    problems = []
    if not ff:
        problems.append("ffmpeg not found on PATH")
    if not fp:
        problems.append("ffprobe not found on PATH")
    if ff:
        r = subprocess.run([ff, "-hide_banner", "-version"], capture_output=True)
        first = r.stdout.decode("utf-8", "ignore").splitlines()[:1]
        m = re.match(r"ffmpeg version (\S+)", first[0]) if first else None
        out["version"] = m.group(1) if m else None
        major = re.match(r"n?(\d+)\.", out["version"] or "")
        # a build from git reports no release number; it is taken to be recent (as the tool itself does)
        if major and int(major.group(1)) < FFMPEG_MIN_MAJOR:
            problems.append(f"ffmpeg {out['version']} is older than {FFMPEG_MIN_MAJOR}.0")
        r = subprocess.run([ff, "-hide_banner", "-filters"], capture_output=True)
        lines = r.stdout.decode("utf-8", "ignore").splitlines()
        start = next((i + 1 for i, ln in enumerate(lines) if ln.strip().startswith("---")), 0)
        have = {ln.split()[1] for ln in lines[start:] if len(ln.split()) > 1}
        out["filters_missing"] = [f for f in FFMPEG_FILTERS if f not in have]
        if out["filters_missing"]:
            problems.append("this ffmpeg lacks the filter(s) " + ", ".join(out["filters_missing"]))
    out["state"] = "missing" if problems else "ready"
    out["problems"] = problems
    return out


# ----------------------------------------------------------------------------- speech recognition
def hf_cache():
    """The Hugging Face cache folder faster-whisper reads models from (its own default rules)."""
    hub = os.environ.get("HF_HUB_CACHE") or os.environ.get("HUGGINGFACE_HUB_CACHE")
    if hub:
        return os.path.expanduser(hub)
    home = os.environ.get("HF_HOME") or os.path.join(
        os.environ.get("XDG_CACHE_HOME") or os.path.join("~", ".cache"), "huggingface"
    )
    return os.path.join(os.path.expanduser(home), "hub")


def speech_model_on_disk(model=TRANSCRIBE_MODEL):
    """(folder, size in bytes) of the model as stored in the Hugging Face cache, or None."""
    repo = SPEECH_MODEL_REPO.get(model)
    if not repo:
        return None
    pattern = os.path.join(hf_cache(), "models--" + repo.replace("/", "--"), "snapshots", "*", "model.bin")
    for mb in sorted(glob.glob(pattern)):
        if os.path.isfile(mb):  # a link into the cache's blobs: the file it points to must be there
            folder = os.path.dirname(mb)
            size = sum(os.path.getsize(os.path.join(folder, f)) for f in os.listdir(folder))
            return folder, size
    return None


def _package_version(name):
    try:
        from importlib import metadata

        return metadata.version(name)
    except Exception:  # not installed as a distribution, or metadata unreadable
        return None


def _in_venv(venv):
    """Whether faster-whisper is installed in the virtual environment at venv (looked up on disk)."""
    pkgs = glob.glob(os.path.join(venv, "lib", "python*", "site-packages", "faster_whisper", "__init__.py"))
    return bool(pkgs) and os.path.exists(os.path.join(venv, "bin", "python"))


def speech_ready_here():
    """Why speech recognition cannot run under this Python, or None when it can: the reason scan records
    when it is given no transcript."""
    if importlib.util.find_spec("faster_whisper") is None:
        return f"the faster-whisper package is not installed for the Python that ran the analysis ({this_python()})"
    if not speech_model_on_disk():
        return f"the speech model ({TRANSCRIBE_MODEL}) is not on this machine"
    return None


def speech_status():
    """The speech recognition entry of `check`: facts about the tool's own tested path (faster-whisper with
    the small model), what preparing it would cost, and the commands that prepare and remove it."""
    venv = os.path.expanduser(VENV)
    vpy = os.path.join(venv, "bin", "python")
    here = importlib.util.find_spec("faster_whisper") is not None
    there = not here and _in_venv(venv)
    model = speech_model_on_disk()
    tool = shlex.split(util.CMD)[-1]
    py = sys.executable if here else vpy
    run_with = f"{_q(py)} -I {_q(tool)}"
    facts, cost, prepare, remove = [], [], [], []
    if here:
        v = _package_version("faster-whisper")
        facts.append(f"faster-whisper {v or '(version unknown)'} is installed for this Python ({sys.executable})")
    elif there:
        facts.append(
            f"faster-whisper is installed in {venv}, not for this Python ({sys.executable}): the tool runs it "
            f"when every riffsheet command is run with {vpy}"
        )
    else:
        facts.append(f"faster-whisper is not installed for this Python ({sys.executable}), nor in {venv}")
        cost.append(
            {
                "what": "the faster-whisper package and the packages it needs, from the Python Package Index",
                "download_mb": SPEECH_PACKAGE_DOWNLOAD_MB,
                "disk_mb": SPEECH_PACKAGE_DISK_MB,
                "network": True,
                "sends_media": False,
                "time": f"the download as long as {SPEECH_PACKAGE_DOWNLOAD_MB} MB takes on the connection, then about "
                f"{SPEECH_PACKAGE_INSTALL_S} s to install",
                "measured": "faster-whisper 1.2.1, Python 3.9, macOS on Apple silicon; other systems differ somewhat",
            }
        )
        if importlib.util.find_spec("ensurepip") is None:
            facts.append(
                "this Python cannot make a virtual environment, which the commands below do: its ensurepip module "
                "is missing (Debian and Ubuntu leave it out of the system Python and ship it as the system package "
                "python3-venv). Installing a system package changes the machine: it needs administrator rights "
                "and the person's yes, like any other cost"
            )
        prepare += [f"{_q(sys.executable)} -m venv {_q(venv)}", f"{_q(vpy)} -m pip install faster-whisper"]
        remove.append(f"rm -rf {_q(venv)}")
    if model:
        facts.append(f"the speech model ({TRANSCRIBE_MODEL}) is on this machine: {_mb(model[1])} MB in {model[0]}")
    else:
        facts.append(f"the speech model ({TRANSCRIBE_MODEL}) is not on this machine (looked in {hf_cache()})")
        cost.append(
            {
                "what": f"the speech model ({TRANSCRIBE_MODEL}), once, into the Hugging Face cache ({hf_cache()})",
                "download_mb": SPEECH_MODEL_MB[TRANSCRIBE_MODEL],
                "disk_mb": SPEECH_MODEL_MB[TRANSCRIBE_MODEL],
                "network": True,
                "sends_media": False,
                "time": f"as long as {SPEECH_MODEL_MB[TRANSCRIBE_MODEL]} MB takes on the connection",
                "measured": "its size as stored in a Hugging Face cache",
            }
        )
        prepare.append(f"{run_with} transcribe VIDEO --out T.json --download")
        remove.append(
            "rm -rf "
            + _q(os.path.join(hf_cache(), "models--" + SPEECH_MODEL_REPO[TRANSCRIBE_MODEL].replace("/", "--")))
        )
    # missing: the package is not anywhere (a model alone does nothing); partly there: the package is
    # installed but the model is not here, or the package is only in the virtual environment
    state = "ready" if here and model else ("partial" if here or there else "missing")
    return {
        "id": "speech_recognition",
        "name": "speech recognition",
        "path": f"the tool's tested path: `transcribe`, faster-whisper with the {TRANSCRIBE_MODEL} model",
        "state": state,
        "facts": facts,
        "adds": SPEECH_ADDS,
        "without": SPEECH_LACKS,
        "run_time": SPEECH_RUN_TIME,
        "cost": cost,
        "prepare": prepare,
        "run_with": run_with,
        "remove": remove,
        "other_ways": SPEECH_OTHER_WAYS,
    }


def speech_for_video(info):
    """A plain fact that rules speech recognition out for this video, or None."""
    return "the video has no audio track: there is nothing to transcribe" if not info["has_audio"] else None


def hearing_status():
    """The hearing check's entry of `check`: whether this machine can make the check's sound. Whether the
    agent can hear is not this machine's to report: only the check settles it."""
    syn = synthesizer()
    facts = [
        f"a speech synthesizer is here to make the check's sound: {syn[0]} at {syn[1]}"
        if syn
        else f"no speech synthesizer is on PATH ({', '.join(SYNTHESIZERS)}), so the check's sound cannot be "
        f"made here. macOS has say; on Linux espeak-ng is a system package (on Debian and Ubuntu, espeak-ng). "
        f"Installing a system package changes the machine: it needs administrator rights and the person's yes, "
        f"like any other cost",
        "whether this agent can hear is not known here: only the check, taken after `scan`, settles it",
    ]
    return {
        "id": "hearing_check",
        "name": "hearing check",
        "path": "`hear-check`: a voice says six random digits, the agent reports what it heard, the tool marks it",
        "state": "ready" if syn else "missing",
        "facts": facts,
        "adds": HEARING_ADDS,
        "without": HEARING_LACKS,
        "run_time": "where measured (Apple M6, macOS `say`), making a check took 1.0 to 1.4 s and marking an "
        "answer 0.38 to 0.61 s, one slow hash whose speed depends on the machine and on the Python's OpenSSL "
        "or LibreSSL",
        "cost": [],
        "prepare": [],
        "run_with": None,
        "remove": [],
        "other_ways": "none in the tool: it cannot hear; hearing is the agent's model's own",
    }


def hearing_for_video(info):
    return "the video has no audio track: there is nothing to hear" if not info["has_audio"] else None


def sound_line(hearing):
    """The sentence riffsheet.md gives near its top on whether what the sound is was judged."""
    st = hearing["state"]
    if st == "passed":
        return (
            "Heard by the agent, which passed the hearing check for this analysis: what this file says the sound "
            "is (music, voices, sound effects) comes from the agent's listening, and its statements under heard "
            "are marked heard by the agent. Times and loudness are measured by the tool."
        )
    why = {
        "failed": "this agent did not pass the hearing check",
        "cannot_hear": "this agent cannot hear (at the hearing check it said it cannot open sound)",
        "not_taken": "no hearing check was taken for this analysis",
    }[st]
    return (
        f"Not judged: {why}. Nothing in this file that says what the sound is was heard: `build` lists each such "
        "statement it finds (music, a song, a sound effect, a tone of voice and like words) as an open check. "
        "Times and loudness are measured by the tool."
    )


CAPABILITIES = (
    (speech_status, speech_for_video),
    (hearing_status, hearing_for_video),
)  # (status, plain exclusion for a video) per capability
# what `check` covers, said at its end: its knowledge is this closed list
COVERS = (
    "This report covers ffmpeg, the tool's own speech recognition path (faster-whisper with the {model} "
    "model, in this Python or in {venv}) and whether the hearing check can be made here. It knows nothing "
    "about other tools on this machine or elsewhere (other speech recognizers, models or services): whether "
    "one would serve this analysis is for the agent to judge, and anything it costs the person is for the "
    "person to agree to."
)


# ----------------------------------------------------------------------------- stage records (scan, build)
# what `transcribe` writes as a transcript's "model" (riffsheet 0.1.0 on): the tool's own path, with the
# model size it ran; the tested path is that command with the default size
TRANSCRIBE_STAMP = re.compile(r"^faster-whisper (\S+) \(int8, cpu\)$")
TESTED_PATH = f"riffsheet transcribe with faster-whisper's {TRANSCRIBE_MODEL} model"


def speech_stage(info, transcript, made_by=None):
    """The speech recognition stage as scan records it. `transcript` is what load_words returned as
    metadata (None without --transcript); `made_by` is what `scan --transcript-by` says made it. A ran
    record says what made the transcript and whether that was the tool's tested path (`tested`)."""
    if transcript is not None:
        if transcript.get("stage"):  # transcribe could not make a transcript and wrote why
            return dict(transcript["stage"])
        model = transcript.get("model")
        stamp = TRANSCRIBE_STAMP.match(model) if isinstance(model, str) and not made_by else None
        if stamp:
            return {"state": "ran", "by": model, "tested": stamp.group(1) == TRANSCRIBE_MODEL}
        if made_by or model:
            return {"state": "ran", "by": made_by or f"{model} (as the transcript names it)", "tested": False}
        # nothing says what made it: whether it was the tested path is not known (tested null)
        return {"state": "ran", "by": "a transcript given to scan that does not say what made it", "tested": None}
    if not info["has_audio"]:
        return {"state": "not_run", "why": "the video has no audio track"}
    why = speech_ready_here()
    return {
        "state": "not_run",
        "why": "no transcript was made"
        + (f", and {why}" if why else " (speech recognition was ready on this machine; `transcribe` makes one)"),
    }


STAGE_RECORDS = {"speech_recognition": speech_stage}


def stages_of(idx):
    """The stage records of a scan. A scan made before riffsheet 0.2.0 has none: they are derived from what
    it does record (a transcript, an audio track), saying so. A ran record without `tested` (written while
    0.2.0 was in development) is given it from its `by`."""
    if idx.get("stages"):
        out = {k: dict(v) for k, v in idx["stages"].items()}
        sp = out.get("speech_recognition") or {}
        if sp.get("state") == "ran" and "tested" not in sp:
            stamp = TRANSCRIBE_STAMP.match(sp.get("by") or "")
            sp["tested"] = bool(stamp) and stamp.group(1) == TRANSCRIBE_MODEL
        return out
    if idx.get("transcript_meta"):
        # the transcript the scan read, when it is still there, says what made it
        try:
            with open(idx.get("transcript") or "", encoding="utf-8") as f:
                model = json.load(f).get("model")
        except (OSError, ValueError, AttributeError):
            model = None
        sp = speech_stage(idx["facts"], {"model": model}) if isinstance(model, str) else {}
        if sp.get("tested") is not True:
            sp = {
                "state": "ran",
                "by": "a transcript given to scan (a scan made before riffsheet 0.2.0 does not say what made it)",
                "tested": None,
            }
    elif not idx["facts"].get("has_audio"):
        sp = {"state": "not_run", "why": "the video has no audio track"}
    else:
        sp = {"state": "not_run", "why": "no transcript was made"}
    return {"speech_recognition": sp}


STAGE_NAMES = {"speech_recognition": "Speech recognition"}
STAGE_LACKS = {
    "speech_recognition": "The speech was not transcribed: no spoken words are quoted, and whether anyone "
    "speaks is not known."
}


def stage_lines(stages, facts):
    """One sentence per optional stage that failed or did not run, for riffsheet.md and the build sheet.
    A stage that did not run because the video has nothing for it (speech, no audio track) says only that.
    Failed means the stage was there and stopped while running; did not run, that it was not there or not
    used."""
    out = []
    for k, st in stages.items():
        if st["state"] == "ran":
            continue
        name = STAGE_NAMES.get(k, k)
        lack = STAGE_LACKS.get(k)
        if k == "speech_recognition" and not facts.get("has_audio"):
            lack = None
        verb = "was there but failed while running" if st["state"] == "failed" else "did not run"
        out.append(f"{name} {verb}: {st['why'].rstrip('.')}." + (f" {lack}" if lack else ""))
    return out


def untested_lines(stages):
    """One sentence per optional stage that ran by other means than the tool's tested path (the agent's own
    choice of recognizer, model size or a transcript the person supplied), or by means nothing records."""
    sp = stages.get("speech_recognition") or {}
    if sp.get("state") != "ran" or sp.get("tested", True):
        return []
    if sp["tested"] is None:
        return [
            f"The spoken words come from {sp['by'].rstrip('.')}: whether the tool's tested path ({TESTED_PATH}) "
            f"made it is not known, nor whether the word accuracy measured for that path applies to it."
        ]
    return [
        f"The spoken words were transcribed by {sp['by'].rstrip('.')}, not by the tool's tested path "
        f"({TESTED_PATH}): the word accuracy measured for that path does not apply to them."
    ]


# ----------------------------------------------------------------------------- check
def cmd_check(a):
    report = {"tool": "riffsheet", "version": VERSION, "network": "not used"}
    report["python"] = {"path": sys.executable, "version": ".".join(map(str, sys.version_info[:3]))}
    ff = ffmpeg_status()
    report["ffmpeg"] = ff
    caps = [status() for status, _ in CAPABILITIES]
    if a.video:
        video = os.path.abspath(a.video)
        if not (ff["ffmpeg"] and ff["ffprobe"]):
            report["video"] = {"path": video, "readable": False, "why": "ffprobe is needed to read it"}
        else:
            info = probe(video)  # an unreadable file stops here, as every command does
            report["video"] = {
                "path": video,
                "duration_s": info["duration_s"],
                "width": info["width"],
                "height": info["height"],
                "has_audio": info["has_audio"],
            }
            for c, (_, excluded) in zip(caps, CAPABILITIES):
                why = excluded(info)
                if why:
                    c["not_for_this_video"] = why
    report["capabilities"] = caps
    report["covers"] = COVERS.format(model=TRANSCRIBE_MODEL, venv=os.path.expanduser(VENV))
    if a.json:
        print(json.dumps(report, indent=1, ensure_ascii=False))
        return
    print(check_text(report))


def check_text(r):
    L = [f"riffsheet {r['version']} check (no network used, nothing changed)"]
    L.append(f"python   {r['python']['path']} ({r['python']['version']})")
    ff = r["ffmpeg"]
    if ff["state"] == "ready":
        L.append(
            f"ffmpeg   ready: ffmpeg {ff['version']} at {ff['ffmpeg']}, ffprobe at {ff['ffprobe']}; all "
            f"{len(FFMPEG_FILTERS)} filters the tool uses are present ({', '.join(FFMPEG_FILTERS)})"
        )
    else:
        L.append(
            f"ffmpeg   MISSING (required, {FFMPEG_MIN_MAJOR}.0 or newer; nothing can be analyzed without it): "
            + "; ".join(ff["problems"])
        )
    v = r.get("video")
    if v:
        if v.get("readable") is False:
            L.append(f"video    {v['path']}: not read ({v['why']})")
        else:
            L.append(
                f"video    {v['path']}: {v['duration_s']} s, {v['width']}x{v['height']}, "
                f"audio track {'yes' if v['has_audio'] else 'no'}"
            )
    for c in r["capabilities"]:
        L.append("")
        state = {"ready": "ready", "missing": "MISSING", "partial": "PARTLY THERE"}[c["state"]]
        L.append(f"{c['name']} (optional; {c['path']}): {state}")
        for f in c["facts"]:
            L.append(f"  - {f}")
        if c.get("not_for_this_video"):
            L.append(f"  for this video: {c['not_for_this_video']}")
        L.append(f"  adds: {c['adds']}")
        L.append(f"  without it: {c['without']}")
        L.append(f"  when run: {c['run_time']}")
        if c["cost"]:
            L.append("  what preparing it costs:")
            for x in c["cost"]:
                L.append(
                    f"    - {x['what']}: about {x['download_mb']} MB to download, {x['disk_mb']} MB on disk; "
                    f"time: {x['time']}; needs the network; sends no audio or video anywhere ({x['measured']})"
                )
        if c["prepare"]:
            L.append("  prepare it (the system Python is not changed):")
            L += [f"    {x}" for x in c["prepare"]]
        if c["state"] != "ready" and c["run_with"]:
            L.append(f"  then run every riffsheet command with: {c['run_with']}")
        if c["remove"]:
            L.append("  to remove what preparing adds: " + "; ".join(c["remove"]))
        L.append(f"  other ways: {c['other_ways']}")
    L.append("")
    L.append(r["covers"])
    return "\n".join(L)
