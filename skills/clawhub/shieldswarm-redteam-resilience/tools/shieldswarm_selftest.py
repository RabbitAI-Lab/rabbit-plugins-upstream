#!/usr/bin/env python3
"""ShieldSwarm self-test harness (v2.1.0 package).

Offline, stdlib only, no network. Verifies the whole published package:
  1.  package hygiene (allowed root files/dirs, no backup artifacts)
  2.  frontmatter (name/slug, description 80..1024, categories/topics, version)
  3.  SKILL.md body <= 500 lines (progressive-disclosure budget)
  4.  every referenced file exists (SKILL.md + references/*.md)
  5.  code fences balanced in all markdown
  6.  YAML templates parse (PyYAML if present, else structural check)
  7.  scripts exist, are executable, and pass `bash -n`
  8.  functional smoke tests for all four scripts (PASS and FAIL paths)
  9.  quality floor matrix semantics (tiers non-empty, task floors valid)
 10.  required safety phrases present
 11.  no secret patterns, no dangerous traffic/exploit patterns
 12.  CHANGELOG contains an entry for the frontmatter version

Usage: python3 tools/shieldswarm_selftest.py [skill_root]
Exit: 0 = ALL CHECKS PASSED, 1 = failure.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
FAILURES: list[str] = []


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    FAILURES.append(msg)


def ok(msg: str) -> None:
    print(f"PASS: {msg}")


def warn(msg: str) -> None:
    print(f"WARN: {msg}")


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter")
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter closing fence not found")
        return "", text
    return text[4:end], text[end + 5:]


def parse_yaml_document(src: str, label: str):
    if yaml is None:
        return None
    try:
        return yaml.safe_load(src)
    except Exception as exc:
        fail(f"{label}: YAML parse error: {exc}")
        return None


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd or ROOT), capture_output=True, text=True, timeout=30)


# ── 1. package hygiene ───────────────────────────────────────────────────────
def check_hygiene() -> None:
    allowed_files = {
        "SKILL.md", "README.md", "CHANGELOG.md", "AGENT_DISCOVERY.md",
        "skill-card.md", "_meta.json", "feedback.jsonl", "improvement_report.md",
        "approval.jsonl",
    }
    allowed_dirs = {"scripts", "templates", "tools", "references", ".clawhub"}
    for item in ROOT.iterdir():
        if item.is_file() and item.name not in allowed_files:
            fail(f"unexpected root file: {item.name}")
        if item.is_dir() and item.name not in allowed_dirs:
            fail(f"unexpected root directory: {item.name}")
    for bad in ROOT.rglob("*"):
        n = bad.name
        if n.startswith("SKILL.md.bak") or n.endswith("~") or n == "__pycache__" or n.endswith(".pyc") or n.startswith(".approval."):
            fail(f"generated/backup artifact found: {bad.relative_to(ROOT)}")
    if not FAILURES:
        ok("package hygiene clean")


# ── 2-3. frontmatter + body budget ───────────────────────────────────────────
def check_frontmatter(text: str) -> dict:
    fm, body = split_frontmatter(text)
    data = parse_yaml_document(fm, "frontmatter")
    meta: dict = {}
    if yaml is not None:
        if not isinstance(data, dict):
            fail("frontmatter did not parse to a mapping")
            return meta
        if data.get("name") != "shieldswarm-redteam-resilience":
            fail("frontmatter name mismatch")
        desc = str(data.get("description", ""))
        if not (80 <= len(desc) <= 1024):
            fail(f"description length outside 80..1024: {len(desc)}")
        if not data.get("categories"):
            fail("frontmatter categories missing")
        if not data.get("topics"):
            fail("frontmatter topics missing")
        meta = {"version": str(data.get("version", ""))}
    else:
        m = re.search(r"^version:\s*([0-9.]+)", fm, re.M)
        meta = {"version": m.group(1) if m else ""}
    n_lines = len(body.splitlines())
    if n_lines > 500:
        fail(f"SKILL.md body exceeds 500 lines: {n_lines}")
    else:
        ok(f"frontmatter ok; SKILL.md body = {n_lines} lines (<=500)")
    return meta


# ── 4. referenced files exist ───────────────────────────────────────────────
def check_references(docs: list[Path]) -> None:
    ref_re = re.compile(r"(?:templates|references|scripts|tools)/[A-Za-z0-9_./-]+\.(?:md|yaml|yml|sh|py|jsonl|json)")
    refs = set()
    for d in docs:
        if d.exists():
            refs.update(ref_re.findall(d.read_text(encoding="utf-8")))
    missing = []
    for r in sorted(refs):
        if not (ROOT / r).exists():
            missing.append(r)
    if missing:
        fail(f"referenced files do not exist: {missing}")
    else:
        ok(f"all {len(refs)} referenced files exist")


# ── 5. code fences ───────────────────────────────────────────────────────────
def check_fences(path: Path) -> None:
    if not path.exists():
        return
    lines = path.read_text(encoding="utf-8").splitlines()
    open_ch = None
    open_line = 0
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            ch = s[0]
            if open_ch is None:
                open_ch, open_line = ch, i
            elif ch == open_ch:
                open_ch = None
    if open_ch is not None:
        fail(f"{path.name}: unclosed code fence opened at line {open_line}")


def check_all_fences() -> None:
    for md in list(ROOT.rglob("*.md")):
        check_fences(md)
    ok("code fences balanced in all markdown")


# ── 6. YAML templates ────────────────────────────────────────────────────────
def check_yaml_templates() -> None:
    tdir = ROOT / "templates"
    if not tdir.is_dir():
        fail("templates/ missing")
        return
    n = 0
    for t in sorted(tdir.iterdir()):
        if t.suffix not in {".yaml", ".yml"}:
            continue
        n += 1
        src = read(t)
        if yaml is not None:
            obj = parse_yaml_document(src, t.name)
            if obj is not None and not isinstance(obj, (dict, list)):
                fail(f"{t.name}: YAML did not parse to mapping/sequence")
        elif ":" not in src:
            fail(f"{t.name}: not YAML-like and PyYAML unavailable")
    ok(f"{n} YAML templates parse")


def check_matrix() -> None:
    p = ROOT / "templates" / "quality_floor_matrix.yaml"
    src = read(p)
    if not src:
        return
    flat = {}
    for line in src.splitlines():
        m = re.match(r"^([A-Za-z0-9_.-]+):\s*(.*)$", line.strip())
        if m and not line.startswith("#"):
            flat[m.group(1)] = m.group(2).strip()
    for key in ("tier1_models", "tier2_models"):
        vals = [v.strip() for v in flat.get(key, "").split(",") if v.strip()]
        if not vals:
            fail(f"matrix {key} empty")
    floors = {k: v for k, v in flat.items() if k.startswith("task_")}
    if "task_default" not in floors:
        fail("matrix task_default missing")
    for k, v in floors.items():
        if v not in {"tier1", "tier2", "tier3"}:
            fail(f"matrix {k} invalid floor: {v}")
    if not any("policy: cloud_only" in l for l in src.splitlines()):
        fail("matrix policy cloud_only missing")
    ok("quality floor matrix valid (tiers, task floors, cloud_only policy)")


# ── 7. scripts ───────────────────────────────────────────────────────────────
SCRIPTS = [
    "scripts/mode_selector.sh",
    "scripts/shieldswarm_validate.sh",
    "scripts/approval_gate.sh",
    "scripts/quality_floor_check.sh",
]


def check_scripts() -> None:
    bash = shutil.which("bash")
    for rel in SCRIPTS:
        p = ROOT / rel
        if not p.exists():
            fail(f"missing script: {rel}")
            continue
        if not p.stat().st_mode & 0o111:
            fail(f"script not executable: {rel}")
        if bash:
            r = run([bash, "-n", str(p)])
            if r.returncode != 0:
                fail(f"bash -n {rel}: {r.stderr.strip()}")
    if not FAILURES:
        ok("scripts present, executable, syntax OK")


# ── 8. functional smoke tests ────────────────────────────────────────────────
def smoke() -> None:
    bash = shutil.which("bash")
    if not bash:
        warn("bash not available; skipping functional smoke tests")
        return
    S = lambda rel: str(ROOT / rel)  # noqa: E731
    cases: list[tuple[str, list[str], int]] = [
        ("mode help", ["bash", S("scripts/mode_selector.sh"), "--help"], 2),
        ("mode no-login", ["bash", S("scripts/mode_selector.sh"), "--symptom", "cannot login", "--evidence", "public"], 0),
        ("mode redteam", ["bash", S("scripts/mode_selector.sh"), "--symptom", "red team staging validation", "--evidence", "operator"], 0),
        ("mode bad evidence", ["bash", S("scripts/mode_selector.sh"), "--symptom", "x", "--evidence", "alien"], 2),
        ("validate clean", ["bash", S("scripts/shieldswarm_validate.sh"), "--command", "curl -s https://status.example.com", "--mode", "operator"], 0),
        ("validate offensive", ["bash", S("scripts/shieldswarm_validate.sh"), "--command", "nmap -sV target.example.com"], 1),
        ("validate secret", ["bash", S("scripts/shieldswarm_validate.sh"), "--command", "curl -H 'x: y' -d password=hunter2 url"], 1),
        ("validate redteam w/o roe", ["bash", S("scripts/shieldswarm_validate.sh"), "--command", "true", "--mode", "red_team"], 1),
        ("floor pass frontier", ["bash", S("scripts/quality_floor_check.sh"), "--task", "security code review", "--proposed-model", "claude-opus-5"], 0),
        ("floor fail weak", ["bash", S("scripts/quality_floor_check.sh"), "--task", "security code review", "--proposed-model", "qwen3-0.6b"], 1),
        ("floor fail local", ["bash", S("scripts/quality_floor_check.sh"), "--task", "any", "--proposed-model", "my-local-gguf-model"], 1),
        ("floor pass tier2", ["bash", S("scripts/quality_floor_check.sh"), "--task", "status update", "--proposed-model", "gemini-3-flash"], 0),
    ]
    for name, cmd, want in cases:
        try:
            r = run(cmd)
        except subprocess.TimeoutExpired:
            fail(f"smoke {name}: timeout")
            continue
        if r.returncode != want:
            fail(f"smoke {name}: exit {r.returncode} != {want}\n  out={r.stdout.strip()}\n  err={r.stderr.strip()}")
    # mode output contract
    r = run(["bash", S("scripts/mode_selector.sh"), "--symptom", "cannot login", "--evidence", "public"])
    if "mode=support_without_login" not in r.stdout or "action=" not in r.stdout or "required=" not in r.stdout:
        fail(f"mode output contract broken:\n{r.stdout}")
    # validator verdict line
    r = run(["bash", S("scripts/shieldswarm_validate.sh"), "--command", "true"])
    if "verdict=" not in r.stdout:
        fail(f"validate verdict line missing:\n{r.stdout}")
    # ROE content gate: untouched template must FAIL, filled copy must PASS
    with tempfile.TemporaryDirectory() as td:
        tdir = Path(td)
        tmpl = ROOT / "templates" / "red_team_roe.yaml"
        unfilled = tdir / "roe_unfilled.yaml"
        unfilled.write_text(tmpl.read_text(encoding="utf-8"), encoding="utf-8")
        r = run(["bash", S("scripts/shieldswarm_validate.sh"), "--command", "true",
                 "--mode", "red_team", "--roe", str(unfilled)])
        if r.returncode != 1 or "roe_unfilled" not in r.stdout:
            fail(f"ROE content gate: untouched template not rejected:\n{r.stdout} {r.stderr}")
        filled = tdir / "roe_filled.yaml"
        filled.write_text(
            tmpl.read_text(encoding="utf-8")
            .replace('exercise_name: ""', 'exercise_name: "staging-tabletop-1"')
            .replace('authorized_by: ""', 'authorized_by: "operator-alice"')
            .replace('rollback_owner: ""', 'rollback_owner: "ops-bob"'),
            encoding="utf-8")
        r = run(["bash", S("scripts/shieldswarm_validate.sh"), "--command", "true",
                 "--mode", "red_team", "--roe", str(filled)])
        if r.returncode != 0 or "verdict=PASS" not in r.stdout:
            fail(f"ROE content gate: filled ROE rejected:\n{r.stdout} {r.stderr}")
        # whitespace-only core value must not count as filled
        ws = tdir / "roe_ws.yaml"
        ws.write_text(
            filled.read_text(encoding="utf-8")
            .replace('authorized_by: "operator-alice"', 'authorized_by: "   "'),
            encoding="utf-8")
        r = run(["bash", S("scripts/shieldswarm_validate.sh"), "--command", "true",
                 "--mode", "red_team", "--roe", str(ws)])
        if r.returncode != 1 or "roe_unfilled" not in r.stdout:
            fail(f"ROE content gate: whitespace-only value accepted:\n{r.stdout} {r.stderr}")
        # commented-out key must not satisfy the structural check
        cm = tdir / "roe_commented.yaml"
        cm.write_text(
            filled.read_text(encoding="utf-8").replace("scope:", "# scope:"),
            encoding="utf-8")
        r = run(["bash", S("scripts/shieldswarm_validate.sh"), "--command", "true",
                 "--mode", "red_team", "--roe", str(cm)])
        if r.returncode != 1 or "roe_fields_missing" not in r.stdout:
            fail(f"ROE content gate: commented-out key accepted:\n{r.stdout} {r.stderr}")

    # approval gate: record + self-approval block + check
    with tempfile.TemporaryDirectory() as td:
        af = f"{td}/approval.jsonl"
        import getpass
        me = getpass.getuser()
        r = run(["bash", S("scripts/approval_gate.sh"), "--scope", "restart gateway", "--risk", "low",
                 "--rollback-owner", "alice", "--approver", "bob", "--file", af])
        if r.returncode != 0 or "approval_id=" not in r.stdout:
            fail(f"approval record failed: {r.stdout} {r.stderr}")
        elif not (Path(td) / "approval.jsonl").exists():
            fail("approval.jsonl not written")
        r = run(["bash", S("scripts/approval_gate.sh"), "--scope", "prod deploy", "--risk", "high",
                 "--rollback-owner", "alice", "--approver", me, "--file", af])
        if r.returncode != 1 or "blocked" not in r.stdout:
            fail(f"high-risk self-approval not blocked: {r.stdout} {r.stderr}")
        aid = (Path(td) / "approval.jsonl").read_text().split('"id":"', 1)[1].split('"', 1)[0]
        r = run(["bash", S("scripts/approval_gate.sh"), "--file", af, "--check", "--id", aid])
        if r.returncode != 0 or "approval_status=found" not in r.stdout:
            fail(f"approval check failed: {r.stdout} {r.stderr}")
    if not any("smoke" in f for f in FAILURES):
        ok("functional smoke tests passed (mode/validate/floor/approval, PASS+FAIL paths)")


# ── 9. safety phrases ────────────────────────────────────────────────────────
REQUIRED_PHRASES = [
    "No attack traffic",
    "No login bypass",
    "STOP SHIELDSWARM EXERCISE NOW",
    "Never silently downgrade",
    "defensive-only",
    "authorization-gated",
    "three single GET or HEAD requests in 10 minutes",
    "Rules of Engagement",
    "not an official",
]


def check_phrases(text: str) -> None:
    for phrase in REQUIRED_PHRASES:
        if phrase not in text:
            fail(f"missing safety phrase: {phrase}")
    if not FAILURES:
        ok("required safety phrases present")


# ── 10. secrets + dangerous patterns ─────────────────────────────────────────
SECRET_PATTERNS = [
    r"clh_[A-Za-z0-9_-]{20,}",
    r"claw_sk_[A-Za-z0-9_-]{12,}",
    r"AKIA[0-9A-Z]{16}",
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    r"Bearer [A-Za-z0-9._-]{16,}",
]
DANGEROUS_PATTERNS = [
    r"\bnmap\b", r"\bmasscan\b", r"\bsqlmap\b", r"\bhydra\b", r"\bmsfconsole\b",
    r"\bslowloris\b", r"\bhping3\b", r"\bwrk\b", r"\bsiege\b", r"\bab -n\b",
    r"\bgobuster\b", r"\bffuf\b", r"\bdirkb\b", r"\bwpscan\b",
]
# patterns allowed to appear ONLY inside the validator's own blocklist (scripts/)


def check_clean() -> None:
    # Secrets: scanned in every text file (code included) — a real credential
    # must never appear anywhere in the package.
    # Dangerous traffic patterns: scanned in docs/config only. Executables
    # (.sh/.py) legitimately name tools inside their own defensive blocklists
    # (the validator's blocklist, this harness's patterns); their behavior is
    # covered by the functional smoke tests instead.
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix not in {".md", ".yaml", ".yml", ".py", ".json"}:
            continue
        body = read(p)
        for pat in SECRET_PATTERNS:
            if re.search(pat, body):
                fail(f"possible secret in {p.name}: {pat}")
        if p.suffix in {".md", ".yaml", ".yml", ".json"}:
            for pat in DANGEROUS_PATTERNS:
                if re.search(pat, body, re.I):
                    fail(f"dangerous pattern in {p.relative_to(ROOT)}: {pat}")
    if not any("secret" in f or "dangerous" in f for f in FAILURES):
        ok("no secrets or dangerous patterns in docs/configs")


# ── 11. changelog/version consistency ────────────────────────────────────────
def check_changelog(version: str) -> None:
    if not version:
        warn("version not parsed; skipping changelog check")
        return
    cl = read(ROOT / "CHANGELOG.md")
    if f"v{version}" not in cl:
        fail(f"CHANGELOG missing entry for v{version}")
    else:
        ok(f"CHANGELOG has v{version} entry")


def main() -> int:
    text = read(SKILL)
    if not text:
        print("ALL CHECKS FAILED (SKILL.md missing)")
        return 1
    check_hygiene()
    meta = check_frontmatter(text)
    check_references([SKILL] + sorted((ROOT / "references").glob("*.md")))
    check_all_fences()
    check_yaml_templates()
    check_matrix()
    check_scripts()
    smoke()
    check_phrases(text)
    check_clean()
    check_changelog(meta.get("version", ""))
    if FAILURES:
        print(f"── grade: {len(FAILURES)} FAILURES ──")
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
