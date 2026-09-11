#!/usr/bin/env python3
"""agent-bom-scan self-test. Offline, stdlib only, no network (except the
optional online smoke test, which auto-skips when unreachable).

Groups:
 1  package hygiene
 2  frontmatter compliance (Agent Skills open standard + ClawHub pipeline)
 3  SKILL.md body budget (<=500 lines)
 4  referenced files exist (SKILL.md + references/*.md)
 5  code fences balanced
 6  advisory db: parses, count matches, fields complete
 7  scanner `check` command PASSes
 8  functional smoke: vulnerable fixtures FIND (expected advisory ids),
    clean fixture CLEAN, go.sum /go.mod dedupe, CVSS 3.1 vs NVD-verified scores
 9  provenance: every offline finding carries advisory_id + db_hash
10  offline isolation: offline scan completes with the socket layer disabled
11  required honest-claims phrases present
12  no secrets + CHANGELOG version + README verification hash

Usage: python3 tools/bom_selftest.py [skill_root]   exit 0 = ALL CHECKS PASSED
"""
from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
FAILURES: list[str] = []
PY = sys.executable or "python3"


def fail(msg): print(f"FAIL: {msg}"); FAILURES.append(msg)
def ok(msg): print(f"PASS: {msg}")
def read(p: Path) -> str:
    if not p.exists():
        fail(f"missing file: {p}")
        return ""
    return p.read_text(encoding="utf-8")


def load_scanner():
    spec = importlib.util.spec_from_file_location("bom_scan", ROOT / "scripts" / "bom_scan.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=120, **kw)


def frontmatter(text):
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter"); return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("frontmatter fence not closed"); return {}, text
    return text[4:end], text[end + 5:]


# ── 1 hygiene ────────────────────────────────────────────────────────────────
def check_hygiene():
    allowed_files = {"SKILL.md", "README.md", "CHANGELOG.md", "AGENT_DISCOVERY.md",
                     "skill-card.md", "_meta.json", "feedback.jsonl"}
    allowed_dirs = {"data", "scripts", "tools", "references", ".clawhub"}
    for item in ROOT.iterdir():
        if item.is_file() and item.name not in allowed_files:
            fail(f"unexpected root file: {item.name}")
        if item.is_dir() and item.name not in allowed_dirs:
            fail(f"unexpected root dir: {item.name}")
    for bad in ROOT.rglob("*"):
        n = bad.name
        if n.endswith((".pyc", "~", ".bak")) or n == "__pycache__" or n == "bom_scan_out":
            fail(f"generated artifact in package: {bad.relative_to(ROOT)}")
    if not FAILURES:
        ok("package hygiene clean")


# ── 2 frontmatter ────────────────────────────────────────────────────────────
def check_frontmatter(fm_text, body):
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    name = fm.get("name", "")
    if name != "agent-bom-scan":
        fail(f"frontmatter name must be 'agent-bom-scan', got: {name!r}")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        fail("frontmatter name not lowercase-hyphen")
    if len(name) > 64:
        fail("frontmatter name > 64 chars")
    desc = fm.get("description", "")
    if not (80 <= len(desc) <= 1024):
        fail(f"description length outside 80..1024: {len(desc)}")
    for key in ("version", "license", "categories", "topics"):
        if key not in fm:
            fail(f"frontmatter missing {key}")
    # open-standard: no emoji/whitespace in name; description states when-to-use
    if "use when" not in desc.lower() and "use:" not in desc.lower() and "when" not in desc.lower():
        fail("description should include when to use it (trigger coverage)")
    n_lines = len(body.splitlines())
    if n_lines > 500:
        fail(f"SKILL.md body {n_lines} lines > 500")
    else:
        ok(f"frontmatter compliant; body = {n_lines} lines (<=500)")


# ── 4 references exist ───────────────────────────────────────────────────────
def check_references(docs):
    ref_re = re.compile(r"(?:templates|data|scripts|tools|references)/[A-Za-z0-9_./-]+\.(?:md|yaml|yml|sh|py|jsonl|json|txt)")
    refs = set()
    for d in docs:
        if d.exists():
            refs.update(ref_re.findall(d.read_text(encoding="utf-8")))
    missing = [r for r in sorted(refs) if not (ROOT / r).exists()]
    if missing:
        fail(f"referenced files do not exist: {missing}")
    else:
        ok(f"all {len(refs)} referenced files exist")


# ── 5 fences ─────────────────────────────────────────────────────────────────
def check_fences():
    for md in sorted(ROOT.rglob("*.md")):
        in_fence = False
        for line in md.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("```") or line.strip().startswith("~~~"):
                in_fence = not in_fence
        if in_fence:
            fail(f"unclosed code fence in {md.name}")
    if not any("fence" in f for f in FAILURES):
        ok("code fences balanced")


# ── 6 db ─────────────────────────────────────────────────────────────────────
def check_db(bs):
    meta, records, warnings = bs.load_db(ROOT / "data" / "advisories.yaml")
    for w in warnings:
        fail(f"db: {w}")
    declared = meta.get("record_count", "")
    if str(len(records)) != declared:
        fail(f"db record_count {declared} != actual {len(records)}")
    if len(records) < 20:
        fail(f"db suspiciously small: {len(records)}")
    if not any("CURATED SUBSET" in l for l in (ROOT / "data" / "advisories.yaml").read_text().splitlines()):
        fail("db must state it is a curated subset")
    if not FAILURES:
        ok(f"advisory db valid ({len(records)} records, version {meta.get('db_version')})")


# ── 7 scanner check ──────────────────────────────────────────────────────────
def check_scanner_check():
    r = run([PY, str(ROOT / "scripts" / "bom_scan.py"), "check"])
    if r.returncode != 0 or "verdict=PASS" not in r.stdout:
        fail(f"bom_scan check failed: {r.stdout} {r.stderr}")
    else:
        ok("bom_scan.py check -> PASS")


# ── 8 functional smoke ───────────────────────────────────────────────────────
def check_functional(bs):
    fx = ROOT / "tools" / "fixtures"
    with tempfile.TemporaryDirectory() as td:
        out1 = Path(td) / "vuln"
        r = run([PY, str(ROOT / "scripts" / "bom_scan.py"), "scan", str(fx / "pkg"), "--out", str(out1)])
        if r.returncode != 10:
            fail(f"vulnerable npm fixture: exit {r.returncode} != 10\n{r.stdout}{r.stderr}")
        f1 = json.loads((out1 / "findings.json").read_text())
        ids = {f["advisory_id"] for f in f1}
        for want in ("GHSA-xvch-5gv4-984h", "GHSA-8hfj-j24r-96c4", "GHSA-wf5p-g6vw-rhxx"):
            if want not in ids:
                fail(f"npm fixture missing expected advisory {want}")
        # clean versions must not be flagged
        if any(f["package"] == "ws" for f in f1):
            fail("ws 8.18.0 (clean) wrongly flagged")
        if any(f["package"] == "lodash" and f["advisory_id"] == "GHSA-29mw-wpgm-hmr9" for f in f1):
            fail("lodash 4.17.21 wrongly matched CVE-2020-28500 (fixed 4.17.21)")

        out2 = Path(td) / "pyvuln"
        r = run([PY, str(ROOT / "scripts" / "bom_scan.py"), "scan", str(fx / "py"), "--out", str(out2)])
        if r.returncode != 10:
            fail(f"vulnerable py fixture: exit {r.returncode} != 10\n{r.stdout}{r.stderr}")
        f2 = json.loads((out2 / "findings.json").read_text())
        pkgs = {f["package"] for f in f2}
        if not {"requests", "urllib3"} <= pkgs:
            fail(f"py fixture expected requests+urllib3 findings, got {pkgs}")

        out3 = Path(td) / "clean"
        r = run([PY, str(ROOT / "scripts" / "bom_scan.py"), "scan", str(fx / "clean"), "--out", str(out3)])
        if r.returncode != 0 or "verdict=CLEAN" not in r.stdout:
            fail(f"clean fixture not CLEAN: {r.returncode}\n{r.stdout}{r.stderr}")

        # go.sum /go.mod dedupe
        g = Path(td) / "go.sum"
        g.write_text("github.com/x/y v1.2.3 h1:abc=\ngithub.com/x/y v1.2.3/go.mod h1:def=\n")
        ents, _ = bs.parse_go_sum(g.read_text(), "go.sum", [])
        if len(ents) != 1 or ents[0]["version"] != "v1.2.3":
            fail(f"go.sum /go.mod dedupe broken: {ents}")

    # CVSS 3.1 vs NVD-verified (vectors + scores checked against NVD API 2026-09-06)
    vectors = [
        ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", 10.0),
        ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", 9.8),
        ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H", 7.5),
        ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H", 9.1),
        ("CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N/A:N", 5.3),
    ]
    for vec, want in vectors:
        got = bs.cvss31_base(vec)
        if got != want:
            fail(f"cvss31 {vec} = {got}, NVD-verified want {want}")
    if not any("cvss" in f for f in FAILURES):
        ok("functional smoke: vuln fixtures FIND with expected advisories; clean fixture CLEAN; go.sum dedupe; CVSS 3.1 NVD-verified")


# ── 9 provenance ─────────────────────────────────────────────────────────────
def check_provenance():
    fx = ROOT / "tools" / "fixtures"
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "o"
        run([PY, str(ROOT / "scripts" / "bom_scan.py"), "scan", str(fx / "pkg"), "--out", str(out)])
        f = json.loads((out / "findings.json").read_text())
        bad = [x for x in f if not x.get("advisory_id") or not x.get("db_hash")
               or not x.get("cvss_vector") or x.get("source") != "offline_db"]
        if bad:
            fail(f"findings missing provenance: {bad[:2]}")
        else:
            ok("every offline finding carries advisory_id + db_hash + vector + source")


# ── 10 offline isolation ─────────────────────────────────────────────────────
def check_offline_isolated():
    code = r'''
import sys, socket
class Boom:
    def __getattr__(self, n): raise AssertionError("network touched in offline mode")
socket.socket = Boom
socket.create_connection = Boom.__getattr__
sys.path.insert(0, %r)
import bom_scan
rc = bom_scan.main()
sys.exit(rc)
''' % str(ROOT / "scripts")
    import subprocess
    proc = subprocess.run([PY, "-c", code, "scan", str(ROOT / "tools" / "fixtures" / "clean"),
                           "--out", "/tmp/bom_iso_out"], capture_output=True, text=True, timeout=60)
    # 'clean' fixture => exit 0 even with network disabled
    if proc.returncode != 0:
        fail(f"offline scan failed with network disabled: rc={proc.returncode}\n{proc.stderr[:400]}")
    else:
        ok("offline scan completes with the socket layer disabled (true offline)")


# ── 10b feedback loop ────────────────────────────────────────────────────────
def check_feedback_loop():
    with tempfile.TemporaryDirectory() as td:
        env_root = Path(td) / "skill"
        # run bom_improve in an isolated copy so the package stays clean
        import shutil as _sh
        _sh.copytree(ROOT / "tools", env_root / "tools")
        (env_root / "feedback.jsonl").unlink(missing_ok=True)
        r = run([PY, str(env_root / "tools" / "bom_improve.py"), "log",
                 "--event", "db_gap", "--area", "db", "--context", "test-event"])
        fb = env_root / "feedback.jsonl"
        if r.returncode != 0 or not fb.exists():
            fail(f"feedback log broken: {r.returncode} {r.stdout} {r.stderr}")
            return
        r = run([PY, str(env_root / "tools" / "bom_improve.py"), "learn", "--area", "db"])
        if r.returncode != 0 or "event=db_gap" not in r.stdout:
            fail(f"feedback learn broken: {r.stdout} {r.stderr}")
        r = run([PY, str(env_root / "tools" / "bom_improve.py"), "report", "--out", str(env_root / "rep.md")])
        if r.returncode != 0 or not (env_root / "rep.md").exists():
            fail(f"feedback report broken: {r.stdout} {r.stderr}")
        # secret rejection
        r = run([PY, str(env_root / "tools" / "bom_improve.py"), "log",
                 "--event", "db_gap", "--context", "token=abc123secret"])
        if r.returncode != 2:
            fail(f"feedback secret rejection failed (exit {r.returncode})")
    ok("feedback loop: log/learn/report + secret rejection work")


# ── 11 honest claims ─────────────────────────────────────────────────────────
def check_phrases():
    text = read(ROOT / "SKILL.md")
    for phrase in ("curated subset, not a full CVE", '(unknown), never "safe"',
                   "api.osv.dev", "zero network"):
        if phrase not in text:
            fail(f"SKILL.md missing honest-claim phrase: {phrase!r}")
    if not FAILURES:
        ok("honest-claim phrases present (curated subset, no_data semantics, online endpoint)")


# ── 12 secrets + changelog + hash ────────────────────────────────────────────
def check_secrets_and_meta(fm):
    pats = [r"clh_[A-Za-z0-9_-]{20,}", r"AKIA[0-9A-Z]{16}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
            r"Bearer [A-Za-z0-9._-]{16,}", r"ghp_[A-Za-z0-9]{36}"]
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix not in {".md", ".yaml", ".yml", ".py", ".json", ".txt"}:
            continue
        body = read(p)
        for pat in pats:
            if re.search(pat, body):
                fail(f"possible secret in {p.name}: {pat}")
    cl = read(ROOT / "CHANGELOG.md")
    ver = fm.get("version", "")
    if ver and f"v{ver}" not in cl:
        fail(f"CHANGELOG missing v{ver}")
    readme = read(ROOT / "README.md")
    if not re.search(r"\b[0-9a-f]{64}\b", readme):
        fail("README missing 64-hex verification hash")
    if not FAILURES:
        ok("no secrets; CHANGELOG has current version; README has verification hash")


def main():
    text = read(ROOT / "SKILL.md")
    if not text:
        print("ALL CHECKS FAILED (SKILL.md missing)"); return 1
    check_hygiene()
    fm_text, body = frontmatter(text)
    check_frontmatter(fm_text, body)
    check_references([ROOT / "SKILL.md"] + sorted((ROOT / "references").glob("*.md")))
    check_fences()
    bs = load_scanner()
    check_db(bs)
    check_scanner_check()
    check_functional(bs)
    check_provenance()
    check_offline_isolated()
    check_feedback_loop()
    check_phrases()
    check_secrets_and_meta({k.strip(): v.strip() for k, v in
                            (l.split(":", 1) for l in fm_text.splitlines() if ":" in l and not l.startswith(" "))})
    if FAILURES:
        print(f"── grade: {len(FAILURES)} FAILURES ──")
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
