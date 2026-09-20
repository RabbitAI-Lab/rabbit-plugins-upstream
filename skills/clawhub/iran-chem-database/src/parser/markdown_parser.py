"""Lightweight markdown/text molecule parser (added v2.6).

Jina Reader returns a page as markdown text. This parser scans the text for
CAS Registry Number patterns and emits a molecule candidate for every line or
paragraph that contains one — enough to salvage catalog data (name + CAS +
purity) from text-only free-access fetches of geo-blocked supplier sites.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import List

_CAS_RE = re.compile(r"\b\d{2,7}-\d{2}-\d\b")
_PURITY_RE = re.compile(r"\b(\d{2,3}(?:\.\d+)?)\s*%")

# Lines that are obviously navigation/boilerplate, not molecule records.
_SKIP_RE = re.compile(
    r"^(title:|url source:|published time:|markdown content:|image \d+|\[!\[|http|"
    r"©|all rights|copyright|contact|email|phone|fax|\+98)", re.IGNORECASE)


class MarkdownCatalogParser:
    """Parses persisted markdown/text files into molecule candidate records."""

    def parse_file(self, file_path: str, supplier_id: int) -> List[dict]:
        if not str(file_path).lower().endswith((".md", ".txt", ".markdown")):
            return []
        try:
            text = Path(file_path).read_text("utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            return []
        out: List[dict] = []
        for block in re.split(r"\n{2,}", text):
            line = " ".join(block.split())
            if not line or _SKIP_RE.search(line):
                continue
            m = _CAS_RE.search(line)
            if not m:
                continue
            # title = the text around the CAS, trimmed to a sane length
            title = line[:200].strip()
            record = {
                "title": title,
                "supplier_id": supplier_id,
                "source_file": file_path,
                "_extraction_method": "markdown-text",
                "cas_number": m.group(0),
            }
            pm = _PURITY_RE.search(line)
            if pm:
                record["purity"] = pm.group(0)
                record["purity_numeric"] = float(pm.group(1))
            out.append(record)
        return out
