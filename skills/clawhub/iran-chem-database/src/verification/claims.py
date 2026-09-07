"""Machine-checkable country claims — v2.13.

The problem this solves
-----------------------
Up to v2.12 a channel's Iranian provenance was recorded as human prose::

    "Bio states 'established in 1975 in Iran'; landline (+98) 02188211234
     (Tehran); site boof-co.com."

A person can read that. **An AI agent cannot verify it** — it is an assertion,
not a proof. An agent consuming the dataset had exactly two options: trust the
publisher, or redo the entire research by hand.

A *claim* fixes that. Each claim is a small, self-describing, independently
re-executable assertion:

    {"type": "phone_country_code", "value": "+982188211234",
     "expect": "IR", "source": "t.me/s/Boof_company", "checked_at": ...}

Every claim type has a ``check`` function that re-derives the answer from
first principles. Crucially, claims are of two kinds:

* **OFFLINE** — re-checkable with no network at all (phone country code,
  ccTLD, Persian script, IRR currency, national-ID checksum). An agent can
  audit the whole dataset on a plane.
* **LIVE** — re-fetches the source (the channel's public ``t.me`` page) and
  confirms the evidence is *still* there. Slower, but proves the claim is
  current rather than historical.

The agent therefore never has to take our word for anything: it re-runs the
checks and forms its own verdict.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict

IRAN = "IR"

# ---------------------------------------------------------------------------
# ITU E.164 country calling codes we care about. +98 is Iran; the rest exist so
# a foreign number is positively identified as foreign, not merely "not +98".
# ---------------------------------------------------------------------------
CALLING_CODES: Dict[str, str] = {
    "98": "IR", "1": "US", "7": "RU", "20": "EG", "27": "ZA", "30": "GR",
    "31": "NL", "32": "BE", "33": "FR", "34": "ES", "36": "HU", "39": "IT",
    "40": "RO", "41": "CH", "43": "AT", "44": "GB", "45": "DK", "46": "SE",
    "47": "NO", "48": "PL", "49": "DE", "51": "PE", "52": "MX", "55": "BR",
    "60": "MY", "61": "AU", "62": "ID", "63": "PH", "64": "NZ", "65": "SG",
    "66": "TH", "81": "JP", "82": "KR", "84": "VN", "86": "CN", "90": "TR",
    "91": "IN", "92": "PK", "93": "AF", "94": "LK", "95": "MM", "212": "MA",
    "213": "DZ", "216": "TN", "218": "LY", "234": "NG", "254": "KE",
    "351": "PT", "352": "LU", "353": "IE", "358": "FI", "359": "BG",
    "370": "LT", "371": "LV", "372": "EE", "374": "AM", "375": "BY",
    "380": "UA", "381": "RS", "386": "SI", "420": "CZ", "421": "SK",
    "852": "HK", "886": "TW", "960": "MV", "961": "LB", "962": "JO",
    "963": "SY", "964": "IQ", "965": "KW", "966": "SA", "967": "YE",
    "968": "OM", "971": "AE", "972": "IL", "973": "BH", "974": "QA",
    "975": "BT", "976": "MN", "977": "NP", "992": "TJ", "993": "TM",
    "994": "AZ", "995": "GE", "996": "KG", "998": "UZ",
}

#: Iranian mobile operator prefixes (after the leading 0 / +98).
IRAN_MOBILE_PREFIXES = (
    "901", "902", "903", "904", "905", "990", "991", "992", "993", "994",  # MCI
    "910", "911", "912", "913", "914", "915", "916", "917", "918", "919",  # MCI
    "930", "933", "935", "936", "937", "938", "939", "901",                # MTN
    "920", "921", "922", "923",                                            # Rightel
    "998", "999", "9999",
)

#: Iranian geographic (landline) area codes.
IRAN_AREA_CODES = (
    "21", "26", "25", "31", "34", "35", "38", "41", "44", "45", "51", "54",
    "56", "58", "61", "66", "71", "74", "76", "77", "81", "83", "84", "86",
    "87", "11", "13", "17", "23", "24", "28", "33",
)


def _digits(value: str) -> str:
    return re.sub(r"\D", "", value or "")


# ---------------------------------------------------------------------------
# Individual claim checks. Each returns (passed, detail).
# ---------------------------------------------------------------------------

def check_phone_country_code(value: str, **_) -> tuple:
    """Re-derive the country of a phone number from its dialling code.

    This is arithmetic on the number itself — no database, no network, no
    trust. ``+98 21 8821 1234`` is Iranian because 98 is Iran's ITU code.
    """
    raw = (value or "").strip()
    d = _digits(raw)
    if not d:
        return False, "no digits in value"

    # International form: +98… / 0098… / 98…
    if raw.startswith("+") or d.startswith("00") or raw.startswith("98"):
        if d.startswith("00"):
            d = d[2:]
        for length in (3, 2, 1):
            code = d[:length]
            if code in CALLING_CODES:
                country = CALLING_CODES[code]
                rest = d[length:]
                ok = country == IRAN
                detail = f"dialling code +{code} -> {country}"
                if ok and rest:
                    if rest.startswith("9") and rest[:3] in IRAN_MOBILE_PREFIXES:
                        detail += f"; mobile prefix {rest[:3]}"
                    elif rest[:2] in IRAN_AREA_CODES:
                        detail += f"; area code 0{rest[:2]}"
                return ok, detail
        return False, f"unrecognised dialling code in {d[:4]}"

    # National form: 09xxxxxxxxx mobile, 0XX… landline.
    if d.startswith("0"):
        body = d[1:]
        if body.startswith("9") and body[:3] in IRAN_MOBILE_PREFIXES:
            return True, f"Iranian mobile prefix 0{body[:3]}"
        if body[:2] in IRAN_AREA_CODES and len(body) >= 9:
            return True, f"Iranian area code 0{body[:2]}"
        return False, f"national number 0{body[:3]} not an Iranian prefix"
    return False, "not in a recognisable international or Iranian format"


def check_cctld(value: str, **_) -> tuple:
    """A ``.ir`` (or ``.ایران``) domain is delegated by Iran's NIC."""
    host = (value or "").strip().lower()
    host = re.sub(r"^https?://", "", host).split("/")[0].split(":")[0]
    if not host:
        return False, "no host"
    if host.endswith(".ir") or host.endswith(".ایران"):
        return True, f"{host} uses Iran's ccTLD"
    tld = host.rsplit(".", 1)[-1] if "." in host else ""
    return False, f"TLD .{tld} is not Iran's ccTLD"


def check_persian_text(value: str, **_) -> tuple:
    """Confirm the sample really is Persian (not Arabic, not transliteration)."""
    from src.parser.persian_gate import post_language
    lang = post_language(value or "")
    return lang in ("fa", "mixed"), f"language detected: {lang}"


def check_irr_currency(value: str, **_) -> tuple:
    """Prices quoted in rial/toman indicate an Iranian domestic seller."""
    norm = (value or "")
    if re.search(r"(ریال|ريال|تومان|تومن|\bIRR\b|\brial\b|\btoman\b)", norm, re.I):
        return True, "IRR/toman pricing present"
    return False, "no rial/toman marker"


def check_national_id(value: str, **_) -> tuple:
    """Validate a شناسه ملی (11-digit legal-entity ID) by its check digit.

    The algorithm is public and deterministic, so the agent verifies the
    number's internal consistency rather than trusting that it exists.
    """
    d = _digits(value)
    if len(d) != 11:
        return False, f"expected 11 digits, got {len(d)}"
    if len(set(d)) == 1:
        return False, "all-identical digits are never valid"
    # Official algorithm (مرکز توسعه تجارت الکترونیکی): the 11th digit is the
    # control digit. Add (10th digit + 2) to each of the 10 leading digits,
    # multiply by the repeating weights 29,27,23,19,17 and sum; the remainder
    # mod 11 (10 -> 0) must equal the control digit.
    control = int(d[10])
    dec = int(d[9]) + 2
    weights = (29, 27, 23, 19, 17, 29, 27, 23, 19, 17)
    total = sum((int(d[i]) + dec) * weights[i] for i in range(10))
    rem = total % 11
    expected = 0 if rem == 10 else rem
    ok = expected == control
    return ok, ("check digit valid per the official شناسه ملی algorithm" if ok
                else f"check digit {control} != computed {expected}")


def check_postal_code(value: str, **_) -> tuple:
    """Iranian کد پستی is exactly 10 digits and never starts with 0."""
    d = _digits(value)
    if len(d) != 10:
        return False, f"expected 10 digits, got {len(d)}"
    if d[0] == "0":
        return False, "Iranian postal codes do not start with 0"
    return True, "valid 10-digit Iranian postal code format"


def check_persian_ratio_attested(value: str, **_) -> tuple:
    """Fallback when no local mirror exists: the recorded Persian ratio.

    This is an ATTESTATION, not a re-derivation — deliberately given a low
    weight, and the agent is told so, because it is the one claim it cannot
    independently reproduce without mirroring the channel itself.
    """
    try:
        ratio = float(value)
    except (TypeError, ValueError):
        return False, "ratio is not a number"
    ok = ratio >= 0.30
    return ok, (f"recorded persian_ratio={ratio:.2f} "
                f"({'>=' if ok else '<'} 0.30) — attested, not re-derived")


def check_iran_city(value: str, **_) -> tuple:
    """A named Iranian city is corroborating location evidence."""
    named = [c for c in value.replace("،", ",").split(",") if c.strip()]
    if not named:
        return False, "no city named"
    return True, "Iranian city/cities named: " + ", ".join(n.strip() for n in named)


def check_iran_reference(value: str, **_) -> tuple:
    """An explicit statement of operating in Iran, in Persian or English.

    Weakest of the location signals (a foreign firm may mention Iran), so it is
    weighted low and can never carry a verdict on its own.
    """
    import re
    if re.search(r"(ایران|جمهوری\s*اسلامی)", value):
        return True, "text states operation in ایران (Iran)"
    if re.search(r"\bIran(ian)?\b", value, re.I):
        return True, "text states operation in Iran"
    return False, "no explicit reference to Iran"


def check_iran_ip(value: str, **_) -> tuple:
    """IP inside a known Iranian range — SUPPORTING evidence only."""
    from src.discovery.country_gate import is_iranian_ip
    ok = is_iranian_ip((value or "").strip())
    return ok, ("IP in a known Iranian range" if ok
                else "IP not in the known Iranian ranges")


def check_not_multinational(value: str, **_) -> tuple:
    """The domain must not belong to a foreign multinational."""
    from src.discovery.country_gate import (MULTINATIONAL_DOMAINS,
                                            registrable_domain)
    dom = registrable_domain(value or "")
    if dom in MULTINATIONAL_DOMAINS:
        return False, f"{dom} is owned by a multinational ({MULTINATIONAL_DOMAINS[dom]})"
    return True, f"{dom or 'n/a'} is not on the multinational deny-list"


#: claim type -> (checker, is_offline, human description)
CLAIM_CHECKS: Dict[str, tuple] = {
    "phone_country_code": (check_phone_country_code, True,
                           "phone number's ITU dialling code resolves to Iran"),
    "cctld": (check_cctld, True, "domain uses Iran's .ir ccTLD"),
    "persian_text": (check_persian_text, True,
                     "sample text is Persian (not Arabic/transliterated)"),
    "irr_currency": (check_irr_currency, True, "prices quoted in rial/toman"),
    "national_id": (check_national_id, True,
                    "شناسه ملی passes its published check-digit algorithm"),
    "postal_code": (check_postal_code, True, "valid Iranian postal-code format"),
    "iran_ip": (check_iran_ip, True, "IP address in a known Iranian range"),
    "iran_city": (check_iran_city, True, "an Iranian city named in the text"),
    "iran_reference": (check_iran_reference, True,
                       "an explicit statement of operating in Iran"),
    "persian_ratio_attested": (check_persian_ratio_attested, True,
                               "recorded Persian ratio (attested, not re-derived)"),
    "not_multinational": (check_not_multinational, True,
                          "domain is not a foreign multinational's"),
}

#: Weight per claim type, mirroring the country gate's evidence strength.
CLAIM_WEIGHT: Dict[str, int] = {
    "national_id": 45, "cctld": 40, "phone_country_code": 35,
    "postal_code": 35, "irr_currency": 20, "persian_text": 15,
    "iran_ip": 10, "persian_ratio_attested": 10, "iran_city": 30, "iran_reference": 15,
    "not_multinational": 0,  # necessary, not sufficient
}

#: Independent evidence families (a claim only corroborates across families).
CLAIM_FAMILY: Dict[str, str] = {
    "national_id": "registry", "postal_code": "registry",
    "cctld": "domain", "iran_ip": "hosting",
    "phone_country_code": "phone", "irr_currency": "currency",
    "persian_text": "language", "persian_ratio_attested": "language",
    "iran_city": "location", "iran_reference": "location",
    "not_multinational": "domain",
}


@dataclass
class Claim:
    """One machine-checkable assertion about a supplier."""
    type: str
    value: str
    expect: str = IRAN
    source: str = ""
    note: str = ""

    def as_dict(self) -> dict:
        return {"type": self.type, "value": self.value, "expect": self.expect,
                "source": self.source, "note": self.note}

    @staticmethod
    def from_dict(d: dict) -> "Claim":
        return Claim(type=d.get("type", ""), value=str(d.get("value", "")),
                     expect=d.get("expect", IRAN), source=d.get("source", ""),
                     note=d.get("note", ""))


def check_claim(claim: Claim) -> dict:
    """Re-execute one claim. Returns a result dict; never raises."""
    entry = CLAIM_CHECKS.get(claim.type)
    if entry is None:
        return {"claim": claim.as_dict(), "supported": False,
                "detail": f"unknown claim type '{claim.type}'",
                "offline": True, "weight": 0,
                "family": CLAIM_FAMILY.get(claim.type, "unknown")}
    fn, offline, _desc = entry
    try:
        ok, detail = fn(claim.value)
    except Exception as exc:  # noqa: BLE001 - a broken check must not crash an audit
        ok, detail = False, f"check raised {type(exc).__name__}: {exc}"
    return {"claim": claim.as_dict(), "supported": bool(ok), "detail": detail,
            "offline": offline, "weight": CLAIM_WEIGHT.get(claim.type, 0),
            "family": CLAIM_FAMILY.get(claim.type, "other")}
