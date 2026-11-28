"""Whether the agent can hear, settled by a test the tool sets and marks, and the sound cut for listening.

The tool cannot hear. Some agents run on a model that takes sound as input; most do not, and an agent's
belief about its own abilities is unreliable: one that cannot hear but is told to describe the sound if it
can tends to invent. So `hear-check` sets a test: a short sound file in which a speech synthesizer on this
machine says six random digits (one in a million to guess). The agent opens the file as sound and reports
the digits; the tool marks the answer and records passed, failed, or that the agent said it cannot open
sound. The digits are never written to a file: the record keeps only a salted, deliberately slow hash
(PBKDF2), so neither reading the folder nor trying every answer against the hash gives them cheaply. What
does give them is measuring the file itself (decoding it, running a speech recognizer on it); the
instructions forbid that, since a check passed that way would make every later description of the sound
an invention. The check protects against an agent that cannot hear inventing what the sound is; it does not
protect against someone who deliberately forges the record, which is a file in the scan folder.

The record and the cut files belong to the scan they were made for: `scan` removes the folders that hold
them (`hearing/`, `listen/`) whenever it writes a scan folder, so a pass or a clip of an earlier video in
the same folder cannot outlive it.

After a pass, `listen` cuts the video's sound around each measured sound event, and the whole track when it
is short, into files the agent opens; `build` then takes the agent's statements of what the sound is (the
judgment's `heard`), each marked heard by the agent. Without a pass, `build` refuses them."""

import datetime
import hashlib
import hmac
import os
import re
import secrets
import shlex
import shutil
import subprocess
import unicodedata

from . import util
from .media import run
from .scandir import load_dir
from .util import die, fmt_t, read_json, write_json

HEAR_DIGITS = 6  # one chance in a million of guessing them; easy to hear for a model that hears speech
# PBKDF2-HMAC-SHA256 rounds for the stored hash. Measured on an Apple M6, one core: 0.38 s per answer tried
# with OpenSSL 3 (Python 3.14), 0.61 s with the LibreSSL of macOS's own Python 3.9. Trying every answer takes
# a million times as long as marking one: at those speeds 4 to 7 days of one core, about half a day of 12
# cores. Marking one answer stays short enough not to notice.
HEAR_ROUNDS = 3_000_000
# speech synthesizers the check can use, in the order tried: macOS has `say`; Linux has espeak-ng or espeak
# when installed (most package managers carry espeak-ng). Each reads the text on standard input, so the
# digits never appear in a file or on a command line.
SYNTHESIZERS = ("say", "espeak-ng", "espeak")
LISTEN_WHOLE_MAX_S = 60  # the whole track is cut as one file when the video is at most this long
LISTEN_BEFORE_S = 1.0  # a clip around a sound event starts this long before its onset
LISTEN_AFTER_S = 2.0  # and ends this long after it (clips that touch are merged)
LISTEN_WHOLE_SHARE = 0.5  # with the whole track cut, a merged window covering this share of it or more is left out
LISTEN_RATE = 32000  # Hz, mono 16-bit WAV: music and voices stay clear, files stay small
HEARD_ABOUT = ("music", "voice", "effect", "ambience", "other")


def synthesizer():
    """(name, path) of the first speech synthesizer on PATH, or None."""
    for name in SYNTHESIZERS:
        p = shutil.which(name)
        if p:
            return name, p
    return None


def hearing_dir(d):
    return os.path.join(d, "hearing")


def listen_dir(d):
    return os.path.join(d, "listen")


def forget(d):
    """Remove the hearing record and the cut sound files of a scan folder: `scan` calls it whenever it
    writes the folder, since both belong to the video they were made for."""
    for p in (hearing_dir(d), listen_dir(d)):
        shutil.rmtree(p, ignore_errors=True)


def record_path(d):
    return os.path.join(hearing_dir(d), "hearing.json")


def _bad_record(d, what):
    die(
        f"the hearing record {record_path(d)} is not one the tool wrote ({what}); remove the folder "
        f"{hearing_dir(d)} and take the check again"
    )


def read_record(d):
    p = record_path(d)
    rec = read_json(p, "hearing record") if os.path.exists(p) else {"checks": []}
    if not (isinstance(rec, dict) and isinstance(rec.get("checks"), list)):
        _bad_record(d, "no list of checks")
    if not all(isinstance(c, dict) for c in rec["checks"]):
        _bad_record(d, "a check that is not a record")
    return rec


HEX = re.compile(r"[0-9a-f]+")


def _complete(d, n, c):
    """Whether check number n (from 1) is a whole record of a check the tool made in this folder: its sound
    file is there under the name the tool gave it, and its salt, hash, rounds and digit count are those the
    tool writes. A pass counts only then."""
    salt, digest = c.get("salt"), c.get("digest")
    return (
        c.get("file") == f"check_{n}.wav"
        and os.path.isfile(os.path.join(hearing_dir(d), c["file"]))
        and isinstance(salt, str)
        and len(salt) == 32
        and bool(HEX.fullmatch(salt))
        and isinstance(digest, str)
        and len(digest) == 64
        and bool(HEX.fullmatch(digest))
        and c.get("rounds") == HEAR_ROUNDS
        and c.get("digits") == HEAR_DIGITS
        and isinstance(c.get("made"), str)
        and isinstance(c.get("answered"), str)
    )


def hearing_state(d):
    """What the hearing record says for this analysis: passed, failed, cannot_hear or not_taken, and the
    checks taken. The last check answered decides; one made but not answered counts for nothing, and so does
    a pass whose record is not whole (see _complete)."""
    rec = read_record(d)
    done = [
        c
        for n, c in enumerate(rec["checks"], 1)
        if c.get("outcome") in ("failed", "cannot_hear") or (c.get("outcome") == "passed" and _complete(d, n, c))
    ]
    state = done[-1]["outcome"] if done else "not_taken"
    return {
        "state": state,
        "checks_answered": len(done),
        "checks_passed": sum(1 for c in done if c["outcome"] == "passed"),
    }


def answer_digits(answer):
    """The digits of an answer, in order, as ASCII: any decimal digit counts (full-width digits typed in a
    Chinese or Japanese reply, Arabic-Indic ones), every other character is ignored."""
    return "".join(str(unicodedata.decimal(ch)) for ch in answer if unicodedata.decimal(ch, None) is not None)


def _digest(answer, salt, rounds):
    return hashlib.pbkdf2_hmac("sha256", answer.encode("ascii"), bytes.fromhex(salt), rounds).hex()


def new_digits():
    return "".join(secrets.choice("0123456789") for _ in range(HEAR_DIGITS))


def synthesize(text, out_wav, tmp_wav):
    """Speak `text` into out_wav (16 kHz mono WAV, no metadata) with the first synthesizer found."""
    syn = synthesizer()
    if not syn:
        die(
            "the hearing check needs a speech synthesizer to make its sound, and none is on PATH "
            f"({', '.join(SYNTHESIZERS)}); without the check, what the sound is stays not judged"
        )
    name, path = syn
    os.makedirs(os.path.dirname(out_wav), exist_ok=True)  # only now: without a synthesizer nothing is written
    if name == "say":
        cmd = [path, "--file-format=WAVE", "--data-format=LEI16@22050", "-o", tmp_wav, "-f", "-"]
    else:
        cmd = [path, "-w", tmp_wav, "--stdin"]
    r = subprocess.run(cmd, input=text.encode("ascii"), capture_output=True)
    if r.returncode != 0 or not os.path.exists(tmp_wav):
        die(f"{name} could not make the hearing check's sound: " + r.stderr.decode("utf-8", "ignore").strip()[-200:])
    r = run(
        ["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", tmp_wav, "-map_metadata", "-1", "-fflags", "+bitexact"]
        + ["-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", out_wav]
    )
    os.remove(tmp_wav)
    if r.returncode != 0:
        die("ffmpeg could not write the hearing check's sound: " + r.stderr.decode("utf-8", "ignore").strip()[-200:])
    return name


def _now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cmd_hear_check(a):
    d = os.path.abspath(a.dir)
    idx, _, _ = load_dir(d)
    if not idx["facts"].get("has_audio"):
        die("the video has no audio track: there is nothing to hear, and no hearing check is needed")
    rec = read_record(d)
    checks = rec["checks"]
    waiting = checks[-1] if checks and not checks[-1].get("outcome") else None
    if a.cannot_hear:
        c = waiting or {"file": None, "made": None}
        if not waiting:
            checks.append(c)
        c.update(outcome="cannot_hear", answered=_now())
        os.makedirs(hearing_dir(d), exist_ok=True)
        write_json(record_path(d), rec, indent=1)
        print(
            "hear-check: recorded that this agent cannot open sound. The riffsheet says that what the sound is "
            "was not judged because this agent cannot hear; times and loudness stay measured."
        )
        return
    if a.answer is not None:
        if not waiting:
            die(f"no hearing check is waiting for an answer: make one with {_cmd()} hear-check {_q(d)}")
        if not (
            isinstance(waiting.get("salt"), str)
            and HEX.fullmatch(waiting["salt"])
            and isinstance(waiting.get("digest"), str)
            and waiting.get("rounds") == HEAR_ROUNDS
        ):
            _bad_record(d, "the waiting check has no salt, hash or rounds")
        given = answer_digits(a.answer)
        if not given:
            die("the answer holds no digits: write the digits you heard, in order (nothing was recorded)")
        passed = len(given) == HEAR_DIGITS and hmac.compare_digest(
            _digest(given, waiting["salt"], waiting["rounds"]), waiting["digest"]
        )
        waiting.update(outcome="passed" if passed else "failed", answered=_now())
        write_json(record_path(d), rec, indent=1)
        if passed:
            print(
                f"hear-check: PASSED: {HEAR_DIGITS} of {HEAR_DIGITS} digits right. This agent may now say what "
                f"the sound is, from the files `listen` cuts: {_cmd()} listen {_q(d)}"
            )
        else:
            print(
                f"hear-check: FAILED: that is not what the file says ({len(given)} digit(s) given, "
                f"{HEAR_DIGITS} spoken). Without a pass, what the sound is stays not judged, and `build` refuses "
                f"statements of it. If you cannot open sound, record it with --cannot-hear; if you heard the "
                f"file and mistyped, take a new check ({_cmd()} hear-check {_q(d)}): each check is a new number."
            )
        return
    n = len(checks) + 1
    wav = os.path.join(hearing_dir(d), f"check_{n}.wav")
    digits = new_digits()
    name = synthesize(". ".join(digits) + ".", wav, os.path.join(hearing_dir(d), f".check_{n}.raw.wav"))
    salt = secrets.token_hex(16)
    if waiting:  # an earlier check left unanswered is abandoned: only the newest one can be answered
        waiting.update(outcome=None, abandoned=_now())
    checks.append(
        {
            "file": os.path.basename(wav),
            "made": _now(),
            "synthesizer": name,
            "digits": HEAR_DIGITS,
            "salt": salt,
            "rounds": HEAR_ROUNDS,
            "digest": _digest(digits, salt, HEAR_ROUNDS),
        }
    )
    write_json(record_path(d), rec, indent=1)
    print(
        f"hear-check: {wav}\n"
        f"  A voice ({name}) says {HEAR_DIGITS} digits, one at a time. Open this file the way you open the "
        f"pictures: with the tool that reads a file into your input, the one that shows you an image. If your "
        f"model takes sound as input, the file reaches you as sound: listen to it, then answer with the "
        f"{HEAR_DIGITS} digits you heard, in order, and nothing else:\n"
        f"    {_cmd()} hear-check {_q(d)} --answer DIGITS\n"
        f"  Answer --cannot-hear only after trying, when opening the file gives you nothing to listen to (an "
        f"error that the file type is not supported, raw bytes, or a description of the file in place of its "
        f"sound). Not knowing whether you can hear is no reason to answer it: open the file first.\n"
        f"    {_cmd()} hear-check {_q(d)} --cannot-hear\n"
        f"  Do not work the digits out by measuring the file (decoding it, a speech recognizer, a script, a "
        f"waveform or spectrum): a check passed that way would make every later description of the sound an "
        f"invention. The digits are not written in any file; the record keeps only a slow hash of them."
    )


def _cmd():
    return util.CMD  # read when called: the entry script sets it after this module is imported


def _q(p):
    return shlex.quote(p)


# ----------------------------------------------------------------------------- listen
def listen_windows(idx):
    """(name, start, end) of each sound file `listen` cuts: the whole track when the video is short, and a
    window around each measured sound event (peak, rise, drop), windows that touch merged. Sound events
    every half second (music) merge into one window as long as the track: the whole file serves for it."""
    dur = idx["facts"]["duration_video_s"]
    out = []
    if dur <= LISTEN_WHOLE_MAX_S:
        out.append(("whole", 0.0, dur))
    spans = []
    for e in (idx.get("audio") or {}).get("events", []):
        t = e.get("onset_t", e["t"])
        a_, b_ = max(0.0, t - LISTEN_BEFORE_S), min(dur, t + LISTEN_AFTER_S)
        if spans and a_ <= spans[-1][1]:
            spans[-1][1] = max(spans[-1][1], b_)
        else:
            spans.append([a_, b_])
    for a_, b_ in spans:
        if out and b_ - a_ >= LISTEN_WHOLE_SHARE * dur:  # nearly the whole track, which is already cut
            continue
        out.append((f"sound_{a_:05.2f}_{b_:05.2f}", round(a_, 3), round(b_, 3)))
    return out


def listen_path(d):
    return os.path.join(listen_dir(d), "listen.json")


def listen_clips(d):
    """name -> [start, end] of the sound files `listen` cut in this scan folder."""
    p = listen_path(d)
    if not os.path.exists(p):
        return {}
    rec = read_json(p, "listen record")
    clips = rec.get("clips") if isinstance(rec, dict) else None
    ok = isinstance(clips, list) and all(
        isinstance(c, dict)
        and isinstance(c.get("name"), str)
        and isinstance(c.get("span"), list)
        and len(c["span"]) == 2
        and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in c["span"])
        for c in clips
    )
    if not ok:
        die(f"the listen record {p} is not one the tool wrote; remove the folder {listen_dir(d)} and run listen again")
    return {c["name"]: c["span"] for c in clips}


def cmd_listen(a):
    d = os.path.abspath(a.dir)
    idx, _, _ = load_dir(d)
    if not idx["facts"].get("has_audio"):
        die("the video has no audio track: there is nothing to listen to")
    st = hearing_state(d)["state"]
    if st != "passed":
        why = {
            "failed": "this agent's last hearing check failed",
            "cannot_hear": "this agent said it cannot open sound",
            "not_taken": "no hearing check was answered for this analysis",
        }[st]
        die(
            f"listen cuts sound for an agent that passed the hearing check, and {why}: "
            f"{_cmd()} hear-check {_q(d)} makes one. Without a pass, what the sound is stays not judged"
        )
    dur = idx["facts"]["duration_video_s"]
    if a.start is not None or a.end is not None:
        a_, b_ = max(0.0, a.start or 0.0), min(dur, dur if a.end is None else a.end)
        if b_ <= a_:
            die(f"empty window: --from {a_} --to {b_} (the video is {dur} s)")
        wins = [(f"sound_{a_:05.2f}_{b_:05.2f}", round(a_, 3), round(b_, 3))]
    else:
        wins = listen_windows(idx)
    ld = listen_dir(d)
    os.makedirs(ld, exist_ok=True)
    known = {k: {"name": k, "span": v} for k, v in listen_clips(d).items()}
    print(f"listen: {len(wins)} sound file(s) in {ld} (mono {LISTEN_RATE} Hz WAV); open each as sound")
    for name, a_, b_ in wins:
        path = os.path.join(ld, name + ".wav")
        r = run(
            ["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", fmt_t(a_), "-to", fmt_t(b_), "-i", idx["video"]]
            + ["-vn", "-map_metadata", "-1", "-fflags", "+bitexact", "-ac", "1", "-ar", str(LISTEN_RATE)]
            + ["-c:a", "pcm_s16le", path]
        )
        if r.returncode != 0:
            die("ffmpeg could not cut the sound: " + r.stderr.decode("utf-8", "ignore").strip()[-200:])
        known[name] = {"name": name, "span": [a_, b_]}
        print(f"  {name}.wav  {fmt_t(a_)}–{fmt_t(b_)} s")
    write_json(listen_path(d), {"clips": sorted(known.values(), key=lambda c: (c["span"], c["name"]))}, indent=1)
    print(
        '  In the judgment file, say what you heard under "heard", one statement per sound: '
        '{"clip": NAME, "time": [start, end], "about": ' + " | ".join(HEARD_ABOUT) + ', "text": "..."}; '
        "each goes out marked heard by the agent. Times and loudness stay the tool's measurements."
    )
