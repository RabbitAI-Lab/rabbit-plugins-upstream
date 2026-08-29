#!/usr/bin/env python3
"""Validate background plates and transparent cutout layers declared in script.json."""

import argparse
import json
from pathlib import Path

from PIL import Image


def alpha_metrics(path: Path) -> tuple[float, float, float, list[int]]:
    with Image.open(path) as image:
        rgba = image.convert("RGBA")
        alpha = rgba.getchannel("A")
        histogram = alpha.histogram()
        pixels = rgba.width * rgba.height
        visible = sum(histogram[6:])
        opaque = sum(histogram[250:])
        semitransparent = sum(histogram[6:250])
        corners = [
            alpha.getpixel((0, 0)),
            alpha.getpixel((rgba.width - 1, 0)),
            alpha.getpixel((0, rgba.height - 1)),
            alpha.getpixel((rgba.width - 1, rgba.height - 1)),
        ]
    visible_ratio = visible / pixels if pixels else 0
    opaque_ratio = opaque / visible if visible else 0
    semi_ratio = semitransparent / visible if visible else 0
    return visible_ratio, opaque_ratio, semi_ratio, corners


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=Path)
    parser.add_argument("public", type=Path)
    parser.add_argument(
        "--min-opaque-ratio",
        type=float,
        default=0.88,
        help="Minimum fraction of visible cutout pixels with alpha >= 250.",
    )
    parser.add_argument(
        "--max-semitransparent-ratio",
        type=float,
        default=0.12,
        help="Maximum fraction of visible cutout pixels with alpha 6–249.",
    )
    args = parser.parse_args()

    data = json.loads(args.script.read_text(encoding="utf-8"))
    backgrounds = {
        scene.get("background")
        for scene in data.get("scenes", [])
        if scene.get("background")
    }
    layers = {
        layer.get("src")
        for scene in data.get("scenes", [])
        for layer in scene.get("layers", [])
        if layer.get("src")
    }
    errors: list[str] = []

    for relative in sorted(backgrounds):
        path = args.public / relative
        if not path.exists():
            errors.append(f"missing background: {path}")
            continue
        try:
            with Image.open(path) as image:
                image.verify()
        except Exception as exc:
            errors.append(f"invalid background image {path}: {exc}")

    for relative in sorted(layers):
        path = args.public / relative
        if not path.exists():
            errors.append(f"missing cutout: {path}")
            continue
        try:
            with Image.open(path) as image:
                has_alpha = image.mode in {"RGBA", "LA"} or (
                    image.mode == "P" and "transparency" in image.info
                )
            if not has_alpha:
                errors.append(f"{relative}: cutout has no alpha channel")
                continue
            visible, opaque, semi, corners = alpha_metrics(path)
        except Exception as exc:
            errors.append(f"invalid cutout image {path}: {exc}")
            continue

        if visible <= 0.01:
            errors.append(f"{relative}: cutout is effectively empty")
        if opaque < args.min_opaque_ratio:
            errors.append(
                f"{relative}: only {opaque:.1%} of visible pixels are opaque; "
                "character may appear ghosted"
            )
        if semi > args.max_semitransparent_ratio:
            errors.append(
                f"{relative}: {semi:.1%} of visible pixels are semitransparent; "
                "character may appear ghosted"
            )
        if min(corners) > 5:
            errors.append(
                f"{relative}: no transparent corner detected; asset may be a flattened plate"
            )
        print(
            f"{relative}: visible={visible:.1%}, opaque={opaque:.1%}, "
            f"semitransparent={semi:.1%}"
        )

    if not layers:
        errors.append("no cutout layers declared")
    if errors:
        raise SystemExit("\n".join(errors))
    print("declared visual layers are valid")


if __name__ == "__main__":
    main()
