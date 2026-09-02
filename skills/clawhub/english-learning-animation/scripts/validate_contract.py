#!/usr/bin/env python3
"""Validate that the voice manifest and Remotion timeline describe the same lesson."""

import argparse
import json
from pathlib import Path, PurePosixPath


def normalized_output(output_dir: str, filename: str) -> str:
    directory = PurePosixPath(output_dir.replace("\\", "/"))
    if directory.is_absolute() or ".." in directory.parts:
        raise ValueError("output_dir must be a safe project-relative path")
    if directory.parts and directory.parts[0] == "public":
        directory = PurePosixPath(*directory.parts[1:])
    return str(directory / filename)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("timeline", type=Path)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    timeline = json.loads(args.timeline.read_text(encoding="utf-8"))
    errors: list[str] = []

    try:
        manifest_rows = {
            normalized_output(manifest["output_dir"], str(item["file"])): item
            for item in manifest.get("segments", [])
        }
    except (KeyError, ValueError) as exc:
        raise SystemExit(f"invalid voice manifest output path: {exc}") from exc

    timeline_rows = {
        str(PurePosixPath(str(item["output"]).replace("\\", "/"))): item
        for item in timeline.get("narration", [])
        if item.get("output")
    }
    manifest_outputs = set(manifest_rows)
    timeline_outputs = set(timeline_rows)

    for output in sorted(timeline_outputs - manifest_outputs):
        errors.append(f"timeline audio is missing from voice manifest: {output}")
    for output in sorted(manifest_outputs - timeline_outputs):
        errors.append(f"voice manifest audio is unused by timeline: {output}")

    for output in sorted(manifest_outputs & timeline_outputs):
        voice = manifest_rows[output]
        narration = timeline_rows[output]
        for field in ("speaker", "text"):
            if str(voice.get(field, "")).strip() != str(
                narration.get(field, "")
            ).strip():
                errors.append(f"{output}: {field} differs between manifest and timeline")

    scenes = timeline.get("scenes", [])
    if scenes:
        fps = float(timeline.get("composition", {}).get("fps", 0))
        if fps <= 0:
            errors.append("timeline composition fps must be positive")
        else:
            timeline_cover_seconds = float(scenes[0]["durationInFrames"]) / fps
            manifest_cover_seconds = float(manifest.get("cover", {}).get("seconds", 0))
            if abs(timeline_cover_seconds - manifest_cover_seconds) > 0.1:
                errors.append(
                    "cover duration differs between manifest "
                    f"({manifest_cover_seconds:.1f}s) and timeline "
                    f"({timeline_cover_seconds:.1f}s)"
                )
        timeline_title = " ".join(
            str(scenes[0].get("caption", {}).get("title", "")).split()
        )
        manifest_title = " ".join(
            str(manifest.get("cover", {}).get("title", "")).split()
        )
        if timeline_title != manifest_title:
            errors.append("cover title differs between manifest and timeline")

    if errors:
        raise SystemExit("\n".join(errors))
    print("voice manifest and timeline contract are consistent")


if __name__ == "__main__":
    main()
