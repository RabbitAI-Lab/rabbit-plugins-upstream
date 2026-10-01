#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from common import PROFILE_DIR, TEMPLATE_DIR, latex_escape, load_json, replace_tokens, write_text


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate cover-letter LaTeX from structured content.")
    parser.add_argument("--content", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--profile", type=Path, default=PROFILE_DIR / "master_profile.json")
    parser.add_argument("--template", type=Path, default=TEMPLATE_DIR / "cover-letter.tex")
    args = parser.parse_args()

    profile, content = load_json(args.profile), load_json(args.content)
    location = profile.get("location") or profile.get("address", "")
    paragraphs = "\n\n".join(latex_escape(p) for p in content.get("paragraphs", []))
    values = {
        "__NAME__": latex_escape(profile["full_name"]),
        "__EMAIL__": latex_escape(profile.get("email", "")),
        "__PHONE__": latex_escape(profile.get("phone", "")),
        "__LOCATION__": latex_escape(location),
        "__TITLE__": latex_escape(profile.get("default_target_title", "")),
        "__COMPANY__": latex_escape(content.get("company", "")),
        "__COMPANY_ADDRESS__": r" \\ ".join(latex_escape(x) for x in content.get("company_address", [])),
        "__DATE__": latex_escape(content.get("date", "")),
        "__SUBJECT__": latex_escape(content.get("subject", "")),
        "__SALUTATION__": latex_escape(content.get("salutation", "Guten Tag,")),
        "__BODY__": paragraphs,
        "__CLOSING__": latex_escape(content.get("closing", "Mit freundlichen Grüßen")),
    }
    write_text(args.output, replace_tokens(args.template.read_text(encoding="utf-8"), values))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
