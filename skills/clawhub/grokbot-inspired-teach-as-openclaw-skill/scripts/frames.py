#!/usr/bin/env python3
"""Frame extractor / splitter for the OpenClaw `teach` skill.

Two modes:

  --check   Extract one frame at ~20% and one at ~70% of the duration and
            report their paths + duration. Used to sanity-check the capture
            before full transcription. A crude brightness-variance heuristic is
            printed when Pillow is available (to flag likely-blank frames).

  default   Extract evenly spaced frames (3..20 depending on length). If the
            video exceeds --max-mb (default 12), split it losslessly with ffmpeg
            so each part stays under attachment limits, and print part paths.

All intermediate files go to a temp dir; the calling agent views them and then
the teach skill deletes the recording.

Usage:
    python3 frames.py <video.mp4> [--check] [--max-mb N]
"""
import sys
import os
import json
import math
import tempfile
import subprocess


def probe_duration(video: str):
    try:
        return float(
            subprocess.check_output(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "csv=p=0", video],
                stderr=subprocess.DEVNULL,
            ).decode().strip()
        )
    except Exception:
        return None


def extract_frame(video: str, t: float, out_png: str) -> None:
    subprocess.run(
        ["ffmpeg", "-y", "-ss", str(t), "-i", video, "-frames:v", "1", out_png],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def variance_heuristic(path: str):
    try:
        from PIL import Image, ImageStat
        im = Image.open(path).convert("L")
        return round(ImageStat.Stat(im).var[0], 1)
    except Exception:
        return None


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit("usage: frames.py <video.mp4> [--check] [--max-mb N]")
    video = args[0]
    check = "--check" in args
    max_mb = 12.0
    for i, a in enumerate(args):
        if a == "--max-mb" and i + 1 < len(args):
            try:
                max_mb = float(args[i + 1])
            except ValueError:
                pass

    dur = probe_duration(video)
    tmp = tempfile.mkdtemp(prefix="teach_frames_")

    if check:
        if dur:
            print(f"DURATION {dur}")
            fa = os.path.join(tmp, "frame_a.png")
            fb = os.path.join(tmp, "frame_b.png")
            extract_frame(video, dur * 0.2, fa)
            extract_frame(video, dur * 0.7, fb)
            print(f"FRAME_A {fa}")
            print(f"FRAME_B {fb}")
            for label, p in (("FRAME_A", fa), ("FRAME_B", fb)):
                v = variance_heuristic(p)
                if v is not None:
                    print(f"{label}_VARIANCE {v}")
        else:
            print("DURATION unknown")
        return

    size = os.path.getsize(video)
    if size > max_mb * 1024 * 1024 and dur:
        parts = math.ceil(size / (max_mb * 1024 * 1024))
        seg = max(0.1, dur / parts)
        pattern = os.path.join(tmp, "demo_part_%03d.mp4")
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", video, "-c", "copy", "-map", "0",
             "-f", "segment", "-segment_time", str(seg), "-reset_timestamps", "1", pattern],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        for p in sorted(os.listdir(tmp)):
            if p.endswith(".mp4"):
                print(f"PART {os.path.join(tmp, p)}")
        if dur:
            print(f"DURATION {dur}")
        return

    n = max(3, min(20, int((dur or 30) // 20) + 1)) if dur else 6
    for i in range(n):
        t = (dur * (i + 0.5) / n) if dur else i * 2
        fp = os.path.join(tmp, f"frame_{i:02d}.png")
        extract_frame(video, t, fp)
        print(f"FRAME {fp}")
    if dur:
        print(f"DURATION {dur}")


if __name__ == "__main__":
    main()
