#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skill Firewall — static security scanner for AI agent skills (SKILL.md packs).

Scans a skill directory (or any text file) for malicious patterns:
  - Prompt injection / instruction override / role hijack
  - Credential theft & data exfiltration
  - Destructive commands & persistence
  - Obfuscation (base64/hex payloads, zero-width steganography, eval chains)
  - Policy attacks (self-modification, spreading, external instruction loading)

Stdlib only. Deterministic. Safe: never executes any content found in scanned files.

Exit codes: 0=SAFE  1=CAUTION  2=SUSPICIOUS  3=MALICIOUS  4=error
"""

import argparse
import base64
import hashlib
import json
import math
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone

SCANNER_VERSION = "1.1.0"
RULESET_VERSION = "2026.11.13.2"

# ---------------------------------------------------------------------------
# Severity model
# ---------------------------------------------------------------------------
SEV_RANK = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
RANK_SEV = {v: k for k, v in SEV_RANK.items()}
SEV_WEIGHT = {4: 25, 3: 10, 2: 4, 1: 1}

VERDICT_EXIT = {"SAFE": 0, "CAUTION": 1, "SUSPICIOUS": 2, "MALICIOUS": 3}

# Context keywords that indicate the finding appears in a DEFENSIVE / documented
# context (security education, red-flag lists, examples). Downgrades severity so
# security skills and honest documentation are not falsely condemned.
DEFENSIVE_CTX = re.compile(
    r"(never|don'?t|do not|avoid|reject|refuse|forbidden|forbid|banned?|disallow"
    r"|red.?flag|malicious|attack|threat|detect|scan for|check for|prevent|guard"
    r"|must not|should not|block|deny|unsafe|danger|warning|beware"
    r"|禁止|拒绝|不得|危险|恶意)",
    re.IGNORECASE,
)
EXAMPLE_CTX = re.compile(r"(example|e\.g\.|for instance|for example|demo|sample|illustrat)", re.IGNORECASE)

# ---------------------------------------------------------------------------
# Rule catalog
# ---------------------------------------------------------------------------
# Each rule: id, name, category, severity, patterns (regex, applied per line,
# case-insensitive unless prefixed with (?-i:))
RULES = [
    # ---------- SF1xx: prompt injection / instruction hijack ----------
    dict(id="SF101", name="Instruction override", category="prompt-injection", severity="HIGH",
         desc="Attempts to override or discard the agent's original instructions",
         patterns=[
             r"ignore\s+(all\s+)?(previous|prior|above|earlier|original)\s+(instructions?|prompts?|rules?|directives?)",
             r"disregard\s+(all\s+)?(previous|prior|above|earlier|all)\s+(instructions?|prompts?|rules?)",
             r"forget\s+(all\s+)?(previous|prior|above|earlier)\s+(instructions?|prompts?|rules?)",
             r"override\s+(your|the|all|previous)\s+(instructions?|rules?|guidelines?|system)",
             r"new\s+instructions?\s*(now\s+)?(follow|replace|override|supersede)",
         ]),
    dict(id="SF102", name="Role hijack / jailbreak", category="prompt-injection", severity="HIGH",
         desc="Attempts to take over the agent's role or enter an unrestricted mode",
         patterns=[
             r"you\s+are\s+now\s+(a|an|the|in)\b",
             r"act\s+as\s+(if\s+you\s+are\s+)?(DAN|an?\s+(unrestricted|jailbroken|uncensored)|developer\s+mode|god\s+mode)",
             r"(enter|switch\s+to|enable)\s+(developer|debug|god|unrestricted|jailbreak)\s*mode",
             r"jailbreak",
             r"pretend\s+(that\s+)?(you\s+have|there\s+are)\s+no\s+(rules?|restrictions?|limits?|guidelines?)",
             r"without\s+any\s+(restrictions?|limitations?|rules?|guidelines?|ethics)",
             r"no\s+(restrictions?|limits?|rules?)\s+mode",
         ]),
    dict(id="SF103", name="Fake system/developer message", category="prompt-injection", severity="HIGH",
         desc="Injects fake system/developer message markers to smuggle instructions",
         patterns=[
             r"<\|?(system|assistant|user|im_start|im_end)\|?>",
             r"\[/?SYSTEM\]|\[/?DEVELOPER\]|\[/?ADMIN\]",
             r"(BEGIN|START)\s+(SYSTEM|DEVELOPER|ADMIN|HIDDEN)\s+(MESSAGE|INSTRUCTION|PROMPT)",
             r"(^|\W)(system\s*prompt|system\s*message|developer\s*message)\s*:",
         ]),
    dict(id="SF104", name="Secrecy / evasion instruction", category="prompt-injection", severity="HIGH",
         desc="Tells the agent to hide actions or content from the user",
         patterns=[
             r"(do\s+not|don'?t|never|without)\s+(tell|inform|mention|show|reveal|alert)\s+(the\s+)?(user|human|anyone|them)",
             r"(hide|conceal|keep)\s+(this|it|everything|the\s+following)\s+(from|secret|hidden|quiet)",
             r"(keep|stay|remain)\s+(this\s+)?(secret|silent|quiet|hidden|undetected)",
             r"(without|avoid)\s+(raising|drawing)\s+(suspicion|attention|alerts?)",
             r"(cover|hide)\s+(your|its|their)\s+(tracks?|footprint|traces?)",
         ]),
    dict(id="SF105", name="System prompt exfiltration", category="prompt-injection", severity="HIGH",
         desc="Requests extraction/replication of the agent's own prompt or rules",
         patterns=[
             r"(output|print|reveal|show|dump|repeat|expose)\s+(your|the)\s+(system\s+prompt|instructions?|hidden\s+(prompt|rules?|instructions?))",
             r"(what|repeat)\s+(is|are)\s+(your|the)\s+(system\s+prompt|initial\s+instructions?)",
             r"replicate\s+(your|the)\s+(system\s+prompt|instructions?)",
         ]),
    dict(id="SF106", name="Anti-refusal mandate", category="prompt-injection", severity="MEDIUM",
         desc="Forbids the agent from refusing any request",
         patterns=[
             r"(never|do\s+not|don'?t|you\s+(must|may)\s+not)\s+(refuse|decline|reject|deny)\b",
             r"(must|shall|will)\s+(always\s+)?(comply|obey|execute|carry\s+out)\s+(with\s+)?(all|any|every)",
             r"(answer|respond|comply)\s+(to|with)\s+(all|any|every)\s+(requests?|prompts?|commands?)\b",
         ]),

    # ---------- SF2xx: credential theft / data exfiltration ----------
    dict(id="SF201", name="Credential store access", category="data-theft", severity="HIGH",
         desc="References access to credential stores or secret files",
         patterns=[
             r"~/\.ssh/|/home/[^/\s]+/\.ssh/|/root/\.ssh/|\bid_(rsa|ed25519|ecdsa|dsa)\b",
             r"~/\.aws/credentials|\.aws/credentials|~/\.kube/config|\.kube/config",
             r"~/\.docker/config\.json|\.git-credentials|~/\.netrc|\.npmrc|\.pypirc",
             r"/etc/(shadow|passwd|sudoers)\b|/etc/ssh/sshd_config",
             r"~/\.openclaw/(credentials|identity|agents)/",
         ]),
    dict(id="SF206", name="Agent personal data reference", category="data-theft", severity="LOW",
         desc="References agent memory/personal files (critical only when combined with exfil)",
         patterns=[
             r"openclaw\.json|paired\.json",
             r"MEMORY\.md|USER\.md|SOUL\.md|IDENTITY\.md|session\s+transcripts?",
             # weak signal: env/config reads described in honest tool docs
             r"(\bread\b|\bopen\b|\bfetch\b|\bcat\b)[^\n]{0,60}\.env(?!\.(example|sample|dist|template))",
         ]),
    dict(id="SF202", name="Secret harvesting", category="data-theft", severity="HIGH",
         desc="Collects API keys, tokens, passwords or private keys",
         patterns=[
             # strong acquisition verbs + sensitive file (HIGH, whole-word verbs)
             r"(\bcat\b|\btype\b|\bdump\b|\bprint\b|\bgrab\b|\bharvest\b|\bcollect\b|\bsteal\b|\bleak\b)[^\n]{0,80}(\.env(?!\.(example|sample|dist|template))|id_(rsa|ed25519)|credentials[\s_-]?file|private[\s_-]?key[\s_-]?(file|path)|/etc/(shadow|passwd)|mnemonic|seed[\s_-]?phrase)",
             # generic verbs + secret material files (HIGH)
             r"(\bread\b|\bopen\b|\bfetch\b)[^\n]{0,80}(id_(rsa|ed25519)|private[\s_-]?key[\s_-]?(file|path)|/etc/(shadow|passwd)|mnemonic|seed[\s_-]?phrase)",
             # theft verbs + secret material WITH determiner ("leak secrets?" questions excluded)
             r"(\bgrab\b|\bharvest\b|\bcollect\b|\bsteal\b|\bexfiltrat\w*\b|\bdump\b|\bleak\b)\s+(all|every|the|their|your|user'?s|victim'?s)\s+(api[\s_-]?keys?|access[\s_-]?tokens?|passwords?|secrets?|private[\s_-]?keys?|credentials?)",
             # secrets taken FROM a person/victim (not from own config)
             r"(api[\s_-]?keys?|access[\s_-]?tokens?|passwords?|secrets?|private[\s_-]?keys?)[^\n]{0,40}(from|out\s+of)\s+(the\s+)?(user'?s?|victim'?s?|target'?s?|host'?s?|browser|credential\s+store|keystore)",
             # browser credential theft (action verb required)
             r"(\bdump\b|\bextract\b|\bharvest\b|\bsteal\b|\bsend\b|\bupload\b|\bleak\b)[^\n]{0,40}(browser|chrome|firefox)[^\n]{0,40}(cookies?|passwords?|sessions?|login\s+data)",
             r"(browser|chrome|firefox)[^\n]{0,40}(cookies?|passwords?|sessions?|login\s+data)[^\n]{0,40}(\bdump\b|\bextract\b|\bharvest\b|\bsteal\b|\bsend\b|\bupload\b|\bleak\b)",
         ]),
    dict(id="SF203", name="Environment credential dumping", category="data-theft", severity="MEDIUM",
         desc="Dumps process environment variables (common credential source)",
         patterns=[
             r"\bprintenv\b|\benv\s*\|\s*(grep|awk|sed|sort)|\bset\s*>\s*\S+",
             r"export\s+[A-Z_]*(TOKEN|SECRET|PASSW|APIKEY|API_KEY)",
             r"Get-ChildItem\s+(:?\s*)?env:|gci\s+env:",
         ]),
    dict(id="SF204", name="Data exfiltration over network", category="data-theft", severity="CRITICAL",
         desc="Sends local data/files to an external endpoint",
         patterns=[
             # tool + sensitive object + data-sending mechanics on one line
             r"(\bcurl\b|\bwget\b|requests?\.(get|post)|fetch\()[^\n]{0,120}(\.ssh|id_rsa|\.env\b|credentials[\s_-]?file|\.netrc|MEMORY\.md|USER\.md|SOUL\.md|paired\.json)[^\n]{0,120}(-d |--data|--data-binary|-F |--form|-T |--upload-file|@/|@~|upload|exfiltrat|webhook)",
             # path-like secret + send mechanics (generic words excluded — docs mention tokens+URLs)
             r"(\.ssh|id_rsa|\.env\b|credentials[\s_-]?file|\.netrc|MEMORY\.md|USER\.md|SOUL\.md|paired\.json)[^\n]{0,120}(\bcurl\b|\bwget\b|upload|exfiltrat|webhook|telegram|discord|pastebin|\bsend\b|--data)",
             r"(\bcurl\b|\bwget\b)[^\n]{0,120}(-d |--data|--data-binary|-F |--form|-T |--upload-file|@/|@~)",
             r"(\bupload\b|\bexfiltrat\w*\b|\btransmit\b|\bforward\b)\s+(all\s+)?(the\s+)?(files?|data|credentials?|secrets?|keys?|contents?|memory|history)[^\n]{0,60}(to|via|over)\s+\S*(http|server|endpoint|webhook|url|host)",
         ]),
    dict(id="SF205", name="Exfil channel / dead-drop service", category="data-theft", severity="HIGH",
         desc="Uses known data-exfiltration or dead-drop services",
         patterns=[
             r"webhook\.site|requestbin|interactsh|oast\.(fun|ify|pro|live|online)|ngrok\.(io|app)|trycloudflare\.com",
             r"api\.telegram\.org/bot[^\n]{0,60}sendMessage",
             r"discord(app)?\.com/api/webhooks/|hooks\.slack\.com/services/",
             r"pastebin\.com/api|paste\.ee|dpaste\.com|transfer\.sh|file\.io",
         ]),

    # ---------- SF3xx: destructive / persistence / privilege ----------
    dict(id="SF301", name="Destructive command", category="sabotage", severity="CRITICAL",
         desc="Destroys data, filesystems or block devices",
         patterns=[
             r"rm\s+(-[a-zA-Z]*r[a-zA-Z]*|--recursive)\s+([^\s]+\s+){0,2}(/|~|\$HOME)",
             r"--no-preserve-root",
             r"\bmkfs(\.\w+)?\b|\bwipefs\b|\bfdisk\b[^\n]{0,20}/dev/",
             r"\bdd\s+[^\n]{0,60}of=/dev/(sd|nvme|hd|vd|xvd)",
             r"\bshred\s+[^\n]{0,40}(-u|--remove)",
             r">\s*/dev/(sd|nvme|hd)",
         ]),
    dict(id="SF302", name="Authentication tampering", category="sabotage", severity="CRITICAL",
         desc="Modifies SSH keys, accounts, sudoers or auth configuration",
         patterns=[
             r"(cat|echo|curl|wget|tee|>>?)[^\n]{0,80}(authorized_keys|sshd_config)",
             r"(useradd|adduser|usermod|passwd|chpasswd|visudo)\b",
             r"(chmod|chown)\s+[^\n]{0,40}(\.ssh|authorized_keys|/etc/shadow|/etc/passwd|sudoers)",
             r"chmod\s+777\b",
         ]),
    dict(id="SF303", name="Persistence mechanism", category="persistence", severity="HIGH",
         desc="Installs persistence via cron, services or shell profiles",
         patterns=[
             r"crontab\s+(-e|-l\s*>\s*|.*<<<|.*>>?\s*/etc/cron)|@reboot\s+",
             r"systemctl\s+(enable|start|daemon-reload)",
             r"(echo|cat|tee|>>?)[^\n]{0,60}(\.bashrc|\.zshrc|\.profile|\.bash_profile)",
             r"(schtasks|reg\s+add|HKEY_|HKLM\\\\|launchctl|plist)",
             r"(systemd|init\.d|upstart|cron\.d)[^\n]{0,40}(write|create|install|add)",
         ]),
    dict(id="SF304", name="Privilege escalation intent", category="privilege", severity="HIGH",
         desc="Attempts to elevate privileges or disable security tooling",
         patterns=[
             r"\bsudo\s+(su\b|-i\b|-s\b|bash|sh\b|chmod|chown|tee|passwd|usermod|visudo|systemctl)",
             r"chmod\s+\+s\b|setuid|setgid\s+4755",
             r"(disable|stop|kill|uninstall)[^\n]{0,40}(firewall|selinux|apparmor|antivirus|defender|auditd|guardd|security\s+agent)",
         ]),
    dict(id="SF305", name="Shell/backdoor & network attack", category="attack", severity="CRITICAL",
         desc="Reverse shells, bind shells, fork bombs or scanning/attack tooling",
         patterns=[
             r"bash\s+-i\s+>&\s*/dev/tcp/|/dev/tcp/\d+\.\d+\.\d+\.\d+/",
             r"\bnc\b[^\n]{0,40}\s-e\s+(bash|sh|/bin/)|ncat\s+[^\n]{0,60}--exec|socat\s+[^\n]{0,60}exec:",
             r"mkfifo[^\n]{0,60}\bnc\b|powershell[^\n]{0,60}-enc(odedcommand)?\s+[A-Za-z0-9+/=]{20,}",
             r":\(\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;\s*:",
             r"\b(nmap|masscan|sqlmap|hydra|metasploit|msfconsole|msfvenom|cobalt\s*strike|john\s+--|hashcat)\b",
             r"(port\s+scan|brute[\s-]?force|exploit\s+(the\s+)?vulnerabilit|reverse[\s-]?shell|payload\s+delivery)",
         ]),

    # ---------- SF4xx: obfuscation / stealth ----------
    dict(id="SF401", name="Encoded payload execution", category="obfuscation", severity="HIGH",
         desc="Decodes obfuscated data and executes/uses it at runtime",
         patterns=[
             r"(exec|eval|system|popen|spawn|run\(|iex|Invoke-Expression|Invoke-Cmd)[^\n]{0,80}(b64decode|base64(\.b64)?decode|atob|fromCharCode|decode\s*\()",
             r"(b64decode|base64(\.b64)?decode|atob|fromCharCode)[^\n]{0,80}(exec|eval|system|popen|spawn|run\(|iex|Invoke-Expression)",
             r"\bbase64\s+(-d\b|--decode)",
         ]),
    dict(id="SF402", name="Hex/charcode obfuscation", category="obfuscation", severity="HIGH",
         desc="Builds strings from hex escapes or char codes to hide intent",
         patterns=[
             r"(?:\\x[0-9a-fA-F]{2}){8,}",
             r"(?:\\u[0-9a-fA-F]{4}){8,}",
             r"String\.fromCharCode\s*\(",
             r"chr\s*\(\s*\d{1,3}\s*\)(\s*\+\s*chr\s*\(\s*\d{1,3}\s*\)){4,}",
             r"\bexec\s*\(\s*['\"]?(\\x|\\u)",
         ]),
    dict(id="SF403", name="Dynamic code execution", category="obfuscation", severity="MEDIUM",
         desc="Evaluates dynamically constructed code strings",
         patterns=[
             r"(?<![.\w])(eval|exec)\s*\(\s*(input\(|request\.|fetch\(|\w+\s*\+|f['\"]|['\"].*%|['\"].*\.format)",
             r"(?<![.\w])(eval|exec)\s*\(\s*(base64|bytes|bytearray|decode)",
             r"compile\s*\([^\n]{0,40}(exec|eval)",
             r"\bInvoke-Expression\b|\biex\b\s+\$",
         ]),
    dict(id="SF404", name="Zero-width steganography", category="obfuscation", severity="MEDIUM",
         desc="Hides content using zero-width/invisible Unicode characters",
         patterns=[]),  # handled by dedicated analyzer
    dict(id="SF405", name="Hidden instruction channel", category="obfuscation", severity="HIGH",
         desc="Conceals instructions in comments, invisible or non-rendered markup",
         patterns=[]),  # handled by dedicated analyzer
    dict(id="SF406", name="High-entropy opaque blob", category="obfuscation", severity="LOW",
         desc="Large high-entropy blob that cannot be decoded as text (packed payload?)",
         patterns=[]),  # handled by dedicated analyzer

    # ---------- SF5xx: policy attacks ----------
    dict(id="SF501", name="External instruction loading", category="policy-attack", severity="HIGH",
         desc="Tells the agent to follow instructions fetched from an external source",
         patterns=[
             r"(follow|obey|execute|apply)\s+(the\s+|these\s+)?(hidden\s+|external\s+|remote\s+)?instructions?[^\n]{0,60}(from|at|in|on)\s+(the\s+)?(url|http|link|website|page|pastebin|gist|repo)",
             r"(read|fetch|load|download|retrieve)\s+(\w+\s+){0,3}(instructions?|prompts?|rules?|directives?)\s+(from|at|in|via)\s+https?://",
             r"https?://[^\s)]+[^\n]{0,60}(instructions?\s+(to\s+)?(follow|execute)|payload\s+to\s+run)",
         ]),
    dict(id="SF502", name="Self-modification / safety disable", category="policy-attack", severity="CRITICAL",
         desc="Instructs the agent to rewrite its own rules or disable safeguards",
         patterns=[
             r"(modify|edit|overwrite|rewrite|update|replace|delete)[^\n]{0,60}(your|the|its)\s+(system\s+prompt|safety\s+(rules?|guidelines?|protocols?)|guardrails?|filters?|SOUL\.md|AGENTS\.md|TOOLS\.md|MEMORY\.md|instructions?)",
             r"(disable|turn\s+off|remove|bypass|neutraliz|circumvent)[^\n]{0,60}(your|the|its|all)\s+(safety|guardrails?|filters?|restrictions?|oversight|security\s+(rules?|checks?))",
             r"(add|write|append)[^\n]{0,60}(new\s+)?(rules?|instructions?|permissions?)[^\n]{0,40}(to\s+)?(your|the)\s+(AGENTS\.md|SOUL\.md|system\s+prompt|config|memory)",
         ]),
    dict(id="SF503", name="Self-replication / spreading", category="policy-attack", severity="CRITICAL",
         desc="Attempts to copy or propagate itself to other agents or sessions",
         patterns=[
             r"(copy|replicate|clone|propagate|spread|install)\s+(yourself|this\s+(skill|file|prompt|code))[^\n]{0,60}(to|into|across|every|all)",
             r"(send|forward|share|post)\s+(this|the)\s+(skill|file|prompt|instructions?|message)[^\n]{0,60}(to\s+)?(every|all|each|other)",
             r"(recruit|enlist|spawn)\s+(other\s+)?(agents?|sessions?|bots?)[^\n]{0,40}(to\s+)?(run|execute|help)",
         ]),
    # ---------- SF4xx extension: remote content ----------
    dict(id="SF408", name="Remote content beacon", category="obfuscation", severity="MEDIUM",
         desc="Loads remote tracking content (beacon/pixel) with session-like parameters",
         patterns=[
             r"!\[[^\]]*\]\(\s*https?://[^)\s]*(\?|&)[^)\s]*(token|key|session|sid|track|pixel|auth|secret)",
             r"<img[^>]+src=[\"']https?://[\"']*(\?|&)[^\"']*(token|key|session|sid|track|pixel|auth|secret)",
             r"!\[[^\]]*\]\(\s*https?://\d{1,3}(\.\d{1,3}){3}",
         ]),
    # ---------- SF6xx: supply chain & CI ----------
    dict(id="SF601", name="Pipe-to-shell install", category="supply-chain", severity="MEDIUM",
         desc="Pipes remote content directly into a shell/interpreter (opaque install step)",
         patterns=[
             r"(\bcurl\b|\bwget\b)[^\n|]{0,120}\|\s*(sudo\s+)?(ba|z|da)?sh\b",
             r"(\bcurl\b|\bwget\b)[^\n|]{0,120}\|\s*(sudo\s+)?python3?\b",
             r"(\bcurl\b|\bwget\b)[^\n|]{0,120}\|\s*(sudo\s+)?node\b",
         ]),
    dict(id="SF602", name="Package lifecycle hook payload", category="supply-chain", severity="HIGH",
         desc="Package lifecycle hook executes suspicious commands at install time",
         patterns=[
             r"\"(preinstall|postinstall|prepare|preuninstall|postuninstall)\"\s*:\s*\"[^\"]*(curl|wget|chmod|bash|sh -c|/dev/tcp|base64|\.env|id_rsa|\bnc\b)",
         ]),
    dict(id="SF603", name="CI workflow injection pattern", category="supply-chain", severity="HIGH",
         desc="Workflow exposes privileged context to untrusted code (pull_request_target, untrusted interpolation)",
         patterns=[
             r"pull_request_target",
             r"\$\{\{\s*github\.event\.(pull_request\.(title|body|head)|issue\.(title|body))",
         ]),
]

# Rules sensitive to evasion splits — also checked across adjacent line pairs
MULTILINE_RULES = {"SF101", "SF204", "SF501", "SF502", "SF503", "SF602"}

# Regexes compiled per rule
for _r in RULES:
    _r["_regex"] = [re.compile(p, re.IGNORECASE) for p in _r["patterns"]]

ZERO_WIDTH = re.compile(r"[\u200b\u200c\u200d\u2060\ufeff\u202a-\u202e\u2066-\u2069]")
HTML_COMMENT = re.compile(r"<!--(.*?)-->", re.DOTALL)
HIDDEN_INSTR = re.compile(
    r"(ignore|instructions?|system|execute|run\s+this|prompt|download|curl|exec)", re.IGNORECASE)
B64_TOKEN = re.compile(r"(?<![A-Za-z0-9+/=])[A-Za-z0-9+/]{32,}={0,2}(?![A-Za-z0-9+/=])")

# Dependency manifests / lockfiles / minified assets carry legitimate high-entropy
# hash strings (npm integrity, checksums). SF406 entropy heuristic is suppressed there.
HEX_ONLY = re.compile(r"^[0-9a-fA-F]+$")
NOISE_FILES = re.compile(
    r"(package-lock\.json|yarn\.lock|pnpm-lock\.yaml|poetry\.lock|Pipfile\.lock|Cargo\.lock"
    r"|go\.sum|composer\.lock|Gemfile\.lock|\.min\.(js|css)|\.map)$", re.IGNORECASE)

SCAN_EXTENSIONS = {
    ".md", ".txt", ".py", ".sh", ".bash", ".zsh", ".js", ".mjs", ".cjs", ".ts",
    ".json", ".yaml", ".yml", ".toml", ".xml", ".html", ".css", ".ps1", ".rb",
    ".go", ".java", ".php", ".lua", ".pl", ".r", ".cfg", ".ini", ".env",
}
SCAN_BASENAMES = {"SKILL.md", "AGENTS.md", "TOOLS.md", "SOUL.md", "Makefile", "Dockerfile"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".tox", ".mypy_cache"}
MAX_FILE_BYTES = 1_000_000
MAX_FILES = 500


@dataclass
class Finding:
    rule_id: str
    rule_name: str
    category: str
    severity: str
    file: str
    line: int
    excerpt: str
    note: str = ""
    context_downgraded: bool = False
    evidence: str = ""
    # internal fields for context analysis (excluded from JSON output)
    _raw_rank: int = 0
    _line_defensive: bool = False
    _line_example: bool = False
    _structural: bool = False


@dataclass
class ScanResult:
    target: str
    scanned_at: str
    scanner_version: str
    files_scanned: int
    findings: list = field(default_factory=list)
    score: int = 0
    verdict: str = "SAFE"
    counts: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in freq.values())


def try_b64decode(token: str):
    """Return decoded str if token decodes to plausible printable text, else None."""
    for decoder in (base64.b64decode,):
        for pad in ("", "=", "==", "==="):
            try:
                raw = decoder(token + pad, validate=False)
            except Exception:
                continue
            if len(raw) < 8:
                return None
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                return None
            printable = sum(1 for ch in text if ch.isprintable() or ch in "\r\n\t")
            if printable / len(text) > 0.9 and sum(ch.isalpha() for ch in text) >= 4:
                return text
    return None


# Unicode confusable folding (homoglyph evasion): Cyrillic/Greek lookalikes and
# fullwidth forms are folded to ASCII before rule matching. NFKC + manual map.
import unicodedata

_CONFUSABLES = {
    "\u0430": "a", "\u0435": "e", "\u043e": "o", "\u0440": "p", "\u0441": "c",
    "\u0443": "y", "\u0445": "x", "\u0456": "i", "\u0455": "s", "\u04cf": "l",
    "\u0501": "d", "\u051b": "q", "\u0578": "o", "\u057a": "u", "\u05df": "l",
    "\u0410": "A", "\u0412": "B", "\u0415": "E", "\u041a": "K", "\u041c": "M",
    "\u041d": "H", "\u041e": "O", "\u0420": "P", "\u0421": "C", "\u0422": "T",
    "\u0425": "X", "\u0391": "A", "\u0392": "B", "\u0395": "E", "\u0396": "Z",
    "\u0397": "H", "\u0399": "I", "\u039a": "K", "\u039c": "M", "\u039d": "N",
    "\u039f": "O", "\u03a1": "P", "\u03a4": "T", "\u03a5": "Y", "\u03a7": "X",
    "\u03bf": "o", "\u03b1": "a", "\u03b5": "e", "\u03b9": "i", "\u03ba": "k",
    "\u03c1": "p", "\u03c4": "t", "\u03c5": "u", "\u03c7": "x",
}


def fold_confusables(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    return "".join(_CONFUSABLES.get(ch, ch) for ch in s)


def decode_hex_escapes(line: str) -> str:
    """Decode runs of \\xNN escapes if present."""
    def _repl(m):
        try:
            return bytes.fromhex(m.group(0).replace("\\x", "")).decode("latin-1")
        except Exception:
            return m.group(0)
    return re.sub(r"(?:\\x[0-9a-fA-F]{2}){2,}", _repl, line)


# Attack phrasing that superficially contains defensive words ("do not tell the
# user", "never refuse") — checked FIRST so it never receives a downgrade.
OFFENSIVE_CTX = re.compile(
    r"(do\s+not|don'?t|never)\s+(tell|inform|mention|show|reveal|alert|refuse|decline)"
    r"|keep\s+(this|it|everything|the\s+following)\s+(secret|silent|quiet|hidden)"
    r"|(hide|conceal)\s+(this|it|your|the)\b",
    re.IGNORECASE)


def context_downgrade(line: str, rank: int):
    """Return (new_rank, kind) where kind in {none, example, defensive}."""
    if OFFENSIVE_CTX.search(line):
        return rank, "none"  # attack phrasing — full severity
    if DEFENSIVE_CTX.search(line):
        return max(1, rank - 2), "defensive"
    if EXAMPLE_CTX.search(line):
        return max(1, rank - 1), "example"
    return rank, "none"


def iter_text_files(target: str):
    if os.path.isfile(target):
        yield target
        return
    count = 0
    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            path = os.path.join(root, name)
            ext = os.path.splitext(name)[1].lower()
            if ext not in SCAN_EXTENSIONS and name not in SCAN_BASENAMES:
                continue
            try:
                if os.path.getsize(path) > MAX_FILE_BYTES:
                    continue
            except OSError:
                continue
            yield path
            count += 1
            if count >= MAX_FILES:
                return


def read_text(path: str) -> str:
    with open(path, "rb") as fh:
        raw = fh.read()
    if b"\x00" in raw[:8192]:
        return None  # binary — caller skips
    return raw.decode("utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Core scanning
# ---------------------------------------------------------------------------
SECURITY_DOC_NAME = re.compile(
    r"(security|threat|red.?flag|malicious|attack|vetting|hardening|injection|pentest|toxic"
    r"|firewall|scanner|defend|detector|antivirus|sanitiz|guard)", re.IGNORECASE)


def finalize_file_findings(findings: list, relpath: str):
    """
    File-level context gate (anti-false-positive + anti-disguise):

    Downgrades apply ONLY when the file itself reads as defensive/educational
    (security documentation by name, or >= 50% of finding lines carry defensive
    context). A malicious file that sprinkles 'Example:' or 'never' onto a few
    lines keeps full severity, so the disguise trick fails.
    """
    flagged = [f for f in findings if not f._structural]
    if not flagged:
        return
    basename = os.path.basename(relpath)
    # Security-doc NAMES only grant a soft downgrade, and only for prose docs —
    # an attacker naming a workflow/script "injection.yml" gets no cover.
    is_prose = basename.lower().endswith((".md", ".txt"))
    security_doc = is_prose and bool(SECURITY_DOC_NAME.search(basename))
    defensive_lines = sum(1 for f in flagged if f._line_defensive)
    ratio = defensive_lines / len(flagged)
    defensive_doc = security_doc or ratio >= 0.5
    for f in flagged:
        if defensive_doc and f._line_defensive:
            f._raw_rank = max(1, f._raw_rank - 2)
            f.context_downgraded = True
        elif defensive_doc and security_doc and not f._line_defensive and not f._line_example:
            f._raw_rank = max(1, f._raw_rank - 1)  # name-based soft cover
            f.context_downgraded = True
        elif defensive_doc and f._line_example:
            f._raw_rank = max(1, f._raw_rank - 1)
            f.context_downgraded = True
        # else: full severity — sprinkled context words do not help
        f.severity = RANK_SEV[f._raw_rank]
        if not defensive_doc and (f._line_defensive or f._line_example):
            f.note += " [context words present but file is not defensive-doc: no downgrade]"


def scan_text(text: str, relpath: str, findings: list):
    lines = text.splitlines()

    # 1) Line-based rule matching (on confusable-folded text; excerpt from raw line)
    homoglyph_lines = set()
    for idx, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        folded = fold_confusables(line)
        changed = folded != line
        for rule in RULES:
            for rx in rule["_regex"]:
                m = rx.search(folded)
                if not m:
                    continue
                rank = SEV_RANK[rule["severity"]]
                new_rank, ctx = context_downgrade(folded, rank)
                note = rule["desc"]
                if changed and not rx.search(line):
                    note += " [matched after Unicode confusable folding — homoglyph evasion]"
                    homoglyph_lines.add(idx)
                f = Finding(
                    rule_id=rule["id"], rule_name=rule["name"], category=rule["category"],
                    severity=rule["severity"], file=relpath, line=idx,
                    excerpt=line.strip()[:240], note=note,
                    evidence=m.group(0)[:120],
                    _raw_rank=rank,
                    _line_defensive=(ctx == "defensive"),
                    _line_example=(ctx == "example"),
                )
                findings.append(f)
                break  # one hit per rule per line is enough

    # 1b) Homoglyph evasion marker (once per line where folding enabled a match)
    for idx in sorted(homoglyph_lines):
        findings.append(Finding(
            rule_id="SF407", rule_name="Unicode confusable/homoglyph evasion",
            category="obfuscation", severity="HIGH", file=relpath, line=idx,
            excerpt=lines[idx - 1].strip()[:240],
            note="Attack strings disguised with Cyrillic/Greek lookalike characters",
            _raw_rank=3, _structural=True,
        ))

    # 2) Hex-escape decoded content (SF402 payload reveal)
    for idx, line in enumerate(lines, start=1):
        decoded = decode_hex_escapes(line)
        if decoded != line and len(decoded) >= 8:
            _scan_decoded(decoded, relpath, idx, "hex-escape-decoded", findings)

    # 3) Base64 blob analysis (entropy heuristic suppressed in lockfiles/manifests)
    noise_file = bool(NOISE_FILES.search(relpath))
    for idx, line in enumerate(lines, start=1):
        for tok in B64_TOKEN.findall(line):
            decoded = try_b64decode(tok)
            depth = 0
            while decoded is not None and depth < 3:
                inner = decoded.strip()
                if len(inner) >= 32 and re.fullmatch(r"[A-Za-z0-9+/=]+", inner):
                    nxt = try_b64decode(inner)
                    if nxt is not None:
                        decoded = nxt
                        depth += 1
                        continue
                break
            if decoded is not None:
                origin = "base64-decoded" if depth == 0 else "base64-decoded x%d (multi-layer)" % (depth + 1)
                _scan_decoded(decoded, relpath, idx, origin, findings)
            elif (not noise_file and not HEX_ONLY.match(tok)
                  and shannon_entropy(tok) > 4.5 and len(tok) >= 64):
                findings.append(Finding(
                    rule_id="SF406", rule_name="High-entropy opaque blob",
                    category="obfuscation", severity="LOW", file=relpath, line=idx,
                    excerpt=tok[:80] + ("…" if len(tok) > 80 else ""),
                    note="Entropy %.2f bits/char; opaque payload" % shannon_entropy(tok),
                    _raw_rank=1, _structural=True,
                ))

    # 4) Zero-width steganography (file-level)
    zw = ZERO_WIDTH.findall(text)
    if len(zw) >= 3:
        findings.append(Finding(
            rule_id="SF404", rule_name="Zero-width steganography",
            category="obfuscation", severity="MEDIUM", file=relpath, line=0,
            excerpt="%d zero-width/invisible Unicode chars found" % len(zw),
            note="Content may be hidden from human review",
            _raw_rank=2, _structural=True,
        ))

    # 5) Hidden instructions in HTML comments (file-level)
    for m in HTML_COMMENT.finditer(text):
        body = m.group(1)
        if HIDDEN_INSTR.search(body):
            line_no = text[:m.start()].count("\n") + 1
            findings.append(Finding(
                rule_id="SF405", rule_name="Hidden instruction channel",
                category="obfuscation", severity="HIGH", file=relpath, line=line_no,
                excerpt=body.strip()[:200],
                note="Instruction-like text concealed in non-rendered markup",
                _raw_rank=3, _structural=True,
            ))

    # 6) Split-evasion combo pass across adjacent lines
    _scan_multiline(lines, relpath, findings)


def _scan_multiline(lines, relpath: str, findings: list):
    """Combo-sensitive rules also run across adjacent line pairs to catch
    split-evasion (attack sentence broken over several short lines)."""
    seen = {(f.rule_id, f.line) for f in findings}
    combo_rules = [r for r in RULES if r["id"] in MULTILINE_RULES]
    for i in range(len(lines) - 1):
        joined = fold_confusables(lines[i] + " " + lines[i + 1])
        if not joined.strip():
            continue
        for rule in combo_rules:
            if (rule["id"], i + 1) in seen or (rule["id"], i + 2) in seen:
                continue
            for rx in rule["_regex"]:
                m = rx.search(joined)
                if not m:
                    continue
                rank = SEV_RANK[rule["severity"]]
                _, ctx = context_downgrade(joined, rank)
                findings.append(Finding(
                    rule_id=rule["id"], rule_name=rule["name"], category=rule["category"],
                    severity=rule["severity"], file=relpath, line=i + 1,
                    excerpt=(lines[i].strip() + " ⏎ " + lines[i + 1].strip())[:240],
                    note=rule["desc"] + " [split across adjacent lines]",
                    evidence=m.group(0)[:120],
                    _raw_rank=rank,
                    _line_defensive=(ctx == "defensive"),
                    _line_example=(ctx == "example"),
                ))
                seen.add((rule["id"], i + 1))
                break


def _scan_decoded(decoded: str, relpath: str, line_no: int, origin: str, findings: list):
    """Run the rule catalog against decoded payload content."""
    hit_rules = set()
    for dl in decoded.splitlines():
        for rule in RULES:
            if rule["id"] in hit_rules:
                continue
            for rx in rule["_regex"]:
                if rx.search(dl):
                    hit_rules.add(rule["id"])
                    # Encoded payloads bypass human review on purpose: no downgrade.
                    findings.append(Finding(
                        rule_id=rule["id"], rule_name=rule["name"], category=rule["category"],
                        severity=rule["severity"], file=relpath, line=line_no,
                        excerpt=(dl.strip() or decoded.strip())[:240],
                        note="%s → hidden content matches: %s" % (origin, rule["desc"]),
                        evidence="decoded-payload",
                        _raw_rank=SEV_RANK[rule["severity"]], _structural=True,
                    ))
                    break
    if not hit_rules and origin == "base64-decoded":
        # Decoded benign content is fine — no finding. Intentional.
        pass


# ---------------------------------------------------------------------------
# Verdict
# ---------------------------------------------------------------------------
def compute_verdict(findings):
    """
    Verdict driven by NON-contextual findings ('real' signals). Findings that
    were downgraded inside defensive/educational documents cap the verdict at
    CAUTION unless their combined mass is extreme (ctx_score >= 30).
    """
    real = [f for f in findings if not f.context_downgraded]
    ctx = [f for f in findings if f.context_downgraded]
    real_score = sum(SEV_WEIGHT[SEV_RANK[f.severity]] for f in real)
    ctx_score = sum(SEV_WEIGHT[SEV_RANK[f.severity]] for f in ctx)
    score = real_score + ctx_score
    real_critical = [f for f in real if f.severity == "CRITICAL"]
    real_high = [f for f in real if f.severity == "HIGH"]
    meaningful = [f for f in real if SEV_RANK[f.severity] >= 2]  # >= MEDIUM
    if real_critical or ctx_score >= 30 or (real_score >= 30 and meaningful):
        verdict = "MALICIOUS"
    elif real_high or (real_score >= 12 and meaningful):
        verdict = "SUSPICIOUS"
    elif findings:
        verdict = "CAUTION"
    else:
        verdict = "SAFE"
    return score, verdict


def _scan_one_file(args):
    path, rel = args
    text = read_text(path)
    if text is None:
        return rel, None  # binary content
    local = []
    scan_text(text, rel, local)
    finalize_file_findings(local, rel)
    return rel, local


def scan_path(target: str) -> ScanResult:
    from concurrent.futures import ThreadPoolExecutor
    jobs = []
    for path in iter_text_files(target):
        rel = os.path.relpath(path, target) if os.path.isdir(target) else os.path.basename(path)
        jobs.append((path, rel))
    findings = []
    files = 0
    if jobs:
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(_scan_one_file, jobs))
        for rel, local in sorted(results, key=lambda x: x[0]):
            if local is not None:
                files += 1
                findings.extend(local)
    findings.sort(key=lambda f: (f.file, f.line, f.rule_id))
    score, verdict = compute_verdict(findings)
    counts = {sev: 0 for sev in SEV_RANK}
    cats = {}
    for f in findings:
        counts[f.severity] += 1
        cats[f.category] = cats.get(f.category, 0) + 1
    return ScanResult(
        target=os.path.abspath(target),
        scanned_at=datetime.now(timezone.utc).isoformat(),
        scanner_version=SCANNER_VERSION,
        files_scanned=files,
        findings=findings,
        score=score,
        verdict=verdict,
        counts={"by_severity": counts, "by_category": cats, "total": len(findings)},
    )


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def render_text(result: ScanResult) -> str:
    out = []
    out.append("=" * 72)
    out.append(" SKILL FIREWALL v%s — static security scan" % SCANNER_VERSION)
    out.append("=" * 72)
    out.append("Target : %s" % result.target)
    out.append("Scanned: %s (UTC)" % result.scanned_at)
    out.append("Files  : %d" % result.files_scanned)
    sev = result.counts["by_severity"]
    out.append("Findings: %d  (CRITICAL:%d  HIGH:%d  MEDIUM:%d  LOW:%d)" % (
        result.counts["total"], sev["CRITICAL"], sev["HIGH"], sev["MEDIUM"], sev["LOW"]))
    out.append("")
    icon = {"SAFE": "✅", "CAUTION": "⚠️", "SUSPICIOUS": "🔶", "MALICIOUS": "🚨"}
    out.append("VERDICT: %s %s   (risk score %d/100)" % (icon[result.verdict], result.verdict, result.score))
    out.append("")
    if result.findings:
        out.append("-" * 72)
        for f in sorted(result.findings, key=lambda x: (-SEV_RANK[x.severity], x.file, x.line)):
            loc = "%s:%s" % (f.file, f.line) if f.line else f.file
            flag = "  [contextual]" if f.context_downgraded else ""
            out.append("[%s] %s %s (%s)%s" % (f.severity, f.rule_id, loc, f.category, flag))
            out.append("    %s — %s" % (f.rule_name, f.note))
            if f.evidence:
                out.append("    evidence: %r" % f.evidence)
            out.append("    > %s" % f.excerpt)
            out.append("")
    else:
        out.append("No findings. ✅")
    out.append("-" * 72)
    if result.counts.get("suppressed_by_baseline"):
        out.append("Suppressed by baseline: %d findings (fingerprints matched)" % result.counts["suppressed_by_baseline"])
    out.append("Verdict scale: SAFE < CAUTION < SUSPICIOUS < MALICIOUS")
    out.append("Exit code: %d" % VERDICT_EXIT[result.verdict])
    return "\n".join(out)


def fingerprint(f: Finding) -> str:
    """Stable suppression fingerprint: rule + file + matched evidence (line-independent)."""
    import hashlib
    key = "%s|%s|%s" % (f.rule_id, os.path.basename(f.file), (f.evidence or f.excerpt).strip().lower())
    return hashlib.sha1(key.encode("utf-8", errors="replace")).hexdigest()[:16]


def render_sarif(result: ScanResult) -> str:
    """SARIF 2.1.0 — integrates with GitHub code scanning and other platforms."""
    level_map = {"CRITICAL": "error", "HIGH": "error", "MEDIUM": "warning", "LOW": "note"}
    rules_seen = {}
    sarif_results = []
    for f in result.findings:
        if f.rule_id not in rules_seen:
            rules_seen[f.rule_id] = {
                "id": f.rule_id,
                "name": f.rule_name.replace(" ", ""),
                "shortDescription": {"text": f.rule_name},
                "fullDescription": {"text": f.note or f.rule_name},
                "defaultConfiguration": {"level": level_map.get(f.severity, "warning")},
                "properties": {"category": f.category},
            }
        sarif_results.append({
            "ruleId": f.rule_id,
            "level": level_map.get(f.severity, "warning"),
            "message": {"text": "[%s] %s — %s | evidence: %s" % (f.severity, f.rule_name, f.note, f.evidence or "-")},
            "locations": [{
                "physicalLocation": {
                    "artifactLocation": {"uri": f.file.replace(os.sep, "/")},
                    "region": {"startLine": max(f.line, 1)},
                }
            }],
            "properties": {"fingerprint": fingerprint(f)},
        })
    payload = {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {
                "name": "Skill Firewall",
                "version": SCANNER_VERSION,
                "informationUri": "https://github.com/openclaw/clawhub",
                "rules": list(rules_seen.values()),
            }},
            "results": sarif_results,
            "properties": {
                "verdict": result.verdict,
                "riskScore": result.score,
                "filesScanned": result.files_scanned,
                "scannedAt": result.scanned_at,
            },
        }],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


def to_json(result: ScanResult) -> str:
    payload = asdict(result)
    for f in payload["findings"]:
        for k in list(f):
            if k.startswith("_"):
                del f[k]
    return json.dumps(payload, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="skill_firewall",
        description="Static security scanner for AI agent skills (SKILL.md packs).")
    ap.add_argument("target", nargs="?", help="Skill directory or text file to scan")
    ap.add_argument("--json", action="store_true", help="JSON output")
    ap.add_argument("--sarif", action="store_true", help="SARIF 2.1.0 output (GitHub code scanning compatible)")
    ap.add_argument("--baseline", metavar="FILE",
                    help="Suppress findings fingerprinted in a previously written baseline file")
    ap.add_argument("--write-baseline", metavar="FILE",
                    help="Write current findings as a suppression baseline and exit 0")
    ap.add_argument("--version", action="store_true", help="Print scanner version and exit")
    ap.add_argument("--quiet", action="store_true", help="Only print the verdict line")
    ap.add_argument("--fail-on", default="caution",
                    choices=["caution", "suspicious", "malicious", "never"],
                    help="Minimum verdict that exits non-zero (default: caution — "
                         "exit code equals the verdict: 0 SAFE, 1 CAUTION, 2 SUSPICIOUS, 3 MALICIOUS; "
                         "'never' always exits 0)")
    args = ap.parse_args(argv)

    if args.version:
        print("skill_firewall %s (ruleset v%s, %d rules)" % (
            SCANNER_VERSION, RULESET_VERSION, len(RULES)))
        return 0
    if not args.target:
        ap.error("target is required (unless --version)")

    if not os.path.exists(args.target):
        print("error: target not found: %s" % args.target, file=sys.stderr)
        return 4

    result = scan_path(args.target)

    # Baseline workflow: fingerprint-suppress acknowledged findings (enterprise triage)
    suppressed = 0
    if args.write_baseline:
        fps = sorted({fingerprint(f) for f in result.findings})
        with open(args.write_baseline, "w", encoding="utf-8") as fh:
            json.dump({"tool": "skill-firewall", "version": SCANNER_VERSION,
                       "target": result.target, "created": result.scanned_at,
                       "fingerprints": fps}, fh, indent=2)
        print("baseline written: %s (%d fingerprints) — review before suppressing!"
              % (args.write_baseline, len(fps)))
        return 0
    if args.baseline and os.path.exists(args.baseline):
        with open(args.baseline, "r", encoding="utf-8") as fh:
            base = json.load(fh)
        allowed = set(base.get("fingerprints", []))
        kept = [f for f in result.findings if fingerprint(f) not in allowed]
        suppressed = len(result.findings) - len(kept)
        result.findings = kept
        score, verdict = compute_verdict(kept)
        result.score, result.verdict = score, verdict
        sev = {s: 0 for s in SEV_RANK}
        cats = {}
        for f in kept:
            sev[f.severity] += 1
            cats[f.category] = cats.get(f.category, 0) + 1
        result.counts = {"by_severity": sev, "by_category": cats,
                         "total": len(kept), "suppressed_by_baseline": suppressed}

    if args.sarif:
        print(render_sarif(result))
    elif args.json:
        print(to_json(result))
    elif args.quiet:
        print("%s  score=%d  findings=%d  target=%s" % (
            result.verdict, result.score, len(result.findings), result.target))
    else:
        print(render_text(result))

    order = ["SAFE", "CAUTION", "SUSPICIOUS", "MALICIOUS"]
    if args.fail_on == "never":
        return 0
    threshold = order.index(args.fail_on.upper())
    return VERDICT_EXIT[result.verdict] if order.index(result.verdict) >= threshold else 0


if __name__ == "__main__":
    sys.exit(main())
