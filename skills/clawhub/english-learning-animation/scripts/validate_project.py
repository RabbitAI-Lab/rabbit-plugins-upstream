#!/usr/bin/env python3
"""Run the complete preflight and optional post-render review pipeline."""

import argparse
import subprocess
import sys
from pathlib import Path


def run(script: Path, *arguments: Path) -> None:
    command = [sys.executable, str(script), *(str(value) for value in arguments)]
    subprocess.run(command, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--video", type=Path)
    parser.add_argument("--review-dir", type=Path)
    args = parser.parse_args()

    project = args.project.expanduser().resolve()
    scripts = Path(__file__).resolve().parent
    manifest = project / "voice-manifest.json"
    timeline = project / "script.json"
    public = project / "public"
    for required in (manifest, timeline, public):
        if not required.exists():
            raise SystemExit(f"missing project input: {required}")

    subprocess.run(
        [sys.executable, str(scripts / "validate_lesson.py"), str(manifest)],
        cwd=project,
        check=True,
    )
    run(scripts / "validate_contract.py", manifest, timeline)
    run(scripts / "validate_semantics.py", timeline, Path("--video-source"), project / "src" / "video.tsx")
    run(scripts / "validate_layers.py", timeline, public)
    run(scripts / "validate_timeline.py", timeline, public)

    if args.video:
        video = args.video.expanduser().resolve()
        review_dir = (
            args.review_dir.expanduser().resolve()
            if args.review_dir
            else project / "work" / "review-frames"
        )
        cover = review_dir / "00-cover-technical-check.png"
        run(
            scripts / "validate_render.py",
            video,
            Path("--cover-frame"),
            cover,
        )
        run(scripts / "extract_review_frames.py", video, timeline, review_dir)
        print(f"post-render review frames: {review_dir}")

    print("all requested project quality gates passed")


if __name__ == "__main__":
    main()
