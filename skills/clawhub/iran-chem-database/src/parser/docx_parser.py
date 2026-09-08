"""DOCX catalogue parser (fix guide §5.4).

Extracts text tables from .docx files using only the standard library
(docx = zip archive of XML), so no heavy dependencies are required.
Legacy binary .doc is NOT supported and is reported as such.
"""
from __future__ import annotations

import re
import zipfile
from typing import List, Optional
from xml.etree import ElementTree

_W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
_CAS_RE = re.compile(r"\b\d{2,7}-\d{2}-\d\b")
_PURITY_RE = re.compile(r"\b(\d{2,3}(?:\.\d+)?)\s*%")
_GRADE_RE = re.compile(r"\b(ACS|HPLC|GC|AR|GR|USP|BP|EP|JP|Reagent|Analytical|Extra pure|Laboratory)\b", re.I)


def _paragraph_text(p) -> str:
    return "".join(t.text or "" for t in p.iter(_W_NS + "t"))


class DOCXCatalogParser:
    """Parses .docx catalogues into molecule candidate records."""

    def parse_file(self, file_path: str, supplier_id: int) -> List[dict]:
        if not str(file_path).lower().endswith(".docx"):
            return []
        try:
            tables = self._extract_tables(file_path)
        except Exception:  # noqa: BLE001
            return []
        records: List[dict] = []
        for table in tables:
            for row in table:
                record = self._row_to_record(row)
                if record:
                    record["supplier_id"] = supplier_id
                    record["source_file"] = file_path
                    record["_extraction_method"] = "docx-table"
                    records.append(record)
        return records

    # ── extraction ─────────────────────────────────────────────────────────
    def _extract_tables(self, file_path: str) -> List[List[List[str]]]:
        out: List[List[List[str]]] = []
        with zipfile.ZipFile(file_path) as zf:
            with zf.open("word/document.xml") as fh:
                root = ElementTree.fromstring(fh.read())
        body = root.find(_W_NS + "body")
        if body is None:
            return out
        for tbl in body.iter(_W_NS + "tbl"):
            table: List[List[str]] = []
            for tr in tbl.iter(_W_NS + "tr"):
                cells = []
                for tc in tr.iter(_W_NS + "tc"):
                    cells.append(" ".join(_paragraph_text(p) for p in tc.iter(_W_NS + "p")).strip())
                table.append(cells)
            if table:
                out.append(table)
        return out

    # ── record mapping ─────────────────────────────────────────────────────
    def _row_to_record(self, cells: List[str]) -> Optional[dict]:
        text = " | ".join(c for c in cells if c).strip()
        if len(text) < 3:
            return None
        cas = _CAS_RE.search(text)
        has_name = any(len(c) > 2 and not c.replace(",", "").replace(".", "").isdigit()
                       for c in cells if c)
        # A row needs either a CAS or a plausible chemical name to be kept.
        if not cas and not has_name:
            return None
        title = ""
        for c in cells:
            c2 = c.strip()
            if c2 and not _CAS_RE.fullmatch(c2) and not re.fullmatch(r"[\d.,\s]+", c2):
                title = c2
                break
        record: dict = {"title": title, "cas_number": cas.group(0) if cas else ""}
        m = _PURITY_RE.search(text)
        if m:
            record["purity"] = f"{m.group(1)}%"
            record["purity_numeric"] = float(m.group(1))
        g = _GRADE_RE.search(text)
        if g:
            record["grade"] = g.group(1)
        price_m = re.search(r"\b(\d{4,12})\b\s*(?:تومان|IRR|﷼)", text)
        if price_m:
            record["price"] = float(price_m.group(1).replace(",", ""))
            record["currency"] = "IRR"
        return record


def is_supported_catalogue_file(path: str) -> bool:
    """.docx is supported; legacy binary .doc is explicitly NOT (fix guide §5.4)."""
    return str(path).lower().endswith(".docx")
