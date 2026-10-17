#!/usr/bin/env python3
"""Compose the bilingual single talking-head video.

Takes the English and Arabic talking-head clips plus their text, then:
  1. Builds proportional .srt subtitles from each text file (timing by audio duration).
  2. Burns subtitles into each clip.
  3. Adds a labeled title card (English / العربية) before each segment.
  4. Concatenates everything into one MP4.

Requires ffmpeg + ffprobe on PATH (or pass --ffmpeg). For best Arabic glyph
rendering, pass --fontfile pointing to an Arabic-capable TTF (e.g. Noto Naskh Arabic).

Usage:
  python compose_bilingual.py \
    --en en_talk.mp4 --ar ar_talk.mp4 \
    --en-text en.txt --ar-text ar.txt \
    --en-label "English" --ar-label "العربية" \
    --out bilingual_final.mp4
"""
import argparse
import os
import shutil
import subprocess
import sys


def find_ffmpeg(explicit=None):
    if explicit:
        return explicit
    found = shutil.which("ffmpeg")
    if not found:
        candidate = os.path.join(
            os.environ.get("LOCALAPPDATA", ""), "PASMStudio", "bin", "ffmpeg.exe"
        )
        if os.path.exists(candidate):
            return candidate
        sys.exit("ffmpeg not found. Install ffmpeg on PATH or pass --ffmpeg.")
    return found


def probe_duration(path: str, ffmpeg: str) -> float:
    ffprobe = shutil.which("ffprobe") or os.path.join(
        os.path.dirname(ffmpeg), "ffprobe"
    )
    out = subprocess.check_output(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            path,
        ],
        stderr=subprocess.DEVNULL,
    )
    return float(out.strip())


def build_srt(text_path: str, duration: float, srt_path: str):
    with open(text_path, encoding="utf-8") as f:
        lines = [ln.strip() for ln in f.read().splitlines() if ln.strip()]
    if not lines:
        lines = [""]
    total_chars = sum(len(ln) for ln in lines) or 1
    # Small tail padding so the last subtitle does not cut off early.
    usable = duration * 0.97
    cursor = 0.0
    entries = []
    for i, ln in enumerate(lines):
        share = (len(ln) / total_chars) * usable
        start = cursor
        end = cursor + share if i < len(lines) - 1 else duration
        entries.append((i + 1, start, end, ln))
        cursor += share

    def fmt(t: float) -> str:
        ms = int(round(t * 1000))
        h, ms = divmod(ms, 3600_000)
        m, ms = divmod(ms, 60_000)
        s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    with open(srt_path, "w", encoding="utf-8") as f:
        for idx, start, end, txt in entries:
            f.write(f"{idx}\n{fmt(start)} --> {fmt(end)}\n{txt}\n\n")
    print(f"[compose] wrote {srt_path} ({len(entries)} cues)")


def run(cmd):
    print("[cmd]", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description="Compose bilingual talking-head video")
    ap.add_argument("--en", required=True, help="English talking-head clip (.mp4)")
    ap.add_argument("--ar", required=True, help="Arabic talking-head clip (.mp4)")
    ap.add_argument("--en-text", required=True, help="English transcript (.txt)")
    ap.add_argument("--ar-text", required=True, help="Arabic transcript (.txt)")
    ap.add_argument("--en-label", default="English")
    ap.add_argument("--ar-label", default="العربية")
    ap.add_argument("--out", required=True, help="Output MP4")
    ap.add_argument("--ffmpeg", default=None)
    ap.add_argument("--fontfile", default=None, help="TTF for Arabic-capable rendering")
    ap.add_argument("--card-dur", type=float, default=2.0, help="Title card seconds")
    ap.add_argument("--resolution", default="1280x720")
    args = ap.parse_args()

    ffmpeg = find_ffmpeg(args.ffmpeg)
    w, h = args.resolution.split("x")
    work = os.path.dirname(os.path.abspath(args.out))
    os.makedirs(work, exist_ok=True)

    en_dur = probe_duration(args.en, ffmpeg)
    ar_dur = probe_duration(args.ar, ffmpeg)

    en_srt = os.path.join(work, "en.srt")
    ar_srt = os.path.join(work, "ar.srt")
    build_srt(args.en_text, en_dur, en_srt)
    build_srt(args.ar_text, ar_dur, ar_srt)

    # Subtitle style; inject a fontfile when provided.
    sub_style = "FontSize=28,Alignment=2,Bold=1,Outline=2,Shadow=1"
    if args.fontfile:
        sub_style += f",FontFile={args.fontfile}"
    en_sub = os.path.join(work, "en_sub.mp4")
    ar_sub = os.path.join(work, "ar_sub.mp4")
    run(
        [
            ffmpeg, "-y", "-i", args.en,
            "-vf", f"subtitles={en_srt}:force_style='{sub_style}'",
            "-c:v", "libx264", "-c:a", "aac", "-movflags", "+faststart", en_sub,
        ]
    )
    run(
        [
            ffmpeg, "-y", "-i", args.ar,
            "-vf", f"subtitles={ar_srt}:force_style='{sub_style}'",
            "-c:v", "libx264", "-c:a", "aac", "-movflags", "+faststart", ar_sub,
        ]
    )

    # Title cards with silent audio (so concat has audio on every input).
    dt = _drawtext(args.en_label, args.fontfile)
    title_en = os.path.join(work, "title_en.mp4")
    run(
        [
            ffmpeg, "-y",
            "-f", "lavfi", "-i", f"color=c=0x101830:s={args.resolution}:d={args.card_dur}",
            "-f", "lavfi", "-i", f"anullsrc=r=44100:cl=stereo:d={args.card_dur}",
            "-vf", dt,
            "-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p", "-shortest", title_en,
        ]
    )
    dt = _drawtext(args.ar_label, args.fontfile)
    title_ar = os.path.join(work, "title_ar.mp4")
    run(
        [
            ffmpeg, "-y",
            "-f", "lavfi", "-i", f"color=c=0x101830:s={args.resolution}:d={args.card_dur}",
            "-f", "lavfi", "-i", f"anullsrc=r=44100:cl=stereo:d={args.card_dur}",
            "-vf", dt,
            "-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p", "-shortest", title_ar,
        ]
    )

    # Normalize resolution then concat (handles mismatched clip sizes).
    scale = (
        f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
        f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,setsar=1"
    )
    run(
        [
            ffmpeg, "-y",
            "-i", title_en, "-i", en_sub, "-i", title_ar, "-i", ar_sub,
            "-filter_complex",
            f"[0:v]{scale}[0v];[1:v]{scale}[1v];[2:v]{scale}[2v];[3:v]{scale}[3v];"
            f"[0v][0:a][1v][1:a][2v][2:a][3v][3:a]concat=n=4:v=1:a=1[outv][outa]",
            "-map", "[outv]", "-map", "[outa]",
            "-c:v", "libx264", "-c:a", "aac", "-movflags", "+faststart",
            "-pix_fmt", "yuv420p", args.out,
        ]
    )
    total = args.card_dur * 2 + en_dur + ar_dur
    print(f"[compose] done -> {args.out} (total ~{total:.1f}s)")


def _drawtext(label: str, fontfile: str) -> str:
    font_part = f"fontfile='{fontfile}'" if fontfile else "font='Arial'"
    return (
        f"drawtext=text='{label}':{font_part}:fontcolor=white:fontsize=72:"
        f"x=(w-text_w)/2:y=(h-text_h)/2"
    )


if __name__ == "__main__":
    main()
