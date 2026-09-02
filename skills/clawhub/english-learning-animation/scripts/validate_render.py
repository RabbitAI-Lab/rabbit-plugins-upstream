#!/usr/bin/env python3
"""Validate the final video stream and extract a cover frame for visual review."""
import argparse
import json
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("--cover-frame", type=Path, required=True)
    args = parser.parse_args()
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,codec_name,width,height", "-of", "json", str(args.video)], capture_output=True, text=True, check=True)
    info = json.loads(probe.stdout)
    streams = info.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    audio = next((s for s in streams if s.get("codec_type") == "audio"), None)
    if not video or not audio:
        raise SystemExit("final render must contain both video and audio")
    if int(video.get("width", 0)) < 720 or int(video.get("height", 0)) < 405:
        raise SystemExit("render is too small for publishing")
    args.cover_frame.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-ss", "0.5", "-i", str(args.video), "-frames:v", "1", str(args.cover_frame)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"render valid; review cover frame: {args.cover_frame}")


if __name__ == "__main__":
    main()
