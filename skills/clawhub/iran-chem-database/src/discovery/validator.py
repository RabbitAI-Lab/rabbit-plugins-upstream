"""SupplierValidator — verify a URL is really an IRANIAN chemical supplier.

v2.11. Scoring alone used to decide admission, which was unsafe: points were
only ever ADDED, so a German vendor whose page said "Tehran office" scored 30
and nothing ever rejected it. Country determination now delegates to
:mod:`src.discovery.country_gate`, which requires >= 2 independent Iranian
signal families AND zero foreign disqualifiers, defaulting to DENY.

:meth:`SupplierValidator.score` is kept for backwards compatibility, but it now
returns 0 for any supplier the country gate refuses — so existing callers that
threshold on ``min_verification_score`` inherit the Iran-only guarantee.
Callers wanting the evidence should use :meth:`verify`.
"""
from __future__ import annotations

import ipaddress
import re
from typing import Tuple
from urllib.parse import urlparse

from src.discovery.country_gate import CountryVerdict
from src.discovery.country_gate import evaluate as evaluate_country
from src.discovery.country_gate import is_iranian_ip

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

    def verify(self, url: str) -> Tuple[float, CountryVerdict, str]:
        """Return ``(score, country_verdict, content)``.

        The score is 0 whenever the country gate rejects the supplier, so a
        foreign vendor can never clear ``min_verification_score``.
        """
        if not url:
            return 0.0, evaluate_country(url="", content=""), ""

        parsed = urlparse(url if "//" in url else "http://" + url)
        host = (parsed.netloc or parsed.path).split("/")[0]
        content = self._fetch_homepage(url)

        ip = ""
        try:  # resolve for supporting hosting evidence only
            import socket
            ip = socket.gethostbyname(host.split(":")[0])
        except Exception:  # noqa: BLE001
            ip = ""

        verdict = evaluate_country(url=url, content=content, ip=ip, source="web_discovery")
        if not verdict.admitted:
            return 0.0, verdict, content

        # Iranian confirmed — now score how good a CHEMICAL supplier it is.
        score = min(float(verdict.score), 70.0)
        if content and CHEMICAL_SIGNALS.search(content):
            score += 30
        return min(score, 100.0), verdict, content

    def score(self, url: str) -> float:
        """Backwards-compatible score. 0 => rejected (foreign or unproven)."""
        return self.verify(url)[0]

    def is_iranian(self, url: str) -> bool:
        return self.verify(url)[1].admitted

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
        """Deprecated: use :func:`src.discovery.country_gate.is_iranian_ip`."""
        return is_iranian_ip(host)

    @staticmethod
    def _is_iranian_ip_legacy(host: str) -> bool:
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
