"""Generic JSON catalogue parser (fix guide §5.3).

Many Iranian storefronts ship product cards via JSON APIs (XHR/GraphQL). The
JS-catalogue capture step persists those API responses next to the mirror;
this parser reads the LOCAL JSON files only and maps common field aliases to
molecule candidate records. Supports list-of-objects, {items/data/rows/list},
and GraphQL-shaped {data:{...}} envelopes.
"""
from __future__ import annotations

import json
import re
from typing import Any, Iterator, List, Optional

_CAS_RE = re.compile(r"\b\d{2,7}-\d{2}-\d\b")
_PURITY_RE = re.compile(r"\b(\d{2,3}(?:\.\d+)?)\s*%")

_TITLE_KEYS = ("title", "name", "name_fa", "name_en", "fa_name", "en_name", "label", "product_name")
_CAS_KEYS = ("cas", "cas_number", "casnumber", "cas_no", "casno", "cas_number_en")
_GRADE_KEYS = ("grade", "grade_label", "purity_grade", "گرید")
_PURITY_KEYS = ("purity", "purity_percent", "خلوص", "purity_text")
_FORMULA_KEYS = ("formula", "molecular_formula", "chemical_formula")
_MW_KEYS = ("mw", "molecular_weight", "molar_mass")
_SMILES_KEYS = ("smiles", "canonical_smiles", "smiles_canonical")
_BRAND_KEYS = ("brand", "brand_name", "manufacturer", "برند")
_SKU_KEYS = ("sku", "code", "product_code", "catalog_number", "cat_no", "merck_code", "id", "mpn")
_PRICE_KEYS = ("price", "price_min", "price_toman", "قیمت", "sell_price", "final_price")
_CURRENCY_KEYS = ("currency", "price_currency", "currency_code")
_AVAIL_KEYS = ("availability", "in_stock", "available", "stock_status", "موجودی")
_URL_KEYS = ("url", "product_url", "link", "href", "permalink")


def _iter_records(node: Any) -> Iterator[dict]:
    """Yield candidate product records from any JSON shape."""
    if isinstance(node, dict):
        # GraphQL envelope: unwrap data layers
        for key in ("data", "products", "items", "rows", "list", "results", "edges"):
            if isinstance(node.get(key), (list, dict)):
                yield from _iter_records(node[key])
                return
        # single product object
        if any(k in node for k in _TITLE_KEYS):
            yield node
        else:
            for v in node.values():
                yield from _iter_records(v)
    elif isinstance(node, list):
        for item in node:
            if isinstance(item, dict):
                if any(k in item for k in _TITLE_KEYS):
                    yield item
                elif "node" in item and isinstance(item["node"], dict):
                    yield from _iter_records(item["node"])
                else:
                    yield from _iter_records(item)


def _pick(record: dict, keys) -> str:
    lowered = {str(k).lower(): v for k, v in record.items()}
    for k in keys:
        v = lowered.get(k.lower())
        if v not in (None, ""):
            return str(v).strip()
    return ""


def _pick_first_text(record: dict, keys) -> Optional[str]:
    for k in keys:
        v = record.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
        if isinstance(v, (int, float)):
            return str(v)
    return None


class JSONCatalogueParser:
    """Parses persisted JSON catalogue responses into molecule candidates."""

    def parse_file(self, file_path: str, supplier_id: int) -> List[dict]:
        if not str(file_path).lower().endswith(".json"):
            return []
        try:
            data = json.loads(open(file_path, encoding="utf-8", errors="replace").read())
        except Exception:  # noqa: BLE001
            return []
        out: List[dict] = []
        for rec in _iter_records(data):
            title = _pick(rec, _TITLE_KEYS)
            if not title:
                continue
            record: dict = {
                "title": title,
                "supplier_id": supplier_id,
                "source_file": file_path,
                "_extraction_method": "json-catalogue",
            }
            cas = _pick(rec, _CAS_KEYS)
            if not cas:
                cas_m = _CAS_RE.search(title + " " + _pick(rec, ("description", "desc", "توضیحات")))
                cas = cas_m.group(0) if cas_m else ""
            record["cas_number"] = cas
            record["grade"] = _pick(rec, _GRADE_KEYS)
            purity = _pick(rec, _PURITY_KEYS)
            if purity:
                record["purity"] = purity
                pm = _PURITY_RE.search(purity)
                if pm:
                    record["purity_numeric"] = float(pm.group(1))
            record["molecular_formula"] = _pick(rec, _FORMULA_KEYS)
            mw = _pick_first_text(rec, _MW_KEYS)
            if mw:
                try:
                    record["molecular_weight"] = float(mw)
                except ValueError:
                    pass
            record["canonical_smiles"] = _pick(rec, _SMILES_KEYS)
            record["brand"] = _pick(rec, _BRAND_KEYS)
            sku = _pick(rec, _SKU_KEYS)
            if sku:
                record["supplier_product_code"] = sku[:200]
                record["sku"] = sku[:200]
            price = _pick_first_text(rec, _PRICE_KEYS)
            if price:
                digits = re.sub(r"[^\d]", "", price)
                if digits and len(digits) <= 12:
                    record["price"] = float(digits)
            record["currency"] = _pick(rec, _CURRENCY_KEYS) or "IRR"
            record["availability_status"] = _pick(rec, _AVAIL_KEYS)
            record["product_url"] = _pick(rec, _URL_KEYS)
            out.append(record)
        return out
