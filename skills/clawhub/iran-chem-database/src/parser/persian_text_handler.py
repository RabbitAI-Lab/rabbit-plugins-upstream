"""Persian text extraction & normalization for mirrored pages (spec §4.2)."""
from __future__ import annotations

from src.utils.persian_utils import (
    extract_persian_chemical_names,
    normalize_fa,
)


class PersianTextHandler:
    def normalize(self, text: str) -> str:
        return normalize_fa(text or "")

    def extract_chemical_names(self, text: str) -> list[str]:
        return extract_persian_chemical_names(text or "")

    def extract_price_rial(self, text: str) -> float | None:
        """Extract a Rial price from Persian text (e.g. 'قیمت: ۵۰۰,۰۰۰ تومان')."""
        import re
        norm = normalize_fa(text or "")
        # تومان (toman) = 10 rial; try toman first, then rial
        m = re.search(r"([\d,]+)\s*(?:هزار\s*)?تومان", norm)
        if m:
            value = float(m.group(1).replace(",", ""))
            return value * 10
        m = re.search(r"([\d,]+)\s*ریال", norm)
        if m:
            return float(m.group(1).replace(",", ""))
        return None

    def bidi(self, text: str) -> str:
        """Wrap text with RTL marks for safe embedding in HTML/RTL UIs."""
        return f"\u200f{text}\u200f" if text else ""
