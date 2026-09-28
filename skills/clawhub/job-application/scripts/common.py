from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

SKILL_DIR = Path(__file__).resolve().parent.parent
BUNDLED_PROFILE_DIR = SKILL_DIR / "assets" / "profile"
PROFILE_DIR = Path(os.environ.get("JOB_APPLICATION_PROFILE_DIR", BUNDLED_PROFILE_DIR)).expanduser().resolve()
OUTPUT_DIR = Path(os.environ.get("JOB_APPLICATION_OUTPUT_DIR", Path.cwd() / "applications")).expanduser().resolve()
TEMPLATE_DIR = SKILL_DIR / "assets" / "templates"


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def latex_escape(value: Any) -> str:
    text = str(value or "")
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
        "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def by_id(items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(item["id"]): item for item in items}


def replace_tokens(template: str, values: dict[str, str]) -> str:
    for token, value in values.items():
        template = template.replace(token, value)
    unresolved = sorted({part.split("__", 1)[0] for part in template.split("__")[1::2] if part})
    if unresolved:
        raise ValueError(f"Unresolved template tokens: {', '.join(unresolved)}")
    return template


def resolve_profile_asset(profile_dir: Path, value: str) -> Path | None:
    if not value:
        return None
    configured = Path(value).expanduser()
    candidates = [configured] if configured.is_absolute() else [
        profile_dir / configured,
        profile_dir.parent / configured,
        SKILL_DIR / configured,
    ]
    return next((candidate.resolve() for candidate in candidates if candidate.is_file()), None)
