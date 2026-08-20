"""HTML product-page parser — BeautifulSoup on LOCAL mirror files (spec §4.2)."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import List, Optional

from bs4 import BeautifulSoup

from src.parser.persian_text_handler import PersianTextHandler
from src.utils.persian_utils import normalize_fa

_persian = PersianTextHandler()


class HTMLProductParser:
    def parse_file(self, file_path: str, supplier_id: int) -> List[dict]:
        with open(file_path, encoding="utf-8", errors="replace") as fh:
            html_content = fh.read()
        soup = BeautifulSoup(html_content, "lxml")
        molecules: List[dict] = []

        molecules.extend(self._parse_json_ld(soup))
        molecules.extend(self._parse_tables(soup))
        molecules.extend(self._parse_product_blocks(soup))
        molecules.extend(self._parse_persian(soup))

        for mol in molecules:
            mol["supplier_id"] = supplier_id
            mol["source_file"] = file_path
        return molecules

    # ── strategy 1: schema.org / JSON-LD ──────────────────────────────────
    def _parse_json_ld(self, soup: BeautifulSoup) -> List[dict]:
        out: List[dict] = []
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.string or "")
            except (json.JSONDecodeError, TypeError):
                continue
            items = data if isinstance(data, list) else [data]
            for item in items:
                if not isinstance(item, dict):
                    continue
                if item.get("@type") not in ("Product", "ChemicalSubstance"):
                    continue
                out.append({
                    "title": item.get("name", ""),
                    "description": item.get("description", ""),
                    "brand": (item.get("brand") or {}).get("name", "") if isinstance(item.get("brand"), dict) else item.get("brand", ""),
                    "price": _first_offer_price(item),
                    "product_url": item.get("url", ""),
                })
        return out

    # ── strategy 2: product tables ────────────────────────────────────────
    def _parse_tables(self, soup: BeautifulSoup) -> List[dict]:
        out: List[dict] = []
        for table in soup.find_all("table"):
            headers = [normalize_fa(th.get_text()) for th in table.find_all("th")]
            for row in table.find_all("tr"):
                cells = [normalize_fa(td.get_text()) for td in row.find_all("td")]
                if not cells:
                    continue
                mol = self._row_to_molecule(headers, cells)
                if mol:
                    out.append(mol)
        return out

    _KEY_ALIASES = {
        "cas": "cas_number", "cas number": "cas_number", "casno": "cas_number",
        "name": "title", "product": "title", "product name": "title", "ماده": "title", "نام": "title",
        "formula": "molecular_formula", "molecular formula": "molecular_formula", "فرمول": "molecular_formula",
        "mw": "molecular_weight", "molecular weight": "molecular_weight",
        "purity": "purity", "grade": "grade", "درجه": "grade", "خلوص": "purity",
    }

    @staticmethod
    def _row_to_molecule(headers: List[str], cells: List[str]) -> Optional[dict]:
        record = {"title": "", "description": ""}
        for i, cell in enumerate(cells):
            key = headers[i].lower() if i < len(headers) else f"col{i}"
            key = HTMLProductParser._KEY_ALIASES.get(key, key)
            record[key] = cell
        # Require at least a name-like value and a grade/purity signal
        has_name = any(len(str(v)) > 2 for k, v in record.items()
                       if k in ("title", "molecular_formula") or k in ("ماده", "نام"))
        has_grade = any(k in record for k in ("grade", "purity"))
        if has_name and has_grade:
            record["title"] = record.get("title") or next(iter(cells), "")
            return record
        return None

    # ── strategy 3: product blocks ────────────────────────────────────────
    _PRODUCT_SELECTORS = [
        {"class_": re.compile(r"product|item", re.I)},
        {"itemprop": "name"},
    ]

    def _parse_product_blocks(self, soup: BeautifulSoup) -> List[dict]:
        out: List[dict] = []
        blocks = set()
        for sel in self._PRODUCT_SELECTORS:
            blocks.update(soup.find_all(**sel))
        for block in blocks:
            text = normalize_fa(block.get_text(" ", strip=True))
            mol = self._extract_from_text_block(text)
            if mol:
                out.append(mol)
        return out

    def _extract_from_text_block(self, text: str) -> Optional[dict]:
        if len(text) < 3:
            return None
        cas = re.search(r"\b\d{2,7}-\d{2}-\d\b", text)
        grade = re.search(
            r"(ACS|HPLC|GC|reagent|analytical|research|extra\s*pure|for\s*synthesis|"
            r"درجه\s*[آا]زمایشگاهی|گرید\s*[آا]زمایشگاهی|خلوص)", text, re.I)
        if not (cas or grade):
            return None
        return {
            "title": text[:120],
            "cas_number": cas.group(0) if cas else "",
            "grade": grade.group(0) if grade else "",
        }

    # ── strategy 4: Persian text extraction ───────────────────────────────
    def _parse_persian(self, soup: BeautifulSoup) -> List[dict]:
        text = normalize_fa(soup.get_text(" ", strip=True))
        names = _persian.extract_chemical_names(text)
        out = []
        for name in names[:20]:
            out.append({"title": name, "persian_name": name})
        return out


def _first_offer_price(item: dict) -> Optional[float]:
    try:
        offers = item.get("offers") or {}
        if isinstance(offers, dict):
            offers = offers.get("offers", offers)
        if isinstance(offers, list):
            offers = offers[0] if offers else {}
        price = offers.get("price") or offers.get("lowPrice")
        return float(price) if price is not None else None
    except (TypeError, ValueError):
        return None
