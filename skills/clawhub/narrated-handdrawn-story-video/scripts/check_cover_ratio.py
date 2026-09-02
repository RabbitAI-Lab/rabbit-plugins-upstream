#!/usr/bin/env python3
"""Check that an opening poster and video canvas share the same aspect ratio."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def image_size(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=width,height", "-of", "json", str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    stream = json.loads(result.stdout)["streams"][0]
    return int(stream["width"]), int(stream["height"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--poster", type=Path, required=True)
    parser.add_argument("--storyboard", type=Path, required=True)
    args = parser.parse_args()

    project = json.loads(args.storyboard.read_text(encoding="utf-8"))["project"]
    video_width = int(project["width"])
    video_height = int(project["height"])
    poster_width, poster_height = image_size(args.poster)
    poster_ratio = poster_width / poster_height
    video_ratio = video_width / video_height
    if abs(poster_ratio - video_ratio) > 0.001:
        raise SystemExit(
            f"Aspect ratio mismatch: poster {poster_width}x{poster_height} "
            f"({poster_ratio:.6f}) vs video {video_width}x{video_height} "
            f"({video_ratio:.6f})"
        )
    print(
        f"OK: poster {poster_width}x{poster_height} matches video "
        f"{video_width}x{video_height} ({video_ratio:.6f})"
    )


if __name__ == "__main__":
    main()
