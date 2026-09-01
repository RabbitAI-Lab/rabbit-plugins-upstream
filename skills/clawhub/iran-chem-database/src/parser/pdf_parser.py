"""PDF catalog parser — pdfplumber/PyMuPDF on LOCAL mirror files (spec §4.2)."""
from __future__ import annotations

from typing import List

from src.parser.cas_resolver import extract_cas_numbers


class PDFCatalogParser:
    def parse_file(self, file_path: str, supplier_id: int) -> List[dict]:
        import os
        if not os.path.exists(file_path):
            return []
        molecules: List[dict] = []
        try:
            molecules.extend(self._parse_with_pdfplumber(file_path, supplier_id))
        except Exception:  # noqa: BLE001
            pass
        if not molecules:
            try:
                molecules.extend(self._parse_with_pymupdf(file_path, supplier_id))
            except Exception:  # noqa: BLE001
                pass
        return molecules

    def _parse_with_pdfplumber(self, file_path: str, supplier_id: int) -> List[dict]:
        import pdfplumber

        molecules: List[dict] = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables() or []
                for table in tables:
                    for row in table:
                        mol = self._parse_catalog_row(row)
                        if mol:
                            mol["supplier_id"] = supplier_id
                            mol["source_file"] = file_path
                            molecules.append(mol)
                text = page.extract_text() or ""
                molecules.extend(self._extract_from_text(text, supplier_id, file_path))
        return molecules

    def _parse_with_pymupdf(self, file_path: str, supplier_id: int) -> List[dict]:
        import pymupdf

        molecules: List[dict] = []
        doc = pymupdf.open(file_path)
        for page in doc:
            text = page.get_text()
            molecules.extend(self._extract_from_text(text, supplier_id, file_path))
        doc.close()
        return molecules

    def _parse_catalog_row(self, row) -> dict | None:
        if not row:
            return None
        cells = [str(c or "").strip() for c in row]
        text = " | ".join(cells)
        cas = extract_cas_numbers(text)
        if not cas:
            return None
        return {
            "title": next((c for c in cells if len(c) > 2), text[:80]),
            "cas_number": cas[0],
            "description": text[:400],
        }

    def _extract_from_text(self, text: str, supplier_id: int, file_path: str) -> List[dict]:
        molecules: List[dict] = []
        for line in text.splitlines():
            line = line.strip()
            if len(line) < 4:
                continue
            cas = extract_cas_numbers(line)
            if not cas:
                continue
            molecules.append({
                "title": line[:160],
                "cas_number": cas[0],
                "description": line,
                "supplier_id": supplier_id,
                "source_file": file_path,
            })
        return molecules
