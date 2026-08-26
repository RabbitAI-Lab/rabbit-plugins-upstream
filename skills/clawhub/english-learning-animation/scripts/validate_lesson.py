#!/usr/bin/env python3
"""Validate the publish-critical fields of an English-learning animation manifest."""
import argparse
import json
import re
import subprocess
from pathlib import Path


def duration(path: Path) -> float:
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)], capture_output=True, text=True, check=True)
    return float(result.stdout.strip())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    errors = []
    cover = data.get("cover", {})
    if not cover.get("title") or re.search(r"[\u4e00-\u9fff]", cover.get("title", "")):
        errors.append("cover title must be English-only")
    if not 2 <= cover.get("seconds", 0) <= 3:
        errors.append("cover must last 2–3 seconds")
    speakers = set()
    profiles = {}
    files = set()
    segments = data.get("segments", [])
    for item in segments:
        speaker = str(item.get("speaker", "")).strip().lower()
        if not re.fullmatch(r"[a-z][a-z0-9_-]*", speaker):
            errors.append(f"{item.get('file')}: invalid stable speaker role id")
        if speaker:
            speakers.add(speaker)
        filename = item.get("file")
        if not filename:
            errors.append("segment is missing file")
            continue
        if filename in files:
            errors.append(f"{filename}: duplicate output file")
        files.add(filename)
        if re.search(r"[\u3400-\u9fff]", str(item.get("text", ""))):
            errors.append(f"{filename}: spoken lesson text must be English-only")
        instruction = item.get("voice_instruction") or " ".join(
            part.strip()
            for part in (
                item.get("voice_profile", ""),
                item.get("performance", ""),
            )
            if part.strip()
        )
        if len(instruction.split()) < 8:
            errors.append(f"{filename}: voice direction is too vague")
        profile = str(item.get("voice_profile", "")).strip()
        if profile:
            if speaker in profiles and profiles[speaker] != profile:
                errors.append(
                    f"{filename}: voice_profile changed within speaker role {speaker}"
                )
            profiles[speaker] = profile
            if not str(item.get("performance", "")).strip():
                errors.append(f"{filename}: missing line-specific performance direction")
        output_dir = Path(data["output_dir"])
        if not output_dir.is_absolute():
            output_dir = args.manifest.resolve().parent / output_dir
        audio = output_dir / item["file"]
        if audio.exists() and duration(audio) <= 0:
            errors.append(f"{audio}: invalid duration")
    if len(segments) < 3:
        errors.append("lesson needs at least three spoken segments")
    if len(speakers - {"narrator"}) < 2:
        errors.append("lesson needs at least two distinct character roles")
    if errors:
        raise SystemExit("\n".join(errors))
    print("lesson manifest is valid")


if __name__ == "__main__":
    main()
