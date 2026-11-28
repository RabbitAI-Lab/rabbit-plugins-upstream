"""Word-timed transcripts: loading, lookups by time, script predicates, `transcribe`."""

import os
import re
import sys
import time

from .media import check_video_path, run
from .util import die, read_json, this_python, write_json


# ----------------------------------------------------------------------------- transcript
def load_words(path):
    if not path:
        return [], None
    d = read_json(path, "transcript")
    segs = d.get("segments", []) if isinstance(d, dict) else d
    if not isinstance(segs, list) or not all(isinstance(s, dict) and "start" in s and "end" in s for s in segs):
        die(
            f'transcript {path}: expected {{"segments": [{{"start": s, "end": s, "text": ..., '
            f'"words": [{{"start": s, "end": s, "word": ...}}]}}]}} (faster-whisper\'s format)'
        )
    lang = d.get("language") if isinstance(d, dict) else None
    stage = d.get("stage") if isinstance(d, dict) else None
    if stage is not None and not (
        isinstance(stage, dict) and stage.get("state") in ("failed", "not_run") and isinstance(stage.get("why"), str)
    ):
        die(f'transcript {path}: "stage" must be {{"state": "failed" or "not_run", "why": "..."}}')
    words = []
    for si, s in enumerate(segs):
        ws = s.get("words") or []
        if not ws and "text" in s:  # segment-level transcript: one pseudo-word per segment
            ws = [{"start": s["start"], "end": s["end"], "word": s["text"]}]
        for w in ws:
            words.append(
                {
                    "start": float(w["start"]),
                    "end": float(w["end"]),
                    "word": str(w.get("word", "")).strip(),
                    "seg": si,
                    "prob": w.get("prob", w.get("probability")),
                }
            )
    words.sort(key=lambda x: x["start"])
    lines = [
        {"i": si, "start": float(s["start"]), "end": float(s["end"]), "text": str(s.get("text", "")).strip()}
        for si, s in enumerate(segs)
    ]
    meta = {"language": lang, "lines": lines, "model": d.get("model") if isinstance(d, dict) else None}
    if stage:  # transcribe's record of why it made no transcript (stop): it holds no words
        if words:
            die(f"transcript {path}: a record of a transcription that {stage['state']} holds no words")
        meta["stage"] = stage
    return words, meta


def words_at(words, t):
    return [w["word"] for w in words if w["start"] <= t < w["end"]]


def words_in(words, a, b):
    return [w["word"] for w in words if w["start"] < b and w["end"] > a]


def join_words(ws):
    """Words of a line as written: no space between two characters of a script written without
    spaces (Chinese, Japanese); a space everywhere else, Korean included."""
    s = ""
    for w in ws:
        if s and not (is_unspaced_script(w[:1]) and is_unspaced_script(s[-1:])):
            s += " "
        s += w
    return s


# Three tests on a character's script, each with its own purpose, so their ranges differ on purpose:
# is_wide is for drawing (label widths: everything from the CJK radicals up is drawn about a full em
# wide); is_unspaced_script is for writing words (Han and kana have no spaces between words, Hangul
# does); counts_by_character is for pace (Chinese, Japanese and Korean are counted in characters,
# about one syllable each, Korean included even though it is written with spaces).
def is_wide(ch):
    """Wide characters (for label widths)."""
    return bool(ch) and ord(ch[0]) >= 0x2E80


def is_unspaced_script(ch):
    """A character of a script written without spaces between words: Han, kana, CJK punctuation
    and full-width forms. Hangul is written with spaces."""
    if not ch:
        return False
    o = ord(ch[0])
    return (
        0x3000 <= o <= 0x30FF
        or 0x3400 <= o <= 0x9FFF
        or 0xF900 <= o <= 0xFAFF
        or 0xFF00 <= o <= 0xFFEF
        or 0x20000 <= o <= 0x3FFFF
    )


TRANSCRIBE_MODEL = "small"  # best of base / small / medium on word errors and word times (references/TOOL.md)


def _norm_word(w):
    return re.sub(r"[^\w']", "", w.lower().replace("’", "'"))


def _align(ref, hyp):
    """Word alignment (edit distance); returns [(i or None, j or None)]."""
    n, m = len(ref), len(hyp)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + (ref[i - 1] != hyp[j - 1]))
    i, j, out = n, m, []
    while i or j:
        if i and j and D[i][j] == D[i - 1][j - 1] + (ref[i - 1] != hyp[j - 1]):
            out.append((i - 1, j - 1))
            i, j = i - 1, j - 1
        elif i and D[i][j] == D[i - 1][j] + 1:
            out.append((i - 1, None))
            i -= 1
        else:
            out.append((None, j - 1))
            j -= 1
    return out[::-1]


def _recognize(WhisperModel, path, audio, a):
    """faster-whisper's segments and words, rounded as the transcript stores them, and its run info."""
    m = WhisperModel(path, device="cpu", compute_type="int8")
    # whisper's own fallback (re-decode at a higher temperature when a decode looks degenerate) stays
    # on: without it sung or music-heavy audio can come back as a stock phrase instead of the words
    segs, info = m.transcribe(audio, word_timestamps=True, language=a.language, hotwords=a.hint or None)
    out = []
    for sg in segs:
        out.append(
            {
                "start": round(sg.start, 2),
                "end": round(sg.end, 2),
                "text": sg.text.strip(),
                "words": [
                    {
                        "start": round(w.start, 2),
                        "end": round(w.end, 2),
                        "word": w.word,
                        "prob": round(w.probability, 3),
                    }
                    for w in (sg.words or [])
                ],
            }
        )
    return out, info


def stop(out, state, why, msg=None):
    """Stop `transcribe` without a transcript, leaving at --out a record of why: `scan --transcript` reads
    it and the riffsheet says the speech recognition failed or did not run, and why. The record holds no
    segments, so nothing in it can be taken for words."""
    write_json(out, {"segments": [], "stage": {"state": state, "why": why}}, ensure_ascii=False, indent=1)
    die((msg or why) + f" (recorded in {out}: pass it to scan --transcript and the riffsheet says why)")


def cmd_transcribe(a):
    """Word-timed transcript with faster-whisper, when it is installed (the only part of riffsheet
    that needs more than the standard library and ffmpeg)."""
    video = os.path.abspath(a.video)
    check_video_path(video)
    r = run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", video]
    )
    if r.returncode != 0:
        die(f"ffprobe cannot read {video}: " + r.stderr.decode("utf-8", "ignore").strip()[-300:])
    if not r.stdout.strip():
        stop(
            a.out,
            "not_run",
            "the video has no audio track",
            "no audio stream in " + video + ": nothing to transcribe (scan works without a transcript)",
        )
    try:
        import numpy as np
        from faster_whisper import WhisperModel, download_model
    except ImportError:
        stop(
            a.out,
            "not_run",
            f"the faster-whisper package is not installed for the Python that ran transcribe ({this_python()})",
            f"transcribe needs the faster-whisper package, which is not importable by this Python "
            f"({sys.executable}). `check` says what installing it costs and prints the commands that put it "
            f"in a virtual environment of its own; then run riffsheet with that environment's Python, for this "
            f"and every other command (every command runs on any Python 3.9 or newer). Or scan without "
            f"--transcript (no spoken lines), or make the transcript elsewhere and pass it to scan --transcript. "
            'Format: JSON {"language": "en", "segments": [{"start": s, "end": s, "text": "...", "words": '
            '[{"start": s, "end": s, "word": " word", "prob": 0.97}, ...]}, ...]} (faster-whisper\'s output with '
            "word_timestamps=True; openai-whisper's 'probability' key is read too).",
        )
    # decoded here, not by faster-whisper: its own decoder depends on the PyAV version installed
    r = run(["ffmpeg", "-nostdin", "-v", "error", "-i", video, "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"])
    if r.returncode != 0:
        why = "audio decode failed: " + re.sub(r"\s+", " ", r.stderr.decode("utf-8", "ignore")[-300:]).strip()
        stop(a.out, "failed", why)
    audio = np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768.0
    if len(audio) == 0:
        stop(a.out, "failed", "the audio track decoded to no samples")
    try:  # a model name is resolved to a local folder first: a folder of that name here would be taken
        path = (
            a.model
            if os.path.isfile(os.path.join(a.model, "model.bin"))
            else download_model(a.model, local_files_only=not a.download, cache_dir=a.model_dir)
        )
    except Exception as e:  # the hub raises its own error types (no network, no such model, no cache)
        # not there is "did not run", even when fetching it was tried: "failed" is kept for a recognizer
        # that was there and stopped while running
        how = "is not on this machine, and fetching it failed" if a.download else "is not on this machine"
        stop(
            a.out,
            "not_run",
            f"the speech model ({a.model}) {how} ({type(e).__name__})",
            f"model {a.model!r} {how} ({type(e).__name__}). "
            + (
                "Check the network and run again."
                if a.download
                else "Pass --download to fetch it (network; `check` says its size), "
            )
            + ("" if a.download else "or --model-dir DIR if it sits in another cache."),
        )
    t0 = time.time()
    try:
        out, info = _recognize(WhisperModel, path, audio, a)
    except Exception as e:  # the model or its runtime failing (a damaged model file, too little memory)
        stop(a.out, "failed", f"faster-whisper stopped with {type(e).__name__}: {str(e)[:200]}")
    res = {"language": info.language, "model": f"faster-whisper {a.model} (int8, cpu)", "hint": a.hint, "segments": out}
    secs = round(time.time() - t0, 1)
    write_json(a.out, res, ensure_ascii=False, indent=1)
    nw = sum(len(sg["words"]) for sg in out)
    print(
        f"transcribe: {a.out}  model {a.model}, language {info.language}, {nw} words, {secs} s"
        + (f", hint {a.hint!r}" if a.hint else "")
    )
    for sg in out:
        print(f"  {sg['start']:6.2f}-{sg['end']:6.2f}  {sg['text']}")
    if a.compare:
        old, _ = load_words(a.compare)
        new, _ = load_words(a.out)
        A = [_norm_word(w["word"]) for w in old]
        B = [_norm_word(w["word"]) for w in new]
        diffs = []
        for i, j in _align(A, B):
            if i is not None and j is not None and A[i] == B[j]:
                continue
            t = new[j]["start"] if j is not None else old[i]["start"]
            diffs.append(
                f"{t:.2f}  {old[i]['word'] if i is not None else '-'} -> {new[j]['word'] if j is not None else '-'}"
            )
        print(
            f"  words that differ from {a.compare} ({len(diffs)}):" + ("".join("\n    " + x for x in diffs) or " none")
        )


def counts_by_character(ch):
    """A character counted one by one for pace: Han, kana and Hangul syllables."""
    o = ord(ch)
    return 0x3040 <= o <= 0x30FF or 0x3400 <= o <= 0x9FFF or 0xAC00 <= o <= 0xD7AF or 0xF900 <= o <= 0xFAFF
