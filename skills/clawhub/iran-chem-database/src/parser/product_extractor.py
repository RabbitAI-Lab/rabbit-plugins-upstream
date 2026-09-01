"""MoleculeExtractorPipeline — walks local mirror files (spec §4.2, fix guide §4/§5/§8).

KEY DESIGN PRINCIPLE: the parser NEVER fetches from the internet. It only reads
files from the local mirror directory (HTML, PDF, Excel, CSV, DOCX, JSON). Each
record passes through:

  1. configurable inclusion policy (grade classifier — strict_research /
     lab_or_research / all_catalogue);
  2. chemical validation (RDKit / PubChem / CAS checksum);
  3. explicit organic classification (structure → CAS → name → unknown);
  4. database sync (LiveSyncEngine) — with every rejection persisted in
     RejectedCatalogueItem so nothing is silently dropped.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import List, Optional

from src.config import get_config
from src.parser.chemical_validator import ChemicalValidator
from src.parser.docx_parser import DOCXCatalogParser
from src.parser.excel_parser import ExcelCatalogParser
from src.parser.grade_classifier import GradeClassifier
from src.parser.html_parser import HTMLProductParser
from src.parser.json_catalogue_parser import JSONCatalogueParser
from src.parser.markdown_parser import MarkdownCatalogParser
from src.parser.organic_classifier import OrganicClassifier
from src.parser.pdf_parser import PDFCatalogParser
from src.parser.mirror_path_utils import mirror_path_to_url

HTML_EXTS = {".html", ".htm", ".php", ".asp", ".aspx", ".jsp"}
# Legacy binary .doc is intentionally NOT parsed (fix guide §5.4) — it is
# neither in this list nor advertised as supported.
# v2.6: .md/.txt added for the free-access (Jina Reader) fallback fetches.
SUPPORTED_EXTS = HTML_EXTS | {".pdf", ".xlsx", ".xls", ".csv", ".docx", ".json", ".md", ".txt"}


class MoleculeExtractorPipeline:
    def __init__(self, db_sync=None, inclusion_mode: str | None = None,
                 supplier_is_lab: bool | None = None,
                 organic_network: bool | None = None,
                 resolve_cas: bool | None = None):
        self.html_parser = HTMLProductParser()
        self.pdf_parser = PDFCatalogParser()
        self.excel_parser = ExcelCatalogParser()
        self.docx_parser = DOCXCatalogParser()
        self.json_parser = JSONCatalogueParser()
        self.markdown_parser = MarkdownCatalogParser()
        self.grade_classifier = GradeClassifier(inclusion_mode, supplier_is_lab)
        self.chemical_validator = ChemicalValidator(resolve_cas=resolve_cas)
        try:
            cfg = get_config().as_dict()
            parsing = cfg.get("parsing", {}) or {}
            self.retain_rejections = bool(parsing.get("retain_rejections", True))
            organic_cfg = parsing.get("organic", {}) or {}
            organic_network = organic_network if organic_network is not None \
                else bool(organic_cfg.get("network_lookup", True))
        except Exception:  # noqa: BLE001 (bare test environments)
            self.retain_rejections = True
        self.organic_classifier = OrganicClassifier(network=organic_network)
        self.db_sync = db_sync

    def process_files(self, files: List[str], supplier_id: int, mirror_base_path: str) -> dict:
        results = {
            "total_found": 0, "new_count": 0, "updated_count": 0,
            "skipped_non_research": 0, "validation_failed": 0,
            "rejected_grade": 0, "rejected_validation": 0, "rejected_sync": 0,
            "organic_true": 0, "organic_false": 0, "organic_unknown": 0,
            "errors": [],
        }
        for file_path in files:
            try:
                ext = Path(file_path).suffix.lower()
                if ext in HTML_EXTS:
                    molecules = self.html_parser.parse_file(file_path, supplier_id)
                elif ext == ".pdf":
                    molecules = self.pdf_parser.parse_file(file_path, supplier_id)
                elif ext in (".xlsx", ".xls", ".csv"):
                    molecules = self.excel_parser.parse_file(file_path, supplier_id)
                elif ext == ".docx":
                    molecules = self.docx_parser.parse_file(file_path, supplier_id)
                elif ext == ".json":
                    molecules = self.json_parser.parse_file(file_path, supplier_id)
                elif ext in (".md", ".txt", ".markdown"):
                    molecules = self.markdown_parser.parse_file(file_path, supplier_id)
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

        # 1) Configurable inclusion policy (was: hard-coded strict filter)
        ok, reason, _conf = self.grade_classifier.classify(mol)
        if not ok:
            results["skipped_non_research"] += 1
            results["rejected_grade"] += 1
            self._record_rejection(mol, "grade", reason)
            return

        # 2) Chemical validation (RDKit / PubChem / CAS checksum)
        validated = self.chemical_validator.validate(mol)
        if validated is None:
            results["validation_failed"] += 1
            results["rejected_validation"] += 1
            self._record_rejection(mol, "validation", "no-identifiable-chemistry")
            return

        # 3) Explicit organic classification (structure → CAS → name → unknown);
        #    lookup failures are recorded distinctly (remediation §6)
        status, o_reason, o_conf, o_err = self.organic_classifier.classify_detailed(validated)
        validated["organic_status"] = status
        validated["organic_reason"] = o_reason
        validated["organic_confidence"] = o_conf
        validated["organic_lookup_error"] = o_err
        validated["classification_review_required"] = bool(
            o_err or (status == "unknown" and (validated.get("cas_number") or validated.get("title"))))
        results[f"organic_{status}"] = results.get(f"organic_{status}", 0) + 1

        results["total_found"] += 1
        if self.db_sync is not None:
            try:
                sync_result = self.db_sync.upsert_molecule(validated, supplier_id)
                if sync_result == "new":
                    results["new_count"] += 1
                elif sync_result == "updated":
                    results["updated_count"] += 1
            except Exception as exc:  # noqa: BLE001
                results["rejected_sync"] += 1
                results["errors"].append({"file": file_path, "error": f"sync:{exc}"})
                self._record_rejection(validated, "database_sync", f"sync-error:{str(exc)[:200]}")

    def _record_rejection(self, record: dict, stage: str, reason: str) -> None:
        if not self.retain_rejections or self.db_sync is None:
            return
        try:
            self.db_sync.record_rejection(record, stage, reason)
        except Exception:  # noqa: BLE001 (audit must never break the pipeline)
            pass

    @staticmethod
    def page_hash(raw_html: str) -> str:
        return hashlib.sha256(raw_html.encode("utf-8", errors="replace")).hexdigest()

    @staticmethod
    def purity_to_numeric(purity: str) -> Optional[float]:
        m = re.search(r"(\d{2,3}(?:\.\d+)?)\s*%", purity or "")
        return float(m.group(1)) if m else None
