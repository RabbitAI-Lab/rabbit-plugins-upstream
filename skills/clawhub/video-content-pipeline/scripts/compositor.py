#!/usr/bin/env python3
"""Saml billeder + voiceover → MP4 (ffmpeg)."""
import json, os, subprocess, sys

def main():
    if len(sys.argv) < 6:
        print("Brug: compositor.py scenes.json images/ audio/ out.mp4 [vertikal]"); sys.exit(1)
    scenes, img_dir, aud_dir, out = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    vertical = len(sys.argv) > 5 and sys.argv[5] == "vertikal"
    scenes = json.load(open(scenes))
    parts = []
    for sc in scenes:
        img = os.path.join(img_dir, f"scene_{sc['id']:02d}.png")
        aud = os.path.join(aud_dir, f"scene_{sc['id']:02d}.mp3")
        if not (os.path.exists(img) and os.path.exists(aud)):
            print(f"⚠️ mangler scene {sc['id']}"); continue
        part = f"/tmp/scene_{sc['id']:02d}.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-loop", "1", "-i", img, "-i", aud,
            "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac",
            "-shortest", "-pix_fmt", "yuv420p", part
        ], capture_output=True)
        parts.append(part)
    if not parts:
        print("Ingen scener at samle."); sys.exit(1)
    concat_file = "/tmp/concat.txt"
    open(concat_file, "w").write("".join(f"file '{p}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_file,
                    "-c", "copy", out], capture_output=True)
    print(f"✅ Video: {out}")

if __name__ == "__main__":
    main()
