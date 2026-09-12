#!/usr/bin/env python3
"""agent-bom-scan — BOM vulnerability scanner (python3.8+ stdlib only).

Contract (machine-readable):
  scan  bom_scan.py scan <path> [--mode offline|online] [--db FILE]
                               [--out DIR] [--severity-floor low|medium|high|critical]
        -> stdout key=value:
           mode= bom_packages= lockfiles= findings= critical= high= medium=
           low= unknown= actionable= db_hash=sha256:... db_version=
           verdict=CLEAN|FINDINGS|ERROR  out=<dir>
        -> writes <out>/bom.json, <out>/findings.json, <out>/bom_report.md
        exit: 0=CLEAN, 10=FINDINGS, 2=usage, 3=fatal
  bom   bom_scan.py bom <path> [--out FILE]   -> BOM only (no matching)
  check bom_scan.py check                     -> self-check (db, parsers, hash)

Rules:
  - Offline mode NEVER touches the network (urllib is imported only inside
    the online code path).
  - A finding exists only when a range actually matched an advisory.
    No match => no CVE claim. Unknown packages are reported as no_data,
    never as safe.
  - Every finding carries provenance: advisory_id, aliases, introduced,
    fixed, cvss_vector, db_hash (offline) or source=osv_online (online).
  - CVSS 3.1 base scores are computed at runtime from the vector.
"""
import argparse
import hashlib
import json
import math
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_DEFAULT = Path(__file__).resolve().parent.parent / "data" / "advisories.yaml"
MAX_DEPTH = 6
SKIP_DIRS = {"node_modules", ".git", "vendor", "dist", "build", "out", ".venv", "venv", "target"}


# ── version comparison ───────────────────────────────────────────────────────

def parse_ver(v):
    """Return (components, prerelease) for ordering. '*' and '' are minimum."""
    if v is None:
        return ([], "")
    s = str(v).strip().lstrip("vV")
    if s in ("", "*", "0", "0.0", "0.0.0"):
        return ([0], "")
    build = s.split("+", 1)[0]
    if "-" in build:
        num_part, pre = build.split("-", 1)
    else:
        num_part, pre = build, ""
    comps = []
    for part in num_part.split("."):
        m = re.match(r"^(\d+)", part)
        comps.append(int(m.group(1)) if m else 0)
    while len(comps) < 3:
        comps.append(0)
    return (comps, pre)


def ver_cmp(a, b):
    """-1, 0, 1. Prerelease sorts before its release (1.0.0-alpha < 1.0.0)."""
    ca, pa = parse_ver(a)
    cb, pb = parse_ver(b)
    n = max(len(ca), len(cb))
    ca += [0] * (n - len(ca))
    cb += [0] * (n - len(cb))
    for x, y in zip(ca, cb):
        if x != y:
            return -1 if x < y else 1
    if pa == pb:
        return 0
    return 1 if pa == "" else -1  # release > prerelease


def in_range(version, introduced, fixed):
    if introduced in (None, "", "*", "0"):
        lower_ok = True
    else:
        lower_ok = ver_cmp(version, introduced) >= 0
    if fixed in (None, "", "*"):
        return lower_ok
    return lower_ok and ver_cmp(version, fixed) < 0


# ── CVSS 3.1 base score ──────────────────────────────────────────────────────

def _roundup(x):
    """CVSS 3.1 spec Roundup: ceil to 4 decimals, then 3, then 2, then 1.
    (Stops at one decimal — do NOT ceil to the integer.)"""
    i = 10000
    while i >= 10:
        x = math.ceil(x * i) / i
        i //= 10
    return x


def cvss31_base(vector):
    """Compute CVSS 3.1 base score from a vector string, or None."""
    if not vector or not vector.startswith("CVSS:3."):
        return None
    vals = {}
    for tok in vector.split("/")[1:]:
        if ":" in tok:
            k, v = tok.split(":", 1)
            vals[k] = v
    try:
        av = {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2}[vals["AV"]]
        ac = {"L": 0.77, "H": 0.44}[vals["AC"]]
        pr_ns = {"N": 0.85, "L": 0.68, "H": 0.50}[vals["PR"]]
        pr_s = {"N": 0.85, "L": 0.62, "H": 0.27}[vals["PR"]]
        ui = {"N": 0.85, "R": 0.62}[vals["UI"]]
        scope = vals["S"]
        c = {"N": 0.0, "L": 0.22, "H": 0.56}[vals["C"]]
        i = {"N": 0.0, "L": 0.22, "H": 0.56}[vals["I"]]
        a = {"N": 0.0, "L": 0.22, "H": 0.56}[vals["A"]]
    except KeyError:
        return None
    iss = 1.0 - ((1 - c) * (1 - i) * (1 - a))
    if iss <= 0:
        return 0.0
    if scope == "U":
        impact = 6.42 * iss
    else:
        impact = 7.52 * (iss - 0.02) - 3.25 * (iss - 0.02) ** 15 - 5.25 * (iss - 0.02) ** 25
        if impact < 0:
            return 0.0
    exploit = 8.22 * av * ac * (pr_s if scope == "C" else pr_ns) * ui
    base = min(impact + exploit, 10.0) if scope == "U" else min(1.08 * (impact + exploit), 10.0)
    return _roundup(base)


def severity_of(score):
    if score is None:
        return "high"  # conservative: no vector => treat as high, flagged no_vector
    if score >= 9.0:
        return "critical"
    if score >= 7.0:
        return "high"
    if score >= 4.0:
        return "medium"
    if score > 0:
        return "low"
    return "low"


# ── advisory db ──────────────────────────────────────────────────────────────

def load_db(path):
    """Parse the flat '=== id' block format. Returns (meta, records, warnings)."""
    meta, records, warnings = {}, {}, []
    cur = None
    for i, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("=== "):
            cur = s[4:].strip()
            records[cur] = {}
            continue
        if ":" in s:
            k, v = s.split(":", 1)
            k, v = k.strip(), v.strip()
            if k in ("schema", "db_version", "record_count", "source"):
                meta[k] = v
            elif cur is None:
                warnings.append(f"db line {i} outside a record: {s[:60]}")
            else:
                records[cur][k] = v
    for rid, r in records.items():
        for field in ("package", "ecosystem", "introduced", "fixed"):
            if field not in r:
                warnings.append(f"db record {rid} missing field {field}")
    return meta, records, warnings


def db_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# ── lockfile parsers (each returns (entries, warnings)) ─────────────────────

def _add(entries, seen, name, version, ecosystem, lockfile, line):
    if not name or not version or version.startswith("$"):
        return
    key = (name, ecosystem, version)
    if key not in seen:
        seen.add(key)
        entries.append({"name": name, "version": version, "ecosystem": ecosystem,
                        "lockfile": lockfile, "line": line})


def parse_package_lock(data, lockfile, warnings):
    entries, seen = [], set()
    try:
        doc = json.loads(data)
    except Exception:
        warnings.append(f"{lockfile}: JSON parse failed; skipped")
        return entries, warnings
    # v2/v3: "packages" map
    pkgs = doc.get("packages")
    if isinstance(pkgs, dict):
        for key, info in pkgs.items():
            if key == "" or not isinstance(info, dict):
                continue
            if info.get("link"):
                continue  # workspace symlink entries: no resolvable version
            name = key.rsplit("node_modules/", 1)[-1] if "node_modules/" in key else key
            ver = info.get("version")
            if ver:
                _add(entries, seen, name, str(ver), "npm", lockfile, key)
        return entries, warnings
    # v1: nested "dependencies"
    def walk(deps, line):
        for name, info in (deps or {}).items():
            if not isinstance(info, dict):
                continue
            ver = info.get("version")
            if ver:
                _add(entries, seen, name, str(ver), "npm", lockfile, line + "/" + name)
            walk(info.get("dependencies"), line + "/" + name)
    walk(doc.get("dependencies"), "dependencies")
    return entries, warnings


def parse_requirements_txt(data, lockfile, warnings):
    entries, seen = [], set()
    for i, raw in enumerate(data.splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line or line.startswith("-"):
            continue
        if "==" in line:
            name, ver = [x.strip() for x in line.split("==", 1)]
            if re.match(r"^[A-Za-z0-9._-]+$", name) and ver:
                _add(entries, seen, name, ver, "PyPI", lockfile, i)
                continue
        if re.match(r"^[A-Za-z0-9._-]+", line):
            warnings.append(f"{lockfile}:{i}: unpinned/complex requirement not scanned: {line[:60]}")
    return entries, warnings


def parse_pipfile_lock(data, lockfile, warnings):
    entries, seen = [], set()
    try:
        doc = json.loads(data)
    except Exception:
        warnings.append(f"{lockfile}: JSON parse failed; skipped")
        return entries, warnings
    for section in ("default", "develop"):
        for name, info in (doc.get(section) or {}).items():
            ver = (info or {}).get("version", "")
            ver = ver.lstrip("=~ ^").strip()
            if ver:
                _add(entries, seen, name, ver, "PyPI", lockfile, section)
    return entries, warnings


def parse_go_sum(data, lockfile, warnings):
    entries, seen = [], set()
    for i, raw in enumerate(data.splitlines(), 1):
        parts = raw.split()
        if len(parts) >= 2 and "/" in parts[0]:
            ver = parts[1]
            if ver.endswith("/go.mod"):
                ver = ver[: -len("/go.mod")]  # go.mod hash line: same module version
            _add(entries, seen, parts[0], ver, "Go", lockfile, i)
    return entries, warnings


def parse_cargo_lock(data, lockfile, warnings):
    entries, seen = [], set()
    name = None
    for i, raw in enumerate(data.splitlines(), 1):
        line = raw.strip()
        m = re.match(r'^\[\[package\]\]', line)
        if m:
            name = None
            continue
        m = re.match(r'^name\s*=\s*"(.+)"', line)
        if m:
            name = m.group(1)
            continue
        m = re.match(r'^version\s*=\s*"(.+)"', line)
        if m and name:
            _add(entries, seen, name, m.group(1), "Cargo", lockfile, i)
            name = None
    return entries, warnings


def parse_gemfile_lock(data, lockfile, warnings):
    entries, seen = [], set()
    section = None
    for i, raw in enumerate(data.splitlines(), 1):
        line = raw.strip()
        if line in ("GEM", "GIT", "PATH", "PLATFORMS", "DEPENDENCIES", "BUNDLED WITH", "RUBY VERSION"):
            section = line
            continue
        if section in ("GEM", "DEPENDENCIES") and re.match(r"^\s{4,}[a-zA-Z0-9._-]+ \(", raw):
            m = re.search(r"([a-zA-Z0-9._-]+) \(([^)]+)\)", raw)
            if m:
                _add(entries, seen, m.group(1), m.group(2), "RubyGems", lockfile, i)
        if section in ("GIT", "PATH"):
            if line and not raw.startswith(" "):
                section = None
    if section in ("GIT", "PATH"):
        warnings.append(f"{lockfile}: GIT/PATH gems not pinned; skipped")
    return entries, warnings


def parse_composer_json(data, lockfile, warnings):
    entries, seen = [], set()
    try:
        doc = json.loads(data)
    except Exception:
        warnings.append(f"{lockfile}: JSON parse failed; skipped")
        return entries, warnings
    for section in ("require", "require-dev"):
        for name, ver in (doc.get(section) or {}).items():
            ver = str(ver).lstrip("^~=>< ").strip()
            if re.match(r"^\d+(\.\d+)*", ver):
                _add(entries, seen, name, ver, "Packagist", lockfile, section)
            else:
                warnings.append(f"{lockfile}: dynamic version for {name} ({ver[:30]}); not scanned")
    return entries, warnings


def parse_pom_xml(data, lockfile, warnings):
    import xml.etree.ElementTree as ET
    entries, seen = [], set()
    props = {}
    try:
        root = ET.fromstring(data)
    except Exception:
        warnings.append(f"{lockfile}: XML parse failed; skipped")
        return entries, warnings
    ns = ""
    if root.tag.startswith("{"):
        ns = root.tag.split("}")[0] + "}"
    for el in root.iter(ns + "properties"):
        for child in el:
            if child.text:
                props[child.tag.replace(ns, "")] = child.text.strip()
    for el in root.iter(ns + "dependency"):
        def txt(tag):
            e = el.find(ns + tag)
            return e.text.strip() if e is not None and e.text else None
        gid, aid, ver = txt("groupId"), txt("artifactId"), txt("version")
        if ver and "${" in ver:
            key = ver.strip("${}")
            ver = props.get(key, ver)
            if "${" in ver:
                warnings.append(f"{lockfile}: unresolved property {ver} for {gid}:{aid}; not scanned")
                continue
        if gid and aid and ver and not ver.startswith("${"):
            _add(entries, seen, f"{gid}:{aid}", ver, "Maven", lockfile, f"{gid}:{aid}")
    return entries, warnings


LOCKFILE_MAP = {
    "package-lock.json": ("npm", parse_package_lock),
    "requirements.txt": ("PyPI", parse_requirements_txt),
    "Pipfile.lock": ("PyPI", parse_pipfile_lock),
    "go.sum": ("Go", parse_go_sum),
    "Cargo.lock": ("Cargo", parse_cargo_lock),
    "Gemfile.lock": ("RubyGems", parse_gemfile_lock),
    "composer.json": ("Packagist", parse_composer_json),
    "pom.xml": ("Maven", parse_pom_xml),
}


# ── discovery + BOM ──────────────────────────────────────────────────────────

def discover_bom(root):
    root = Path(root)
    entries, seen, warnings, lockfiles = [], set(), [], []
    if not root.exists():
        return entries, warnings, lockfiles, f"path not found: {root}"
    if root.is_file():
        lockfiles = [root]
    else:
        deep_skipped = 0
        for dirpath, dirnames, filenames in os.walk(root):
            rel = Path(dirpath).relative_to(root)
            if len(rel.parts) > MAX_DEPTH:
                dirnames[:] = []
                deep_skipped += 1
                continue
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if fn in LOCKFILE_MAP:
                    lockfiles.append(Path(dirpath) / fn)
        if deep_skipped:
            warnings.append(f"lockfiles deeper than {MAX_DEPTH} directories not scanned "
                            f"({deep_skipped} dirs skipped)")
    for lf in sorted(lockfiles):
        eco, parser = LOCKFILE_MAP[lf.name]
        try:
            data = lf.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            warnings.append(f"{lf.name}: unreadable ({e})")
            continue
        ents, warnings = parser(data, str(lf.relative_to(root) if root.is_dir() else lf.name), warnings)
        entries.extend(ents)
    return entries, warnings, lockfiles, None


def match_bom(bom, db_records, mode, db_h, online_results=None):
    """Return findings. A finding requires a real range match (offline) or an
    OSV response (online). Never invents vulnerabilities."""
    findings = []
    idx = {}
    for rid, r in db_records.items():
        idx.setdefault((r.get("package"), r.get("ecosystem")), []).append((rid, r))
    seen = set()
    for pkg in bom:
        key = (pkg["name"], pkg["ecosystem"])
        for rid, r in idx.get(key, []):
            if in_range(pkg["version"], r.get("introduced"), r.get("fixed")):
                vector = r.get("cvss_vector", "NONE")
                score = cvss31_base(vector)
                f = {
                    "advisory_id": rid,
                    "aliases": [] if r.get("aliases", "-") == "-" else r.get("aliases", "").split(","),
                    "package": pkg["name"],
                    "version": pkg["version"],
                    "ecosystem": pkg["ecosystem"],
                    "introduced": r.get("introduced"),
                    "fixed": r.get("fixed"),
                    "cvss_vector": vector,
                    "cvss_score": score,
                    "severity": severity_of(score),
                    "no_vector": score is None,
                    "summary": r.get("summary", ""),
                    "lockfile": pkg["lockfile"],
                    "source": "offline_db",
                    "db_hash": db_h,
                    "below_floor": False,
                }
                k = (rid, pkg["name"], pkg["version"])
                if k not in seen:
                    seen.add(k)
                    findings.append(f)
    if online_results:
        for (name, ver, eco), vulns in online_results.items():
            for v in vulns:
                vid = v.get("id", "")
                sev = v.get("severity") or []
                vector = next((s.get("score") for s in sev if s.get("type") == "CVSS_V3"), "NONE")
                score = cvss31_base(vector) if isinstance(vector, str) else None
                f = {
                    "advisory_id": vid,
                    "aliases": v.get("aliases", []),
                    "package": name,
                    "version": ver,
                    "ecosystem": eco,
                    "introduced": "",
                    "fixed": "",
                    "cvss_vector": vector if isinstance(vector, str) else "NONE",
                    "cvss_score": score,
                    "severity": "high" if vid.startswith("MAL-") else severity_of(score),
                    "no_vector": not isinstance(vector, str),
                    "summary": (v.get("summary") or "")[:200],
                    "malicious_package": vid.startswith("MAL-"),
                    "lockfile": "",
                    "source": "osv_online",
                    "db_hash": "",
                    "below_floor": False,
                }
                k = (vid, name, ver)
                if k not in seen:
                    seen.add(k)
                    findings.append(f)
    findings.sort(key=lambda f: (-(f["cvss_score"] if f["cvss_score"] is not None else -1),
                                 f["package"], f["advisory_id"]))
    return findings


# ── online mode (only when explicitly requested) ─────────────────────────────

def osv_online(bom, chunk=40, timeout=20):
    """Query api.osv.dev /v1/querybatch. Data sent: package name + version +
    ecosystem ONLY (strict per-query dict). Returns {(name, version,
    ecosystem): [vuln, ...]}; None on network error (offline findings still
    valid). Large BOMs are sent in chunks of `chunk` (default 40)."""
    import urllib.request
    triples = sorted({(p["name"], p["version"], p["ecosystem"]) for p in bom})
    if not triples:
        return {}
    out = {}
    for start in range(0, len(triples), chunk):
        batch = triples[start:start + chunk]
        queries = [{"package": {"name": n, "ecosystem": e}, "version": v}
                   for (n, v, e) in batch]
        req = urllib.request.Request(
            "https://api.osv.dev/v1/querybatch",
            data=json.dumps({"queries": queries}).encode(),
            headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                resp = json.load(r)
        except Exception as e:
            print(f"online_error={type(e).__name__}: {e} "
                  f"(offline findings still valid)", file=sys.stderr)
            return None
        results = resp.get("results", [])
        if len(results) != len(batch):
            print(f"online_error=result_mismatch got={len(results)} want={len(batch)} "
                  f"(offline findings still valid)", file=sys.stderr)
            return None
        for (n, v, e), res in zip(batch, results):
            vulns = res.get("vulns", []) if isinstance(res, dict) else []
            if vulns:
                out[(n, v, e)] = vulns
    return out


# ── report ──────────────────────────────────────────────────────────────────

def render_report(mode, bom, findings, warnings, lockfiles, meta, db_h, floor, error):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    verdict = "ERROR" if error else ("FINDINGS" if findings else "CLEAN")
    L = []
    L.append("# BOM Scan Report")
    L.append("")
    L.append(f"- generated: {now}")
    L.append(f"- mode: {mode}")
    L.append(f"- lockfiles: {len(lockfiles)}")
    L.append(f"- bom_packages: {len(bom)}")
    L.append(f"- db_version: {meta.get('db_version', '?')}")
    L.append(f"- db_hash: sha256:{db_h}")
    L.append(f"- severity_floor: {floor}")
    L.append(f"- verdict: **{verdict}** (critical={counts['critical']} high={counts['high']} "
             f"medium={counts['medium']} low={counts['low']})")
    if error:
        L.append(f"\nerror: {error}")
    if findings:
        L.append("\n## Findings (sorted by CVSS 3.1 base score)")
        L.append("")
        L.append("| advisory | package | version | fixed | score | severity | below_floor | source |")
        L.append("|---|---|---|---|---|---|---|---|")
        for f in findings:
            score = f["cvss_score"] if f["cvss_score"] is not None else "n/v"
            L.append(f"| {f['advisory_id']} | {f['package']} | {f['version']} | {f['fixed'] or '?'} "
                     f"| {score} | {f['severity']} | {str(f['below_floor']).lower()} | {f['source']} |")
        L.append("\n### Finding detail")
        for f in findings:
            al = ", ".join(a for a in f["aliases"] if a and a != "-") or "-"
            L.append(f"- **{f['advisory_id']}** ({al}) — {f['package']} {f['version']}: "
                     f"{f['summary'][:160]}  range=[{f['introduced'] or '*'} .. {f['fixed'] or '*'})")
    else:
        L.append("\nNo range matches in the selected database mode. "
                 "This means 'no data for these packages in this mode', not 'no vulnerabilities'.")
    if warnings:
        L.append("\n## Warnings (not scanned)")
        for w in warnings[:40]:
            L.append(f"- {w}")
    L.append("\n## BOM")
    L.append("")
    L.append("| package | version | ecosystem | lockfile |")
    L.append("|---|---|---|---|")
    for p in sorted(bom, key=lambda x: (x["ecosystem"], x["name"], x["version"])):
        L.append(f"| {p['name']} | {p['version']} | {p['ecosystem']} | {p['lockfile']} |")
    L.append("")
    L.append("---")
    L.append("agent-bom-scan · offline findings carry db_hash provenance · online findings cite OSV ids")
    return "\n".join(L) + "\n"


# ── commands ─────────────────────────────────────────────────────────────────

def cmd_check(args):
    meta, records, warnings = load_db(args.db)
    h = db_hash(args.db)
    print(f"db={args.db}")
    print(f"db_hash=sha256:{h}")
    print(f"db_version={meta.get('db_version', '?')}")
    print(f"records={len(records)}")
    ok = len(records) > 0
    for w in warnings:
        print(f"db_warning={w}")
        ok = False
    # parser sanity: minimal fixtures
    sanity = [
        ("package-lock.json", '{"name":"x","lockfileVersion":3,"packages":{"":"{}","node_modules/lodash":{"version":"4.17.20"}}}', 1),
        ("requirements.txt", "requests==2.30.0\n# comment\nflask>=2.0\n", 1),
        ("go.sum", "github.com/x/y v1.2.3 h1:abc=\ngithub.com/x/y v1.2.3/go.mod h1:def=\n", 1),
        ("Cargo.lock", '[[package]]\nname = "serde"\nversion = "1.0.100"\n', 1),
    ]
    for name, data, expect in sanity:
        eco, parser = LOCKFILE_MAP[name]
        ents, _ = parser(data, name, [])
        if len(ents) != expect:
            print(f"parser_check={name} FAIL got={len(ents)} want={expect}")
            ok = False
    if ok:
        print("verdict=PASS")
        return 0
    print("verdict=FAIL")
    return 3


def cmd_bom(args):
    bom, warnings, lockfiles, err = discover_bom(args.path)
    if err:
        print(f"error={err}")
        return 3
    out = {"generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "packages": sorted(bom, key=lambda p: (p["ecosystem"], p["name"], p["version"])),
           "warnings": warnings, "lockfiles": [str(l) for l in lockfiles]}
    if args.out:
        Path(args.out).write_text(json.dumps(out, indent=1), encoding="utf-8")
        print(f"bom_out={args.out}")
    else:
        print(json.dumps(out, indent=1))
    print(f"bom_packages={len(bom)} lockfiles={len(lockfiles)}")
    return 0


def cmd_scan(args):
    floor_rank = {"low": 0, "medium": 1, "high": 2, "critical": 3}
    floor = floor_rank[args.severity_floor]
    meta, records, db_warnings = load_db(args.db)
    db_h = db_hash(args.db)
    bom, warnings, lockfiles, err = discover_bom(args.path)
    warnings = db_warnings + warnings
    if not bom:
        warnings.append("no lockfiles found under path: nothing scanned (verdict CLEAN means no data)")
    online_results = None
    if err:
        findings = []
    else:
        if args.mode == "online":
            online_results = osv_online(bom)
        findings = match_bom(bom, records, args.mode, db_h, online_results)
        rank = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        for f in findings:
            f["below_floor"] = rank[f["severity"]] < floor
    out = Path(args.out) if args.out else Path(args.path) / "bom_scan_out"
    out.mkdir(parents=True, exist_ok=True)
    (out / "bom.json").write_text(json.dumps(
        {"generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
         "packages": sorted(bom, key=lambda p: (p["ecosystem"], p["name"], p["version"])),
         "warnings": warnings, "lockfiles": [str(l) for l in lockfiles]}, indent=1), encoding="utf-8")
    (out / "findings.json").write_text(json.dumps(findings, indent=1), encoding="utf-8")
    (out / "bom_report.md").write_text(render_report(args.mode, bom, findings, warnings,
                                                      lockfiles, meta, db_h, args.severity_floor, err),
                                       encoding="utf-8")
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for f in findings:
        counts[f["severity"]] += 1
    actionable = sum(1 for f in findings if not f["below_floor"])
    # no_data = BOM packages (name+ecosystem) with zero findings for that pair
    bom_pairs = {(p["name"], p["ecosystem"]) for p in bom}
    found_pairs = {(f["package"], f["ecosystem"]) for f in findings}
    unknown_pkgs = len(bom_pairs - found_pairs)
    print(f"mode={args.mode}")
    print(f"lockfiles={len(lockfiles)}")
    print(f"bom_packages={len(bom)}")
    print(f"findings={len(findings)}")
    print(f"critical={counts['critical']} high={counts['high']} medium={counts['medium']} low={counts['low']}")
    print(f"actionable={actionable}")
    print(f"no_data_packages={unknown_pkgs}")
    print(f"db_hash=sha256:{db_h}")
    print(f"db_version={meta.get('db_version', '?')}")
    print(f"out={out}")
    print(f"verdict={'ERROR' if err else ('FINDINGS' if findings else 'CLEAN')}")
    if err:
        print(f"error={err}")
        return 3
    return 10 if findings else 0


def main():
    ap = argparse.ArgumentParser(prog="bom_scan.py", description="BOM vulnerability scanner (stdlib only)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan", help="build BOM + match advisories")
    s.add_argument("path")
    s.add_argument("--mode", choices=["offline", "online"], default="offline")
    s.add_argument("--db", default=str(DB_DEFAULT))
    s.add_argument("--out", default=None)
    s.add_argument("--severity-floor", choices=["low", "medium", "high", "critical"], default="low")
    s.set_defaults(fn=cmd_scan)
    b = sub.add_parser("bom", help="build BOM only (no matching, no network)")
    b.add_argument("path")
    b.add_argument("--out", default=None)
    b.set_defaults(fn=cmd_bom)
    c = sub.add_parser("check", help="self-check: db parses, hash, parser sanity")
    c.add_argument("--db", default=str(DB_DEFAULT))
    c.set_defaults(fn=cmd_check)
    args = ap.parse_args()
    try:
        return args.fn(args)
    except SystemExit:
        raise
    except Exception as e:
        print(f"error={type(e).__name__}: {e}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
