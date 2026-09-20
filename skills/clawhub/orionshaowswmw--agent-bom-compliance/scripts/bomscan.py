#!/usr/bin/env python3
"""bomscan.py — Agent BOM Compliance engine (v2.0.0). Offline, stdlib-only.

Subcommands
  doctor                       environment check (JSON, agent_bom.doctor.v1)
  sbom DIR [-o out.json]       CycloneDX 1.5 JSON SBOM from npm/pip/go manifests
  scan DIR [--fail-severity S] verifiable rule engine → findings JSON
  report DIR [-o report.json]  sbom + scan + verdict + hash-chained audit entry
  trend DIR [--json]           findings delta vs previous audited run (self-tuning)
  audit [--verify]             show / chain-verify the tamper-evident audit log

Verifiable-check ruleset is curated and every finding cites STATIC control refs
from CONTROL_REGISTRY (OWASP-LLM-2025 LLM01–LLM10, OWASP Agentic AG07/AG04,
NIST SSDF SP 800-218, CISA-min SBOM practice) — hallucinated control IDs are
impossible by construction. Full standards posture is HONEST: this is a
verifiable-compliance *signal*, not a certification.

Exit codes: 0 ok/pass · 2 usage · 3 target/environment error · 4 policy FAIL.
"""
import argparse, hashlib, json, os, re, sys, time, uuid

SPEC = "1.5"
RULESET_VERSION = "2.0.0"
SEV_ORDER = ["INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"]

CONTROL_REGISTRY = {
    "OWASP-LLM-2025:LLM01": "Prompt Injection (OWASP LLM Top 10 2025)",
    "OWASP-LLM-2025:LLM02": "Sensitive Information Disclosure (OWASP LLM Top 10 2025)",
    "OWASP-LLM-2025:LLM03": "Supply Chain Vulnerabilities (OWASP LLM Top 10 2025)",
    "OWASP-LLM-2025:LLM06": "Excessive Agency (OWASP LLM Top 10 2025)",
    "OWASP-AGENTIC:AG04":  "Insufficient Guardrails (OWASP Agentic AI Top 10)",
    "OWASP-AGENTIC:AG07":  "Repudiation & Audit Gaps (OWASP Agentic AI Top 10)",
    "NIST-SSDF:PW.4":      "Reuse of well-secured components; verify integrity (SP 800-218 PW.4)",
    "NIST-SSDF:PS.3":      "Follow secure practices for software construction (SP 800-218 PS.3)",
    "CISA-MIN-ELEMENTS":   "Minimum SBOM elements expected per CISA / EO 14028 guidance",
}

SECRET_PATTERNS = [
    ("openai-style key",    re.compile(r"sk-[A-Za-z0-9_-]{16,}")),
    ("github token",        re.compile(r"(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}")),
    ("slack token",         re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("aws access key",      re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private key block",   re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH|DSA) PRIVATE KEY-----")),
    ("generic gcp key",     re.compile(r"AIza[0-9A-Za-z_-]{35}")),
]

TEXT_EXT = (".js", ".ts", ".py", ".sh", ".bash", ".md", ".txt", ".json", ".yml",
            ".yaml", ".toml", ".cfg", ".ini", ".env", ".html", ".css", ".rb",
            ".go", ".rs", ".java", ".c", ".h", ".cpp", ".php")
MODEL_EXT = (".gguf", ".safetensors", ".bin", ".pt", ".pth", ".ckpt", ".onnx", ".h5")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist",
             "build", ".arena", ".cache", ".next", "coverage", "out", "target"}


def now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def audit_path(a=None, target=None):
    return os.environ.get("AGENT_BOM_AUDIT") or os.path.join(
        target or ".", ".agent_bom_audit.jsonl")


def walk_files(root):
    out = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            out.append(os.path.join(dp, f))
    return out


# ── SBOM (CycloneDX 1.5) ────────────────────────────────────────────────────
def purl_npm(name, ver):
    n = name
    if n.startswith("@"):                        # @scope/name → %40scope/name
        n = "%40" + n[1:]
    return f"pkg:npm/{n}@{ver}"


def parse_package_json(path):
    comps = []
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception:
        return comps, {}
    root_dir = os.path.dirname(path)
    lockvers = {}
    lock = os.path.join(root_dir, "package-lock.json")
    if os.path.exists(lock):
        try:
            lj = json.load(open(lock, encoding="utf-8"))
            for pk, meta in (lj.get("packages") or {}).items():
                if pk.startswith("node_modules/") and meta.get("version"):
                    lockvers[pk.split("node_modules/", 1)[1]] = meta["version"]
        except Exception:
            pass
    for scope_name, sc in (("dependencies", "required"), ("devDependencies", "optional")):
        for name, spec in (data.get(scope_name) or {}).items():
            ver = lockvers.get(name) or str(spec)
            comps.append({"type": "library",
                          "bom-ref": f"npm:{name}@{ver}",
                          "name": name, "version": ver, "spec_raw": str(spec),
                          "scope": sc, "purl": purl_npm(name, ver)})
    return comps, {"name": data.get("name"), "version": data.get("version"),
                   "license": data.get("license"), "path": path}


def parse_requirements(path):
    comps = []
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except Exception:
        return comps
    for ln in lines:
        ln = ln.split(" #", 1)[0].strip()
        if not ln or ln.startswith(("#", "-c", "-r", "--")):
            continue
        # env markers are NOT part of the version (PEP 508): `pkg==1.0; python_version<"3.9"`
        ln = ln.split(";", 1)[0].strip()
        # URL / VCS / editable installs are skipped here (DEP-01 still flags
        # their no-== form as unpinned); nothing verifiable to put in an SBOM.
        if "://" in ln or ln.startswith(("-e", "git+")):
            continue
        m = re.match(r"^([A-Za-z0-9_.\-+]+)(\[.*?\])?\s*(==|>=|~=|<=|!=|<|>)?\s*([^;,]+)?$", ln)
        if not m:
            continue
        name, _ex, _op, ver = m.group(1), m.group(2), m.group(3), m.group(4)
        ver = (ver or "").strip() or "UNPINNED"
        if _op != "==":
            ver = "UNPINNED"
        n = name.lower()
        comps.append({"type": "library", "bom-ref": f"pypi:{n}@{ver}",
                      "name": n, "version": ver, "spec_raw": ln,
                      "scope": "required",
                      "purl": f"pkg:pypi/{n}@{ver}" if ver != "UNPINNED" else f"pkg:pypi/{n}"})
    return comps


def _pip_comp(name, ver, scope, spec_raw):
    n = name.lower()
    comps_kind = (ver != "UNPINNED")
    return {"type": "library", "bom-ref": f"pypi:{n}@{ver}", "name": n,
            "version": ver, "spec_raw": spec_raw, "scope": scope,
            "purl": f"pkg:pypi/{n}@{ver}" if comps_kind else f"pkg:pypi/{n}"}


def parse_pyproject(path):
    """Two layouts, stdlib-regex only:
      PEP 621  [project]  dependencies = ["flask==2.3", "tomli>=2.0", ...]
      Poetry   [tool.poetry.dependencies]  flask = "^2.3"
    Only exact == pins count as pinned; everything else is UNPINNED (DEP-01's
    raw `==` check still decides MEDIUM findings at scan time)."""
    comps = []
    try:
        txt = open(path, encoding="utf-8").read()
    except Exception:
        return comps
    sect = None
    in_arr = None  # "project"|"poetry" once inside a dependencies = [ ... ] array
    for ln in txt.splitlines():
        s = ln.split(" #", 1)[0].strip()
        if not s:
            continue
        if in_arr:  # consuming a multi-line dependencies array
            end = "]" in s
            s = s.split("]", 1)[0]
            for m in re.finditer(r"\"([^\"]+)\"|'([^']+)'", s):
                spec = m.group(1) or m.group(2)
                mm = re.match(r"^([A-Za-z0-9_.\-+]+)(\[.*?\])?\s*(==)([^;,]+)", spec)
                name = re.match(r"^([A-Za-z0-9_.\-+]+)", spec).group(1)
                comps.append(_pip_comp(name, mm.group(4).strip() if mm else "UNPINNED",
                                       "required", spec))
            if end:
                in_arr = None
            continue
        if s.startswith("["):
            sect = s
            continue
        if sect and sect.lower() == "[project]" and re.match(
                r"^(dependencies|optional-dependencies\b.*)\s*=\s*\[", s):
            in_arr = "project" if "]" not in s else None
            for m in re.finditer(r"\"([^\"]+)\"|'([^']+)'", s):
                spec = m.group(1) or m.group(2)
                mm = re.match(r"^([A-Za-z0-9_.\-+]+)(\[.*?\])?\s*(==)([^;,]+)", spec)
                name = re.match(r"^([A-Za-z0-9_.\-+]+)", spec).group(1)
                comps.append(_pip_comp(name, mm.group(4).strip() if mm else "UNPINNED",
                                       "required", spec))
            continue
        m = re.match(r"^([A-Za-z0-9_.\-+]+)\s*=\s*[^=].*$", s)
        if sect and "dependencies" in sect.lower() and m and m.group(1) not in ("name", "version", "python"):
            name = m.group(1).lower()
            vmm = re.match(r'^[A-Za-z0-9_.\-+]+(?:\[.*?\])?\s*=\s*"?==?\s*([^";,\]"]+)', s)
            ver = vmm.group(1).strip() if vmm and "==" in s.split("=", 1)[1].split(",")[0][:3] else "UNPINNED"
            comps.append(_pip_comp(name, ver, "required", s))
    return comps





def parse_gomod(path):
    """Line-based go.mod reader: matches `require x v` and bare `x v` lines
    inside require blocks; skips comments, `module`, `go`, `toolchain`,
    `replace`, `retract` lines. Returns (components, replace_directive_lines)."""
    comps, replaces = [], []
    rx = re.compile(r"^\s*(?:require\s+)?([\w][\w.\-/]*\.\w[\w.\-/]*)\s+(v[\w.\-+=]+)(?:\s*//.*)?$")
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except Exception:
        return comps, replaces
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s or s.startswith("//"):
            continue
        if s.startswith(("module ", "go ", "toolchain ", ")", "(")):
            continue
        if s.startswith("replace ") or s.startswith("retract ") or s == "replace (":
            replaces.append(i)
            continue
        m = rx.match(ln)
        if m:
            name, ver = m.group(1), m.group(2)
            comps.append({"type": "library", "bom-ref": f"golang:{name}@{ver}",
                          "name": name, "version": ver, "scope": "required",
                          "purl": f"pkg:golang/{name}@{ver}"})
    return comps, replaces


def build_sbom(root, name=None, version=None):
    comps, meta = [], {}
    locked = False
    for f in walk_files(root):
        b = os.path.basename(f).lower()
        if b == "package.json" and not locked:
            comps.extend(parse_package_json(f)[0]); meta = parse_package_json(f)[1]; locked = True
        elif b == "requirements.txt":
            comps.extend(parse_requirements(f))
        elif b == "pyproject.toml":
            comps.extend(parse_pyproject(f))
        elif b == "go.mod":
            comps.extend(parse_gomod(f)[0])
    root_name = name or meta.get("name") or os.path.basename(os.path.abspath(root))
    root_ver = version or meta.get("version") or "0.0.0"
    root_ref = f"root:{root_name}@{root_ver}"
    # dedupe by bom-ref — CycloneDX requires refs to be unique, and the same
    # pinned dep can legitimately appear in both requirements.txt and pyproject.
    seen, unique = set(), []
    for c in comps:
        if c["bom-ref"] not in seen and c["bom-ref"] != root_ref:
            seen.add(c["bom-ref"]); unique.append(c)
    return {"bomFormat": "CycloneDX", "specVersion": SPEC, "version": 1,
            "serialNumber": f"urn:uuid:{uuid.uuid4()}",
            "metadata": {"timestamp": now_iso(),
                         "tools": [{"vendor": "orionshaowswmw", "name": "bomscan.py",
                                    "version": RULESET_VERSION}],
                         "component": {"type": "application", "name": root_name,
                                       "version": root_ver, "bom-ref": root_ref}},
            "components": unique,
            "dependencies": [{"ref": root_ref,
                              "dependsOn": [c["bom-ref"] for c in unique]}]}


# ── Verifiable rule engine ───────────────────────────────────────────────────
ABS_OFFSET = 0

def _cli(root, rel, line_no, control, severity, what, remediation):
    return {"rule": _cli.rule_id, "severity": severity, "control_refs": control,
            "title": what, "evidence": {"file": rel, "line": line_no},
            "remediation": remediation}


def scan_rules(root):
    findings = []
    files = walk_files(root)
    txt_files = [f for f in files if os.path.splitext(f)[1].lower() in TEXT_EXT
                 or os.path.basename(f).lower() in ("dockerfile", ".env")]
    # SEC-01 secrets in committed files. Redaction contract: NOT ONE character
    # of the matched value ever leaves the engine — only pattern kind, length,
    # and a sha256 prefix tag (allows operators to correlate identical finds).
    _cli.rule_id = "SEC-01"
    for f in txt_files:
        rel = os.path.relpath(f, root)
        try:
            lines = open(f, encoding="utf-8", errors="replace").read().splitlines()
        except Exception:
            continue
        for i, ln in enumerate(lines, 1):
            if rel.endswith("bomscan.py") or "__pycache__" in rel:
                continue
            for kind, pat in SECRET_PATTERNS:
                m = pat.search(ln)
                if m:
                    v = m.group(0)
                    tag = hashlib.sha256(v.encode()).hexdigest()[:8]
                    findings.append(_cli(
                        root, rel, i,
                        ["OWASP-LLM-2025:LLM02", "OWASP-AGENTIC:AG07"],
                        "HIGH",
                        f"possible {kind} committed [REDACTED len={len(v)} sha256:{tag}]",
                        "revoke and move to a secret manager / 0600 file; purge VCS history"))
                    break
    # DEP-01 unpinned dependencies (supply chain integrity). npm "pinned" means
    # an EXACT x.y.z (npm treats "1.2" as a range); tags/git/file/other schemes
    # are unpinned by construction.
    _cli.rule_id = "DEP-01"
    npm_pinned = re.compile(r"^\d+\.\d+\.\d+$")
    for f in files:
        b = os.path.basename(f).lower(); rel = os.path.relpath(f, root)
        if b == "package.json":
            try:
                d = json.load(open(f, encoding="utf-8"))
                for s in ("dependencies", "devDependencies"):
                    for n, spec in (d.get(s) or {}).items():
                        if not npm_pinned.match(str(spec).strip()):
                            findings.append(_cli(root, rel, 1, ["OWASP-LLM-2025:LLM03", "NIST-SSDF:PW.4"],
                                "MEDIUM", f"unpinned npm spec {n}:{spec}",
                                "pin exact versions + commit package-lock.json"))
            except Exception:
                pass
        elif b == "requirements.txt":
            try:
                rlines = open(f, encoding="utf-8").read().splitlines()
            except Exception:
                continue
            for i, ln in enumerate(rlines, 1):
                s = ln.split(" #", 1)[0].strip()
                if not s or s.startswith(("#", "-c", "-r", "--")):
                    continue
                if "==" not in s:
                    findings.append(_cli(root, rel, i, ["OWASP-LLM-2025:LLM03", "NIST-SSDF:PW.4"],
                        "MEDIUM", f"unpinned pip requirement `{s}`",
                        "use `name==version` + hash-locked requirements"))
        elif b == "pyproject.toml":
            # single source of truth: whatever the SBOM parser could not pin
            try:
                for c in parse_pyproject(f):
                    if c["version"] == "UNPINNED":
                        findings.append(_cli(root, rel, 1, ["OWASP-LLM-2025:LLM03", "NIST-SSDF:PW.4"],
                            "MEDIUM", f"unpinned pyproject dep `{c['spec_raw']}`",
                            "use `name==version` pins"))
            except Exception:
                pass
    # GO-01 go.mod replace/retract directives (local-path fork = supply-chain
    # redirect; retract/version directives themselves are always-pinned, fine)
    _cli.rule_id = "GO-01"
    for f in files:
        if os.path.basename(f).lower() == "go.mod":
            try:
                glines = open(f, encoding="utf-8").read().splitlines()
            except Exception:
                continue
            for i, ln in enumerate(glines, 1):
                s = ln.strip()
                if s.startswith(("replace ", "retract ")) or "=>" in s:
                    findings.append(_cli(root, os.path.relpath(f, root), i,
                        ["OWASP-LLM-2025:LLM03", "NIST-SSDF:PW.4"], "LOW",
                        f"go.mod {s.split()[0] if s else '?'} directive redirects module resolution: `{s[:60]}`",
                        "avoid replace=>local-path in shipped code; document any required fork"))
    # NET-01 declared-vs-actual network boundary drift (when SKILL.md present).
    # Host match is boundary-safe: u == h or u.endswith("." + h) — a declared
    # `example.com` must NOT bless `badexample.com`. Empty/wildcard-only
    # declarations (`*`) collapse to nothing declared (strict, not lax).
    _cli.rule_id = "NET-01"
    skl = None
    for c in ("SKILL.md", "skill.md"):
        p = os.path.join(root, c)
        if os.path.exists(p):
            skl = p; break
    if skl:
        fm_txt = open(skl, encoding="utf-8", errors="replace").read()
        declared = re.findall(r"outbound:\s*\[(.*?)\]", fm_txt, re.S)
        declared_hosts = set()
        for d in declared:
            for h in re.findall(r"[\w.*-]+\.[\w.*-]+", d):
                h = h.replace("*", "").strip().strip(".").lower()
                if h and "." in h:
                    declared_hosts.add(h)
        none_declared = any(not x.strip() for x in declared)
        url_re = re.compile(r"(?:https?|ftps?|sftp|ssh|git|wss?)://"
                            r"([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|\d{1,3}(?:\.\d{1,3}){3})")
        for f in txt_files:
            if os.path.abspath(f) == os.path.abspath(skl):
                continue
            rel = os.path.relpath(f, root)
            try:
                flines = open(f, encoding="utf-8", errors="replace").read().splitlines()
            except Exception:
                continue
            for i, ln in enumerate(flines, 1):
                for u in url_re.findall(ln):
                    ul = u.lower()
                    allowed = (not none_declared) and any(
                        ul == h or ul.endswith("." + h) for h in declared_hosts)
                    if not allowed:
                        findings.append(_cli(root, rel, i, ["OWASP-LLM-2025:LLM06", "OWASP-AGENTIC:AG04"],
                            "MEDIUM", f"undeclared network egress to host `{u}` "
                                      f"(frontmatter declares {sorted(declared_hosts) or 'none'})",
                            "declare it under metadata.network.outbound or remove the call"))
    # MODEL-01 unverified model artifact committed
    _cli.rule_id = "MODEL-01"
    for f in files:
        if os.path.splitext(f)[1].lower() in MODEL_EXT:
            findings.append(_cli(root, os.path.relpath(f, root), 1,
                ["OWASP-LLM-2025:LLM03", "CISA-MIN-ELEMENTS"], "LOW",
                "model artifact in tree — provenance not declared",
                "record source+hash of the model in the SBOM; prefer signed artifacts"))
    # LIC-01 license provenance missing
    _cli.rule_id = "LIC-01"
    if not any(os.path.basename(f).lower() in ("license", "license.md", "license.txt",
                                               "licence", "licence.md", "licence.txt",
                                               "copying")
               for f in files):
        findings.append(_cli(root, ".", 1, ["NIST-SSDF:PS.3", "CISA-MIN-ELEMENTS"], "LOW",
            "no LICENSE file — component usage/reuse rights undocumented",
            "add a LICENSE file and declare it in package metadata"))
    # validate rule registry discipline: every emitted ref must exist
    for f in findings:
        for c in f["control_refs"]:
            assert c in CONTROL_REGISTRY, f"hallucinated control {c!r} — registry discipline broken"
    return findings


def verdict_for(findings, fail_sev):
    sev = SEV_ORDER.index(fail_sev)
    worst = max([SEV_ORDER.index(f["severity"]) for f in findings] + [-1])
    return "FAIL" if worst >= sev else ("WARN" if any(
        SEV_ORDER.index(f["severity"]) >= SEV_ORDER.index("MEDIUM") for f in findings) else "PASS")


# ── audit (hash-chained JSONL) ───────────────────────────────────────────────
def audit_append(target, summary):
    """Hash-chained, keyless tamper-EVIDENCE for the ledger: modification,
    reordering, or in-place forgery of existing records is provable via
    audit --verify; `seq` gives a monotonic index for forensic gap-spotting.
    Hardened write: O_NOFOLLOW (no symlink swaps), mode 0600 set atomically
    via fchmod at create (no looser-perm window).
    LIMITS (documented, honest): an attacker with write+read on this file can
    still truncate the tail or append forged-but-consistent records — the chain
    is keyless. Anchor `tail -1` hashes out-of-band (git notes, CI artifact)
    to bound that. Never expose via AGENT_BOM_AUDIT to a path you don't own."""
    ap = audit_path(target=target)
    entries = audit_read(ap)
    prev = entries[-1]["hash"] if entries else "0" * 64
    rec = {"ts": now_iso(), "seq": len(entries), "target": os.path.abspath(target),
           "ruleset": RULESET_VERSION, "summary": summary, "prev": prev}
    rec["hash"] = hashlib.sha256(json.dumps(rec, separators=(",", ":")).encode()).hexdigest()
    flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    fd = os.open(ap, flags, 0o600)
    try:
        os.fchmod(fd, 0o600)  # also tightens pre-existing looser modes, no race
        os.write(fd, (json.dumps(rec) + "\n").encode("utf-8"))
    finally:
        os.close(fd)


def audit_read(path=None):
    p = path or audit_path()
    if not os.path.exists(p):
        return []
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def audit_verify(path=None):
    bad, prev = [], "0" * 64
    for i, r in enumerate(audit_read(path)):
        h = r.pop("hash", None)
        calc = hashlib.sha256(json.dumps(r, separators=(",", ":")).encode()).hexdigest()
        if r.get("prev") != prev or calc != h:
            bad.append(i)
        prev = h or prev
    return bad


# ── commands ─────────────────────────────────────────────────────────────────
def doctor():
    out = {"schema": "agent_bom.doctor.v1", "python": sys.version.split()[0],
           "spec": f"CycloneDX {SPEC}", "ruleset": RULESET_VERSION,
           "controls": sorted(CONTROL_REGISTRY.items()),
           "supported_manifests": ["package.json", "package-lock.json",
                                   "requirements.txt", "pyproject.toml", "go.mod"]}
    print(json.dumps(out, indent=2))
    return 0


def cmd_sbom(a):
    if not os.path.isdir(a.dir):
        print(f"error: not a directory: {a.dir}", file=sys.stderr); return 3
    bom = build_sbom(a.dir, a.name, a.version)
    txt = json.dumps(bom, indent=2, ensure_ascii=False)
    if a.out:
        try:
            open(a.out, "w", encoding="utf-8").write(txt + "\n")
        except OSError as e:
            print(f"error: cannot write {a.out}: {e.strerror or e}", file=sys.stderr)
            return 3
        print(json.dumps({"schema": "agent_bom.sbom.v1", "out": a.out,
                          "components": len(bom["components"])}))
    else:
        print(txt)
    return 0


def cmd_scan(a):
    if not os.path.isdir(a.dir):
        print(f"error: not a directory: {a.dir}", file=sys.stderr); return 3
    findings = scan_rules(a.dir)
    summ = {s: sum(1 for f in findings if f["severity"] == s) for s in SEV_ORDER}
    verdict = verdict_for(findings, a.fail_severity)
    out = {"schema": "agent_bom.scan.v1", "target": os.path.abspath(a.dir),
           "ruleset": RULESET_VERSION, "summary": summ,
           "verdict": verdict, "fail_severity": a.fail_severity,
           "controls": CONTROL_REGISTRY, "findings": findings}
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 4 if verdict == "FAIL" else 0


def cmd_report(a):
    if not os.path.isdir(a.dir):
        print(f"error: not a directory: {a.dir}", file=sys.stderr); return 3
    bom = build_sbom(a.dir)
    findings = scan_rules(a.dir)
    summ = {s: sum(1 for f in findings if f["severity"] == s) for s in SEV_ORDER}
    verdict = verdict_for(findings, a.fail_severity)
    rep = {"schema": "agent_bom.report.v1", "target": os.path.abspath(a.dir),
           "generated": now_iso(), "ruleset": RULESET_VERSION,
           "sbom": {"components": len(bom["components"]),
                    "entrypoints": ["sbom subcommand regenerates the full CycloneDX 1.5 document"],
                    "serial": bom["serialNumber"]},
           "summary": summ, "verdict": verdict, "fail_severity": a.fail_severity,
           "findings": findings}
    rep["report_sha256"] = hashlib.sha256(
        json.dumps(rep, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    if a.out:
        try:
            open(a.out, "w", encoding="utf-8").write(json.dumps(rep, indent=2, ensure_ascii=False) + "\n")
            open(a.out + ".sbom.json", "w", encoding="utf-8").write(json.dumps(bom, indent=2, ensure_ascii=False) + "\n")
        except OSError as e:
            print(f"error: cannot write {a.out}: {e.strerror or e}", file=sys.stderr)
            return 3
    try:
        audit_append(a.dir, {"verdict": verdict, **summ,
                             "report_sha256": rep["report_sha256"]})
    except OSError as e:
        print(f"warning: audit ledger unwritable ({e.strerror or e}) — this run is unaudited",
              file=sys.stderr)
    out_rep = {"schema": "agent_bom.report.v1", **{k: v for k, v in rep.items() if k != "findings"},
               "findings_total": len(findings)}
    print(json.dumps(out_rep, indent=2, ensure_ascii=False))
    return 4 if verdict == "FAIL" else 0


def cmd_trend(a):
    entries = [r for r in audit_read(audit_path(target=a.dir))
               if r.get("target") == os.path.abspath(a.dir)]
    if len(entries) < 2:
        out = {"schema": "agent_bom.trend.v1", "target": os.path.abspath(a.dir),
               "note": "need >=2 audited runs for this target — run `report` first"}
        print(json.dumps(out, indent=2)); return 0
    pre, cur = entries[-2]["summary"], entries[-1]["summary"]
    def tot(s): return sum(s.get(x, 0) for x in SEV_ORDER)
    delta = {"verdict_prev": pre.get("verdict"), "verdict_now": cur.get("verdict"),
             "open_prev": tot(pre), "open_now": tot(cur), "net": tot(cur) - tot(pre)}
    out = {"schema": "agent_bom.trend.v1", "target": os.path.abspath(a.dir), **delta,
           "direction": "REGRESSED" if delta["net"] > 0 else ("IMPROVED" if delta["net"] < 0 else "UNCHANGED")}
    print(json.dumps(out, indent=2)); return 1 if delta["net"] > 0 else 0


def cmd_audit(a):
    p = audit_path(target=a.dir)
    if a.verify:
        bad = audit_verify(p)
        print(json.dumps({"schema": "agent_bom.audit.v1", "chain_ok": not bad,
                          "entries": len(audit_read(p)), "bad_lines": bad}, indent=2))
        return 0 if not bad else 4
    print(json.dumps({"schema": "agent_bom.audit.v1",
                      "entries": audit_read(p)}, indent=2, ensure_ascii=False))
    return 0


def main():
    ap = argparse.ArgumentParser(prog="bomscan.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("doctor")
    p = sub.add_parser("sbom"); p.add_argument("dir"); p.add_argument("-o", "--out")
    p.add_argument("--name"); p.add_argument("--version")
    p = sub.add_parser("scan"); p.add_argument("dir")
    p.add_argument("--fail-severity", default="HIGH", choices=SEV_ORDER)
    p = sub.add_parser("report"); p.add_argument("dir"); p.add_argument("-o", "--out")
    p.add_argument("--fail-severity", default="HIGH", choices=SEV_ORDER)
    p = sub.add_parser("trend"); p.add_argument("dir")
    p = sub.add_parser("audit"); p.add_argument("dir", default="."); p.add_argument("--verify", action="store_true")
    a = ap.parse_args()
    fn = {"doctor": lambda x: doctor(), "sbom": cmd_sbom, "scan": cmd_scan,
          "report": cmd_report, "trend": cmd_trend, "audit": cmd_audit}[a.cmd]
    try:
        return fn(a)
    except AssertionError as e:   # registry-discipline trip → honest hard stop
        print(f"bomscan internal: {e}", file=sys.stderr); return 2


if __name__ == "__main__":
    sys.exit(main())
