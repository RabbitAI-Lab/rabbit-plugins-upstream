#!/usr/bin/env python3
"""safety_validator.py — deterministic safety gate for SpeechCanvas prompt packs.

Verdicts (machine-readable JSON on stdout):
  pass  → exit 0   block → exit 1   warn  → exit 2

Reads a prompt pack (JSON) or plain text from --file, --text or stdin.
Read-only: never writes, never networks, never touches user state.

Usage:
  python3 scripts/safety_validator.py --file pack.json
  python3 scripts/safety_validator.py --text "prompt text"
  echo "text" | python3 scripts/safety_validator.py
  python3 scripts/safety_validator.py --selftest
"""
import argparse
import json
import re
import sys

# ── forbidden mechanics (mirrors references/rules.md — keep both in sync) ──
F = [
    ("F01", "block", r"(?:\bfake[ds]?\b|\bforg(?:e[ds]?|ing|ery)\b|\bcounterfeit\b|\bfabricat(?:e[ds]?|ed|ion)\b|\bfalsif(?:ie[ds]?|ied|ication)\b)",
     r"\b(?:evidence|document|doc|passport|id\s?card|driver'?s?\s?licen[cs]e|ballot|certificate|receipt|invoice|screenshot|admission|confession|legal\s+notice|news\s+(?:report|story|article)|breaking\s+news|headline|signature|banknote|currency|stamp|seal)\b",
     "fake/forged/counterfeit documents, evidence, IDs, receipts, screenshots, admissions"),
    ("F02", "block", r"\b(?:photoreal(?:istic)?|photo-real|hyperrealistic|lifelike|indistinguishable\s+from\s+(?:a\s+)?(?:real\s+)?photo|(?:realistic\s+)?photo(?:graph|graphic)?\s+of)\b",
     r"\b(?:real\s+(?:person|people|public\s+figure|politician|celebrity|president|minister|senator|leader)|named\s+(?:person|individual)|the\s+(?:president|minister|senator))\b.{0,100}?\b(?:doing\s+(?:things|something)\s+(?:they|he|she)\s+(?:did\s?n[o']t|never\s+did)|saying\s+(?:things|words)\s+(?:they|he|she)\s+never|that\s+never\s+(?:happened|occurred|took\s+place)|(?:accepting|taking|receiving)\s+(?:bribes?|payments?|money))",
     "photoreal/photo of real people doing/saying things they didn't"),
    ("F03", "block", r"\b(?:real\s+name|official\s+(?:seal|emblem|insignia)|state\s+seal|government\s+seal|readable\s+(?:civic\s+|voting\s+)?instructions?|how\s+to\s+vote|ballot\s+instructions?|voting\s+instructions?|real\s+(?:public\s+)?(?:figures?|persons?|people|politicians?|celebrities?|presidents?|ministers?|senators?))\b",
     None, "real names/likenesses, official seals, readable civic/voting instructions, real public figures"),
    ("F04", "block", r"\b(?:hoax|fabricated|staged|misleading|invented)\b.{0,60}?\b(?:news|report|footage|broadcast|headline|story)\b|\b(?:presented|passed\s+off|passed\s+as)\b.{0,30}?\b(?:as\s+)?(?:real|authentic|genuine|breaking)\b",
     None, "hoax/fabricated content presented as real news"),
    ("F05", "block", r"\b(?:misleading|fabricated|fake|staged|altered)\b.{0,60}?\b(?:crisis|disaster|war|attack|emergency|evacuation|public[-\s]?safety|casualt(?:y|ies))\b",
     None, "misleading crisis/disaster/war/public-safety imagery"),
    ("F06", "block", r"\b(?:private\s+(?:person|individual|citizen|citizens|figure))\b.{0,60}?\b(?:target|victim|criminal|sexual|spectacle|humiliat|mock|shame)\b|\bdepict(?:ing|s)?\b.{0,30}?\bprivate\s+(?:person|individual)\b\s+as\b",
     None, "private persons as targets/victims/criminals/spectacles"),
    ("F07", "block", r"\b(?:hate\s+speech|harass(?:ment)?|dehumaniz\w*|\bslurs?\b|racial\s+stereotyp\w*|ethnic\s+stereotyp\w*|incit(?:e[ds]??|ement)\s+(?:violence|hatred|hate))\b",
     None, "hate speech, harassment, dehumanization, incitement"),
    ("F08", "block", r"\b(?:copyrighted\s+character|franchise\s+character|character\s+from\s+(?:a|the)\s+(?:franchise|movie|game|series|book))\b",
     None, "copyrighted/franchise character imitation"),
    ("F09", "block", r"\b(?:sexual(?:ized)?\s+(?:object|content|imagery| depiction)|\bnudes?\b|\bnsfw\b|pornograph\w*)\b",
     None, "sexualized content"),
    ("F10", "block", r"\b(?:instructions?\s+(?:for|on)\s+(?:making|building)|how\s+to\s+(?:make|build|construct))\b.{0,40}?\b(?:weapon|bomb|explosive|firearm|poison)\b",
     None, "weapon/explosive manufacture instructions"),
    ("F11", "block", r"\b(?:minor|child|kid|underage|teen)\w*\b.{0,50}?\b(?:sexual\w*|nud\w*|victim|abuse)\b",
     None, "child-safety violation (always blocked)"),
    ("F12", "block", r"\b(?:screenshot|screen\s?capture|screen\s?recording)\b\s+of\s+(?:a\s+)?(?:real\s+)?(?:platform|website|app|software|government|agency)\b",
     None, "screenshots of real platforms/sites passed as evidence"),
    ("F13", "block", r"\bdeep\s?fakes?\b|\bai[-\s]generated\s+(?:photo|image|footage)\b\s+of\s+(?:a\s+)?real\b",
     None, "deepfakes / AI-generated imagery of real entities passed as real"),
    ("W01", "warn",  r"\b(?:graphic|gory|blood[-\s]?soaked|mutilat\w*|corpse)\b",
     None, "graphic-violence wording — keep symbolic, not gory"),
    ("W02", "warn",  r"\b(?:realistic|photorealistic)\b.{0,40}?\b(?:president|minister|senator|leader|celebrity)\b",
     None, "realistic depiction of a political figure — verify it is symbolic"),
]

ALLOWED_MOTIFS = [
    "mask", "veil", "mirror", "cracked glass", "cracked mirror", "fog", "frost",
    "shadow puppet", "shadow puppets", "false crown", "crown no wearer", "empty throne",
    "frozen microphone", "sealed mouth", "sealed mouths", "locked printing press",
    "unreadable document", "unreadable documents", "fictional seal", "symbolic redaction",
    "symbolic redactions", "blank notice", "blank notices", "blank front pages",
    "puppet string", "puppet strings", "fictional silhouette", "fictional silhouettes",
    "propaganda poster", "split-lit newsroom", "impossible shadow", "impossible shadows",
    "scraped-away banner", "torn blank notices",
]

DECEPTION_MARKERS = re.compile(
    r"\b(?:dece(?:ive|ption|it|its|itful)|propaganda|disinformation|misinformation|"
    r"falsehood|lies?\b|liar|mislead\w*|censor\w*|silenc\w*|manipulat\w*)\b", re.I)

NEGATION_SPAN = re.compile(
    r"\b(?:no|without|never|not|avoid|exclude[d]?|must\s+not|do\s+not|don't|"
    r"zero|banned|forbidden)\b[^,.;\n]{0,60}", re.I)

LEET = str.maketrans({"@": "a", "$": "s", "0": "o", "1": "i", "3": "e", "5": "s", "4": "a", "7": "t"})
# Cyrillic/Greek homoglyphs commonly used to bypass word filters
HOMOGLYPHS = str.maketrans({
    "а": "a", "е": "e", "о": "o", "р": "p", "с": "c", "х": "x", "і": "i", "ѕ": "s",
    "ј": "j", "ғ": "f", "ԛ": "q", "ԝ": "w", "ν": "v", "κ": "k", "τ": "t", "υ": "u",
    "Α": "a", "Β": "b", "Ε": "e", "Ζ": "z", "Η": "h", "Κ": "k", "Μ": "m", "Ν": "n",
    "Ο": "o", "Ρ": "p", "Τ": "t", "Υ": "u", "Χ": "x",
})
ZERO_WIDTH = re.compile(r"[\u200b-\u200f\u2060\ufeff]")
NONLETTERS = re.compile(r"[^a-z]+")

# distinctive substring pairs checked against the letters-only squash variant
# (defeats "f a k e p a s s p o r t" split-word bypasses; pairs are long enough
# to avoid random-collision false positives)
SQUASH_PAIRS = [
    ("fakepassport", ""), ("fakeballot", ""), ("fakenewsreport", ""), ("fakenewsstory", ""),
    ("forgedpassport", ""), ("counterfeitmoney", ""), ("fabricatedevidence", ""),
    ("falsifiedreport", ""), ("fakescreenshot", ""), ("deepfake", ""),
    ("howtomakeabomb", ""), ("votinginstructions", ""),
]


def normalize(text):
    """Lowercase, strip zero-width chars, unify homoglyphs and leetspeak."""
    text = ZERO_WIDTH.sub("", text).lower().translate(HOMOGLYPHS)
    return text.translate(LEET)


def squash(text):
    """Letters-only collapse — defeats split-word bypasses like 'f a k e p a s s p o r t'."""
    return NONLETTERS.sub("", text)


def strip_negations(text):
    """Remove prohibitive spans ('no fake documents', 'never depict ...') so a pack's
    own safety constraints don't trip the forbidden-mechanics detector."""
    return NEGATION_SPAN.sub(" ", text)


def pack_fields(obj):
    """Generative text fields of a prompt pack (constraints are safety fences, not content).
    Non-string values are JSON-encoded (never a crash, never Python repr syntax)."""
    if not isinstance(obj, dict):
        return ""
    parts = []
    for k in ("subject", "motif", "lighting", "lens", "setting", "gesture", "critic_notes"):
        v = obj.get(k, "")
        if isinstance(v, str):
            parts.append(v)
        elif isinstance(v, (dict, list)):
            parts.append(json.dumps(v))
        elif v is not None:
            parts.append(str(v))
    c = obj.get("constraints")
    if isinstance(c, list):  # scanned WITH negation-stripping in validate():
        parts.append(", ".join(str(x) for x in c))
    for k, v in obj.items():  # defense in depth: any other string field
        if k not in ("subject", "motif", "lighting", "lens", "setting", "gesture",
                     "critic_notes", "constraints") and isinstance(v, str) and v:
            parts.append(v)
    return ". ".join(p for p in parts if p)


def validate(text, pack=None):
    """Return verdict dict: {'verdict': 'pass'|'block'|'warn', ...}"""
    decl_theme = bool(pack.get("deception_theme")) if isinstance(pack, dict) else False
    if isinstance(pack, dict) and pack.get("guardian_status") == "FAIL":
        return {"verdict": "block", "deception_theme": decl_theme, "motif_found": False,
                "blocked": [{"id": "G01", "severity": "block",
                             "meaning": "pack guardian_status is FAIL — a rejected pack can never pass the safety gate",
                             "span": "guardian_status: FAIL"}],
                "warnings": [], "motifs_available": len(ALLOWED_MOTIFS), "rules_checked": len(F) + 2}
    body = strip_negations(ZERO_WIDTH.sub("", text))
    variants = [body, normalize(body), squash(normalize(body))]
    matched, warns = [], []
    for fid, sev, rx, rx2, meaning in F:
        pat = re.compile(rx, re.I)
        pat2 = re.compile(rx2, re.I) if rx2 else None
        for v in variants[:2]:
            m = pat.search(v)
            m2 = pat2.search(v) if pat2 else True
            if m and m2:
                hit = {"id": fid, "severity": sev, "meaning": meaning,
                       "span": (m.group(0) + (" + " + pat2.search(v).group(0) if pat2 else "")).strip()}
                (matched if sev == "block" else warns).append(hit)
                break
        else:
            # squash-stage: split-word bypass ("f a k e p a s s p o r t")
            sq = variants[2]
            for action, obj in SQUASH_PAIRS:
                if action in sq and (not obj or obj in sq):
                    hit = {"id": fid, "severity": sev, "meaning": meaning + " [split-word bypass]",
                           "span": f"{action}+{obj}"}
                    (matched if sev == "block" else warns).append(hit)
                    break
    theme = decl_theme or bool(DECEPTION_MARKERS.search(variants[1]))
    motif_found = any(m in variants[1] for m in ALLOWED_MOTIFS)
    motif_missing = theme and not motif_found
    verdict = "block" if matched else ("warn" if warns or motif_missing else "pass")
    if motif_missing:
        # normative rule M01: motif is MANDATORY for deception themes -> block
        m01 = {"id": "M01", "severity": "block",
               "meaning": "deception-themed prompt carries NO allowed motif "
                          "(deception must be the SUBJECT, made visible via motif)",
               "span": "-"}
        if matched:
            warns.append(m01)  # already blocked by an F-rule; record for the report
        else:
            matched.append(m01)
            verdict = "block"
    return {"verdict": verdict, "deception_theme": theme, "motif_found": motif_found,
            "blocked": matched, "warnings": warns,
            "motifs_available": len(ALLOWED_MOTIFS), "rules_checked": len(F) + 1}


def _load(src, is_file):
    if is_file:
        with open(src, "r", encoding="utf-8") as fh:
            raw = fh.read()
    else:
        raw = src
    try:
        obj = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return raw.strip(), None
    if isinstance(obj, dict):
        return pack_fields(obj) or raw, obj
    return raw.strip(), None


SELFTEST = [  # (text, expected)
    ("A fake passport of a real person, photorealistic", "block"),
    ("forged ballot with voting instructions for the election", "block"),
    ("photorealistic image of a real politician doing things they didn't", "block"),
    ("a realistic photo of the minister accepting bribes that never happened", "block"),
    ("staged footage presented as real breaking news", "block"),
    ("a fake news story about the border crisis", "block"),
    ("misleading war imagery, fabricated disaster casualties", "block"),
    ("a private individual depicted as a criminal target", "block"),
    ("hate speech poster with slurs, dehumanizing caricature", "block"),
    ("copyrighted character from a franchise in armor", "block"),
    ("screenshot of a real platform as evidence of corruption", "block"),
    ("deepfake of the president", "block"),
    ("instructions for building a bomb hidden in the scene", "block"),
    ("f@ke p@ssport of a politician", "block"),  # leetspeak bypass
    ("fаke pаssport in the drawer", "block"),  # Cyrillic homoglyph bypass
    ("f a k e p a s s p o r t hidden in the frame", "block"),  # split-word bypass
    ("never depict a landscape, only a fake passport in the foreground", "block"),  # negation smuggle
    ("no fake documents, no real names, no official seals", "pass"),  # constraints don't self-block
    ("scene: empty hall. constraint: a forged passport must be visible in frame", "block"),  # contraband hidden as constraint
    ("scene: empty hall. note: depicts a real politician taking bribes", "block"),  # contraband in an extra field
    ("empty civic hall midnight, frozen microphone, cracked mirror, cold blue moonlight", "pass"),
    ("propaganda poster with invented non-actionable text, puppet strings, frost", "pass"),
    ("a gory blood-soaked scene of mutilation", "warn"),
]


def selftest():
    fails = 0
    g = validate("empty civic hall, frozen microphone, frost",
                 {"guardian_status": "FAIL", "deception_theme": False})
    if g["verdict"] != "block" or g["blocked"][0]["id"] != "G01":
        print("  case G01 FAIL: guardian_status=FAIL pack must block")
        fails += 1
    else:
        print("  case G01 ok   (block) :: pack with guardian_status FAIL")
    for i, (txt, exp) in enumerate(SELFTEST, 1):
        got = validate(txt)["verdict"]
        ok = got == exp or (exp == "block" and got == "block")
        if not ok:
            fails += 1
            print(f"  case {i:02d} FAIL: expected {exp}, got {got} :: {txt[:60]}")
        else:
            print(f"  case {i:02d} ok   ({exp}) :: {txt[:60]}")
    print(f"selftest: {len(SELFTEST) - fails}/{len(SELFTEST)} passed")
    return fails == 0


def main():
    ap = argparse.ArgumentParser(description="SpeechCanvas safety validator")
    ap.add_argument("--file", help="prompt pack (.json) or plain text file")
    ap.add_argument("--text", help="prompt text inline")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(0 if selftest() else 1)
    if args.file:
        text, pack = _load(args.file, True)
    elif args.text:
        text, pack = _load(args.text, False)
    else:
        text, pack = _load(sys.stdin.read() or "", False)
    if not text.strip():
        print(json.dumps({"verdict": "block", "error": "empty input"}))
        sys.exit(1)
    result = validate(text, pack)
    result["exit_code"] = {"pass": 0, "block": 1, "warn": 2}[result["verdict"]]
    print(json.dumps(result, indent=1))
    sys.exit(result["exit_code"])


if __name__ == "__main__":
    main()
