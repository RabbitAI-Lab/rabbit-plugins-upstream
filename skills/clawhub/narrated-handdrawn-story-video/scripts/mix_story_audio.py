#!/usr/bin/env python3
"""Mux a silent story video with poster-delayed narration and ducked BGM."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=Path, required=True)
    parser.add_argument("--voice", type=Path, required=True)
    parser.add_argument("--bgm", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--poster-seconds", type=float, default=3.0)
    parser.add_argument("--bgm-volume", type=float, default=0.20)
    args = parser.parse_args()

    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg is required")
    for source in (args.video, args.voice, args.bgm):
        if not source.is_file():
            raise SystemExit(f"Missing input: {source}")
    if args.poster_seconds < 0 or args.bgm_volume <= 0:
        raise SystemExit("poster-seconds must be >= 0 and bgm-volume must be > 0")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    delay_ms = round(args.poster_seconds * 1000)
    graph = (
        f"[1:a]adelay={delay_ms}|{delay_ms},volume=1.35,asplit=2[voice_sc][voice_mix];"
        f"[2:a]volume={args.bgm_volume}[bgm];"
        "[bgm][voice_sc]sidechaincompress=threshold=0.025:ratio=12:attack=20:release=550[ducked];"
        "[ducked][voice_mix]amix=inputs=2:duration=first:normalize=0[audio]"
    )
    command = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(args.video), "-i", str(args.voice), "-i", str(args.bgm),
        "-filter_complex", graph, "-map", "0:v:0", "-map", "[audio]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
        "-shortest", str(args.output),
    ]
    subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
