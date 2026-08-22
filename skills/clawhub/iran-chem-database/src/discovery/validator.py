"""SupplierValidator — score whether a URL is really an Iranian chemical supplier.

Signals (spec §2.2 validate_supplier):
  1. .ir TLD or Iranian IP range
  2. page content mentions chemical products
  3. contact info shows Iranian address/phone
  Returns a confidence score 0-100.
"""
from __future__ import annotations

import ipaddress
import re
from urllib.parse import urlparse

CHEMICAL_SIGNALS = re.compile(
    r"(chemical|reagent|laboratory|chemicals|مواد شیمیایی|آزمایشگاه|آزمایشگاهی|"
    r"شیمی|reactive|solvent|حلال|خلوص|گرید)",
    re.I,
)
IRAN_PHONE_SIGNALS = re.compile(r"(\+98|0098|\(0?2[0-9]\)|\b0[0-9]{2}\s?[0-9]{7,8})")
IRAN_ADDRESS_SIGNALS = re.compile(
    r"\b(Tehran|Isfahan|Karaj|Mashhad|Tabriz|Shiraz|Tehran|Iran|تهران|اصفهان|کرج|مشهد)\b",
    re.I,
)


class SupplierValidator:
    def __init__(self, timeout: int = 15):
        self.timeout = timeout

    def score(self, url: str) -> float:
        if not url:
            return 0.0
        score = 0.0
        parsed = urlparse(url)
        host = parsed.netloc or parsed.path

        if host.endswith(".ir"):
            score += 40
        elif self._is_iranian_ip(host):
            score += 40

        content = self._fetch_homepage(url)
        if content:
            if CHEMICAL_SIGNALS.search(content):
                score += 30
            if IRAN_PHONE_SIGNALS.search(content) or IRAN_ADDRESS_SIGNALS.search(content):
                score += 30
        else:
            score += 10  # unreachable — weak signal only

        return min(score, 100.0)

    def _fetch_homepage(self, url: str) -> str:
        try:
            import requests
            resp = requests.get(url, timeout=self.timeout,
                                headers={"User-Agent": "IranChemDB/1.0 validator"})
            if resp.status_code < 400:
                return resp.text[:200_000]
        except Exception:  # noqa: BLE001
            pass
        return ""

    @staticmethod
    def _is_iranian_ip(host: str) -> bool:
        try:
            ip = ipaddress.ip_address(host)
        except ValueError:
            return False
        # Common Iranian IPv4 ranges (indicative, not exhaustive)
        for cidr in ("5.52.0.0/16", "5.234.128.0/19", "31.14.80.0/20", "37.148.0.0/17",
                     "46.209.0.0/16", "62.60.128.0/17", "78.38.0.0/15", "85.185.0.0/16",
                     "91.98.0.0/15", "109.125.128.0/18", "151.232.0.0/14", "178.131.0.0/16",
                     "185.116.160.0/22", "188.158.0.0/15", "213.176.0.0/17", "217.218.0.0/15"):
            if ip in ipaddress.ip_network(cidr):
                return True
        return False
