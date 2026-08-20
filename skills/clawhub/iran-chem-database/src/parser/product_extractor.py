"""MoleculeExtractorPipeline — walks local HTTrack mirror files (spec §4.2).

KEY DESIGN PRINCIPLE: the parser NEVER fetches from the internet. It only reads
files from the local HTTrack mirror directory. Each file is HTML, PDF, or Excel.
Extracted records are filtered (research grade ONLY), validated (RDKit/PubChem),
deduplicated (InChIKey), and handed to the DB sync layer.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import List, Optional

from src.parser.chemical_validator import ChemicalValidator
from src.parser.excel_parser import ExcelCatalogParser
from src.parser.grade_classifier import GradeClassifier
from src.parser.html_parser import HTMLProductParser
from src.parser.pdf_parser import PDFCatalogParser
from src.parser.mirror_path_utils import mirror_path_to_url

HTML_EXTS = {".html", ".htm", ".php", ".asp", ".aspx", ".jsp"}


class MoleculeExtractorPipeline:
    def __init__(self, db_sync=None):
        self.html_parser = HTMLProductParser()
        self.pdf_parser = PDFCatalogParser()
        self.excel_parser = ExcelCatalogParser()
        self.grade_classifier = GradeClassifier()
        self.chemical_validator = ChemicalValidator()
        self.db_sync = db_sync

    def process_files(self, files: List[str], supplier_id: int, mirror_base_path: str) -> dict:
        results = {
            "total_found": 0, "new_count": 0, "updated_count": 0,
            "skipped_non_research": 0, "validation_failed": 0, "errors": [],
        }
        for file_path in files:
            try:
                ext = Path(file_path).suffix.lower()
                if ext in HTML_EXTS:
                    molecules = self.html_parser.parse_file(file_path, supplier_id)
                elif ext == ".pdf":
                    molecules = self.pdf_parser.parse_file(file_path, supplier_id)
                elif ext in (".xlsx", ".xls"):
                    molecules = self.excel_parser.parse_file(file_path, supplier_id)
                elif ext == ".csv":
                    molecules = self.excel_parser.parse_file(file_path, supplier_id)
                else:
                    continue

                for mol in molecules:
                    self._process_one(mol, supplier_id, file_path, mirror_base_path, results)
            except Exception as exc:  # noqa: BLE001
                results["errors"].append({"file": file_path, "error": str(exc)})
        return results

    def _process_one(self, mol: dict, supplier_id: int, file_path: str,
                     mirror_base_path: str, results: dict) -> None:
        # Enrich with provenance
        mol.setdefault("supplier_id", supplier_id)
        mol.setdefault("source_file", file_path)
        mol.setdefault("product_url", mirror_path_to_url(file_path))

        # CRITICAL: research-grade filter (spec §4.4)
        ok, _reason = self.grade_classifier.classify(mol)
        if not ok:
            results["skipped_non_research"] += 1
            return

        # Chemical validation (RDKit / PubChem / CAS checksum)
        validated = self.chemical_validator.validate(mol)
        if validated is None:
            results["validation_failed"] += 1
            return

        results["total_found"] += 1
        if self.db_sync is not None:
            try:
                sync_result = self.db_sync.upsert_molecule(validated, supplier_id)
                if sync_result == "new":
                    results["new_count"] += 1
                elif sync_result == "updated":
                    results["updated_count"] += 1
            except Exception as exc:  # noqa: BLE001
                results["errors"].append({"file": file_path, "error": f"sync:{exc}"})

    @staticmethod
    def page_hash(raw_html: str) -> str:
        return hashlib.sha256(raw_html.encode("utf-8", errors="replace")).hexdigest()

    @staticmethod
    def purity_to_numeric(purity: str) -> Optional[float]:
        m = re.search(r"(\d{2,3}(?:\.\d+)?)\s*%", purity or "")
        return float(m.group(1)) if m else None
