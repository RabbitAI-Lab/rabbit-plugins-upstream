"""Small helpers: one-line errors, JSON and text files, time and color formatting, box arithmetic."""

import functools
import json
import os
import re
import shlex
import sys

# how printed commands call this tool: with the Python running it now (a virtual environment's Python
# stays the one used) and the entry script the user ran (scripts/riffsheet.py, next to this package),
# both quoted so a pasted command survives spaces in the path (bash and zsh)
CMD = (
    shlex.quote(sys.executable or "python3")
    + " -I "
    + shlex.quote(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "riffsheet.py"))
)


def set_entry(path):
    """Name the entry script in printed commands (cli.main is given it by scripts/riffsheet.py)."""
    global CMD
    CMD = shlex.quote(sys.executable or "python3") + " -I " + shlex.quote(path)


# ----------------------------------------------------------------------------- basics
def die(msg, code=1):
    """Stop with one line on stderr and a non-zero status. ffmpeg's own error text can span lines;
    it is folded onto the one line so a caller reading the last line of stderr gets all of it."""
    sys.stderr.write("riffsheet: " + re.sub(r"\s*\n\s*", " | ", str(msg).strip()) + "\n")
    raise SystemExit(code)


def this_python():
    """The Python running the tool, as a record names it: its version, not its path (a path in a home
    folder names the person)."""
    return "Python " + ".".join(map(str, sys.version_info[:3]))


def private(text):
    """`text` with this person's home folder written as ~, for files meant to be shared (riffsheet.json and
    riffsheet.md): a path can reach them in a stage's reason, an error message or the agent's own words."""
    home = os.path.expanduser("~").rstrip(os.sep)
    for h in sorted({home, os.path.realpath(home)}, key=len, reverse=True):
        if len(h) > 1:
            text = re.sub(re.escape(h) + r"(?![\w.-])", "~", text)
    return text


def private_doc(x):
    """A JSON document with private() applied to every string in it, keys included."""
    if isinstance(x, dict):
        return {private(k): private_doc(v) for k, v in x.items()}
    if isinstance(x, list):
        return [private_doc(v) for v in x]
    return private(x) if isinstance(x, str) else x


def warn(msg):
    sys.stderr.write("riffsheet: warning: " + msg + "\n")


def fmt_t(t):
    return f"{t:.3f}"


# Text files are read and written as UTF-8 whatever the locale: paths and transcripts may hold any
# script, and a C locale would otherwise refuse them.
def read_json(path, what="file"):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        die(f"{what} not found: {path}")
    except ValueError as e:
        die(f"{what} is not valid JSON: {path} ({e})")


def write_json(path, obj, **kw):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, **kw)


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def _hex(c):
    return "#%02X%02X%02X" % tuple(int(round(v)) for v in c)


def _rgb(h):
    return [int(h[i : i + 2], 16) for i in (1, 3, 5)]


def weighted_median(xs):
    """The value at half the total weight of sorted (value, weight) pairs."""
    half, acc = sum(w for _, w in xs) / 2, 0
    for v, w in xs:
        acc += w
        if acc >= half:
            return v


if hasattr(int, "bit_count"):  # Python 3.10+

    def _pc(x):
        """Set bits of a non-negative int (masks here hold one 0/1 byte per pixel)."""
        return x.bit_count()
else:  # Python 3.9

    def _pc(x):
        """Set bits of a non-negative int (masks here hold one 0/1 byte per pixel)."""
        return bin(x).count("1")


def _overlap(a, b):
    """Intersection over the smaller box."""
    ix = max(0.0, min(a[2], b[2]) - max(a[0], b[0]))
    iy = max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
    sa = (a[2] - a[0]) * (a[3] - a[1])
    sb = (b[2] - b[0]) * (b[3] - b[1])
    return ix * iy / max(1e-9, min(sa, sb))


def _box_px(box, W, H):
    cx, cy = even(int(box[0] * W)), even(int(box[1] * H))
    cw = min(W - cx, max(2, even(int((box[2] - box[0]) * W))))
    ch = min(H - cy, max(2, even(int((box[3] - box[1]) * H))))
    return cx, cy, cw, ch


def even(x):
    """x rounded down to an even number (frame sizes and crops for yuv420 video are even)."""
    return x // 2 * 2


@functools.cache
def above(t):
    """A bytes.translate table: 1 for byte values above t, 0 for the rest (a mask from a difference)."""
    return bytes(1 if v > t else 0 for v in range(256))


@functools.cache
def at_most(t):
    """A bytes.translate table: 1 for byte values of t or less, 0 for the rest."""
    return bytes(1 if v <= t else 0 for v in range(256))


def mmss(t):
    """t as mm:ss.s, rounded to the tenth before it is split, so 59.97 s is 01:00.0 (not 00:60.0)."""
    t = round(max(0.0, t), 1)
    m = int(t // 60)
    return f"{m:02d}:{t - 60 * m:04.1f}"
