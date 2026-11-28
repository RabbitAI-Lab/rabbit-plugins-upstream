"""The scan folder: loading it, frame lookups, followup records, box arguments."""

import bisect
import contextlib
import os
import re
import shutil
import tempfile
import time

from .media import run_timeout_for, set_timeout
from .transcript import join_words, words_at
from .util import die, read_json, write_json


# ----------------------------------------------------------------------------- shared state
def load_dir(d):
    p = os.path.join(d, "index.json")
    if not os.path.exists(p):
        die(f"{p} not found; run `scan` first")
    idx = read_json(p, "scan index")
    fr = read_json(os.path.join(d, "frames.json"), "scan frame list")
    words = idx.get("_words", [])
    if not os.path.exists(idx.get("video", "")):
        die(f"the video this scan was made from is no longer at {idx.get('video')}; scan it again")
    set_timeout(run_timeout_for(idx["facts"].get("duration_video_s", 0)))
    return idx, fr["pts"], words


def nearest_frame(pts, t):
    k = bisect.bisect_left(pts, t)
    cands = [c for c in (k - 1, k) if 0 <= c < len(pts)]
    return min(cands, key=lambda c: abs(pts[c] - t))


def frames_between(pts, a, b):
    return [i for i, t in enumerate(pts) if a - 1e-6 <= t <= b + 1e-6]


# Agents often run several follow-up commands at once on one scan folder. Each command works in a
# scratch folder of its own, and adds its record to index.json under a lock.
LOCK_STALE_S = 60  # a lock file older than this was left by a command that was stopped
_scratch = []


SCRATCH_STALE_S = 24 * 3600  # a scratch folder this old was left by a command that was killed
_SCRATCH_NAME = re.compile(r"\.tmp_[a-z]+-[A-Za-z0-9_]+")  # as tempfile.mkdtemp names them below


def remove_stale_scratch(d):
    """Remove the scratch folders in d that commands left more than a day ago. A command stopped
    outright (killed, not interrupted) cannot remove its own; one still running beside this one is far
    younger than a day, so it keeps its folder."""
    now = time.time()
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name)
        try:
            if _SCRATCH_NAME.fullmatch(name) and os.path.isdir(p) and now - os.path.getmtime(p) > SCRATCH_STALE_S:
                shutil.rmtree(p, ignore_errors=True)
        except OSError:
            continue  # removed by another command meanwhile


def scratch_dir(d, what):
    """A new, empty scratch folder of this command's own inside d (stale ones are removed first).
    main() removes it when the command ends, also when it stops on an error."""
    remove_stale_scratch(d)
    tmp = tempfile.mkdtemp(prefix=f".tmp_{what}-", dir=d)
    _scratch.append(tmp)
    return tmp


def remove_scratch():
    while _scratch:
        shutil.rmtree(_scratch.pop(), ignore_errors=True)


@contextlib.contextmanager
def locked(path):
    """Hold the lock file `path` (made with O_EXCL, so only one process holds it) while the block runs."""
    while True:
        try:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError:
            try:
                if time.time() - os.path.getmtime(path) > LOCK_STALE_S:
                    os.remove(path)
                    continue
            except OSError:
                continue  # released while we looked
            time.sleep(0.02)
    try:
        yield
    finally:
        os.close(fd)
        with contextlib.suppress(OSError):
            os.remove(path)


def record_followup(d, entry):
    """Add a command's record to index.json: read, add and write under a lock, so records added at the
    same time are all kept, and the new file replaces the old in one step, so a reader never sees half."""
    p = os.path.join(d, "index.json")
    with locked(p + ".lock"):
        idx = read_json(p, "scan index")
        idx.setdefault("followups", []).append(entry)
        tmp = f"{p}.{os.getpid()}.tmp"
        write_json(tmp, idx, indent=1, ensure_ascii=False)
        os.replace(tmp, p)


def parse_box(s):
    try:
        b = [float(x) for x in s.split(",")]
    except ValueError:
        b = []
    if not (len(b) == 4 and 0 <= b[0] < b[2] <= 1 and 0 <= b[1] < b[3] <= 1):
        die("--box must be x0,y0,x1,y1 as fractions with x0<x1, y0<y1 (e.g. 0.05,0.6,0.95,0.72)")
    return b


def label_word(words, t):
    w = words_at(words, t)
    return ("“" + join_words(w) + "”") if w else "·"
