#!/usr/bin/env python3
"""skill-auditor — automated security audit for AI agent skills.

Usage:
    # Audit a single skill folder
    python3 vet.py path/to/some-skill

    # JSON output (for CI)
    python3 vet.py path/to/some-skill --json

    # Score only (0-100)
    python3 vet.py path/to/some-skill --score

    # Batch audit a directory of skills
    python3 vet.py --batch path/to/skills/

    # CI mode: exit non-zero if any skill scores above threshold
    python3 vet.py --batch path/to/skills/ --fail-on high
    python3 vet.py path/to/some-skill --fail-on critical

Exit codes:
    0  — all skills passed (or below fail-on threshold)
    1  — at least one skill hit the fail-on threshold
    2  — usage error / scan error
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path

# Allow running both from repo root and from inside the skill folder.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from score import (  # noqa: E402
    RULES,
    SEVERITY_WEIGHT,
    score_violations,
    severity_for_score,
    verdict_for_score,
    SEVERITY_CRITICAL,
    SEVERITY_HIGH,
    SEVERITY_MEDIUM,
    SEVERITY_LOW,
)

# ────────────────────────────────────────────────────────────────────
# Rule patterns. Each maps rule_id -> compiled regex (or list of regex).
# Patterns are case-insensitive. Keep in sync with references/rules.md.
# ────────────────────────────────────────────────────────────────────

# File extensions we actually scan. Other extensions (images, etc.) are skipped.
SCANNABLE_EXT = {
    ".md", ".markdown",
    ".py",
    ".sh", ".bash", ".zsh",
    ".js", ".ts", ".jsx", ".tsx", ".mjs", ".cjs",
    ".yaml", ".yml",
    ".json",
    ".txt", ".toml", ".ini", ".cfg",
}

DEFAULT_ALLOWLIST = {
    "github.com", "api.github.com", "raw.githubusercontent.com",
    "clawhub.ai",
    "pypi.org", "files.pythonhosted.org",
    "registry.npmjs.org",
    "openai.com", "api.openai.com",
    "anthropic.com", "api.anthropic.com",
    "googleapis.com",
    "cloudflare.com", "workers.cloudflare.com",
    "api.open-meteo.com",  # public free weather API, no key
    "localhost", "127.0.0.1",  # local dev
}


# CRITICAL patterns
PATTERNS_CRITICAL = {
    "CRED_SSH": [
        re.compile(r"~?/\.ssh/", re.I),
        re.compile(r"\b(id_rsa|id_ed25519|id_ecdsa)\b", re.I),
    ],
    "CRED_AWS": [
        re.compile(r"~?/\.aws/(credentials|config)", re.I),
        re.compile(r"\bAWS_SHARED_CREDENTIALS_FILE\b"),
    ],
    "CRED_KEYCHAIN": [
        re.compile(r"\bsecurity\s+find-generic-password", re.I),
        re.compile(r"\bsecret-tool\s+lookup", re.I),
        re.compile(r"\bcmdkey\s+/list", re.I),
    ],
    "CRED_COOKIES": [
        re.compile(r"(Cookies|cookies\.db|cookies\.sqlite)", re.I),
        re.compile(r"(Library/Application Support/Google/Chrome)", re.I),
        re.compile(r"\bSessionStorage\b", re.I),
    ],
    "IDENTITY_FILES": [
        re.compile(r"\b(MEMORY|USER|SOUL|IDENTITY)\.md\b", re.I),
    ],
    "RCE_EVAL": [
        re.compile(r"\beval\s*\(", re.I),
        re.compile(r"\bexec\s*\(", re.I),
    ],
    "RCE_PICKLE": [
        re.compile(r"\bpickle\.loads?\s*\(", re.I),
        re.compile(r"\byaml\.load\s*\((?![^)]*Loader\s*=\s*SafeLoader)", re.I),
    ],
    "EXFIL_LARGE": [
        # heuristic: glob read user files + network
        re.compile(r"(glob|os\.listdir|Path\.glob).*(\~\/|/Users/|/home/)", re.I),
    ],
    "PERM_SUDO": [
        re.compile(r"\bsudo\s+(apt|yum|brew|chmod|chown|rm|cp|mv|tee)", re.I),
        re.compile(r"/etc/sudoers", re.I),
        re.compile(r"\bos\.getSudo\b", re.I),
    ],
}

# HIGH patterns
PATTERNS_HIGH = {
    "NET_CURL_PIPED": [
        re.compile(r"curl[^|]*\|\s*(sh|bash|python)", re.I),
        re.compile(r"wget[^|]*\|\s*(sh|bash|python)", re.I),
    ],
    "NET_IP_LITERAL": [
        re.compile(r"https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"),
    ],
    "NET_PASTEBIN": [
        re.compile(r"https?://(pastebin\.com|paste\.ee|0bin\.net|hastebin|ix\.io)", re.I),
    ],
    "NET_UNKNOWN_HOST": [],  # filled dynamically per-file
    "OBFUSCATE_BASE64": [
        re.compile(r"base64\s+-d", re.I),
        re.compile(r"\bb64decode\b", re.I),
        # long base64-looking blob
        re.compile(r"['\"][A-Za-z0-9+/=]{120,}['\"]"),
    ],
    "OBFUSCATE_HEX_BLOB": [
        re.compile(r"\\x[0-9a-f]{2}", re.I),  # hex escapes
        re.compile(r"['\"][0-9a-f]{200,}['\"]", re.I),
    ],
    "OBFUSCATE_MINIFIED": [
        # minified JS in non-JS file
        re.compile(r"\.(md|sh|yaml)\b.*[a-z]\{[a-z]:[a-z]", re.I),
    ],
    "SHELL_TRUE": [
        re.compile(r"subprocess\.(run|call|Popen|check_output)\s*\([^)]*shell\s*=\s*True", re.I),
    ],
    "SUPPLY_PIP_URL": [
        re.compile(r"pip\s+install\s+https?://", re.I),
        re.compile(r"npm\s+install\s+https?://", re.I),
    ],
    "FILE_WRITE_OUTSIDE": [
        re.compile(r"~\/\.bashrc", re.I),
        re.compile(r"~\/\.zshrc", re.I),
        re.compile(r"\/etc\/", re.I),
        re.compile(r"~\/Library\/LaunchAgents", re.I),
    ],
    "PERM_CHMOD_777": [
        re.compile(r"chmod\s+[-\w]*777\b", re.I),
    ],
}

# MEDIUM patterns
PATTERNS_MEDIUM = {
    "NET_NO_TLS": [
        re.compile(r"http://(?!localhost|127\.0\.0\.1)[a-z0-9.-]+\.[a-z]{2,}", re.I),
    ],
    "NET_TOR": [
        re.compile(r"\.onion\b", re.I),
        re.compile(r"\btor\s+proxy\b", re.I),
    ],
    "CRED_ENV_TOKEN": [],  # filled dynamically based on frontmatter
    "DYN_IMPORT": [
        re.compile(r"importlib\.import_module\s*\(", re.I),
    ],
    "FILE_DELETE": [
        re.compile(r"os\.remove\s*\(", re.I),
        re.compile(r"\brm\s+-rf\s+~?\/", re.I),
        re.compile(r"shutil\.rmtree\s*\(", re.I),
    ],
    "NET_TELEMETRY": [
        re.compile(r"(analytics|telemetry|tracking)\.(post|send|track)", re.I),
    ],
    "SUPPLY_PKG_LIST": [],  # heuristic: pip install without metadata
    "PERM_BROAD_SCOPE": [
        re.compile(r"scope\s*=\s*[\"'].*\b(repo|admin|user)\b", re.I),
    ],
    "PERM_REQUEST_KEY": [
        re.compile(r"(please\s+paste|enter\s+your|provide\s+your)\s+(api\s+key|token|password|secret)", re.I),
    ],
}

# LOW patterns
PATTERNS_LOW = {
    "MISSING_FRONTMATTER": [],  # checked separately on SKILL.md
    "NO_LICENSE": [],            # checked separately (no LICENSE file)
    "NO_VERSION": [],            # checked separately on SKILL.md frontmatter
    "HARDCODED_PATH": [
        re.compile(r"/Users/[a-z_]+/", re.I),
        re.compile(r"C:\\Users\\[a-z_]+\\", re.I),
        re.compile(r"/home/[a-z_]+/", re.I),
    ],
    "EVAL_NO_INPUT": [],  # if eval() with no obvious input (subset of RCE_EVAL)
    "SLEEP_LONG": [
        re.compile(r"time\.sleep\s*\(\s*(\d{2,})\s*\)"),
        re.compile(r"\bsleep\s+(\d{2,})\b"),
    ],
}

ALL_PATTERN_GROUPS = [
    (SEVERITY_CRITICAL, PATTERNS_CRITICAL),
    (SEVERITY_HIGH, PATTERNS_HIGH),
    (SEVERITY_MEDIUM, PATTERNS_MEDIUM),
    (SEVERITY_LOW, PATTERNS_LOW),
]


@dataclass
class Violation:
    rule_id: str
    severity: str
    file: str
    line: int
    col: int
    snippet: str
    description: str


@dataclass
class AuditResult:
    skill_path: str
    skill_name: str = ""
    skill_version: str = ""
    author: str = ""
    files_scanned: int = 0
    lines_scanned: int = 0
    violations: list[Violation] = field(default_factory=list)
    permission_mismatches: list[str] = field(default_factory=list)
    risk_score: int = 0
    severity_label: str = ""
    verdict: str = ""
    audited_at: str = ""
    auditor_version: str = "1.0.0"


# ────────────────────────────────────────────────────────────────────
# Frontmatter parsing
# ────────────────────────────────────────────────────────────────────

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FM_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.startswith("#"):
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip().strip("\"'")
    return fm


def parse_metadata_block(fm: dict[str, str]) -> dict:
    """Parse the metadata.openclaw block if present.
    It's stored as a single-line JSON in the value."""
    raw = fm.get("metadata", "")
    if not raw:
        return {}
    try:
        # metadata is JSON
        return json.loads(raw)
    except Exception:
        return {}


# ────────────────────────────────────────────────────────────────────
# Scanning
# ────────────────────────────────────────────────────────────────────


def find_skill_files(skill_path: Path) -> list[Path]:
    """Recursively find scannable files in a skill folder.

    Skips:
    - Hidden directories (.git, .clawhub, __pycache__) — except .github
    - references/ and tests/ subdirectories — these are documentation and
      test samples by convention, and audit-skill's own references/ naturally
      mentions sensitive patterns when describing rules. For a normal skill
      without references/ or tests/, this is a no-op.
    """
    EXCLUDE_DIRS = {"references", "tests", "examples", "__pycache__"}
    files = []
    for p in sorted(skill_path.rglob("*")):
        if not p.is_file():
            continue
        if any(part.startswith(".") and part not in (".github",) for part in p.parts):
            # skip hidden dirs (.git, .clawhub) but keep .github
            continue
        # Skip excluded subdirs (relative to skill root)
        try:
            rel_parts = p.relative_to(skill_path).parts
            if any(part in EXCLUDE_DIRS for part in rel_parts[:-1]):
                continue
        except ValueError:
            pass
        if p.suffix.lower() in SCANNABLE_EXT:
            files.append(p)
    return files


def extract_domains(text: str) -> set[str]:
    """Extract domain names from text for allowlist comparison."""
    domains = set()
    for m in re.finditer(r"https?://([a-z0-9.-]+\.[a-z]{2,})", text, re.I):
        domains.add(m.group(1).lower())
    return domains


def strip_python_non_code(text: str) -> str:
    """Remove comments and string literals from Python code.

    Static analysis of detection-rule code is tricky: the rule descriptions
    and regex patterns are themselves strings that naturally contain the very
    patterns we scan for (e.g. score.py has "Reads ~/.aws/credentials" as a
    rule description). Stripping strings and comments leaves only actual
    code, so pattern matches reflect real behaviour, not documentation.
    """
    # Remove triple-quoted strings (docstrings)
    text = re.sub(r'"""[\s\S]*?"""', '""', text)
    text = re.sub(r"'''[\s\S]*?'''", "''", text)
    # Remove single-line comments
    text = re.sub(r'(?m)#.*$', '', text)
    # Remove string literals (single and double quoted, with escape handling)
    text = re.sub(r'"[^"\\]*(?:\\.[^"\\]*)*"', '""', text)
    text = re.sub(r"'[^'\\]*(?:\\.[^'\\]*)*'", "''", text)
    return text


def extract_md_code_blocks(text: str) -> str:
    """Extract only fenced code blocks from Markdown.

    Prose and inline code in .md files are documentation: they naturally
    mention sensitive patterns when describing rules (e.g. "the rule
    `CRED_AWS` matches `~/.aws/credentials`"). Only fenced code blocks
    represent actual commands/programs that would be executed, so we scan
    only those.
    """
    blocks = []
    # Match fenced code blocks: ```lang\n...\n```
    for m in re.finditer(r'```[a-zA-Z0-9]*\n(.*?)```', text, re.DOTALL):
        blocks.append(m.group(1))
    return "\n".join(blocks)


def preprocess_for_scanning(text: str, ext: str) -> str:
    """Preprocess file content based on extension to reduce false positives."""
    if ext == ".py":
        return strip_python_non_code(text)
    if ext in (".md", ".markdown"):
        return extract_md_code_blocks(text)
    return text


def scan_file(path: Path, skill_root: Path, declared_env: set[str]) -> list[Violation]:
    """Scan a single file, return all violations found."""
    try:
        raw_text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    # Preprocess: for .py, strip strings/comments; for .md, keep only code blocks
    text = preprocess_for_scanning(raw_text, path.suffix.lower())
    if not text.strip():
        return []

    rel = str(path.relative_to(skill_root))
    violations: list[Violation] = []

    # Find domains in this file for NET_UNKNOWN_HOST
    file_domains = extract_domains(text)
    unknown_domains = {d for d in file_domains if d not in DEFAULT_ALLOWLIST}

    # Read token-like env vars to check against declared primaryEnv
    undeclared_token_reads = []
    for m in re.finditer(r"\b([A-Z][A-Z0-9_]*(TOKEN|API_KEY|SECRET|PASSWORD))\b", text):
        if m.group(1) not in declared_env:
            undeclared_token_reads.append(m.group(1))

    lines = text.splitlines()
    for severity, group in ALL_PATTERN_GROUPS:
        for rule_id, patterns in group.items():
            # Special-case dynamic rules
            if rule_id == "NET_UNKNOWN_HOST":
                # one violation per unknown domain
                for d in unknown_domains:
                    # find first line where it appears
                    for i, line in enumerate(lines, 1):
                        if d in line:
                            violations.append(Violation(
                                rule_id=rule_id, severity=severity,
                                file=rel, line=i, col=line.find(d) + 1,
                                snippet=line.strip()[:100],
                                description=f"Network call to non-allowlisted domain: {d}",
                            ))
                            break
                continue

            if rule_id == "CRED_ENV_TOKEN":
                seen = set()
                for env_var in undeclared_token_reads:
                    if env_var in seen:
                        continue
                    seen.add(env_var)
                    # find line
                    for i, line in enumerate(lines, 1):
                        if env_var in line:
                            violations.append(Violation(
                                rule_id=rule_id, severity=severity,
                                file=rel, line=i, col=line.find(env_var) + 1,
                                snippet=line.strip()[:100],
                                description=f"Reads undeclared env var: {env_var}",
                            ))
                            break
                continue

            for pat in patterns:
                for m in pat.finditer(text):
                    line_no = text.count("\n", 0, m.start()) + 1
                    col = m.start() - text.rfind("\n", 0, m.start())
                    snippet = lines[line_no - 1].strip()[:100] if line_no <= len(lines) else ""
                    violations.append(Violation(
                        rule_id=rule_id, severity=severity,
                        file=rel, line=line_no, col=col,
                        snippet=snippet,
                        description=RULES.get(rule_id).description if rule_id in RULES else "",
                    ))

    return violations


def check_skill_level_rules(skill_path: Path, fm: dict) -> list[Violation]:
    """Rules that aren't line-based: missing frontmatter, no license, no version."""
    v: list[Violation] = []
    skill_md = skill_path / "SKILL.md"
    if skill_md.exists():
        if "name" not in fm or "description" not in fm:
            v.append(Violation(
                rule_id="MISSING_FRONTMATTER", severity=SEVERITY_LOW,
                file="SKILL.md", line=1, col=1, snippet="",
                description="SKILL.md frontmatter missing required field(s) name/description",
            ))
        if "version" not in fm:
            v.append(Violation(
                rule_id="NO_VERSION", severity=SEVERITY_LOW,
                file="SKILL.md", line=1, col=1, snippet="",
                description="No version field in frontmatter",
            ))
    if not (skill_path / "LICENSE").exists() and not (skill_path / "LICENSE.md").exists():
        v.append(Violation(
            rule_id="NO_LICENSE", severity=SEVERITY_LOW,
            file="", line=0, col=0, snippet="",
            description="No LICENSE file in skill folder",
        ))
    return v


def check_permission_mismatch(fm: dict, metadata: dict, violations: list[Violation]) -> list[str]:
    """Compare declared permissions against actual behavior observed in violations."""
    mismatches = []
    declared_bins = set()
    declared_env = set()
    if isinstance(metadata, dict):
        oc = metadata.get("openclaw", {})
        if isinstance(oc, dict):
            req = oc.get("requires", {})
            if isinstance(req, dict):
                if req.get("bins"):
                    declared_bins.update(req["bins"])
                if req.get("env"):
                    declared_env.update(req["env"])

    has_net = any(v.rule_id.startswith("NET_") for v in violations)
    uses_curl = any("curl" in v.snippet.lower() or "wget" in v.snippet.lower() for v in violations)
    uses_http_lib = any("requests" in v.snippet or "fetch(" in v.snippet for v in violations)

    if (uses_curl or uses_http_lib) and "curl" not in declared_bins and "wget" not in declared_bins:
        mismatches.append("Uses curl/wget in code but not declared in metadata.openclaw.requires.bins")

    if has_net and not declared_env and not metadata:
        mismatches.append("Makes network calls but no metadata.openclaw declared")

    return mismatches


def audit_skill(skill_path: Path) -> AuditResult:
    """Audit a single skill folder. Returns AuditResult."""
    skill_path = skill_path.resolve()
    if not skill_path.is_dir():
        raise SystemExit(f"Not a directory: {skill_path}")

    result = AuditResult(
        skill_path=str(skill_path),
        audited_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
    )

    skill_md = skill_path / "SKILL.md"
    fm = parse_frontmatter(skill_md.read_text(encoding="utf-8")) if skill_md.exists() else {}
    metadata = parse_metadata_block(fm)

    result.skill_name = fm.get("name", skill_path.name)
    result.skill_version = fm.get("version", "")

    declared_env = set()
    if isinstance(metadata, dict):
        oc = metadata.get("openclaw", {})
        if isinstance(oc, dict):
            req = oc.get("requires", {})
            if isinstance(req, dict) and req.get("env"):
                declared_env.update(req["env"])

    files = find_skill_files(skill_path)
    result.files_scanned = len(files)

    all_violations: list[Violation] = []
    total_lines = 0
    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
            total_lines += text.count("\n") + 1
        except Exception:
            pass
        all_violations.extend(scan_file(f, skill_path, declared_env))

    all_violations.extend(check_skill_level_rules(skill_path, fm))
    result.permission_mismatches = check_permission_mismatch(fm, metadata, all_violations)

    result.violations = all_violations
    result.lines_scanned = total_lines

    rule_ids = list({v.rule_id for v in all_violations})
    result.risk_score = score_violations(rule_ids)
    result.severity_label = severity_for_score(result.risk_score)
    result.verdict = verdict_for_score(result.risk_score)

    return result


# ────────────────────────────────────────────────────────────────────
# Output
# ────────────────────────────────────────────────────────────────────


def format_markdown(result: AuditResult) -> str:
    lines = [
        "SKILL AUDIT REPORT",
        "═" * 50,
        f"Skill:    {result.skill_name}",
        f"Path:     {result.skill_path}",
        f"Version:  {result.skill_version or '(none)'}",
        f"Audited:  {result.audited_at} by skill-auditor v{result.auditor_version}",
        "─" * 50,
        "METRICS:",
        f"• Files scanned:    {result.files_scanned}",
        f"• Lines scanned:    {result.lines_scanned}",
        f"• Rule violations:  {len(result.violations)}",
        "─" * 50,
        f"RISK SCORE: {result.risk_score}/100  →  {result.severity_label}",
        "",
    ]

    by_sev = {SEVERITY_CRITICAL: [], SEVERITY_HIGH: [], SEVERITY_MEDIUM: [], SEVERITY_LOW: []}
    for v in result.violations:
        by_sev.get(v.severity, []).append(v)

    for sev, label in [
        (SEVERITY_CRITICAL, "⛔ CRITICAL"),
        (SEVERITY_HIGH, "🔴 HIGH"),
        (SEVERITY_MEDIUM, "🟡 MEDIUM"),
        (SEVERITY_LOW, "🟢 LOW"),
    ]:
        items = by_sev[sev]
        if not items:
            continue
        pts = SEVERITY_WEIGHT[sev]
        lines.append(f"{label} ({pts} pts each):")
        for v in items:
            loc = f"{v.file}:{v.line}" if v.file else "(skill-level)"
            lines.append(f"  • [{v.rule_id}] {loc} — {v.description}")
            if v.snippet:
                lines.append(f"      {v.snippet}")
        lines.append("")

    if result.permission_mismatches:
        lines.append("PERMISSION MISMATCHES:")
        for m in result.permission_mismatches:
            lines.append(f"  • {m}")
        lines.append("")

    lines.append(f"VERDICT: {result.verdict}")
    lines.append("═" * 50)
    return "\n".join(lines)


def format_json(result: AuditResult) -> str:
    return json.dumps(asdict(result), indent=2, ensure_ascii=False)


SEVERITY_RANK = {
    SEVERITY_CRITICAL: 4, SEVERITY_HIGH: 3,
    SEVERITY_MEDIUM: 2, SEVERITY_LOW: 1,
}
SCORE_THRESHOLD = {SEVERITY_LOW: 15, SEVERITY_MEDIUM: 40, SEVERITY_HIGH: 70, SEVERITY_CRITICAL: 100}


def result_meets_fail_threshold(result: AuditResult, fail_on: str) -> bool:
    """True if result is at least as bad as fail_on tier."""
    threshold = SCORE_THRESHOLD[fail_on]
    return result.risk_score > (
        SCORE_THRESHOLD[{SEVERITY_LOW: SEVERITY_LOW, SEVERITY_MEDIUM: SEVERITY_LOW,
                          SEVERITY_HIGH: SEVERITY_MEDIUM, SEVERITY_CRITICAL: SEVERITY_HIGH}[fail_on]]
    ) and result.risk_score >= 0


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("path", nargs="?", help="Path to skill folder to audit")
    p.add_argument("--batch", metavar="DIR", help="Audit all subdirectories of DIR as skills")
    p.add_argument("--json", action="store_true", help="Output JSON (machine-readable)")
    p.add_argument("--score", action="store_true", help="Print only the 0-100 risk score")
    p.add_argument("--fail-on", choices=[SEVERITY_LOW, SEVERITY_MEDIUM, SEVERITY_HIGH, SEVERITY_CRITICAL],
                   help="Exit 1 if any skill reaches this severity (CI mode)")
    args = p.parse_args(argv)

    if not args.path and not args.batch:
        p.print_help()
        return 2

    results: list[AuditResult] = []
    if args.batch:
        batch_root = Path(args.batch).resolve()
        if not batch_root.is_dir():
            print(f"Error: {batch_root} is not a directory", file=sys.stderr)
            return 2
        for sub in sorted(batch_root.iterdir()):
            if sub.is_dir() and (sub / "SKILL.md").exists():
                results.append(audit_skill(sub))
    else:
        results.append(audit_skill(Path(args.path)))

    fail_on = args.fail_on
    had_failure = False

    for r in results:
        if args.score:
            print(f"{r.skill_name}: {r.risk_score}/100  {r.severity_label}")
        elif args.json:
            print(format_json(r))
        else:
            print(format_markdown(r))
            print()
        if fail_on and r.risk_score >= SCORE_THRESHOLD.get(fail_on, 0):
            had_failure = True

    if fail_on:
        return 1 if had_failure else 0
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
