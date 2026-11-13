#!/usr/bin/env python3
"""Extract clean plain-text transcripts from YouTube videos using yt-dlp."""

import argparse
from html import unescape
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def download_subs(url: str, lang: str = "en") -> str:
    """Download auto-generated subtitles and return the VTT content."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "sub"
        subprocess.run(
            [
                "yt-dlp",
                "--write-auto-sub",
                "--write-sub",
                "--skip-download",
                "--sub-lang", lang,
                "-o", str(out),
                url,
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        # prefer manual subs over auto-generated
        for suffix in [f".{lang}.vtt", f".{lang}.vtt"]:
            vtt = Path(f"{out}{suffix}")
            if vtt.exists():
                return vtt.read_text(encoding="utf-8")

        # fallback: grab whatever vtt file was written
        vtts = list(Path(tmp).glob("*.vtt"))
        if vtts:
            return vtts[0].read_text(encoding="utf-8")

        raise FileNotFoundError("No subtitles found. Try --list-subs on the video.")


def parse_vtt(vtt_text: str) -> str:
    """Parse VTT content into clean deduplicated plain text."""
    lines: list[str] = []
    prev = ""

    for line in vtt_text.splitlines():
        # skip VTT header, metadata, timestamps, blank lines
        if re.match(r"^(WEBVTT|Kind:|Language:|\s*$)", line):
            continue
        if "-->" in line:
            continue

        # strip HTML-style tags (<c>, <b>, etc.) and formatting
        clean = re.sub(r"<[^>]+>", "", line)
        # decode HTML entities (&gt; &amp; &lt; etc.)
        clean = unescape(clean)
        # normalize whitespace
        clean = re.sub(r"\s+", " ", clean).strip()

        if not clean or clean == prev:
            continue

        # handle overlapping cues: skip if current line is a suffix of prev
        # or prev is a suffix of current (common in auto-subs)
        if prev and (prev.endswith(clean) or clean.startswith(prev)):
            # replace prev with the longer version
            if clean.startswith(prev) and clean != prev:
                lines[-1] = clean
                prev = clean
            continue

        lines.append(clean)
        prev = clean

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extract YouTube transcript as plain text")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-l", "--lang", default="en", help="Subtitle language code (default: en)")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    args = parser.parse_args()

    try:
        vtt = download_subs(args.url, args.lang)
    except subprocess.CalledProcessError as e:
        print(f"yt-dlp error: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    transcript = parse_vtt(vtt)

    if args.output:
        Path(args.output).write_text(transcript, encoding="utf-8")
        print(f"Saved to {args.output}", file=sys.stderr)
    else:
        print(transcript)


if __name__ == "__main__":
    main()
