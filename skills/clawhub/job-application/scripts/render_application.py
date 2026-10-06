#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def render(source: Path, pdflatex: str) -> str:
    command = [
        pdflatex,
        "-interaction=nonstopmode",
        "-halt-on-error",
        source.name,
    ]
    outputs = []
    for pass_number in (1, 2):
        completed = subprocess.run(
            command,
            cwd=source.parent,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        outputs.append(f"--- pass {pass_number} ---\n{completed.stdout}{completed.stderr}")
        if completed.returncode:
            raise RuntimeError(f"pdflatex failed for {source.name} on pass {pass_number}; see build.log")
    return "\n".join(outputs)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render CV.tex and cover_letter.tex with pdflatex.")
    parser.add_argument("application_directory", type=Path)
    args = parser.parse_args()

    pdflatex = shutil.which("pdflatex")
    if not pdflatex:
        raise SystemExit("pdflatex was not found on PATH. Install a LaTeX distribution first.")

    app_dir = args.application_directory.expanduser().resolve()
    if not app_dir.is_dir():
        raise SystemExit(f"Directory not found: {app_dir}")

    sources = [app_dir / "CV.tex", app_dir / "cover_letter.tex"]
    missing = [source.name for source in sources if not source.is_file()]
    if missing:
        raise SystemExit(f"Missing source files: {', '.join(missing)}")

    logs = []
    try:
        for source in sources:
            logs.append(f"===== {source.name} =====\n{render(source, pdflatex)}")
    finally:
        (app_dir / "build.log").write_text("\n".join(logs), encoding="utf-8")

    print(f"Rendered {app_dir / 'CV.pdf'} and {app_dir / 'cover_letter.pdf'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
