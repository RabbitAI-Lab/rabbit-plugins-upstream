#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from common import PROFILE_DIR, TEMPLATE_DIR, by_id, latex_escape, load_json, replace_tokens, resolve_profile_asset, write_text


def selected(ids: list[str], filename: str, profile_dir: Path) -> list[dict]:
    records = by_id(load_json(profile_dir / filename))
    missing = [record_id for record_id in ids if record_id not in records]
    if missing:
        raise ValueError(f"Unknown IDs in {filename}: {', '.join(missing)}")
    return [records[record_id] for record_id in ids]


def entries(records: list[dict]) -> str:
    blocks = []
    for record in records:
        description = " ".join(record.get("description", [])[:2])
        subtitle = " · ".join(
            str(value).strip()
            for value in (
                record.get("organization", ""),
                record.get("context_label", ""),
                record.get("subtitle", ""),
            )
            if str(value).strip()
        )
        blocks.append(
            "\\cvitem{%s}{%s}{%s}{%s}" % tuple(
                latex_escape(value) for value in (
                    record.get("period", ""), record.get("title", ""),
                    subtitle, description,
                )
            )
        )
    return "\n".join(blocks)


def skill_bars(records: list[dict]) -> str:
    return "\n".join(
        f"\\skillbar{{{latex_escape(item['label'])}}}{{{max(0, min(5, int(item.get('score', 0))))}}}"
        for item in records
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate CV LaTeX from a reviewed selection.")
    parser.add_argument("--selection", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--profile-dir", type=Path, default=PROFILE_DIR)
    parser.add_argument("--template", type=Path, default=TEMPLATE_DIR / "cv.tex")
    args = parser.parse_args()

    profile = load_json(args.profile_dir / "master_profile.json")
    choice = load_json(args.selection)
    location = profile.get("location") or profile.get("address", "")
    skills = selected(choice.get("skills", [])[:5], "skills.json", args.profile_dir)
    languages = selected(choice.get("languages", [])[:3], "languages.json", args.profile_dir)
    photo_source = resolve_profile_asset(args.profile_dir, profile.get("profile_picture", ""))
    photo_target = args.output.parent / "assets" / "profile-photo.png"
    photo_block = ""
    if photo_source is not None:
        photo_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(photo_source, photo_target)
        photo_block = r"""\begin{tikzpicture}
    \clip (0,0) circle (2.18cm);
    \node at (0,-0.05) {\includegraphics[width=4.55cm]{assets/profile-photo.png}};
  \end{tikzpicture}
  \vspace{0.12cm}"""
    values = {
        "__NAME__": latex_escape(profile["full_name"]),
        "__TITLE__": latex_escape(choice["target_title"]),
        "__EMAIL__": latex_escape(profile.get("email", "")),
        "__PHONE__": latex_escape(profile.get("phone", "")),
        "__LOCATION__": latex_escape(location),
        "__PHOTO_BLOCK__": photo_block,
        "__ABOUT__": latex_escape(choice.get("about_me", "")),
        "__SKILLS__": skill_bars(skills),
        "__EXPERIENCE__": entries(selected(choice.get("experience", [])[:3], "experience.json", args.profile_dir)),
        "__EDUCATION__": entries(selected(choice.get("education", [])[:2], "education.json", args.profile_dir)),
        "__PROJECTS__": entries(selected(choice.get("projects", [])[:1], "projects.json", args.profile_dir)),
        "__LANGUAGES__": skill_bars(languages),
    }
    write_text(args.output, replace_tokens(args.template.read_text(encoding="utf-8"), values))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
