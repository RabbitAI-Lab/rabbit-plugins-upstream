#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from common import PROFILE_DIR, load_json


def terms(job: dict) -> set[str]:
    text = " ".join(str(value) for value in job.values()).lower()
    return set(re.findall(r"[a-zA-ZÀ-ÿ0-9+#.]+", text))


def ranked(items: list[dict], job_terms: set[str], limit: int) -> list[str]:
    def score(item: dict) -> tuple[int, int, str]:
        item_terms = terms(item)
        matches = len(item_terms & job_terms)
        return matches, int(item.get("score", 0)), str(item["id"])

    return [item["id"] for item in sorted(items, key=score, reverse=True)[:limit]]


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest CV records relevant to a job description.")
    parser.add_argument("--job", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--profile-dir", type=Path, default=PROFILE_DIR)
    args = parser.parse_args()

    job = load_json(args.job)
    profile = load_json(args.profile_dir / "master_profile.json")
    job_terms = terms(job)
    result = {
        "target_title": job.get("role", profile["default_target_title"]),
        "language": job.get("language", profile["default_language"]),
        "about_me": " ".join(profile["about_me_base"]),
        "skills": ranked(load_json(args.profile_dir / "skills.json"), job_terms, 5),
        "experience": ranked(load_json(args.profile_dir / "experience.json"), job_terms, 3),
        "education": ranked(load_json(args.profile_dir / "education.json"), job_terms, 2),
        "projects": ranked(load_json(args.profile_dir / "projects.json"), job_terms, 1),
        "languages": ranked(load_json(args.profile_dir / "languages.json"), job_terms, 3),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
