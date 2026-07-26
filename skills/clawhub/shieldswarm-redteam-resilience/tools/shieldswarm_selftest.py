#!/usr/bin/env python3
"""Local static/self-test harness for the ShieldSwarm skill package.

This script performs offline checks only. It does not contact Arena.ai, OpenClaw,
ClawHub, or any external service.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
TEMPLATES = ROOT / "templates"

REQUIRED_SECTIONS = [
    "# ShieldSwarm: Red-Team Resilience Commander",
    "## 1. First minute",
    "## 2. Choose the right mode",
    "## 3. Core safety rules",
    "## 4. Support without login",
    "## 5. Authenticated user support mode",
    "## 6. Authenticated operator mode",
    "## 7. Authorized red-team and purple-team work",
    "## 8. Swarm roles and minimum teams",
    "## 9. Incident response playbook",
    "## 10. Observability and evidence handling",
    "## 11. DDoS, bot, and edge-defense guidance",
    "## 12. Server, application, database, and queue hardening",
    "## 13. AI model resilience and weak-model fallback",
    "## 14. Approval-gated code and configuration execution",
    "## 15. Defensive examples",
    "## 16. Provider and platform notes",
    "## 17. Templates and package files",
    "## 18. Ethical promotion",
    "## 19. Validation before publishing",
    "## 20. Refusal and redirection",
    "## 21. Changelog",
]

REQUIRED_TEMPLATE_FILES = [
    "authorization_intake.yaml",
    "operator_authorization.yaml",
    "red_team_roe.yaml",
    "no_login_diagnostic.md",
    "support_ticket.md",
    "arena_improvement_report.md",
    "incident_report.md",
    "approval_request.md",
    "rollback_plan.md",
    "postmortem.md",
    "abuse_case.md",
    "red_team_finding.md",
    "risk_acceptance.md",
    "exercise_go_no_go.md",
    "exercise_abort.md",
    "model_resilience_policy.yaml",
    "model_router_change_review.md",
    "model_fallback_audit.md",
    "waf_rule_review.md",
    "false_positive_report.md",
    "status_page_update.md",
    "stakeholder_update.md",
    "secret_exposure_response.md",
    "redaction_checklist.md",
    "provider_escalation.md",
    "role_prompts.md",
    "quickstart.md",
    "validation_checklist.md",
    "promotion_copy.md",
    "account_hygiene.md",
    "onboarding_report.md",
]

REQUIRED_SAFETY_PHRASES = [
    "not an official Arena.ai",
    "No attack traffic",
    "No login bypass",
    "Support without login",
    "By default, the agent should make no active public requests",
    "Maximum: three single GET or HEAD requests in 10 minutes",
    "Rules of Engagement are required",
    "STOP SHIELDSWARM EXERCISE NOW",
    "Never use weak-model fallback for",
    "Approval-gated code and configuration execution",
    "No spam promotion",
]

DANGEROUS_EXEC_PATTERNS = [
    r"\bwhile\s+true\b.*\bcurl\b",
    r"\bfor\b.*\bcurl\b.*\bdone\b",
    r"\bab\s+-n\b",
    r"\bwrk\s+-",
    r"\bsiege\s+-",
    r"\bhping3\b",
    r"\bslowloris\b",
    r"\bhydra\b",
    r"\bnmap\b.*(-p-|--script|/0)",
    r"\bmasscan\b",
    r"\bsqlmap\b",
    r"\bffuf\b",
    r"\bgobuster\b",
    r"\bmsfconsole\b",
]

SECRET_PATTERNS = [
    r"clh_[A-Za-z0-9_-]{20,}",
    r"claw_sk_[A-Za-z0-9_-]{12,}",
    r"AKIA[0-9A-Z]{16}",
    r"-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY-----",
    r"Authorization:\s*Bearer\s+[A-Za-z0-9._-]{10,}",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def ok(msg: str) -> None:
    print(f"PASS: {msg}")


def warn(msg: str) -> None:
    print(f"WARN: {msg}")


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path}")
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter closing fence not found")
    return text[4:end], text[end + 5 :]


def parse_yaml_document(src: str, label: str) -> object:
    if yaml is None:
        # Minimal fallback: ensure colon-ish lines exist; the runtime normally has PyYAML.
        if ":" not in src:
            fail(f"{label}: not YAML-like and PyYAML unavailable")
        return {}
    try:
        return yaml.safe_load(src)
    except Exception as exc:
        fail(f"{label}: YAML parse error: {exc}")



def check_package_hygiene() -> None:
    allowed_root_files = {"SKILL.md", ".published", "_meta.json", "skill-card.md", "AGENT_DISCOVERY.md"}
    # ClawHub may add provenance metadata during installation; it is not package content.
    allowed_root_dirs = {"templates", "tools", ".clawhub"}
    for item in ROOT.iterdir():
        if item.is_file() and item.name not in allowed_root_files:
            fail(f"unexpected root file in package: {item.name}")
        if item.is_dir() and item.name not in allowed_root_dirs:
            fail(f"unexpected root directory in package: {item.name}")
    for bad in ROOT.rglob("*"):
        name = bad.name
        if name.startswith("SKILL.md.bak") or name.endswith("~") or name == "__pycache__" or name.endswith(".pyc"):
            fail(f"generated/backup artifact found: {bad.relative_to(ROOT)}")
    ok("package hygiene clean")


def check_frontmatter(text: str) -> None:
    fm, _ = split_frontmatter(text)
    data = parse_yaml_document(fm, "frontmatter")
    if not isinstance(data, dict):
        fail("frontmatter did not parse to mapping")
    allowed = {"name", "description", "permissions", "metadata"}
    extra = set(data) - allowed
    if extra:
        fail(f"unsupported frontmatter keys: {sorted(extra)}")
    if data.get("name") != "shieldswarm-redteam-resilience":
        fail("frontmatter name mismatch")
    desc = str(data.get("description", ""))
    if not (80 <= len(desc) <= 500):
        fail(f"frontmatter description length outside expected range: {len(desc)}")
    perms = data.get("permissions")
    if not isinstance(perms, dict):
        fail("frontmatter permissions missing or not a mapping")
    for key in ("file_read", "file_write", "network", "shell"):
        if key not in perms:
            fail(f"frontmatter permission missing: {key}")
        if not isinstance(perms[key], dict) or "scope" not in perms[key]:
            fail(f"frontmatter permission lacks scope: {key}")
    ok("frontmatter parses with supported keys and permission scopes")


def check_code_fences(path: Path) -> None:
    lines = read(path).splitlines()
    stack: list[tuple[int, str]] = []
    fence_re = re.compile(r"^(`{3,}|~{3,})")
    for i, line in enumerate(lines, 1):
        m = fence_re.match(line.strip())
        if not m:
            continue
        fence = m.group(1)
        if not stack:
            stack.append((i, fence[0]))
        else:
            start, ch = stack[-1]
            if fence[0] == ch:
                stack.pop()
            else:
                fail(f"{path}: mismatched fence at line {i}; opened line {start}")
    if stack:
        start, _ = stack[-1]
        fail(f"{path}: unclosed code fence opened at line {start}")


def check_required_sections(text: str) -> None:
    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            fail(f"missing required section: {sec}")
    ok("required sections present")


def check_heading_sequence(text: str) -> None:
    in_fence = False
    nums = []
    for line in text.splitlines():
        if line.strip().startswith("```") or line.strip().startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^## (\d+)\. ", line)
        if m:
            nums.append(int(m.group(1)))
    expected = list(range(1, 22))
    if nums != expected:
        fail(f"major heading sequence mismatch: {nums} != {expected}")
    ok("major heading numbering is sequential")


def check_templates(text: str) -> None:
    if not TEMPLATES.is_dir():
        fail("templates directory missing")
    for name in REQUIRED_TEMPLATE_FILES:
        path = TEMPLATES / name
        if not path.exists():
            fail(f"missing required template: {name}")
        check_code_fences(path)
        if name.endswith((".yaml", ".yml")):
            parse_yaml_document(read(path), name)
    referenced = sorted(set(re.findall(r"templates/([A-Za-z0-9_.-]+)", text)))
    for name in referenced:
        if not (TEMPLATES / name).exists():
            fail(f"referenced template does not exist: {name}")
    ok(f"templates present and parse ({len(REQUIRED_TEMPLATE_FILES)} required, {len(referenced)} referenced)")


def check_safety_phrases(text: str) -> None:
    for phrase in REQUIRED_SAFETY_PHRASES:
        if phrase not in text:
            fail(f"missing safety phrase: {phrase}")
    ok("required safety phrases present")


def check_no_secrets(text: str) -> None:
    for pat in SECRET_PATTERNS:
        if re.search(pat, text):
            fail(f"possible secret matched pattern: {pat}")
    for path in TEMPLATES.glob("*"):
        body = read(path)
        for pat in SECRET_PATTERNS:
            if re.search(pat, body):
                fail(f"possible secret in {path.name}: {pat}")
    ok("no obvious secrets detected")


def check_no_dangerous_exec(text: str) -> None:
    body = text + "\n" + "\n".join(read(p) for p in TEMPLATES.glob("*"))
    for pat in DANGEROUS_EXEC_PATTERNS:
        if re.search(pat, body, flags=re.IGNORECASE | re.DOTALL):
            fail(f"dangerous executable pattern detected: {pat}")
    ok("no dangerous traffic/exploit command patterns detected")


def check_line_lengths(text: str) -> None:
    long_lines = []
    for i, line in enumerate(text.splitlines(), 1):
        if len(line) > 220:
            long_lines.append((i, len(line)))
    if long_lines:
        warn(f"{len(long_lines)} lines exceed 220 chars: {long_lines[:5]}")
    else:
        ok("no very long lines in SKILL.md")


def simulate_modes(text: str) -> None:
    scenarios = {
        "no_login_public": ["Support without login", "public check limits", "support_ticket.md"],
        "authenticated_user": ["Authenticated user support mode", "Safe login guidance", "one-time codes directly"],
        "authenticated_operator": ["Authenticated operator mode", "operator_authorization.yaml", "approval gates"],
        "red_team": ["Rules of Engagement are required", "red_team_roe.yaml", "emergency stop phrase"],
        "model_resilience": ["weak-model fallback", "model_resilience_policy.yaml", "Never use weak-model fallback"],
        "promotion": ["Ethical promotion", "promotion_copy.md", "No spam promotion"],
    }
    for name, needles in scenarios.items():
        missing = [n for n in needles if n not in text]
        if missing:
            fail(f"scenario {name} missing: {missing}")
    ok("scenario coverage checks passed")


def main() -> None:
    text = read(SKILL)
    check_package_hygiene()
    check_frontmatter(text)
    check_code_fences(SKILL)
    ok("SKILL.md code fences balanced")
    check_required_sections(text)
    check_heading_sequence(text)
    check_templates(text)
    check_safety_phrases(text)
    check_no_secrets(text)
    check_no_dangerous_exec(text)
    check_line_lengths(text)
    simulate_modes(text)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
