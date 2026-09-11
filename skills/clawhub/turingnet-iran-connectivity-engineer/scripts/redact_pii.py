#!/usr/bin/env python3
"""redact_pii.py — privacy-first evidence redactor for TuringNet (Iran context, FA/EN).

Pipeline: build a normalized copy (Persian/Arabic digits -> ASCII, zero-width
chars removed, Arabic ye/kaf -> Persian) with an index map back to the original,
match PII on the normalized copy, then replace spans in the ORIGINAL text — so
Persian-digit PII (۰۹۱۲…) is redacted while the surrounding Persian text stays
readable. Numeric identifiers are checksum-verified before redaction (Melli
code, Luhn, IBAN mod-97, ICCID) to avoid nuking timestamps and order IDs.

Redacts: Iranian phones, national ID (کد ملی), IMEI, IMSI (432-MCC), SIM ICCID,
bank PAN (Shetab), IBAN/Sheba, IPv4/IPv6, MAC, GPS pairs (keyword-anchored),
emails (obfuscated), bearer/basic tokens, secret assignments, AWS keys.

Verdict JSON with --json. Exit codes: 0 = clean pass, 1 = input error,
2 = residual PII suspicion remains (strict mode). Never networks.
"""
import argparse
import json
import re
import sys

SCHEMA = "turingnet.redaction.v1"

PERSIAN = "۰۱۲۳۴۵۶۷۸۹"
ARABIC = "٠١٢٣٤٥٦٧٨٩"
DIGIT_TABLE = str.maketrans(PERSIAN + ARABIC, "01234567890123456789")
ZW = re.compile(r"[\u200b-\u200f\u2060\ufeff]")
YK = str.maketrans({"ي": "ی", "ك": "ک"})


def build_normalized(text):
    """Return (normalized, idx_map) where idx_map[i] = index in original text
    of normalized char i (ZW chars are dropped from both views)."""
    norm_chars, idx_map = [], []
    stripped = []           # original text minus ZW, and its index map
    stripped_map = []
    for i, ch in enumerate(text):
        if ZW.match(ch):
            continue
        stripped.append(ch)
        stripped_map.append(i)
    s = "".join(stripped)
    s = s.translate(YK).translate(DIGIT_TABLE)
    # translate is 1:1 for our tables (single chars -> single chars)
    return s, stripped_map


# ── checksums: redact only on validity (kills timestamp/order-id false hits) ─
def luhn_ok(digits):
    total, alt = 0, False
    for ch in reversed(digits):
        d = int(ch)
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        alt = not alt
    return total % 10 == 0


def melli_ok(digits):
    if len(digits) != 10 or digits == digits[0] * 10:
        return False
    s = sum(int(digits[i]) * (10 - i) for i in range(9))
    r = s % 11
    return (r if r < 2 else 11 - r) == int(digits[9])


def iban_ok(raw):
    raw = raw.upper()
    if len(raw) != 26 or not raw.startswith("IR"):
        return False
    try:
        n = int("".join(str(int(c, 36)) for c in raw[4:] + raw[:4]))
        return n % 97 == 1
    except ValueError:
        return False


# ── rule table: (type, regex on NORMALIZED text, replacement, validator) ─────
# validator receives the raw matched (normalized) text; return False = keep.
RULES = [
    ("phone-ir",
     r"(?<!\d)(?:(?:\+?98[\s\-.]?|0098[\s\-.]?)?9\d{2}[\s\-.]?\d{3}[\s\-.]?\d{4}|(?:\+?98[\s\-.]?|0098[\s\-.]?|0)\d{2,3}[\s\-.]?\d{4}[\s\-.]?\d{4})(?!\d)",
     "[PHONE]", None),
    # national-id-ir is CONTEXT-ANCHORED: a bare valid checksum is not enough —
    # 10-digit timestamps/order-ids can pass Melli by chance (verified:
    # 1725552000 and 1000000001 are checksum-valid). Redact when a Melli
    # keyword is nearby; otherwise flag as residual so a human decides.
    ("imsi", r"(?<!\d)(432\d{12})(?!\d)", "[IMSI]", None),
    ("imei", r"(?<!\d)(\d{15})(?!\d)", "[IMEI]",
     lambda raw: luhn_ok(raw)),
    ("iccid-sim", r"(?<!\d)(89\d{17,18})(?!\d)", "[SIM]",
     lambda raw: luhn_ok(raw)),
    ("bank-pan", r"(?<!\d)(\d{16})(?!\d)", "[CARD]",
     lambda raw: luhn_ok(raw)),
    ("iban-ir", r"(?<![0-9A-Za-z])(IR\d{24})(?![0-9A-Za-z])", "[IBAN]",
     lambda raw: iban_ok(raw)),
    ("ipv4",
     r"(?<![\d.])(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(?![\d.])",
     "[IPV4]", None),
    ("ipv6", r"(?<![0-9A-Fa-f:])(?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}(?![0-9A-Fa-f:])",
     "[IPV6]", None),
    ("mac", r"(?<![0-9A-Fa-f])(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}(?![0-9A-Fa-f])",
     "[MAC]", None),
    ("bearer-token", r"\b(?:Bearer|Basic)\s+[A-Za-z0-9\-_.~=+/]{16,}\b", "[TOKEN]", None),
    ("secret-assign",
     r"(?i)\b(?:api[_-]?key|apikey|secret|password|passwd|pwd|token|session[_-]?id)\b\s*[:=]\s*['\"]?[^\s'\"]{6,}",
     "[SECRET]", None),
    ("aws-key", r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b", "[AWS-KEY]", None),
]

EMAIL = re.compile(r"\b([A-Za-z0-9._%+-]{1,3})[A-Za-z0-9._%+-]*@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")
GPS = re.compile(
    r"(?i)(?:lat(?:itude)?|long(?:itude)?|lng|موقعیت|عرض|طول)\s*[:=]?\s*"
    r"[-+]?\d{1,3}\.\d{3,}\s*[,;]?\s*"
    r"(?:(?:long(?:itude)?|lng|lat(?:itude)?)\s*[:=]?\s*)?[-+]?\d{1,3}\.\d{3,}")

SYNTHETIC = {
    "[PHONE]": "+98-9XX-XXX-XXXX", "[NID]": "0012345678", "[IMEI]": "000000000000000",
    "[IMSI]": "[IMSI]", "[SIM]": "8900000000000000000", "[CARD]": "0000000000000000",
    "[IBAN]": "IR000000000000000000000000", "[IPV4]": "192.0.2.1", "[IPV6]": "2001:db8::1",
    "[MAC]": "00:00:00:00:00:00", "[GPS]": "35.7,51.4 (city-level)", "[TOKEN]": "[TOKEN]",
    "[SECRET]": "[SECRET]", "[AWS-KEY]": "[AWS-KEY]", "[EMAIL-DOMAIN]": "@example.com",
}

RESIDUAL = [
    (r"(?<![\d.])(?:\d[\s\-.]?){11,}(?![\d.])", "long-digit-run"),
    (r"(?i)\b(?:imei|imsi|iccid|subscriber\s*id|کد\s*ملی|شماره\s*ملی|شبا)\b\s*[:=]?\s*[\d۰-۹]{8,}", "id-context-digits"),
    (r"(?<!\d)\d{10}(?!\d)", "possible-melli-unlabeled"),
]


def redact(text, mode="strict", synthetic=False):
    """Returns (redacted_text, counts, residual)."""
    norm, imap = build_normalized(text)
    spans = []          # (norm_start, norm_end, replacement, ttype)

    def take(pattern, repl, ttype, validator=None):
        for m in re.finditer(pattern, norm):
            raw = m.group(0)
            if validator is not None:
                # validators get the digit-bearing or alnum raw match
                if not validator(raw):
                    continue
            spans.append((m.start(), m.end(), repl, ttype))

    for ttype, rx, repl, validator in RULES:
        take(rx, repl, ttype, validator)

    # national-id-ir (context-anchored variant of the retired bare rule)
    NID_CTX = re.compile(r"(?i)(?:melli|national[\s_-]?id|\bnid\b|کد[\s]*ملی|شماره[\s]*ملی)[^\n]{0,40}?(?<!\d)(\d{10})(?!\d)")
    for m in NID_CTX.finditer(norm):
        if melli_ok(m.group(1)):
            spans.append((m.start(1), m.end(1), "[NID]", "national-id-ir"))
    for m in GPS.finditer(norm):
        spans.append((m.start(), m.end(), "[GPS]", "gps"))
    for m in EMAIL.finditer(norm):
        # full placeholder: partial local-part prefixes and full domains both
        # identify (audit finding v2.3.0) — synthetic mode supplies an example
        spans.append((m.start(), m.end(), "[EMAIL]", "email"))

    # de-overlap: the LONGEST match wins globally (greedy by length, then left);
    # this guarantees a specific long redaction (e.g. "Bearer eyJ...") is never
    # dropped in favour of a shorter overlapping one that would leak its tail.
    spans.sort(key=lambda s: (-(s[1] - s[0]), s[0]))
    final, taken = [], []
    for s in spans:
        if any(t[0] < s[1] and s[0] < t[1] for t in taken):
            continue
        taken.append(s)
        final.append(s)
    final.sort()
    counts = {}
    for _, _, _, ttype in final:
        counts[ttype] = counts.get(ttype, 0) + 1

    # map normalized spans -> original spans; replace right-to-left
    # (build the output on the ZW-stripped original so Persian text stays intact)
    stripped, smap = [], []
    for i, ch in enumerate(text):
        if not ZW.match(ch):
            stripped.append(ch)
            smap.append(i)
    base = "".join(stripped)
    # normalized was built FROM this same stripped sequence; after YK+digit
    # translation lengths match 1:1, so norm index == stripped index.
    edits = []
    for ns, ne, repl, _t in final:
        edits.append((smap[ns], smap[ne - 1] + 1, repl))
    edits.sort(reverse=True)
    for os_, oe_, repl in edits:
        base = base[:os_] + repl + base[oe_:]

    if synthetic:
        for marker, val in SYNTHETIC.items():
            base = base.replace(marker, val)

    residual = []
    if mode == "strict":
        rnorm, _ = build_normalized(base)
        for rx, why in RESIDUAL:
            for m in re.finditer(rx, rnorm):
                residual.append({"type": why, "span": m.group(0)[:24]})
    return base, counts, residual


def main():
    ap = argparse.ArgumentParser(description="TuringNet evidence redactor (FA/EN)")
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", default="-")
    ap.add_argument("--mode", choices=["strict", "standard"], default="strict")
    ap.add_argument("--synthetic", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        with open(args.input, "r", encoding="utf-8", errors="replace") as f:
            raw = f.read()
    except Exception as e:
        print(json.dumps({"schema": SCHEMA, "error": f"cannot read input: {e}"}))
        return 1
    red, counts, residual = redact(raw, args.mode, args.synthetic)
    if args.output == "-":
        sys.stdout.write(red + "\n")
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(red)
    verdict = {"schema": SCHEMA, "file_in": args.input, "file_out": args.output,
               "mode": args.mode, "synthetic": bool(args.synthetic),
               "replacements": dict(sorted(counts.items())),
               "total_replacements": sum(counts.values()),
               "residual_suspects": residual[:20]}
    if args.json:
        print(json.dumps(verdict, indent=1))
    else:
        sys.stderr.write(f"[redactor] {verdict['total_replacements']} replacements "
                         f"{verdict['replacements']}\n")
        if residual:
            sys.stderr.write(f"[redactor] residual suspicion: {residual[:5]}\n")
    return 2 if (args.mode == "strict" and residual) else 0


if __name__ == "__main__":
    sys.exit(main())
