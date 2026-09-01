#!/usr/bin/env python3
"""Extract the cover and one representative frame per spoken segment."""

import argparse
import json
import re
import subprocess
from pathlib import Path


def safe_name(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", value).strip("-") or "segment"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("script", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    data = json.loads(args.script.read_text(encoding="utf-8"))
    fps = float(data["composition"]["fps"])
    scene_offsets: dict[str, int] = {}
    cursor = 0
    for scene in data.get("scenes", []):
        scene_offsets[scene["id"]] = cursor
        cursor += int(scene["durationInFrames"])

    frames: list[tuple[str, float]] = [("00-cover", 0.5)]
    for index, item in enumerate(data.get("narration", []), start=1):
        scene = item.get("scene")
        if scene not in scene_offsets:
            raise SystemExit(f"{item.get('id')}: unknown scene {scene}")
        midpoint = (
            scene_offsets[scene]
            + int(item["from"])
            + int(item["durationInFrames"]) / 2
        ) / fps
        label = (
            f"{index:02d}-{safe_name(str(item.get('id', index)))}-"
            f"{safe_name(str(item.get('speaker', 'unknown')))}"
        )
        frames.append((label, midpoint))

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for label, timestamp in frames:
        output = args.output_dir / f"{label}.png"
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-ss",
                f"{timestamp:.3f}",
                "-i",
                str(args.video),
                "-frames:v",
                "1",
                str(output),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        print(f"{label}: {timestamp:.3f}s -> {output}")

    print(f"extracted {len(frames)} review frames")


if __name__ == "__main__":
    main()
