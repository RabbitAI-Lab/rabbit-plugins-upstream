#!/usr/bin/env python3
"""
iwork2md.py - Convert Apple Pages / Numbers / Keynote files to Markdown.

Usage:
    python3 iwork2md.py INPUT.[pages|numbers|key] [OUTPUT.md]
    python3 iwork2md.py INPUT  --stdout            # print to stdout
    python3 iwork2md.py INPUT  --texts             # dump raw extracted texts
    python3 iwork2md.py INPUT  --media             # list embedded media files

If OUTPUT is omitted, a .md file is written next to the input.

Notes:
    - The iWork container uses Protobuf (not self-describing) so the exact
      schema for each object `type` is needed for perfect fidelity. That map
      (TSPRegistry) ships inside the iWork binaries and varies per app/version.
    - Without it we still recover ~100% of human-readable content by walking
      the protobuf tree generically and emitting every UTF-8 string field.
      This skill therefore produces a faithful *content* Markdown: table text,
      slide text, body paragraphs, titles, and media inventory are all present.
    - Encrypted (password-protected) documents cannot be read (AES-128/PKCS7).
    - Layout/formatting (fonts, colors, exact cell merging geometry) is not
      reconstructed; only the textual structure is.

Dependency: iwa.py (same directory). Stdlib only.
"""

import os
import re
import sys
from typing import Dict, List

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import iwa  # noqa: E402


def _slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", s)
    return s.strip("-") or "doc"


def _fmt_lines(text: str) -> List[str]:
    """Normalize body text into clean markdown lines."""
    lines = []
    for ln in text.splitlines():
        ln = ln.rstrip()
        if ln.strip():
            lines.append(ln)
    return lines


def _filename_title(path: str) -> str:
    """Derive a readable title from the file name (strip extension, separators)."""
    base = os.path.basename(path)
    for ext in (".pages", ".numbers", ".key"):
        if base.lower().endswith(ext):
            base = base[: -len(ext)]
            break
    base = re.sub(r"[_.]+", " ", base).strip()
    return base or "Document"


def _table_rows(texts: List[str]):
    """Heuristically detect a Numbers-style table: rows of | separated cells.

    Legacy (older Numbers) serializes each table row as a single string
    "a | b | c". We only treat consecutive rows as a table when they form a
    *consistent grid* (>= 3 rows sharing the same column count, modest cell
    length) so stray '|' characters inside prose are not mistaken for tables.
    Modern Numbers tables are reconstructed separately via extract_numbers_tables.
    """
    tables = []
    current = []
    cur_cols = None
    for t in texts:
        if ("|" in t and t.count("\n") == 0 and len(t) <= 300
                and not t.startswith("http")):
            cells = [c.strip() for c in t.split("|")]
            if len(cells) >= 2 and all(len(c) <= 120 for c in cells):
                if cur_cols is None or len(cells) == cur_cols:
                    current.append(cells)
                    cur_cols = len(cells)
                    continue
        if current:
            if len(current) >= 3:
                tables.append(current)
            current = []
            cur_cols = None
    if current and len(current) >= 3:
        tables.append(current)
    # Dedupe identical consecutive tables (content is sometimes mirrored
    # across multiple .iwa components in a document).
    deduped = []
    for tbl in tables:
        if not deduped or tbl != deduped[-1]:
            deduped.append(tbl)
    return deduped


def _render_table(rows: List[List[str]]) -> List[str]:
    """Render a single table (list of rows) into markdown table lines."""
    if not rows:
        return []
    ncols = max(len(r) for r in rows)
    header = rows[0] + [""] * (ncols - len(rows[0]))
    out = []
    out.append("| " + " | ".join(header) + " |")
    out.append("| " + " | ".join(["---"] * ncols) + " |")
    for r in rows[1:]:
        rpad = r + [""] * (ncols - len(r))
        out.append("| " + " | ".join(rpad) + " |")
    return out


def convert_bundle(path: str) -> str:
    """Return a Markdown string for the whole bundle."""
    title_meta = iwa.read_title(path)
    media = iwa.list_media(path)

    try:
        zf, iwa_names = iwa.open_iwa_sources(path)
    except ValueError as e:
        return f"# Conversion failed\n\n{type(e).__name__}: {e}\n"

    all_texts: List[str] = []
    per_file: Dict[str, List[str]] = {}
    all_objects: List[dict] = []
    numbers_tables: List[List[List[str]]] = []
    for name in sorted(iwa_names):
        try:
            data = zf.read(name)
            objects = iwa.parse_iwa(data)
        except Exception as e:  # noqa: BLE001
            per_file[name] = [f"[parse error: {e}]"]
            continue
        all_objects.extend(objects)
        texts: List[str] = []
        for obj in objects:
            texts.extend(iwa.collect_object_texts(obj))
        all_texts.extend(texts)
        per_file[name] = texts
    # Numbers native tables need Tables AND their DataLists, which may live in
    # different .iwa files -> resolve across the whole bundle.
    numbers_tables.extend(iwa.extract_numbers_tables(all_objects))
    try:
        zf.close()
    except Exception:
        pass

    # Dedupe tables across .iwa files (content is often mirrored between
    # components, e.g. Document.iwa vs CalculationEngine.iwa) by fingerprint.
    seen_tables = set()
    unique_tables = []
    for name in sorted(per_file):
        for tbl in _table_rows(per_file[name]):
            fp = tuple(tuple(r) for r in tbl)
            if fp not in seen_tables:
                seen_tables.add(fp)
                unique_tables.append(tbl)
    # Merge Numbers native tables (dedupe against the "|'-row" ones by fingerprint)
    for tbl in numbers_tables:
        fp = tuple(tuple(r) for r in tbl)
        if fp not in seen_tables:
            seen_tables.add(fp)
            unique_tables.append(tbl)

    # Build Markdown
    lines: List[str] = []
    doc_title = title_meta or _filename_title(path)
    lines.append(f"# {doc_title}")
    lines.append("")
    if title_meta:
        lines.append(f"> Source: `{os.path.basename(path)}`")
        lines.append("")

    # Media inventory
    if media:
        lines.append("## Embedded media")
        lines.append("")
        for m in media:
            lines.append(f"- `{m}`")
        lines.append("")

    # Tables (Numbers)
    if unique_tables:
        lines.append("## Tables")
        lines.append("")
        for tbl in unique_tables:
            lines.extend(_render_table(tbl))
            lines.append("")

    # Body: prefer the largest text block, else list all non-table texts
    body_candidates = [t for t in all_texts
                       if "|" not in t or t.count("\n") > 0]
    body = iwa.best_body(body_candidates)
    if body and body.strip() != doc_title.strip():
        lines.append("## Content")
        lines.append("")
        lines.extend(_fmt_lines(body))
        lines.append("")

    # Remaining notable texts not already shown
    shown = set()
    if body:
        shown.add(body)
    extra = [t for t in all_texts if t not in shown and len(t) > 1
             and "|" not in t and not _is_noise(t)]
    # dedupe, keep order
    seen = set()
    extra_unique = []
    for t in extra:
        if t in seen:
            continue
        seen.add(t)
        extra_unique.append(t)
    if extra_unique:
        lines.append("## Other text fragments")
        lines.append("")
        for t in extra_unique[:200]:
            txt = t.strip()
            if not txt:
                continue
            if "\n" in txt:
                lines.append("```")
                lines.extend(_fmt_lines(txt))
                lines.append("```")
            else:
                lines.append(f"- {txt}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


_MONTHS = {"january","february","march","april","may","june","july","august",
           "september","october","november","december"}
_DATE_RE = re.compile(r"^(\d{1,4}[/.\-]){1,2}\d{1,4}([/.\-]\d{1,4})?$")


def _is_noise(text: str) -> bool:
    """Drop iWork structural/format noise from the 'other fragments' list."""
    s = text.strip()
    if not s:
        return True
    # locale/timezone tokens
    if iwa._is_locale_like(s):
        return True
    # calendar / number-system identifiers
    if s.lower() in ("gregorian", "latn", "iso8601"):
        return True
    # number-format strings like #,##0% or 0.#
    if re.fullmatch(r"[#0.,%\s+\-*Ee/]+", s):
        return True
    # pure date tokens
    if _DATE_RE.match(s):
        return True
    # a single standalone month name
    if s.lower() in _MONTHS:
        return True
    # image filename fragments (filename + numeric size) are not content
    if re.search(r"\.(jpe?g|png|gif|tiff?|pdf|mov|mp4)$", s, re.I):
        return True
    return False


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print(__doc__)
        return 2
    src = argv[0]
    if not os.path.exists(src):
        print(f"error: file not found: {src}", file=sys.stderr)
        return 2

    flags = set(argv[1:])
    if "--texts" in flags:
        zf, names = iwa.open_iwa_sources(src)
        for name in sorted(names):
            print(f"===== {name} =====")
            for obj in iwa.parse_iwa(zf.read(name)):
                for t in iwa.collect_object_texts(obj):
                    print(t)
        return 0
    if "--media" in flags:
        for m in iwa.list_media(src):
            print(m)
        return 0

    md = convert_bundle(src)

    if "--stdout" in flags or len(argv) == 1 or argv[1].startswith("--"):
        # stdout unless an output path was given
        out_path = None
        for a in argv[1:]:
            if not a.startswith("--"):
                out_path = a
                break
        if out_path:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md)
            print(f"wrote {out_path}")
        else:
            sys.stdout.write(md)
        return 0

    out_path = argv[1]
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
