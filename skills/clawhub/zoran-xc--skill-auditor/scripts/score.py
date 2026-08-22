#!/usr/bin/env python3
"""Risk scoring model for skill-auditor.

Each rule has a weight (points). The total score is the sum of all
triggered rule weights, capped at 100. Higher = riskier.

Severity tiers:
  CRITICAL  25 pts  — direct credential exfil, remote code execution
  HIGH      15 pts  — strong indicators of malicious intent
  MEDIUM    10 pts  — suspicious patterns that warrant review
  LOW        5 pts  — minor concerns / bad practice

The scoring model is intentionally simple (additive, no bayesian magic)
so it's easy to reason about and audit. See references/scoring.md for
the rationale and how to tune it.
"""
from __future__ import annotations
from dataclasses import dataclass


SEVERITY_CRITICAL = "critical"
SEVERITY_HIGH = "high"
SEVERITY_MEDIUM = "medium"
SEVERITY_LOW = "low"

SEVERITY_WEIGHT = {
    SEVERITY_CRITICAL: 25,
    SEVERITY_HIGH: 15,
    SEVERITY_MEDIUM: 10,
    SEVERITY_LOW: 5,
}


@dataclass
class Rule:
    rule_id: str
    severity: str
    description: str


# Rule catalog. Keep in sync with references/rules.md.
RULES: dict[str, Rule] = {
    # ── CRITICAL (25 pts) ──────────────────────────────────────────
    "CRED_SSH": Rule(
        "CRED_SSH", SEVERITY_CRITICAL,
        "Reads ~/.ssh (SSH private keys) without explicit justification.",
    ),
    "CRED_AWS": Rule(
        "CRED_AWS", SEVERITY_CRITICAL,
        "Reads ~/.aws/credentials or ~/.aws/config.",
    ),
    "CRED_KEYCHAIN": Rule(
        "CRED_KEYCHAIN", SEVERITY_CRITICAL,
        "Accesses macOS keychain / Linux secret service / Windows credential manager.",
    ),
    "CRED_COOKIES": Rule(
        "CRED_COOKIES", SEVERITY_CRITICAL,
        "Reads browser cookies, session storage, or saved passwords.",
    ),
    "IDENTITY_FILES": Rule(
        "IDENTITY_FILES", SEVERITY_CRITICAL,
        "Touches MEMORY.md / USER.md / SOUL.md / IDENTITY.md (core agent identity).",
    ),
    "RCE_EVAL": Rule(
        "RCE_EVAL", SEVERITY_CRITICAL,
        "Uses eval() / exec() with external or untrusted input.",
    ),
    "RCE_PICKLE": Rule(
        "RCE_PICKLE", SEVERITY_CRITICAL,
        "Uses pickle.loads / yaml.load (unsafe) on external data.",
    ),
    "EXFIL_LARGE": Rule(
        "EXFIL_LARGE", SEVERITY_CRITICAL,
        "Bulk-reads user files then prepares network upload (data exfiltration).",
    ),
    "PERM_SUDO": Rule(
        "PERM_SUDO", SEVERITY_CRITICAL,
        "Requests sudo / root / modifies sudoers.",
    ),

    # ── HIGH (15 pts) ──────────────────────────────────────────────
    "NET_CURL_PIPED": Rule(
        "NET_CURL_PIPED", SEVERITY_HIGH,
        "curl|sh / curl|bash / wget|bash pattern (remote code execution).",
    ),
    "NET_IP_LITERAL": Rule(
        "NET_IP_LITERAL", SEVERITY_HIGH,
        "Network call to raw IP address instead of domain (evades DNS audit).",
    ),
    "NET_PASTEBIN": Rule(
        "NET_PASTEBIN", SEVERITY_HIGH,
        "Uploads to pastebin/paste.ee/0bin/etc (credential drops).",
    ),
    "NET_UNKNOWN_HOST": Rule(
        "NET_UNKNOWN_HOST", SEVERITY_HIGH,
        "Network call to non-allowlisted domain (see references/trust-database.md).",
    ),
    "OBFUSCATE_BASE64": Rule(
        "OBFUSCATE_BASE64", SEVERITY_HIGH,
        "base64 decode of long strings (>120 chars) — likely obfuscated payload.",
    ),
    "OBFUSCATE_HEX_BLOB": Rule(
        "OBFUSCATE_HEX_BLOB", SEVERITY_HIGH,
        "Long hex blob (>200 chars) — likely encoded binary or payload.",
    ),
    "OBFUSCATE_MINIFIED": Rule(
        "OBFUSCATE_MINIFIED", SEVERITY_HIGH,
        "Minified/encoded payload detected in a .md or .sh file.",
    ),
    "SHELL_TRUE": Rule(
        "SHELL_TRUE", SEVERITY_HIGH,
        "subprocess with shell=True and external input (command injection).",
    ),
    "SUPPLY_PIP_URL": Rule(
        "SUPPLY_PIP_URL", SEVERITY_HIGH,
        "pip/npm install from raw URL (not a registry) — typosquat / malware.",
    ),
    "FILE_WRITE_OUTSIDE": Rule(
        "FILE_WRITE_OUTSIDE", SEVERITY_HIGH,
        "Writes outside workspace (e.g. ~/.bashrc, /etc/, ~/Library/).",
    ),
    "PERM_CHMOD_777": Rule(
        "PERM_CHMOD_777", SEVERITY_HIGH,
        "chmod 777 — world-writable, common precursor to persistence.",
    ),

    # ── MEDIUM (10 pts) ───────────────────────────────────────────
    "NET_NO_TLS": Rule(
        "NET_NO_TLS", SEVERITY_MEDIUM,
        "http:// instead of https:// (plaintext network, MITM risk).",
    ),
    "NET_TOR": Rule(
        "NET_TOR", SEVERITY_MEDIUM,
        "References .onion or tor proxies.",
    ),
    "CRED_ENV_TOKEN": Rule(
        "CRED_ENV_TOKEN", SEVERITY_MEDIUM,
        "Reads *_TOKEN / *_API_KEY / *_SECRET env vars without declaring primaryEnv.",
    ),
    "DYN_IMPORT": Rule(
        "DYN_IMPORT", SEVERITY_MEDIUM,
        "Dynamic import (importlib.import_module) with external input.",
    ),
    "FILE_DELETE": Rule(
        "FILE_DELETE", SEVERITY_MEDIUM,
        "Deletes files outside workspace.",
    ),
    "NET_TELEMETRY": Rule(
        "NET_TELEMETRY", SEVERITY_MEDIUM,
        "Sends analytics/telemetry to third party without opt-in.",
    ),
    "SUPPLY_PKG_LIST": Rule(
        "SUPPLY_PKG_LIST", SEVERITY_MEDIUM,
        "Installs packages without explicit listing in skill metadata.",
    ),
    "PERM_BROAD_SCOPE": Rule(
        "PERM_BROAD_SCOPE", SEVERITY_MEDIUM,
        "Requests broad OAuth scopes (e.g. repo, admin:*) when narrow would do.",
    ),
    "PERM_REQUEST_KEY": Rule(
        "PERM_REQUEST_KEY", SEVERITY_MEDIUM,
        "Asks user for API key / token / password directly (vs using system keychain).",
    ),

    # ── LOW (5 pts) ────────────────────────────────────────────────
    "MISSING_FRONTMATTER": Rule(
        "MISSING_FRONTMATTER", SEVERITY_LOW,
        "SKILL.md missing required frontmatter (name/description).",
    ),
    "NO_LICENSE": Rule(
        "NO_LICENSE", SEVERITY_LOW,
        "No LICENSE file — usage rights unclear.",
    ),
    "NO_VERSION": Rule(
        "NO_VERSION", SEVERITY_LOW,
        "No version field — supply chain audit harder.",
    ),
    "HARDCODED_PATH": Rule(
        "HARDCODED_PATH", SEVERITY_LOW,
        "Hardcoded absolute paths (portability + audit issue).",
    ),
    "EVAL_NO_INPUT": Rule(
        "EVAL_NO_INPUT", SEVERITY_LOW,
        "Uses eval()/exec() but input appears static (still bad practice).",
    ),
    "SLEEP_LONG": Rule(
        "SLEEP_LONG", SEVERITY_LOW,
        "Long sleep() calls — possible timing-based evasion or C2 beacon.",
    ),
}


def score_violations(rule_ids: list[str]) -> int:
    """Compute 0-100 risk score from triggered rule IDs."""
    total = 0
    for rid in rule_ids:
        rule = RULES.get(rid)
        if rule:
            total += SEVERITY_WEIGHT[rule.severity]
    return min(total, 100)


def severity_for_score(score: int) -> str:
    """Map numeric score to severity tier label."""
    if score <= 15:
        return "🟢 LOW"
    if score <= 40:
        return "🟡 MEDIUM"
    if score <= 70:
        return "🔴 HIGH"
    return "⛔ EXTREME"


def verdict_for_score(score: int) -> str:
    """Map numeric score to install verdict."""
    if score <= 15:
        return "✅ SAFE TO INSTALL"
    if score <= 40:
        return "⚠️ INSTALL WITH CAUTION"
    if score <= 70:
        return "⚠️ HUMAN APPROVAL REQUIRED"
    return "❌ DO NOT INSTALL"
