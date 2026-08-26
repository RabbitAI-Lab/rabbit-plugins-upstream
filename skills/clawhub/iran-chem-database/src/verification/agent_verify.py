"""Agent-runnable verification that data comes from Iranian sellers — v2.13.

Purpose
-------
An AI agent consuming this dataset should never have to *trust* that the
suppliers are Iranian. This module lets it **verify and become sure**, by
re-deriving every country conclusion from evidence it can inspect itself.

Three levels, each stricter and slower than the last:

``offline``   Re-check the machine-checkable claims attached to each supplier
              (phone dialling code, ccTLD, Persian script, national-ID check
              digit, postal-code format, currency). No network. Milliseconds.
``live``      Additionally re-fetch each channel's public ``t.me`` page and
              confirm the evidence is still present *right now* — proving the
              attestation is current, not historical.
``paranoid``  ``live`` plus an independent re-derivation of the country from
              the freshly fetched page, ignoring the stored claims entirely.
              This is the mode for an agent that assumes the dataset may be
              wrong or tampered with.

Every level returns the same :class:`AgentVerdict` shape, so an agent can pick
a level by how much it cares and how much latency it can afford, without
changing how it reads the answer.

Design rules
------------
* **Fail closed.** Anything unproven is ``verified=False``. A network error
  during ``live`` never silently downgrades to "probably fine".
* **Independent corroboration.** As in the country gate, admission needs >=2
  claims from *different* evidence families, so one signal can never carry a
  supplier on its own.
* **Disqualifiers win.** A failed ``not_multinational`` claim (or a foreign
  dialling code) rejects the supplier regardless of other evidence.
* **Explain everything.** The verdict lists each claim, whether it passed, and
  why — so the agent can show its work, and a human can audit the agent.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Optional

from src.verification.claims import (IRAN, Claim, check_claim,
                                     check_phone_country_code)

#: Minimum corroborating evidence, mirroring src.discovery.country_gate.
MIN_FAMILIES = 2
MIN_SCORE = 60

LEVELS = ("offline", "live", "paranoid")


@dataclass
class ClaimResult:
    type: str
    value: str
    supported: bool
    detail: str
    family: str
    weight: int

    def as_dict(self) -> dict:
        return {"type": self.type, "value": self.value,
                "supported": self.supported, "detail": self.detail,
                "family": self.family, "weight": self.weight}


@dataclass
class AgentVerdict:
    """What the agent concluded, and exactly why."""
    subject: str
    verified: bool = False
    country: Optional[str] = None
    level: str = "offline"
    score: int = 0
    families: List[str] = field(default_factory=list)
    claims: List[ClaimResult] = field(default_factory=list)
    failures: List[str] = field(default_factory=list)
    live_evidence: Dict[str, object] = field(default_factory=dict)
    reason: str = ""
    checked_at: str = ""

    def as_dict(self) -> dict:
        return {
            "subject": self.subject, "verified": self.verified,
            "country": self.country, "level": self.level, "score": self.score,
            "families": sorted(self.families),
            "claims": [c.as_dict() for c in self.claims],
            "failures": self.failures, "live_evidence": self.live_evidence,
            "reason": self.reason, "checked_at": self.checked_at,
        }

    def explain(self) -> str:
        """Human/agent-readable rationale."""
        head = (f"{'VERIFIED IRANIAN' if self.verified else 'NOT VERIFIED'}: "
                f"{self.subject} (level={self.level}, score={self.score}, "
                f"families={len(set(self.families))})")
        lines = [head, f"  reason: {self.reason}"]
        for c in self.claims:
            lines.append(f"  [{'PASS' if c.supported else 'FAIL'}] "
                         f"{c.type:20} {str(c.value)[:34]:34} {c.detail}")
        for f in self.failures:
            lines.append(f"  [FAIL] {f}")
        return "\n".join(lines)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ---------------------------------------------------------------------------
# Claim construction — turn stored provenance into checkable assertions
# ---------------------------------------------------------------------------

def claims_for_channel(handle: str) -> List[Claim]:
    """Build machine-checkable claims from a channel's stored provenance.

    Prose evidence ("bio says established in Iran") is not a claim; only the
    concrete, re-derivable artefacts are — phone numbers, domains, ratios.
    """
    from src.discovery.social_seed_list import (SOCIAL_CHANNELS,
                                                country_provenance)
    meta = SOCIAL_CHANNELS.get(handle)
    if not meta:
        return []
    prov = country_provenance(handle)
    src = f"t.me/s/{handle}"
    claims: List[Claim] = []

    for sig in prov.get("country_signals") or []:
        name, _, val = str(sig).partition(":")
        name, val = name.strip(), val.strip()
        if name.startswith("phone") and val:
            claims.append(Claim("phone_country_code", val, source=src))
        elif name == "cctld" and val:
            claims.append(Claim("cctld", val, source=src))
        elif name == "irr_pricing":
            claims.append(Claim("irr_currency", "ریال تومان", source=src,
                                note="observed in channel posts"))

    # The channel handle itself must not be a multinational's.
    claims.append(Claim("not_multinational", handle, source=src))

    # Derive further claims from the LOCAL MIRROR when one exists. This is the
    # point of the exercise: the agent re-reads the supplier's own posts rather
    # than trusting our summary of them.
    prov = str(meta.get("country_evidence", "") or "")
    if prov:
        claims.append(Claim("iran_reference", prov, source=src,
                            note="channel bio/provenance statement"))

    mirror = _mirror_signals(handle)
    if mirror.get("phone") and not any(c.type == "phone_country_code"
                                       for c in claims):
        claims.append(Claim("phone_country_code", mirror["phone"], source=src,
                            note="found in mirrored posts"))
    if mirror.get("irr"):
        claims.append(Claim("irr_currency", mirror["irr"], source=src,
                            note="rial/toman pricing in mirrored posts"))
    if mirror.get("postal_code"):
        claims.append(Claim("postal_code", mirror["postal_code"], source=src,
                            note="کد پستی in mirrored posts"))
    if mirror.get("cities"):
        claims.append(Claim("iran_city", mirror["cities"], source=src,
                            note="Iranian city named in mirrored posts"))
    if mirror.get("iran_reference"):
        claims.append(Claim("iran_reference", mirror["iran_reference"],
                            source=src, note="stated in mirrored posts"))
    if mirror.get("national_id"):
        claims.append(Claim("national_id", mirror["national_id"], source=src,
                            note="شناسه ملی in mirrored posts"))

    # Persian is measured over the whole MIRROR, not from a prose note. Sample
    # real post text so the claim is re-derivable; fall back to the recorded
    # ratio when no mirror is present locally.
    if meta.get("language") == "fa":
        sample = _persian_sample(handle)
        ratio = meta.get("persian_ratio")
        if sample:
            claims.append(Claim("persian_text", sample, source=src,
                                note=f"sampled from mirrored posts; "
                                     f"channel persian_ratio={ratio}"))
        elif isinstance(ratio, (int, float)) and ratio >= 0.30:
            # No local mirror: the recorded ratio is the attestation. Marked
            # explicitly so the agent knows this one was not re-derived.
            claims.append(Claim("persian_ratio_attested", str(ratio), source=src,
                                note="no local mirror; recorded ratio used"))
    return claims


def _mirror_dir(handle: str) -> str:
    try:
        from src.config import get_config
        cfg = get_config().as_dict()
        base = (cfg.get("httrack", {}) or {}).get(
            "base_mirror_dir", "/var/lib/iran_chem_db/mirrors")
    except Exception:  # noqa: BLE001
        base = "/var/lib/iran_chem_db/mirrors"
    return os.path.join(base, "social", "telegram", handle)


def _mirror_signals(handle: str, max_posts: int = 400) -> dict:
    """Re-derive checkable artefacts directly from the supplier's own posts."""
    import re
    cdir = _mirror_dir(handle)
    if not os.path.isdir(cdir):
        return {}
    try:
        from src.parser.persian_gate import fa_digits_to_en
        from src.parser.telegram_parser import parse_channel_dir
        posts = parse_channel_dir(cdir, channel=handle)[:max_posts]
    except Exception:  # noqa: BLE001
        return {}
    out: Dict[str, str] = {}
    for post in posts:
        raw = post.get("text") or ""
        t = fa_digits_to_en(raw)
        if "phone" not in out:
            m = re.search(r"(?:\+\s?98|0098)[\s\-()]?\d{2,3}[\s\-()]?\d{3,4}"
                          r"[\s\-]?\d{4}|(?<!\d)09\d{2}[\s\-]?\d{3}[\s\-]?\d{4}(?!\d)",
                          t)
            if m:
                out["phone"] = m.group(0).strip()
        if "irr" not in out and re.search(r"(ریال|تومان)", raw):
            out["irr"] = "ریال/تومان"
        if "postal_code" not in out:
            m = re.search(r"کد\s*پستی\D{0,12}(\d{10})(?!\d)", t)
            if m:
                out["postal_code"] = m.group(1)
        if "national_id" not in out:
            m = re.search(r"شناسه\s*مل[یي]\D{0,12}(\d{11})(?!\d)", t)
            if m:
                out["national_id"] = m.group(1)
        if "iran_reference" not in out:
            m = re.search(r"ایران|\bIran(ian)?\b", raw, re.I)
            if m:
                # Keep the window AROUND the match: slicing the head of the
                # post can cut off the very word that matched, producing a
                # claim that fails its own checker.
                lo, hi = max(0, m.start() - 70), m.end() + 70
                out["iran_reference"] = " ".join(raw[lo:hi].split())
        if "cities" not in out:
            found = _iranian_cities(raw)
            if found:
                out["cities"] = "، ".join(found[:3])
        if len(out) >= 5:
            break
    return out


def _persian_sample(handle: str, max_chars: int = 400) -> str:
    """Pull real Persian text from the local mirror, if one exists."""
    try:
        from src.config import get_config
        cfg = get_config().as_dict()
        base = (cfg.get("httrack", {}) or {}).get(
            "base_mirror_dir", "/var/lib/iran_chem_db/mirrors")
    except Exception:  # noqa: BLE001
        base = "/var/lib/iran_chem_db/mirrors"
    cdir = os.path.join(base, "social", "telegram", handle)
    if not os.path.isdir(cdir):
        return ""
    try:
        from src.parser.persian_gate import persian_char_count
        from src.parser.telegram_parser import parse_channel_dir
        out = []
        for post in parse_channel_dir(cdir, channel=handle):
            t = (post.get("text") or "").strip()
            if persian_char_count(t) >= 10:
                out.append(" ".join(t.split()))
            if sum(len(x) for x in out) >= max_chars:
                break
        return " ".join(out)[:max_chars]
    except Exception:  # noqa: BLE001
        return ""


def _score(results: Iterable[ClaimResult]) -> tuple:
    """Weight = sum of the strongest passing claim per family."""
    best: Dict[str, int] = {}
    for r in results:
        if not r.supported or r.weight <= 0:
            continue
        if r.weight > best.get(r.family, 0):
            best[r.family] = r.weight
    return sum(best.values()), sorted(best)


def _judge(subject: str, results: List[ClaimResult], level: str,
           failures: List[str], live: Optional[dict] = None) -> AgentVerdict:
    v = AgentVerdict(subject=subject, level=level, claims=results,
                     failures=failures, checked_at=_now(),
                     live_evidence=live or {})
    # Disqualifier: an explicit not_multinational failure is fatal.
    dq = [r for r in results if r.type == "not_multinational" and not r.supported]
    if dq:
        v.verified, v.country = False, None
        v.reason = f"disqualified: {dq[0].detail}"
        return v
    # A phone claim that resolves to a FOREIGN country is fatal too.
    for r in results:
        if r.type == "phone_country_code" and not r.supported and "-> " in r.detail:
            other = r.detail.split("-> ")[-1].strip()
            if other and other != IRAN and len(other) == 2:
                v.verified, v.country = False, other
                v.reason = f"disqualified: contact number resolves to {other}"
                return v
    if failures:
        v.verified = False
        v.reason = "; ".join(failures[:3])
        return v

    score, families = _score(results)
    v.score, v.families = score, families
    if not results:
        v.reason = "no checkable claims available (default deny)"
    elif len(families) < MIN_FAMILIES:
        v.reason = (f"insufficient corroboration: {len(families)} evidence "
                    f"family/families ({', '.join(families) or 'none'}), "
                    f"need {MIN_FAMILIES} independent")
    elif score < MIN_SCORE:
        v.reason = f"evidence too weak: score {score} < {MIN_SCORE}"
    else:
        v.verified, v.country = True, IRAN
        v.reason = (f"independently re-verified: {len(families)} evidence "
                    f"families, score {score}, level={level}")
    return v


# ---------------------------------------------------------------------------
# Live re-check
# ---------------------------------------------------------------------------

def _fetch_channel_page(handle: str, timeout: int = 25) -> Optional[str]:
    try:
        import urllib.request
        req = urllib.request.Request(
            f"https://t.me/s/{handle}",
            headers={"User-Agent": "Mozilla/5.0 (IranChemDB agent-verify)"})
        return urllib.request.urlopen(req, timeout=timeout).read().decode(
            "utf-8", "ignore")
    except Exception:  # noqa: BLE001 - unreachable must fail closed, not crash
        return None


def _live_signals(html_text: str) -> dict:
    """Re-derive Iranian signals from a freshly fetched page, from scratch."""
    import html as _html
    import re
    raw = _html.unescape(re.sub(r"<[^>]+>", " ", html_text or ""))
    from src.parser.persian_gate import (fa_digits_to_en, persian_char_count,
                                         post_language)
    # Persian/Arabic-Indic digits are normal in these posts; fold them before
    # matching numbers, but keep `raw` for letter-based checks.
    text = fa_digits_to_en(raw)
    phones = re.findall(
        r"(?:\+\s?98|0098)[\s\-()]?\d{2,3}[\s\-()]?\d{3,4}[\s\-]?\d{4}"
        r"|(?<!\d)09\d{2}[\s\-]?\d{3}[\s\-]?\d{4}(?!\d)"
        # Iranian landlines: 0XX area code + 8-digit subscriber number.
        r"|(?<!\d)0\d{2}[\s\-()]?\d{4}[\s\-]?\d{4}(?!\d)", text)
    # Judge the language on the POST BODIES, not on the raw page: the first
    # few KB of a t.me page are English HTML/CSS boilerplate, which would
    # otherwise mask a wholly Persian channel.
    bodies = re.findall(
        r'<div class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>',
        html_text or "", re.S)
    body_text = _html.unescape(re.sub(r"<[^>]+>", " ", " ".join(bodies)))
    sample = body_text if body_text.strip() else text
    return {
        "reachable": True,
        "persian_chars": persian_char_count(sample),
        "language": post_language(sample[:6000]),
        "posts_sampled": len(bodies),
        "iranian_phones": sorted(set(p.strip() for p in phones))[:5],
        "has_irr": bool(re.search(r"(ریال|تومان)", raw)),
        "mentions_iran": bool(re.search(r"(ایران|Iran|تهران|Tehran)", raw, re.I)),
        "cities": _iranian_cities(raw),
    }


# Bounded by Persian word edges: bare substring matching produces false hits
# (e.g. "ری" inside "دیگری"), which would manufacture evidence that is not there.
_CITIES = ("تهران", "اصفهان", "مشهد", "شیراز", "تبریز", "کرج", "قم", "اهواز",
           "کرمانشاه", "ارومیه", "رشت", "زاهدان", "همدان", "کرمان", "یزد",
           "اردبیل", "بندرعباس", "قزوین", "سنندج", "خرم‌آباد", "شهرری")


def _iranian_cities(text: str) -> list:
    import re
    edge = r"(?<![\u0600-\u06FF])"
    return [c for c in _CITIES
            if re.search(edge + re.escape(c) + r"(?![\u0600-\u06FF])", text)]


def verify_channel(handle: str, *, level: str = "offline",
                   timeout: int = 25) -> AgentVerdict:
    """Verify ONE Telegram channel is an Iranian seller.

    ``level``: ``offline`` | ``live`` | ``paranoid`` (see module docstring).
    """
    if level not in LEVELS:
        raise ValueError(f"level must be one of {LEVELS}")

    from src.discovery.social_seed_list import (SOCIAL_CHANNELS,
                                                is_foreign_channel)
    failures: List[str] = []

    if is_foreign_channel(handle):
        from src.discovery.social_seed_list import foreign_reason
        v = AgentVerdict(subject=handle, level=level, checked_at=_now())
        v.reason = f"on the foreign deny-list: {foreign_reason(handle)}"
        return v
    if handle not in SOCIAL_CHANNELS:
        v = AgentVerdict(subject=handle, level=level, checked_at=_now())
        v.reason = "not a seeded channel — no provenance to verify (default deny)"
        return v

    results = [ClaimResult(type=r["claim"]["type"], value=r["claim"]["value"],
                           supported=r["supported"], detail=r["detail"],
                           family=r["family"], weight=r["weight"])
               for r in (check_claim(c) for c in claims_for_channel(handle))]

    live: dict = {}
    if level in ("live", "paranoid"):
        page = _fetch_channel_page(handle, timeout=timeout)
        if page is None:
            failures.append("live re-check failed: channel page unreachable")
            live = {"reachable": False}
        else:
            live = _live_signals(page)
            if live["language"] not in ("fa", "mixed"):
                failures.append(
                    f"live page language is {live['language']}, not Persian")
            elif level == "live":
                # The live page independently CONFIRMS Persian right now, and
                # may surface contact evidence the stored claims lacked. Credit
                # it — that is the point of paying for a network round-trip.
                if not any(r.type in ("persian_text", "persian_ratio_attested")
                           and r.supported for r in results):
                    results.append(ClaimResult(
                        "persian_text", f"{live['persian_chars']} Persian chars",
                        True, "confirmed Persian on the live page today",
                        "language", 15))
                known = {r.value.strip() for r in results
                         if r.type == "phone_country_code"}
                for ph in live["iranian_phones"]:
                    if ph.strip() in known:
                        continue
                    ok, detail = check_phone_country_code(ph)
                    results.append(ClaimResult(
                        "phone_country_code", ph, ok,
                        f"{detail} (seen live)", "phone", 35))
                    break
                if live.get("cities") and not any(r.type == "iran_city"
                                                  for r in results):
                    results.append(ClaimResult(
                        "iran_city", "، ".join(live["cities"][:3]), True,
                        "Iranian city named on the live page", "location", 30))
                if live.get("mentions_iran") and not any(
                        r.type in ("iran_city", "iran_reference")
                        for r in results):
                    results.append(ClaimResult(
                        "iran_reference", "ایران / Iran", True,
                        "live page states operation in Iran", "location", 15))
                if live["has_irr"] and not any(r.type == "irr_currency"
                                               for r in results):
                    results.append(ClaimResult(
                        "irr_currency", "ریال/تومان", True,
                        "rial/toman pricing on the live page", "currency", 20))
            if level == "paranoid":
                # Ignore stored claims: re-derive everything from this page.
                fresh: List[ClaimResult] = []
                for ph in live["iranian_phones"]:
                    ok, detail = check_phone_country_code(ph)
                    fresh.append(ClaimResult("phone_country_code", ph, ok,
                                             detail, "phone", 35))
                fresh.append(ClaimResult("persian_text",
                                         f"{live['persian_chars']} Persian chars",
                                         live["language"] in ("fa", "mixed"),
                                         f"live language={live['language']}",
                                         "language", 15))
                if live["has_irr"]:
                    fresh.append(ClaimResult("irr_currency", "ریال/تومان", True,
                                             "rial/toman seen on live page",
                                             "currency", 20))
                if live.get("mentions_iran") and not live.get("cities"):
                    fresh.append(ClaimResult(
                        "iran_reference", "ایران / Iran", True,
                        "live page states operation in Iran", "location", 15))
                if live.get("cities"):
                    fresh.append(ClaimResult(
                        "iran_city", "، ".join(live["cities"][:3]), True,
                        "Iranian city named on the live page", "location", 30))
                nm = check_claim(Claim("not_multinational", handle))
                fresh.append(ClaimResult("not_multinational", handle,
                                         nm["supported"], nm["detail"],
                                         "domain", 0))
                if (not live["iranian_phones"] and not live["has_irr"]
                        and not live.get("cities")
                        and not live.get("mentions_iran")):
                    failures.append(
                        "paranoid: live page shows no Iranian phone, IRR pricing or city")
                results = fresh

    return _judge(handle, results, level, failures, live)


def verify_listing_row(row: dict, *, level: str = "offline") -> AgentVerdict:
    """Verify the supplier behind one listing row.

    Accepts a row from the CSV/JSON export (needs at least ``channel``).
    """
    handle = (row or {}).get("channel") or (row or {}).get("supplier") or ""
    if not handle:
        v = AgentVerdict(subject="<unknown>", level=level, checked_at=_now())
        v.reason = "row has no 'channel' field — cannot attribute a supplier"
        return v
    return verify_channel(handle, level=level)


def verify_dataset(rows: Iterable[dict], *, level: str = "offline",
                   timeout: int = 25) -> dict:
    """Verify EVERY supplier appearing in a dataset.

    This is the call an agent makes before using an export: it groups the rows
    by supplier, verifies each one, and reports whether *any* row in the file
    comes from an unverified source.
    """
    rows = list(rows or [])
    by_channel: Dict[str, int] = {}
    for r in rows:
        ch = (r or {}).get("channel") or (r or {}).get("supplier") or "<none>"
        by_channel[ch] = by_channel.get(ch, 0) + 1

    verdicts, unverified_rows = {}, 0
    for ch in sorted(by_channel):
        v = (verify_channel(ch, level=level, timeout=timeout)
             if ch != "<none>" else
             AgentVerdict(subject="<none>", level=level, checked_at=_now(),
                          reason="rows without a supplier attribution"))
        verdicts[ch] = v
        if not v.verified:
            unverified_rows += by_channel[ch]

    all_ok = bool(verdicts) and all(v.verified for v in verdicts.values())
    return {
        "policy": "iranian_sellers_only",
        "level": level,
        "checked_at": _now(),
        "rows_total": len(rows),
        "rows_from_unverified_suppliers": unverified_rows,
        "suppliers_total": len(verdicts),
        "suppliers_verified": sum(1 for v in verdicts.values() if v.verified),
        "all_suppliers_verified_iranian": all_ok,
        "safe_to_use": all_ok and unverified_rows == 0,
        "row_counts": by_channel,
        "verdicts": {k: v.as_dict() for k, v in verdicts.items()},
    }


def load_rows(path: str) -> List[dict]:
    """Load listings from a .csv or .json export produced by this skill."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".json":
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        if isinstance(data, dict):
            return data.get("listings") or data.get("rows") or []
        return data if isinstance(data, list) else []
    import csv
    with open(path, encoding="utf-8-sig", newline="") as fh:
        # The banner comment may be written as a QUOTED csv field ("# ...),
        # so test the first non-quote character, not the raw line start.
        lines = [ln for ln in fh.read().splitlines()
                 if not ln.lstrip().lstrip('"\'').startswith("#")]
    return list(csv.DictReader(lines))


# --------------------------------------------------------------------------
# Row-level attestation: make an exported row carry its own proof.
# --------------------------------------------------------------------------

ATTESTATION_COLUMNS = (
    "supplier_country",
    "supplier_verified",
    "supplier_verify_score",
    "supplier_verify_families",
    "supplier_verify_evidence",
    "supplier_verify_level",
    "supplier_verified_at",
)


def attestation_for(handle: str, *, level: str = "offline",
                    _cache: Optional[dict] = None) -> Dict[str, str]:
    """Return the attestation columns for one supplier handle.

    The point of the ``evidence`` column is that it is not a badge: it lists
    the concrete claims (``phone_country_code:+98…``) that a consuming agent
    can re-check with :func:`src.verification.claims.check_claim` without ever
    trusting this file.
    """
    v = verify_channel(handle, level=level)
    passing = [c for c in v.claims if c.supported and c.weight]
    evidence = "; ".join(f"{c.type}={c.value[:40]}" for c in passing[:5])
    return {
        "supplier_country": v.country or ("IR" if v.verified else ""),
        "supplier_verified": "true" if v.verified else "false",
        "supplier_verify_score": str(v.score),
        "supplier_verify_families": ",".join(sorted(set(v.families))),
        "supplier_verify_evidence": evidence,
        "supplier_verify_level": v.level,
        "supplier_verified_at": v.checked_at,
    }


def attach_attestations(rows: Iterable[dict], *,
                        level: str = "offline") -> List[dict]:
    """Add the attestation columns to every row, verifying each supplier once."""
    rows = list(rows or [])
    cache: Dict[str, Dict[str, str]] = {}
    out: List[dict] = []
    for r in rows:
        r = dict(r or {})
        handle = r.get("channel") or r.get("supplier") or ""
        if handle not in cache:
            cache[handle] = (attestation_for(handle, level=level) if handle
                             else {c: "" for c in ATTESTATION_COLUMNS})
        r.update(cache[handle])
        out.append(r)
    return out
