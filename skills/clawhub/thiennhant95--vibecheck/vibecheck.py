#!/usr/bin/env python3
"""
vibecheck — audit AI-generated code before it ships.

Zero-dependency Python 3.8+ CLI. Scans a file or directory for common
security holes, code smells, and "AI slop" patterns, then gives a
0-100 vibe score with actionable findings.

v1.0: AST-hardened rules (aliases, constant propagation, unsafe YAML
loaders, os.system), .env secret detection, severity-capped scoring,
cross-platform path handling (Windows-safe ignores).

Usage:
    python3 vibecheck.py <path> [--format text|json|md|sarif] [--min-score N]
                        [--exclude PATTERN ...] [--fail-on SEVERITY] [--version]

Inline suppression (comment on the line above, or trailing the line):
    # vibecheck: disable=<rule-id,rule-id>   (or bare "disable" for all rules)
    # vibecheck: ignore                      (whole file, first line)

Exit codes: 0 = pass, 1 = below min-score or finding at/above --fail-on.
"""

import argparse
import ast
import hashlib
import json
import re
import sys
from contextlib import suppress
from pathlib import Path

__version__ = "1.0.11"

# ---------------------------------------------------------------- config

SEVERITY_WEIGHT = {"critical": 15, "high": 10, "medium": 5, "low": 2, "info": 0}
SEVERITY_ORDER = ["critical", "high", "medium", "low", "info"]

CODE_EXTS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rb", ".java", ".php",
    ".sh", ".bash", ".cs", ".rs", ".kt", ".swift", ".yaml", ".yml",
    ".json", ".toml", ".env", ".cfg", ".ini", ".tf",
}
SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "venv", ".venv", "env",
    "__pycache__", "dist", "build", ".tox", "vendor", ".idea", ".vscode",
    ".openclaw",
}
PLACEHOLDER_RE = re.compile(
    r"(?i)(example|placeholder|your[-_]|changeme|xxx+|<[^>]+>|\$\{|getenv|environ|process\.env|config)"
)

MAX_FILE_BYTES = 2_000_000

# Rule scopes:
#   "code"    -> matched against code-only mask (strings + comments blanked)
#   "raw"     -> matched against original text (secrets/SQL live in strings)
#   "comment" -> matched against comment-only mask
RULES = [
    {
        "id": "private-key",
        "severity": "critical",
        "scope": "raw",
        "title": "Private key committed in source",
        "advice": "Rotate the key NOW and move it to a secret manager. Remove it from git history.",
        "pattern": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        "exts": None,
        "skip_if": None,
    },
    {
        "id": "secret-aws",
        "severity": "critical",
        "scope": "raw",
        "title": "AWS access key id in source",
        "advice": "Rotate the IAM key and load it from environment/secret manager.",
        "pattern": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "exts": None,
        "skip_if": None,
    },
    {
        "id": "secret-token",
        "severity": "high",
        "scope": "raw",
        "title": "Hardcoded API token / secret",
        "advice": "Load secrets from env vars or a secret manager, never commit them.",
        "pattern": re.compile(
            r"\b(sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{36}|gho_[A-Za-z0-9]{36}"
            r"|xox[baprs]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_-]{35})"
        ),
        "exts": None,
        "skip_if": None,
    },
    {
        "id": "secret-assignment",
        "severity": "high",
        "scope": "raw",
        "title": "Hardcoded password/secret assignment",
        "advice": "Use env vars (os.getenv / process.env) or a vault. Never inline credentials.",
        "pattern": re.compile(
            r"(?i)\b(password|passwd|pwd|secret|api_?key|access_?token|auth_?token)\b\s*[:=]\s*[\"'][^\"'\n]{8,}[\"']"
        ),
        "exts": None,
        "skip_if": lambda line: bool(PLACEHOLDER_RE.search(line)),
    },
    {
        "id": "env-secret",
        "severity": "high",
        "scope": "raw",
        "title": "Hardcoded secret in a .env file",
        "advice": "Move real values out of .env into a secret manager; commit only .env.example.",
        "pattern": re.compile(r"(?m)^\s*(?:export\s+)?[A-Za-z_][A-Za-z0-9_]*\s*=\s*\S{8,}\s*$"),
        "exts": None,
        "skip_if": None,
        "manual": True,
        "env_files": True,
    },
    {
        "id": "sql-injection",
        "severity": "high",
        "scope": "raw",
        "title": "SQL built by string interpolation",
        "advice": "Use parameterized queries / prepared statements (? or %s placeholders).",
        "pattern": re.compile(
            r"(?i)(f[\"'][^\"\n]*\b(select|insert|update|delete)\b[^\"\n]*\{"  # vibecheck: disable=sql-injection
            r"|f'[^'\n]*\b(select|insert|update|delete)\b[^'\n]*\{"  # vibecheck: disable=sql-injection
            r"|[\"'][^\"'\n]*\b(select|insert|update|delete)\b[^\"'\n]*[\"']\s*(%|\.format\s*\(|\+))"
        ),
        "exts": {".py", ".js", ".ts", ".go", ".rb", ".java", ".php"},
        "skip_if": None,
    },
    {
        "id": "cors-wildcard",
        "severity": "medium",
        "scope": "raw",
        "title": "CORS allows all origins",
        "advice": "allow_origins=['*'] is fine for public APIs only. Restrict to real origins.",  # vibecheck: disable=cors-wildcard
        "pattern": re.compile(
            r"allow_origins\s*=\s*\[[^\]\n]*[\"']\*[\"']|Access-Control-Allow-Origin[^\n]*\*|origin\s*:\s*[\"']\*[\"']"  # vibecheck: disable=cors-wildcard
        ),
        "exts": None,
        "skip_if": None,
    },
    {
        "id": "eval-exec",
        "severity": "high",
        "scope": "code",
        "title": "Dynamic code execution (eval/exec)",
        "advice": "eval/exec on untrusted input = remote code execution. Use ast.literal_eval, json, or explicit dispatch.",
        "pattern": re.compile(r"\b(eval|exec)\s*\("),
        "exts": {".py"},
        "skip_if": lambda line: "literal_eval" in line,
    },
    {
        "id": "js-eval",
        "severity": "high",
        "scope": "code",
        "title": "Dynamic code execution (eval/Function)",
        "advice": "Avoid eval/new Function on dynamic input. Use JSON.parse or explicit logic.",
        "pattern": re.compile(r"\beval\s*\(|new\s+Function\s*\("),
        "exts": {".js", ".jsx", ".ts", ".tsx"},
        "skip_if": None,
    },
    {
        "id": "shell-true",
        "severity": "high",
        "scope": "code",
        "title": "subprocess with shell=True",
        "advice": "shell=True enables command injection. Pass an args list instead.",
        "pattern": re.compile(r"shell\s*=\s*True"),
        "exts": {".py"},
        "skip_if": None,
    },
    {
        "id": "os-shell",
        "severity": "high",
        "scope": "code",
        "title": "Command execution via os.system / os.popen",
        "advice": "os.system/os.popen run through a shell. Use subprocess with an argv list and shell=False.",
        "pattern": re.compile(r"\bos\.(?:system|popen)\s*\("),
        "exts": {".py"},
        "skip_if": None,
    },
    {
        "id": "verify-false",
        "severity": "high",
        "scope": "code",
        "title": "TLS certificate verification disabled",
        "advice": "verify=False allows MITM. Fix the cert chain instead of disabling verification.",
        "pattern": re.compile(r"verify\s*=\s*False|rejectUnauthorized\s*:\s*false|NODE_TLS_REJECT_UNAUTHORIZED\s*=\s*['\"]?0"),
        "exts": None,
        "skip_if": None,
    },
    {
        "id": "weak-hash",
        "severity": "medium",
        "scope": "code",
        "title": "Weak hash (MD5/SHA1)",
        "advice": "MD5/SHA1 are broken. Use SHA-256+ for integrity, bcrypt/argon2 for passwords.",
        "pattern": re.compile(r"\bhashlib\.(md5|sha1)\s*\(|\b(md5|sha1)\s*\("),
        "exts": {".py", ".js", ".ts", ".go", ".rb", ".java", ".php"},
        "skip_if": lambda line: "usedforsecurity" in line,
    },
    {
        "id": "pickle-load",
        "severity": "medium",
        "scope": "code",
        "title": "Unsafe deserialization (pickle)",
        "advice": "pickle.load on untrusted data = arbitrary code execution. Use json or a safe serializer.",
        "pattern": re.compile(r"pickle\.loads?\s*\("),
        "exts": {".py"},
        "skip_if": None,
    },
    {
        "id": "yaml-unsafe-load",
        "severity": "medium",
        "scope": "code",
        "title": "yaml.load without safe Loader",
        "advice": "Use yaml.safe_load unless you fully trust the input.",
        "pattern": re.compile(r"yaml\.load\s*\("),
        "exts": {".py"},
        "skip_if": lambda line: ("safe_load" in line or "SafeLoader" in line
                                 or "CSafeLoader" in line or "BaseLoader" in line
                                 or "FullLoader" in line),
    },
    {
        "id": "except-pass",
        "severity": "low",
        "scope": "code",
        "title": "Swallowed exception (except: pass)",
        "advice": "Silent failures hide bugs. Log the error or re-raise with context.",
        "pattern": re.compile(r"except[^\n]*:\s*(?:\n\s*)?pass\b|catch\s*\([^)]*\)\s*\{\s*\}"),
        "exts": None,
        "skip_if": None,
    },
    {
        "id": "debug-log",
        "severity": "low",
        "scope": "code",
        "title": "Debug logging left in code",
        "advice": "Remove console.log leftovers or gate them behind a debug flag/logger level.",
        "pattern": re.compile(r"console\.log\s*\("),
        "exts": {".js", ".jsx", ".ts", ".tsx"},
        "skip_if": None,
    },
    {
        "id": "todo-fixme",
        "severity": "info",
        "scope": "comment",
        "title": "TODO/FIXME marker",
        "advice": "AI loves leaving TODOs. Turn them into issues or finish the job.",
        "pattern": re.compile(r"\b(TODO|FIXME|HACK|XXX+)\b"),
        "exts": None,
        "skip_if": None,
    },
]

RULES_BY_ID = {r["id"]: r for r in RULES}

# ---------------------------------------------------------------- masking

# Language configs: (line_comment tokens, block_comment (start,end) or None,
#                    quote chars, triple-quote tokens)
LANGS = {
    ".py": (["#"], None, "'\"", ["'''", '"""']),
    ".js": (["//"], ("/*", "*/"), "'\"`", []),
    ".jsx": (["//"], ("/*", "*/"), "'\"`", []),
    ".ts": (["//"], ("/*", "*/"), "'\"`", []),
    ".tsx": (["//"], ("/*", "*/"), "'\"`", []),
    ".go": (["//"], ("/*", "*/"), "'\"`", []),
    ".java": (["//"], ("/*", "*/"), "'\"", []),
    ".cs": (["//"], ("/*", "*/"), "'\"", []),
    ".kt": (["//"], ("/*", "*/"), "'\"", []),
    ".swift": (["//"], ("/*", "*/"), "'\"", []),
    ".rs": (["//"], ("/*", "*/"), "'\"", []),
    ".php": (["//", "#"], ("/*", "*/"), "'\"", []),
    ".rb": (["#"], None, "'", []),
    ".sh": (["#"], None, "'", []),
    ".bash": (["#"], None, "'", []),
    ".yaml": (["#"], None, "'", []),
    ".yml": (["#"], None, "'", []),
    ".toml": (["#"], None, "'\"", []),
    ".ini": (["#", ";"], None, "'", []),
    ".cfg": (["#", ";"], None, "'", []),
    ".env": (["#"], None, "'", []),
    ".tf": (["#", "//"], ("/*", "*/"), "'\"", []),
    ".json": ([], None, "\"", []),
}
DEFAULT_LANG = (["#", "//"], ("/*", "*/"), "'\"`", [])


def mask_text(text, ext):
    """Return (code_mask, comment_mask): strings/comments blanked (code_mask),
    only comments kept (comment_mask). Same length as text, newlines preserved."""
    line_c, block_c, quotes, triples = LANGS.get(ext, DEFAULT_LANG)
    n = len(text)
    code = list(text)
    comments = ["\n" if ch == "\n" else " " for ch in text]
    i = 0
    while i < n:
        ch = text[i]
        # triple-quoted strings
        matched_triple = None
        for t in triples:
            if text.startswith(t, i):
                matched_triple = t
                break
        if matched_triple:
            end = text.find(matched_triple, i + 3)
            end = (end + 3) if end != -1 else n
            for j in range(i, end):
                if code[j] != "\n":
                    code[j] = " "
            i = end
            continue
        # block comment
        if block_c and text.startswith(block_c[0], i):
            end = text.find(block_c[1], i + 2)
            end = (end + 2) if end != -1 else n
            for j in range(i, end):
                if code[j] == "\n":
                    continue
                comments[j] = text[j]
                code[j] = " "
            i = end
            continue
        # line comment
        line_tok = next((tok for tok in line_c if text.startswith(tok, i)), None)
        if line_tok:
            end = text.find("\n", i)
            end = end if end != -1 else n
            for j in range(i, end):
                comments[j] = text[j]
                code[j] = " "
            i = end
            continue
        # string literal
        if ch in quotes:
            quote = ch
            j = i + 1
            while j < n:
                if text[j] == "\\":
                    j += 2
                    continue
                if text[j] == quote or text[j] == "\n":
                    break
                j += 1
            end = min(j + 1, n)
            for k in range(i, end):
                if code[k] != "\n":
                    code[k] = " "
            i = end
            continue
        i += 1
    return "".join(code), "".join(comments)


# ---------------------------------------------------------------- scanning

REDACT_PATTERNS = [
    (re.compile(r"\b(AKIA)[0-9A-Z]{16}\b"),
     lambda m: m.group(1) + "*" * 12 + "****"),
    (re.compile(r"\b(sk-|ghp_|gho_|xox[baprs]-|AIza)[A-Za-z0-9_-]{10,}"),
     lambda m: m.group(1) + "***redacted***"),
    (re.compile(r"(?i)(\b(?:password|passwd|pwd|secret|api_?key|access_?token|auth_?token|token)\b\s*[:=]\s*)([\"'])([^\"']{0,4})[^\"']*([\"'])"),
     lambda m: m.group(1) + m.group(2) + m.group(3) + "***" + m.group(4)),
    (re.compile(r"(?m)^(\s*(?:export\s+)?[A-Za-z_][A-Za-z0-9_]*\s*=\s*)([\"']?)\S{8,}([\"']?)\s*$"),
     lambda m: m.group(1) + m.group(2) + "***redacted***" + m.group(3)),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*"),
     lambda m: "-----BEGIN PRIVATE KEY----- [REDACTED]"),  # vibecheck: disable=private-key
]


def redact_snippet(text):
    """Mask credential material before it reaches reports, SARIF, or baselines."""
    out = text
    for pat, repl in REDACT_PATTERNS:
        out = pat.sub(repl, out)
    return out


class Finding:
    __slots__ = ("rule", "severity", "file", "line", "snippet")

    def __init__(self, rule, file, line, snippet):
        self.rule = rule["id"]
        self.severity = rule["severity"]
        self.file = str(file)
        self.line = line
        self.snippet = redact_snippet(snippet.strip()[:160])

    def fingerprint(self):
        basis = f"{self.rule}|{self.file}|{self.snippet}"
        return hashlib.sha256(basis.encode("utf-8", "replace")).hexdigest()[:16]

    def to_dict(self):
        return {
            "rule": self.rule,
            "severity": self.severity,
            "file": self.file,
            "line": self.line,
            "snippet": self.snippet,
            "fingerprint": self.fingerprint(),
        }


SUPPRESS_RE = re.compile(r"vibecheck:\s*(?:disable(?:=([\w,\s-]+))?|ignore)\s*$")
FILE_IGNORE_NAME = ".vibecheckignore"


def load_ignore_file(root: Path):
    p = root / FILE_IGNORE_NAME if root.is_dir() else root.parent / FILE_IGNORE_NAME
    pats = []
    if p.is_file():
        for ln in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#"):
                pats.append(re.compile(ln))
    return pats


def parse_suppressions(text):
    """Return (file_ignored, {(lineno, rule_id|None)}) from vibecheck comments."""
    ignored = False
    sup = set()
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        m = SUPPRESS_RE.search(line)
        if not m:
            continue
        lineno = idx + 1
        if "vibecheck: ignore" in m.group(0) and "disable" not in m.group(0):
            if idx == 0:
                ignored = True
            else:
                sup.add((lineno, None))  # applies to this line
            continue
        rules_raw = m.group(1)
        rule_ids = (
            [r.strip() for r in rules_raw.split(",") if r.strip()]
            if rules_raw
            else [None]
        )
        stripped = line.strip()
        own_line = stripped.startswith(("#", "//", "/*", "*", ";", "<!--"))
        target = lineno + 1 if own_line else lineno
        for rid in rule_ids:
            sup.add((target, rid))
    return ignored, sup


def iter_files(root: Path, excludes):
    if root.is_file():
        yield root
        return
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        rel_parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in rel_parts[:-1]):
            continue
        rel = Path(*rel_parts).as_posix()
        if any(re.search(pat, rel) for pat in excludes):
            continue
        if path.suffix.lower() not in CODE_EXTS and path.name != ".env":
            continue
        if path.stat().st_size > MAX_FILE_BYTES:
            continue
        yield path


def scan_file(path: Path, rel_base: Path, excludes):
    try:
        rel = path.relative_to(rel_base).as_posix()
    except ValueError:
        rel = path.as_posix()
    if any(re.search(pat, rel) for pat in excludes):
        return []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    if "\x00" in text:
        return []  # binary

    file_ignored, sup = parse_suppressions(text)
    if file_ignored:
        return []

    ext = path.suffix.lower()
    code_mask, comment_mask = mask_text(text, ext)
    lines = text.splitlines()
    findings = []
    seen = set()

    for rule in RULES:
        if rule.get("manual"):
            continue
        if rule["exts"] is not None and ext not in rule["exts"]:
            continue
        target = {"code": code_mask, "raw": text, "comment": comment_mask}[rule["scope"]]
        hits = 0
        for m in rule["pattern"].finditer(target):
            lineno = target.count("\n", 0, m.start()) + 1
            if (lineno, rule["id"]) in sup or (lineno, None) in sup:
                continue
            key = (rule["id"], lineno)
            if key in seen:
                continue
            seen.add(key)
            snippet = lines[lineno - 1] if lineno <= len(lines) else m.group(0)
            if rule["skip_if"] and rule["skip_if"](snippet):
                continue
            findings.append(Finding(rule, rel, lineno, snippet))
            hits += 1
            if hits >= 20:  # cap noise per rule per file
                break

    findings.extend(structural_checks(rel, lines, ext))
    if path.name.startswith(".env"):
        env_rule = RULES_BY_ID["env-secret"]
        for idx, line in enumerate(lines, 1):
            if not env_secret_hit(line):
                continue
            if (idx, "env-secret") in sup or (idx, None) in sup:
                continue
            key = ("env-secret", idx)
            if key in seen:
                continue
            seen.add(key)
            findings.append(Finding(env_rule, rel, idx, line))
    if ext == ".py":
        for f in ast_findings(text, rel, lines):
            key = (f.rule, f.line)
            if key in seen or (f.line, f.rule) in sup or (f.line, None) in sup:
                continue
            seen.add(key)
            findings.append(f)
    return findings


FUNC_START = re.compile(
    r"^\s*(def\s+(?P<py>\w+)|class\s+(?P<cls>\w+)|function\s+(?P<js>\w+)|const\s+(?P<fn>\w+)\s*=\s*(?:async\s*)?\()",
    re.M,
)


# ---------------------------------------------------------------- AST layer
# Semantic analysis for Python: catches what regex cannot — aliased calls,
# multi-line statements, commented-out except bodies.

def _dotted(func):
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        base = _dotted(func.value)
        return f"{base}.{func.attr}" if base else func.attr
    return None


def _const_true(node):
    return isinstance(node, ast.Constant) and node.value is True


def _const_false(node):
    return isinstance(node, ast.Constant) and node.value is False


def ast_findings(text, rel, lines):
    findings = []
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        return findings  # template/partial file: regex pass still applies

    def add(rule_id, lineno):
        rule = RULES_BY_ID.get(rule_id)
        if not rule:
            return
        snippet = lines[lineno - 1] if 0 < lineno <= len(lines) else ""
        findings.append(Finding(rule, rel, lineno, snippet))

    # --- name resolution: imports, module/function aliases, bool constants ---
    module_alias, value_alias, consts = {}, {}, {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                top = (a.name or "").split(".")[0]
                module_alias[a.asname or top] = a.name if a.asname else top
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            for a in node.names:
                target = f"{mod}.{a.name}" if mod else a.name
                if a.name in ("eval", "exec") or target in (
                        "os.system", "os.popen", "pickle.load", "pickle.loads",
                        "yaml.load"):
                    value_alias[a.asname or a.name] = target
        elif isinstance(node, ast.Assign):
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                val = node.value
                if isinstance(val, ast.Constant) and isinstance(val.value, bool):
                    consts[name] = val.value
                dotted_val = _dotted(val)
                if dotted_val:
                    base, _, rest = dotted_val.partition(".")
                    resolved = module_alias.get(base, base) + ("." + rest if rest else "")
                    if resolved in ("eval", "exec", "os.system", "os.popen",
                                    "pickle", "pickle.load", "pickle.loads",
                                    "yaml", "yaml.load"):
                        value_alias[name] = resolved

    def resolve(dotted):
        if not dotted:
            return dotted
        if dotted in value_alias:
            return value_alias[dotted]
        base, _, rest = dotted.partition(".")
        base = value_alias.get(base) or module_alias.get(base) or base
        resolved = base + ("." + rest if rest else "")
        return value_alias.get(resolved, resolved)

    def const_bool(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, bool):
            return node.value
        if isinstance(node, ast.Name):
            return consts.get(node.id)
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            dotted = resolve(_dotted(node.func))
            short = dotted.split(".")[-1] if dotted else ""

            if dotted in ("eval", "exec", "builtins.eval", "builtins.exec"):
                add("eval-exec", node.lineno)
            if dotted and dotted.startswith("hashlib.") and short in ("md5", "sha1"):
                add("weak-hash", node.lineno)
            if dotted and dotted.startswith("pickle.") and short in ("load", "loads"):
                add("pickle-load", node.lineno)
            if dotted in ("os.system", "os.popen"):
                add("os-shell", node.lineno)
            if dotted and dotted.startswith("yaml.") and short == "load":
                loader = next((kw.value for kw in node.keywords if kw.arg == "Loader"), None)
                if loader is None:
                    add("yaml-unsafe-load", node.lineno)
                else:
                    lname = resolve(_dotted(loader)) or ""
                    if lname.split(".")[-1] in ("UnsafeLoader", "Loader"):
                        add("yaml-unsafe-load", node.lineno)
            if short in ("run", "Popen", "call", "check_call", "check_output"):
                for kw in node.keywords:
                    if kw.arg == "shell" and const_bool(kw.value) is True:
                        add("shell-true", kw.value.lineno)
            for kw in node.keywords:
                if kw.arg == "verify" and const_bool(kw.value) is False:
                    add("verify-false", kw.value.lineno)

        if isinstance(node, ast.ExceptHandler):
            if node.body and all(isinstance(s, ast.Pass) for s in node.body):
                add("except-pass", node.lineno)

    return findings


ENV_SECRET_TOKENS = {"PASSWORD", "PASSWD", "PASS", "PWD", "SECRET", "TOKEN",
                     "CREDENTIAL", "CREDENTIALS", "APIKEY", "ACCESSKEY",
                     "PRIVATEKEY", "DBPASS"}


def env_secret_hit(line):
    """True when a .env-style line assigns a real-looking secret value."""
    s = line.strip()
    if not s or s.startswith("#"):
        return False
    m = re.match(r"^(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$", s)
    if not m:
        return False
    key, val = m.group(1).upper(), m.group(2).strip()
    parts = [p for p in key.split("_") if p]
    looks_secret = (
        any(p in ENV_SECRET_TOKENS for p in parts)
        or key.endswith(("_KEY", "_TOKEN", "_SECRET", "_PASS"))
    )
    if not looks_secret:
        return False
    if any(p in ("PUBLIC", "PUB") for p in parts):
        return False
    val = val.strip('"').strip("'")
    if len(val) < 8:
        return False
    if val.startswith(("$", "{{", "<")):
        return False
    if PLACEHOLDER_RE.search(val):
        return False
    return True


def structural_checks(rel, lines, ext):
    findings = []
    n = len(lines)

    if n > 800:
        findings.append(Finding(
            {"id": "file-too-long", "severity": "info"}, rel, 1,
            f"file is {n} lines long",
        ))

    long_lines = sum(1 for ln in lines if len(ln) > 140)
    if long_lines > 10:
        findings.append(Finding(
            {"id": "long-lines", "severity": "info"}, rel, 1,
            f"{long_lines} lines exceed 140 chars",
        ))

    text = "\n".join(lines)
    starts = [(m.start(), (m.group("py") or m.group("cls") or m.group("js") or m.group("fn")))
              for m in FUNC_START.finditer(text)]
    for i, (pos, name) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        body_lines = text.count("\n", pos, end) + 1
        if body_lines > 100:
            lineno = text.count("\n", 0, pos) + 1
            findings.append(Finding(
                {"id": "long-function", "severity": "info"}, rel, lineno,
                f"'{name}' is ~{body_lines} lines long",
            ))
    return findings


# ---------------------------------------------------------------- autofix

# Safety tiers:
#   "safe"   -> behavior-preserving, applied with --fix
#   "unsafe" -> behavior-changing, applied only with --fix --unsafe
# Fix pattern value None = drop the whole line.
FIX_PATTERNS = {
    "yaml-unsafe-load": {
        # safe_load rejects arbitrary Python objects: this changes behavior,
        # so it requires the explicit --fix-unsafe opt-in.
        "unsafe": [(re.compile(r"yaml\.load\s*\("), "yaml.safe_load(")],
    },
    "debug-log": {
        "unsafe": [(re.compile(r"^\s*console\.log\(.*\);?\s*$"), None)],
    },
    "verify-false": {
        "unsafe": [
            (re.compile(r",\s*verify\s*=\s*False"), ""),
            (re.compile(r"verify\s*=\s*False\s*,\s*"), ""),
        ],
    },
}


def apply_fixes(findings, rel_base, include_unsafe, dry_run):
    """Apply available fixes per file. Returns list of applied fix dicts."""
    applied = []
    by_file = {}
    for f in findings:
        if f.rule in FIX_PATTERNS:
            by_file.setdefault(f.file, []).append(f)

    for rel, items in sorted(by_file.items()):
        path = rel_base / rel
        try:
            base = rel_base.resolve()
            path.resolve().relative_to(base)
        except (OSError, ValueError):
            continue  # never edit outside the scanned root (or through symlinks)
        if path.is_symlink() or not path.is_file():
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        except OSError:
            continue
        dirty = False
        for f in sorted(items, key=lambda x: -x.line):
            if not (0 < f.line <= len(lines)):
                continue
            tiers = FIX_PATTERNS[f.rule]
            tier = "safe" if "safe" in tiers else "unsafe"
            if tier == "unsafe" and not include_unsafe:
                continue
            text = original = lines[f.line - 1]
            nxt = lines[f.line] if f.line < len(lines) else ""
            if f.rule == "yaml-unsafe-load" and (
                    "Loader" in text or "safe_load" in text or "Loader" in nxt):
                continue  # rewriting would duplicate/preserve an incompatible Loader arg
            changed = False
            for pat, repl in tiers[tier]:
                if repl is None:
                    if pat.match(text):
                        text = ""
                        changed = True
                else:
                    new = pat.sub(repl, text)
                    if new != text:
                        text = new
                        changed = True
            if changed:
                lines[f.line - 1] = text
                dirty = True
                applied.append({
                    "rule": f.rule,
                    "file": rel,
                    "line": f.line,
                    "tier": tier,
                    "before": redact_snippet(original.strip()[:120]),
                    "after": redact_snippet(text.strip()[:120]),
                })
        if dirty and not dry_run:
            path.write_text("".join(lines), encoding="utf-8")
    return applied


# ---------------------------------------------------------------- scoring

def compute_score(findings):
    deductions = {}
    for f in findings:
        deductions[f.rule] = deductions.get(f.rule, 0) + 1
    total = 0
    for rule in RULES:
        cnt = deductions.get(rule["id"], 0)
        if cnt:
            total += min(cnt, 3) * SEVERITY_WEIGHT[rule["severity"]]
    for rid, cnt in deductions.items():
        if rid in ("file-too-long", "long-lines", "long-function"):
            total += min(cnt, 3) * SEVERITY_WEIGHT["info"]
    score = max(0, min(100, 100 - total))
    severities = {f.severity for f in findings}
    if "critical" in severities:
        score = min(score, 30)
    elif "high" in severities:
        score = min(score, 69)
    return score


def summarize(findings):
    counts = {s: 0 for s in SEVERITY_ORDER}
    for f in findings:
        counts[f.severity] = counts.get(f.severity, 0) + 1
    return counts


# ---------------------------------------------------------------- output

COLORS = {
    "critical": "\033[91m", "high": "\033[93m", "medium": "\033[33m",
    "low": "\033[96m", "info": "\033[90m", "reset": "\033[0m",
    "bold": "\033[1m", "green": "\033[92m", "red": "\033[91m",
}


def c(text, key, use_color):
    return f"{COLORS[key]}{text}{COLORS['reset']}" if use_color else str(text)


def verdict(score, min_score):
    if score >= 90:
        return "CLEAN — production ready"
    if score >= 70:
        return "OK — minor cleanup needed"
    if score >= 50:
        return "RISKY — fix before merge"
    return "DANGER — do not ship"


def render_text(findings, score, counts, min_score, use_color, suppressed=0, fix_info=None):
    out = []
    out.append(c("── vibecheck ──────────────────────────────", "bold", use_color))
    v = verdict(score, min_score)
    color = "green" if score >= min_score else "red"
    out.append(f"Vibe score: {c(f'{score}/100', color, use_color)}  [{v}]")
    out.append(
        "Findings: "
        + "  ".join(c(f"{counts[s]} {s}", s, use_color) for s in SEVERITY_ORDER if counts.get(s))
    )
    if suppressed:
        out.append(c(f"Baseline: {suppressed} known findings suppressed", "info", use_color))
    if fix_info and fix_info["count"]:
        mode = " (dry-run, nothing written)" if fix_info["dry_run"] else ""
        out.append(c(f"Autofix: {fix_info['count']} applied{mode}", "green", use_color))
    out.append("")
    order = {s: i for i, s in enumerate(SEVERITY_ORDER)}
    for f in sorted(findings, key=lambda f: (order.get(f.severity, 9), f.file, f.line)):
        tag = c(f.severity.upper().ljust(8), f.severity, use_color)
        out.append(f"{tag} {f.file}:{f.line}  [{f.rule}]")
        out.append(f"         {f.snippet}")
    if not findings:
        out.append(c("No issues found. Suspiciously clean... nice.", "green", use_color))
    return "\n".join(out)


def render_md(findings, score, counts, min_score, suppressed=0, fix_info=None):
    out = ["# vibecheck report", ""]
    out.append(f"**Vibe score: {score}/100** — {verdict(score, min_score)}")
    if suppressed:
        out.append(f"")
        out.append(f"_{suppressed} known findings suppressed by baseline._")
    if fix_info and fix_info["count"]:
        out.append(f"_{fix_info['count']} issues auto-fixed._")
    out.append("")
    out.append("| Severity | Count |")
    out.append("|---|---|")
    for s in SEVERITY_ORDER:
        if counts.get(s):
            out.append(f"| {s} | {counts[s]} |")
    out.append("")
    if findings:
        out.append("| Severity | File:Line | Rule | Snippet |")
        out.append("|---|---|---|---|")
        order = {s: i for i, s in enumerate(SEVERITY_ORDER)}
        for f in sorted(findings, key=lambda f: (order.get(f.severity, 9), f.file, f.line)):
            snip = f.snippet.replace("|", "\\|")
            out.append(f"| {f.severity} | `{f.file}:{f.line}` | {f.rule} | `{snip}` |")
    return "\n".join(out)


def render_json(findings, score, counts, min_score, suppressed=0, fix_info=None):
    return json.dumps({
        "tool": "vibecheck",
        "version": __version__,
        "score": score,
        "verdict": verdict(score, min_score),
        "min_score": min_score,
        "baseline": {"suppressed": suppressed},
        "autofix": fix_info,
        "summary": counts,
        "findings": [f.to_dict() for f in findings],
    }, indent=2, ensure_ascii=False)


SEVERITY_TO_SARIF = {
    "critical": "error", "high": "error", "medium": "warning",
    "low": "note", "info": "note",
}


def render_sarif(findings, score, counts, min_score, suppressed=0):
    """SARIF 2.1.0 — plugs into GitHub code scanning natively."""
    rules, seen = [], set()
    for f in findings:
        if f.rule in seen:
            continue
        seen.add(f.rule)
        meta = RULES_BY_ID.get(f.rule, {"severity": f.severity, "title": f.rule})
        rules.append({
            "id": f.rule,
            "shortDescription": {"text": meta["title"]},
            "defaultConfiguration": {"level": SEVERITY_TO_SARIF.get(meta["severity"], "note")},
        })
    results = []
    for f in findings:
        meta = RULES_BY_ID.get(f.rule, {"title": f.rule, "advice": ""})
        results.append({
            "ruleId": f.rule,
            "level": SEVERITY_TO_SARIF.get(f.severity, "note"),
            "message": {"text": f"{meta['title']}: {f.snippet}\n{meta.get('advice', '')}".strip()},
            "locations": [{"physicalLocation": {
                "artifactLocation": {"uri": f.file},
                "region": {"startLine": max(f.line, 1)},
            }}],
        })
    return json.dumps({
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {
                "name": "vibecheck",
                "version": __version__,
                "rules": rules,
            }},
            "results": results,
        }],
    }, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------- main

def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        with suppress(AttributeError, OSError):
            # Windows consoles default to cp1252; never crash on reports.
            stream.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(
        prog="vibecheck",
        description="Audit AI-generated code before it ships. Zero dependencies.",
    )
    ap.add_argument("path", nargs="?", default=".", help="file or directory to scan (default: .)")
    ap.add_argument("--version", action="version", version=f"vibecheck {__version__}")
    ap.add_argument("--format", choices=["text", "json", "md", "sarif"], default="text")
    ap.add_argument("--min-score", type=int, default=70, help="minimum passing score (default 70)")
    ap.add_argument("--fail-on", choices=SEVERITY_ORDER, default="critical",
                    help="exit 1 if any finding at/above this severity (default critical)")
    ap.add_argument("--exclude", action="append", default=[], help="regex to exclude paths (repeatable)")
    ap.add_argument("--baseline", help="baseline file: hide known findings recorded in it")
    ap.add_argument("--write-baseline", help="record current findings to baseline file")
    ap.add_argument("--fix", action="store_true", help="apply SAFE auto-fixes in place")
    ap.add_argument("--fix-unsafe", action="store_true",
                    help="also apply behavior-changing fixes (use with --fix)")
    ap.add_argument("--fix-dry-run", action="store_true",
                    help="show what --fix would change without writing")
    ap.add_argument("--no-color", action="store_true")
    args = ap.parse_args(argv)

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"vibecheck: path not found: {args.path}", file=sys.stderr)
        return 2

    excludes = args.exclude + [p.pattern for p in load_ignore_file(root)]
    rel_base = root if root.is_dir() else root.parent

    findings = []
    for fpath in iter_files(root, excludes):
        findings.extend(scan_file(fpath, rel_base, excludes))

    if args.write_baseline:
        payload = {
            "tool": "vibecheck",
            "version": __version__,
            "findings": [f.to_dict() for f in findings],
        }
        Path(args.write_baseline).write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    suppressed = 0
    if args.baseline:
        bpath = Path(args.baseline)
        if bpath.exists():
            known = {
                item.get("fingerprint")
                for item in json.loads(bpath.read_text(encoding="utf-8")).get("findings", [])
            }
            kept = [f for f in findings if f.fingerprint() not in known]
            suppressed = len(findings) - len(kept)
            findings = kept

    fix_info = None
    if args.fix or args.fix_dry_run:
        dry = args.fix_dry_run
        fixes = apply_fixes(findings, rel_base, args.fix_unsafe, dry)
        fix_info = {"applied": fixes, "count": len(fixes), "dry_run": dry}
        if fixes and not dry:
            # re-scan so score reflects the fixed code
            findings = []
            for fpath in iter_files(root, excludes):
                findings.extend(scan_file(fpath, rel_base, excludes))
            if args.baseline:
                bpath = Path(args.baseline)
                if bpath.exists():
                    known = {
                        item.get("fingerprint")
                        for item in json.loads(bpath.read_text(encoding="utf-8")).get("findings", [])
                    }
                    findings = [f for f in findings if f.fingerprint() not in known]

    score = compute_score(findings)
    counts = summarize(findings)
    use_color = (
        args.format == "text"
        and not args.no_color
        and sys.stdout.isatty()
    )

    if args.format == "text":
        print(render_text(findings, score, counts, args.min_score, use_color, suppressed, fix_info))
    elif args.format == "md":
        print(render_md(findings, score, counts, args.min_score, suppressed, fix_info))
    elif args.format == "sarif":
        print(render_sarif(findings, score, counts, args.min_score, suppressed))
    else:
        print(render_json(findings, score, counts, args.min_score, suppressed, fix_info))

    fail_idx = SEVERITY_ORDER.index(args.fail_on)
    has_blocking = any(SEVERITY_ORDER.index(f.severity) <= fail_idx for f in findings)
    return 1 if (score < args.min_score or has_blocking) else 0


if __name__ == "__main__":
    sys.exit(main())
