"""Excel/CSV catalog parser — openpyxl/pandas on LOCAL mirror files (spec §4.2)."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import List

# candidate column-name mappings (lowercased)
COLUMN_ALIASES = {
    "name": ["name", "product", "product name", "title", "ماده", "نام ماده", "نام"],
    "cas": ["cas", "cas number", "cas no", "cas_number", "casno", "شماره cas"],
    "formula": ["formula", "molecular formula", "chemical formula", "فرمول"],
    "mw": ["mw", "molecular weight", "mol weight", "وزن مولکولی"],
    "grade": ["grade", "purity grade", "quality", "درجه", "گرید"],
    "purity": ["purity", "assay", "خلوص", "درصد خلوص"],
    "price": ["price", "price (irr)", "قیمت", "قیمت (ریال)"],
    "brand": ["brand", "manufacturer", "برند"],
    "pack": ["pack", "pack size", "package", "بسته بندی"],
}


class ExcelCatalogParser:
    def parse_file(self, file_path: str, supplier_id: int) -> List[dict]:
        ext = Path(file_path).suffix.lower()
        if ext == ".csv":
            return self._parse_csv(file_path, supplier_id)
        return self._parse_excel(file_path, supplier_id)

    def _parse_excel(self, file_path: str, supplier_id: int) -> List[dict]:
        import pandas as pd

        molecules: List[dict] = []
        sheets = pd.read_excel(file_path, sheet_name=None)
        for _, sheet_df in sheets.items():
            if sheet_df.empty:
                continue
            col_map = self.detect_column_mapping(list(sheet_df.columns))
            if not col_map.get("name"):
                continue
            for _, row in sheet_df.iterrows():
                mol = self._row_to_molecule(row, col_map)
                if mol:
                    mol["supplier_id"] = supplier_id
                    mol["source_file"] = file_path
                    molecules.append(mol)
        return molecules

    def _parse_csv(self, file_path: str, supplier_id: int) -> List[dict]:
        molecules: List[dict] = []
        with open(file_path, encoding="utf-8", errors="replace", newline="") as fh:
            reader = csv.DictReader(fh)
            if not reader.fieldnames:
                return molecules
            col_map = self.detect_column_mapping(list(reader.fieldnames))
            if not col_map.get("name"):
                return molecules
            for row in reader:
                mol = self._row_to_molecule(row, col_map)
                if mol:
                    mol["supplier_id"] = supplier_id
                    mol["source_file"] = file_path
                    molecules.append(mol)
        return molecules

    @staticmethod
    def detect_column_mapping(columns: List[str]) -> dict:
        """Return {field: column_name}. Works for both DataFrames and dict rows."""
        mapping: dict = {}
        for col in columns:
            low = str(col).strip().lower()
            for target, aliases in COLUMN_ALIASES.items():
                if target not in mapping and any(a in low for a in aliases):
                    mapping[target] = str(col)
        return mapping

    @staticmethod
    def _row_to_molecule(row, col_map: dict) -> dict | None:
        def get(field):
            col_name = col_map.get(field)
            if col_name is None:
                return ""
            try:
                if hasattr(row, "iloc"):          # pandas Series
                    val = row[col_name]
                else:                             # csv dict
                    val = row.get(col_name, "")
            except (IndexError, KeyError, TypeError):
                return ""
            if val is None:
                return ""
            if isinstance(val, float):
                if val != val:  # NaN
                    return ""
                return str(val).rstrip("0").rstrip(".") if val.is_integer() else str(val)
            return str(val).strip()

        name = get("name")
        cas = get("cas")
        if not name or not (cas or get("formula")):
            return None
        record = {
            "title": name,
            "cas_number": cas,
            "molecular_formula": get("formula"),
            "molecular_weight": get("mw"),
            "grade": get("grade"),
            "purity": get("purity"),
            "brand": get("brand"),
            "pack_sizes": [get("pack")] if get("pack") else [],
        }
        price_raw = get("price")
        try:
            record["price"] = float(str(price_raw).replace(",", "").replace("٬", "")) if price_raw else None
        except ValueError:
            record["price"] = None
        import re
        m = re.search(r"(\d{2,3}(?:\.\d+)?)\s*%", record["purity"] or "")
        if m:
            record["purity_numeric"] = float(m.group(1))
        return record
