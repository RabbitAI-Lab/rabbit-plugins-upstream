#!/usr/bin/env python3
"""Validate audio-driven timing, speaker ownership, and immersion language."""
import argparse
import math
import json
import re
import subprocess
from pathlib import Path


def seconds(path: Path) -> float:
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)], capture_output=True, text=True, check=True)
    return float(result.stdout.strip())


def contains_cjk(value: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", value))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=Path)
    parser.add_argument("public", type=Path)
    args = parser.parse_args()
    data = json.loads(args.script.read_text(encoding="utf-8"))
    fps = data["composition"]["fps"]
    scenes = data.get("scenes", [])
    scene_length = {scene["id"]: int(scene["durationInFrames"]) for scene in scenes}
    scene_layers = {
        scene["id"]: [
            " ".join(
                [
                    str(layer.get("speaker", "")).lower(),
                    Path(str(layer.get("src", ""))).stem.lower(),
                ]
            )
            for layer in scene.get("layers", [])
        ]
        for scene in scenes
    }
    errors = []
    if len(scene_length) != len(scenes):
        errors.append("scene ids must be unique")
    if len(scenes) < 4:
        errors.append("lesson needs at least four distinct visual scenes/beats")

    total_seconds = sum(scene_length.values()) / fps if fps else 0
    if total_seconds <= 0:
        errors.append("total runtime must be positive")
    if scenes:
        cover = scenes[0]
        cover_seconds = int(cover["durationInFrames"]) / fps
        if not 2 <= cover_seconds <= 3:
            errors.append(
                f"first scene cover is {cover_seconds:.1f}s; expected 2–3 seconds"
            )
        cover_copy = " ".join(
            str(cover.get("caption", {}).get(field, ""))
            for field in ("title", "subtitle")
        )
        runtime_claims = re.findall(
            r"\b(\d{1,3})\s*[- ]?(?:seconds?|secs?|s)\b",
            cover_copy,
            flags=re.IGNORECASE,
        )
        for claim in runtime_claims:
            claimed_seconds = int(claim)
            if abs(claimed_seconds - total_seconds) > 1.5:
                errors.append(
                    f"cover claims {claimed_seconds}s but timeline is "
                    f"{total_seconds:.1f}s"
                )

    allow_bilingual = bool(data.get("allowBilingualOnVideo", False))
    windows: dict[str, list[tuple[int, int, str]]] = {}
    required = {"id", "scene", "speaker", "text", "output", "from", "durationInFrames"}
    seen_ids: set[str] = set()

    for item in data.get("narration", []):
        missing = sorted(key for key in required if item.get(key) in {None, ""})
        if missing:
            errors.append(f"{item.get('id', '<unknown>')}: missing {', '.join(missing)}")
            continue
        item_id = str(item["id"])
        if item_id in seen_ids:
            errors.append(f"duplicate narration id: {item_id}")
        seen_ids.add(item_id)

        scene = str(item["scene"])
        if scene not in scene_length:
            errors.append(f"{item_id}: unknown scene {scene}")
            continue
        speaker = str(item["speaker"]).strip().lower()
        if not re.fullmatch(r"[a-z][a-z0-9_-]*", speaker):
            errors.append(f"{item_id}: speaker must be a stable ASCII role id")
        if not allow_bilingual:
            for field in ("text", "caption"):
                if contains_cjk(str(item.get(field, ""))):
                    errors.append(
                        f"{item_id}: {field} contains Chinese in English-only mode"
                    )

        audio = args.public / str(item["output"])
        if not audio.exists():
            errors.append(f"missing audio: {audio}")
            continue
        actual = math.ceil(seconds(audio) * fps)
        declared = int(item["durationInFrames"])
        start = int(item["from"])
        actual_end = start + actual
        declared_end = start + declared
        if declared < actual:
            errors.append(
                f"{item_id}: declared {declared} frames but audio needs {actual}"
            )
        if actual_end > scene_length[scene]:
            errors.append(
                f"{item_id}: audio ends at frame {actual_end}, outside "
                f"scene {scene} ({scene_length[scene]})"
            )
        if declared_end > scene_length[scene]:
            errors.append(
                f"{item_id}: declared window ends at frame {declared_end}, outside "
                f"scene {scene} ({scene_length[scene]})"
            )
        if speaker != "narrator" and not any(
            speaker in layer_identity for layer_identity in scene_layers.get(scene, [])
        ):
            errors.append(
                f"{item_id}: scene {scene} has no cutout filename matching speaker "
                f"role '{speaker}'"
            )
        windows.setdefault(scene, []).append((start, actual_end, item_id))

    for scene, entries in windows.items():
        ordered = sorted(entries)
        for previous, current in zip(ordered, ordered[1:]):
            if current[0] < previous[1]:
                errors.append(
                    f"{scene}: audio overlap between {previous[2]} and {current[2]}"
                )

    if not allow_bilingual:
        for scene in scenes:
            caption = scene.get("caption", {})
            for field in ("title", "subtitle"):
                if contains_cjk(str(caption.get(field, ""))):
                    errors.append(
                        f"{scene['id']}: cover/scene {field} contains Chinese "
                        "in English-only mode"
                    )
    if errors:
        raise SystemExit("\n".join(errors))
    print(
        "timeline, speaker ownership, and language mode are valid "
        f"(content-driven runtime: {total_seconds:.1f}s)"
    )


if __name__ == "__main__":
    main()
