#!/usr/bin/env python3
"""Fetch the latest Bloomberg Surveillance full episode's transcript + chapters.

Source: @markets (Bloomberg Television) on YouTube. Finds the newest
"Bloomberg Surveillance M/D/YYYY" episode (>60 min), downloads EN captions
and the description (which carries chapter timestamps), and writes a cleaned,
timestamped transcript.

Notes:
- Uses the android player client to dodge YouTube's datacenter-IP bot check.
- Output is for PERSONAL CONSUMPTION ONLY. Never synced to B2 or the website.
- Idempotent: skips re-download if the transcript file already exists
  (unless --force).

Usage:
    python3 surveillance_fetch.py [--force] [--out-dir DIR]
Prints: video URL, title, and transcript path for the calling worker.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

YTDLP = [str(Path.home() / ".local" / "bin" / "yt-dlp")]
if not Path(YTDLP[0]).exists():
    YTDLP = ["yt-dlp"]
BASE_ARGS = ["--extractor-args", "youtube:player_client=android",
             "--no-warnings", "--quiet"]
CHANNEL = "https://www.youtube.com/@markets/videos"

# Security: subprocess is always list-form (shell=False, never shell=True),
# so arguments cannot escape into shell interpretation. As defense-in-depth,
# every URL handed to yt-dlp must be built by watch_url() below — never raw
# external input — and must stay on YouTube's domains.
_ALLOWED_URL_PREFIXES = ("https://www.youtube.com/", "https://youtu.be/")
_VID_RE = None  # compiled lazily to keep import light


def watch_url(vid):
    """Build a validated YouTube watch URL from a video id. Refuses anything
    that is not an 11-char YouTube video id."""
    global _VID_RE
    if _VID_RE is None:
        import re as _re
        _VID_RE = _re.compile(r"^[A-Za-z0-9_-]{11}$")
    if not _VID_RE.match(vid or ""):
        raise ValueError(f"refusing malformed video id: {vid!r}")
    url = f"https://www.youtube.com/watch?v={vid}"
    if not url.startswith(_ALLOWED_URL_PREFIXES):
        raise ValueError(f"refusing non-YouTube URL: {url[:80]}")
    return url


def run(*args, check=True):
    p = subprocess.run(YTDLP + BASE_ARGS + list(args),
                       capture_output=True, text=True, timeout=300)
    if check and p.returncode != 0:
        raise RuntimeError(f"yt-dlp failed: {p.stderr.strip()[:300]}")
    return p


def find_latest_episode():
    p = run("--flat-playlist",
            "--print", "%(id)s\t%(title)s\t%(duration)s",
            "--playlist-end", "20", CHANNEL)
    best = None
    for line in p.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        vid, title, dur = parts
        try:
            dur_s = float(dur)
        except ValueError:
            continue
        if re.search(r"Bloomberg Surveillance \d{1,2}/\d{1,2}/\d{4}", title) \
                and dur_s > 3600:
            m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{4})", title)
            aired = f"{m.group(3)}-{int(m.group(1)):02d}-{int(m.group(2)):02d}"
            if best is None or aired > best[0]:
                best = (aired, vid, title)
    return best  # (aired_date, video_id, title)


def download_subs(vid, tmpdir):
    # prefer manual subs, fall back to auto
    p = run("--write-subs", "--write-auto-subs", "--sub-langs", "en",
            "--sub-format", "vtt", "--skip-download",
            "-o", str(tmpdir / "%(id)s.%(ext)s"),
            watch_url(vid), check=False)
    vtts = sorted(tmpdir.glob(f"{vid}*.vtt"))
    # manual subs land as .en.vtt, auto as .en.vtt too; pick non-auto first
    for v in vtts:
        if ".en.vtt" in v.name:
            return v
    return vtts[0] if vtts else None


def get_description(vid):
    p = run("--print", "%(description)s", "--skip-download",
            watch_url(vid))
    return p.stdout


def parse_vtt(path):
    cues = []
    for block in path.read_text(encoding="utf-8", errors="replace").split("\n\n"):
        m = re.match(r"(\d{2}):(\d{2}):(\d{2})\.(\d{3}) -->", block)
        if not m:
            continue
        h, mi, s, _ = map(int, m.groups())
        text = re.sub(r"<[^>]+>", "", block.split("\n", 1)[1] if "\n" in block else "")
        text = re.sub(r"\s+", " ", text).strip()
        # drop cue-position junk and music-only cues
        if not text or re.fullmatch(r"\[Music\]", text):
            continue
        cues.append((h * 3600 + mi * 60 + s, text))
    return cues


def dedupe_words(cues):
    """Rolling-window auto captions repeat words; keep only new words."""
    out_words, out = [], []
    for t, text in cues:
        words = text.split()
        # longest suffix of out_words matching a prefix of words
        maxk = min(len(out_words), len(words))
        k = maxk
        while k > 0 and out_words[-k:] != words[:k]:
            k -= 1
        new = words[k:]
        if new:
            out.append((t, new))
            out_words.extend(new)
    return out


def fmt_ts(sec):
    return f"{sec // 3600:02d}:{(sec % 3600) // 60:02d}:{sec % 60:02d}"


def parse_chapters(description):
    chapters = []
    for line in description.splitlines():
        m = re.match(r"\s*(\d{1,2}:\d{2}(?::\d{2})?)\s+(.+)", line.strip())
        if m and len(m.group(2)) > 8:
            chapters.append((m.group(1), m.group(2).strip()))
    # drop the Chapters: header line if captured
    return [(t, c) for t, c in chapters if not c.lower().startswith("chapters")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--out-dir", default=str(Path.home() / "workspace" / "briefs" / "us"))
    a = ap.parse_args()
    outdir = Path(a.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    found = find_latest_episode()
    if not found:
        print("no Surveillance episode found", file=sys.stderr)
        sys.exit(1)
    aired, vid, title = found
    url = watch_url(vid)
    tpath = outdir / f"surveillance-{aired}.transcript.md"
    if tpath.exists() and not a.force:
        print(f"exists: {tpath}")
        print(f"url: {url}\ntitle: {title}")
        return

    tmpdir = outdir / ".tmp-subs"
    tmpdir.mkdir(exist_ok=True)
    vtt = download_subs(vid, tmpdir)
    desc = get_description(vid)
    chapters = parse_chapters(desc)
    cues = parse_vtt(vtt) if vtt else []
    for f in tmpdir.glob(f"{vid}*"):
        f.unlink()

    lines = [f"# {title}", f"URL: {url}", f"Aired: {aired}",
             f"Fetched: {datetime.now(timezone.utc).isoformat()}",
             "", "## Chapters (from video description)", ""]
    for t, c in chapters:
        lines.append(f"- [{t}] {c}")
    lines += ["", "## Transcript (cleaned, timestamps every ~45s)", ""]
    if cues:
        segs = dedupe_words(cues)
        last_mark = -10**9
        buf = []
        for t, words in segs:
            if t - last_mark >= 45 and buf:
                lines.append(f"[{fmt_ts(last_mark)}] " + " ".join(buf))
                buf, last_mark = [], t
            elif not buf:
                last_mark = t
            buf.extend(words)
        if buf:
            lines.append(f"[{fmt_ts(last_mark)}] " + " ".join(buf))
    else:
        lines.append("_No captions available for this episode._")
    tpath.write_text("\n".join(lines) + "\n")
    print(f"wrote: {tpath}")
    print(f"url: {url}\ntitle: {title}\nchapters: {len(chapters)}")


if __name__ == "__main__":
    main()
