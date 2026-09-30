#!/usr/bin/env python3
"""backup-chain v1.1.1 — fenced, hash-chained workspace backups.

Protocol invariants (argued in references/PROTOCOL.md):
  1. Ordering is asserted, never inferred: a monotonic `generation` integer
     lives in a manifest INSIDE each archive; mtime and filename are claims.
  2. The chain is hash-linked: each manifest records `parent_sha256`.
     Parent resolution: ledger entry first, local manifest second, never filenames.
  3. The ledger lives outside the blast radius: an append-only record of
     `gen=N sha256=HEX parent=HEX built=ISO file=NAME entries=K` lines.
     Adapters: none | file | command. The command adapter runs ONLY the
     operator-configured commands from .vault/config.json, and only when the
     invocation carries --allow-cmd-ledger (argv vectors, never a shell).
     A file ledger whose destination resolves outside the workspace (absolute,
     traversing, or through a planted symlink) runs only when the invocation
     carries --allow-external-ledger: the config may propose, the operator
     disposes. This script itself contains no platform code and makes no
     network calls.
  4. A build is not done until a restore drill passed: extract to staging,
     hash-compare every member against the manifest's member map.
  5. Restore is per-member and verified: never bulk-extract (a failure class
     that exits 0 while writing nothing has been observed twice in production
     environments); stream each member and verify its sha256.
  6. Fencing failures are loud or refused, never silent: unreachable ledger is
     a marked SKIP, an archive older than the ledger head is a refused stale
     handoff.

Witness layer (v1.1) — witnesses, never gates:
  Each generation may carry a compressed decision trace (cot): trigger,
  belief, consciously-accepted risk, falsifier — written at decision time,
  bounded at build time (refusal, never truncation), stored in the manifest,
  and prefix-digested into its ledger line, so the why survives even when the
  archives do not. The ledger also carries two more witness entry types:
  `op=ack gen=N ts=… note=…` (a human saying "I have seen gen N and its drill
  receipt" — written when the operator actually looks, never on a schedule)
  and `event=restore|drill gen=N ts=…` (the consequential custody acts).
  None of these gate anything: a witness disagreement is an alarm, and a
  refusal is a gate; confusing the two teaches users to fix the alarm.
  The standing rule — every control addition must name the blind spot it
  creates, or be refused as control-inflation — lives in
  references/RESIDUAL_RISK.md.

Exit codes: 0 success · 1 failure (gate/verification/drill/mismatch) ·
2 refused (fencing refuse, overwrite without --overwrite, dangerous target).

Python 3.8+, standard library only. No network. Member bytes are hashed and
streamed, never parsed, logged, or transmitted.
"""
import argparse
import fnmatch
import hashlib
import io
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tarfile
import time
from datetime import datetime, timezone

VERSION = "1.1.1"
VAULT = ".vault"
MANIFEST_NAME = "backup-manifest.json"
MARKER_NAME = "backup-chain-dir"
LAST_BUILD = "last_build.json"
DRILL_DIR = "drill"
LEDGER_FILE = "ledger.log"
GEN_RE = re.compile(r"^gen=(\d+)\b", re.M)
SHA_RE = re.compile(r"sha256=([0-9a-f]{64})")
COT_RE = re.compile(r"(?:^|\s)cot=(\S+)")
ACK_RE = re.compile(r"^op=ack\s+gen=(\d+)(?:\s+ts=([^\s]+))?(?:\s+note=(.*))?$")
# Witness-layer budgets. The caps are refusal boundaries, not truncation
# targets: truncation silently edits reasoning, and silent edits are what
# this skill exists to refuse.
COT_TRIGGERS = ("schedule", "pre-migration", "pre-risky-op", "post-heal",
                "manual", "anomaly")
COT_CAPS = {"b": 140, "r": 80, "f": 80}
COT_TOTAL_CAP = 320
COT_DIGEST_LEN = 96
ACK_NOTE_CAP = 120
SECRET_HINTS = ("credential", "creds", "secret", "token", "passwd", "password",
                "private_key", "id_rsa", "id_ed25519", "id_ecdsa", ".pem",
                ".p12", ".keystore", "apikey", "api_key", "auth_header")
DEFAULT_EXCLUDES = ["*.tar.gz", "*.tar.gz.sha256", "*.part"]


class GateError(Exception):
    """Exit 1 — a gate, verification, drill, or restore failure."""


class Refused(Exception):
    """Exit 2 — dangerous or fencing-refused operation."""


def now_iso():
    return datetime.now(timezone.utc).isoformat()[:19] + "Z"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def atomic_write(path, data, binary=False):
    d = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(d, exist_ok=True)
    mode = "wb" if binary else "w"
    tmp = os.path.join(d, "." + os.path.basename(path) + ".tmp")
    with open(tmp, mode) as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def normalize_member(p):
    """Normalize a member path to a safe forward-slash relpath. Refuse escapes."""
    if p.startswith("~"):
        raise Refused(f"member path may not start with '~': {p}")
    parts = [x for x in re.split(r"[\\/]+", p) if x not in ("", ".")]
    if p.startswith("/") or (len(parts) > 0 and ":" in parts[0] and len(parts[0]) <= 2):
        raise Refused(f"member path must be relative to the project root: {p}")
    if any(x == ".." for x in parts):
        raise Refused(f"member path may not contain '..': {p}")
    if not parts:
        raise Refused("empty member path")
    return "/".join(parts)


def validate_archive_names(names):
    """Defence in depth: refuse any archive member that would escape the target.

    Rejects POSIX absolute paths, backslashes, '..' segments, NUL, and
    drive-letter paths (e.g. 'C:/x' or 'C:\\x'). The drive-letter case only
    bites on Windows hosts (os.path.join treats 'C:/x' as absolute there,
    silently dropping --target), but this script may run on one, and a
    restored archive is not necessarily one this script built.
    """
    bad = []
    for n in names:
        first = re.split(r"[\\/]+", n, maxsplit=1)[0]
        if (n.startswith("/") or n.startswith("\\") or "\\" in n
                or ".." in n.split("/") or "\x00" in n
                or (":" in first and len(first) <= 2)):
            bad.append(n)
    if bad:
        raise GateError("archive contains unsafe member paths: " + ", ".join(bad[:5]))


# ---------------------------------------------------------------- config ----

def vault_dir(root):
    return os.path.join(root, VAULT)


def config_path(root):
    return os.path.join(vault_dir(root), "config.json")


def validate_chain_name(name):
    """Audit T09 (round 4): chain_name becomes part of archive FILENAMES
    (<name>-g<N>.tar.gz), so a workspace-contributed config may not use it to
    traverse. Separator-free; spaces/unicode stay legal because init derives
    the default from the workspace basename."""
    if not isinstance(name, str) or not name:
        raise GateError("chain_name is empty — edit .vault/config.json or re-init")
    if len(name) > 128 or "\x00" in name:
        raise GateError(f"chain_name is not a usable filename component: "
                        f"{name[:24]!r}…")
    if "/" in name or "\\" in name or any(x == ".." for x in name.split()):
        raise GateError(f"chain_name may not contain path separators or '..': {name!r}")
    return name


def config_rel_inside(p, what):
    """Audit T09 (round 4): config-supplied filesystem paths (output_dir) must
    stay inside the workspace. Absolute, home-relative, traversing, and empty
    paths are refused; the per-invocation CLI (--output) remains the
    operator's escape hatch for external locations. Returns the normalized
    value, so downstream joins cannot reintroduce separators games."""
    if not isinstance(p, str) or not p.strip():
        raise GateError(f"{what} is empty — edit .vault/config.json or re-init")
    if p.startswith("~"):
        raise GateError(f"{what} may not start with '~': {p!r}")
    parts = [x for x in re.split(r"[\\/]+", p) if x not in ("", ".")]
    if p.startswith("/") or (parts and ":" in parts[0] and len(parts[0]) <= 2):
        raise GateError(f"{what} must be relative to the project root "
                        f"(pass --output for an external location): {p!r}")
    if any(x == ".." for x in parts) or "\x00" in p:
        raise GateError(f"{what} may not traverse outside the project root: {p!r}")
    if not parts:
        raise GateError(f"{what} may not be empty: {p!r}")
    return "/".join(parts)


def load_config(root):
    """Load and RE-VALIDATE .vault/config.json (audit T09, round 4).

    The config is workspace-contributed state — adversarial input, same trust
    class as the ledger command adapter: it may propose, the invocation root
    disposes. The stored root is pinned to the canonical invocation root, and
    every path the config controls (members, chain_name, output_dir) is
    re-validated HERE, not only at 'init'/'member add' time, so a hand-edited
    or planted config cannot redirect what gets read or where archives land.
    """
    p = config_path(root)
    if not os.path.exists(p):
        raise GateError(f"no backup-chain config at {p} — run 'init' first")
    with open(p) as f:
        cfg = json.load(f)
    if cfg.get("protocol") != "backup-chain/1":
        raise GateError(f"unsupported config protocol: {cfg.get('protocol')!r}")
    # Root pin: the stored root must BE this workspace (realpath equality, so
    # symlinked paths to the same workspace still pass). A config claiming a
    # different root would otherwise redirect member collection, output
    # resolution, and ledger paths — collecting files far outside the tree
    # the user selected. If the workspace MOVED, fix 'root' in the config or
    # re-init with --force; neither direction is taken silently.
    stored = cfg.get("root")
    if not isinstance(stored, str) or not stored:
        raise GateError("config has no root — re-init (init --force)")
    root_rp = os.path.realpath(root)
    if os.path.realpath(stored) != root_rp:
        raise GateError(
            "config root is not this workspace: initialized at "
            f"{stored!r}, invoked at {root!r} — a workspace config may not "
            "redirect the backup boundary. If the workspace moved, fix 'root' "
            "in .vault/config.json (or re-init with --force).")
    cfg["root"] = root_rp  # authoritative from here on
    cfg["chain_name"] = validate_chain_name(cfg.get("chain_name"))
    cfg["output_dir"] = config_rel_inside(cfg.get("output_dir"), "output_dir")
    members = cfg.get("members")
    if not isinstance(members, list):
        raise GateError("config members is not a list — edit .vault/config.json")
    for mem in members:
        if not isinstance(mem, dict) or not isinstance(mem.get("path"), str):
            raise GateError("config member without a string path — "
                            "edit .vault/config.json")
        try:
            mem["path"] = normalize_member(mem["path"])
        except Refused as e:
            raise GateError(f"config member rejected: {e}")
    # Audit T09 (round 5): ledger is the last config-controlled sink — validate
    # its SHAPE here (type/emptiness/NUL). Containment is decided at every USE
    # (ledger_state/ledger_append -> ledger_file_path), because the decision
    # depends on a per-invocation flag, not on the config alone.
    led = cfg.get("ledger")
    if led is not None:
        if not isinstance(led, dict):
            raise GateError("config ledger is not an object — edit "
                            ".vault/config.json or re-init")
        lf = led.get("file")
        if lf is not None and (not isinstance(lf, str) or not lf.strip()
                               or "\x00" in lf):
            raise GateError("ledger.file is not a usable path — edit "
                            ".vault/config.json or re-init")
    return cfg


def save_config(root, cfg):
    cfg["protocol"] = "backup-chain/1"
    atomic_write(config_path(root), json.dumps(cfg, indent=2, sort_keys=True) + "\n")
    atomic_write(os.path.join(vault_dir(root), MARKER_NAME),
                 "owned by backup-chain; commands refuse to touch unmarked vaults\n")


def default_config(root, name, output_dir, ledger, ledger_file, read_cmd, append_cmd):
    # init-time validation (audit T09, round 4): the operator's own arguments
    # face the same boundary checks that config re-validation applies later,
    # so an unsafe value can never get INTO the config in the first place.
    try:
        name = validate_chain_name(
            name or os.path.basename(os.path.realpath(root)) or "workspace")
        output_dir = config_rel_inside(output_dir or "download", "output_dir")
    except GateError as e:
        raise Refused(str(e))
    led = {"adapter": ledger or "file"}
    if (ledger or "file") == "file":
        led["file"] = ledger_file or os.path.join(VAULT, LEDGER_FILE)
        if ledger_file:
            cand = (ledger_file if os.path.isabs(ledger_file)
                    else os.path.join(root, ledger_file))
            root_rp = os.path.realpath(root)
            if not (os.path.realpath(cand).startswith(root_rp + os.sep)):
                print(f"WARN  init: ledger file resolves outside the workspace "
                      f"({os.path.realpath(cand)}) — every runtime invocation "
                      f"that touches the ledger will need "
                      f"--allow-external-ledger", file=sys.stderr)
    if (ledger or "file") == "command":
        if not read_cmd or not append_cmd:
            raise Refused("adapter 'command' needs both --read-cmd and --append-cmd")
        led["read_cmd"], led["append_cmd"] = read_cmd, append_cmd
    return {
        "protocol": "backup-chain/1",
        "version": VERSION,
        "chain_name": name,
        "root": os.path.realpath(root),
        "output_dir": output_dir,
        "members": [],
        "exclude": [],
        "ledger": led,
        "created_at": now_iso(),
    }


def output_abs(cfg):
    p = cfg["output_dir"]
    return p if os.path.isabs(p) else os.path.join(cfg["root"], p)


def archive_names_for(cfg):
    base = f"{cfg['chain_name']}-g"
    try:
        files = sorted(os.listdir(output_abs(cfg)))
    except OSError:
        return []
    return [f for f in files if f.startswith(base) and f.endswith(".tar.gz")]


def is_excluded(cfg, rel):
    if rel == VAULT or rel.startswith(VAULT + "/") or rel.startswith(VAULT + "\\"):
        return True
    for pat in DEFAULT_EXCLUDES + list(cfg.get("exclude", [])):
        if fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(os.path.basename(rel), pat):
            return True
    return False


# ---------------------------------------------------------------- ledger ----

def parse_entries(text):
    """Build entries (`gen=…` lines). op=ack and event= lines are witness
    traffic, not build entries: GEN_RE anchors at line start, so they are
    invisible here by construction (and by test)."""
    entries = []
    for line in (text or "").splitlines():
        m = GEN_RE.search(line)
        if not m:
            continue
        e = {"gen": int(m.group(1)), "raw": line.strip()}
        s = SHA_RE.search(line)
        e["sha256"] = s.group(1) if s else None
        c = COT_RE.search(line)
        e["cot"] = c.group(1) if c else None
        entries.append(e)
    return entries


def parse_acks(text):
    """Operator ack lines (`op=ack gen=N ts=… note=…`). The ledger parser
    trusts any line shaped like an entry — same honesty as build entries:
    an ack is a witness, and a forged ack is detectable only as any forged
    ledger text is, by its disagreement with everything else on record."""
    acks = []
    for line in (text or "").splitlines():
        m = ACK_RE.match(line.strip())
        if m:
            acks.append({"gen": int(m.group(1)), "ts": m.group(2) or "",
                         "note": (m.group(3) or "").strip(),
                         "raw": line.strip()})
    return acks


# ----------------------------------------------------- decision traces ----
# The trace is written when the decision is made or it is worthless: a trace
# written later is a narrative with better formatting (doctor_memory's
# receipts-vs-identity argument; katarina_martinity's "the receipt is written
# at decision time"). The manifest copy lives inside the archive, where a
# rollback cannot edit it without breaking hashes; the ledger line carries a
# prefix digest, so the why survives even when the archives do not.

def validate_cot(args):
    """Compose + bound the decision trace from CLI flags. Refuses; never
    truncates. All four flags absent -> None (pre-v1.1 behavior, valid)."""
    t, b = getattr(args, "cot_trigger", None), getattr(args, "cot_belief", None)
    r, f = getattr(args, "cot_risk", None), getattr(args, "cot_falsifier", None)
    if t is None and b is None and r is None and f is None:
        return None
    if t is None:
        raise Refused("--cot-belief/--cot-risk/--cot-falsifier given without "
                      "--cot-trigger — a trace names its trigger")
    if t not in COT_TRIGGERS:
        raise Refused(f"cot trigger must be one of {', '.join(COT_TRIGGERS)}: {t!r}")
    cot = {"t": t, "b": b or "", "r": r or "", "f": f or ""}
    for k, cap in COT_CAPS.items():
        v = cot[k]
        if "\n" in v or "\r" in v or "\x00" in v:
            raise Refused(f"cot {k} must be a single line")
        if len(v) > cap:
            raise Refused(f"cot {k} exceeds {cap} chars ({len(v)}) — shorten the "
                          "trace or split the generation; traces are refused, "
                          "never truncated")
    total = len(cot["b"]) + len(cot["r"]) + len(cot["f"])
    if total > COT_TOTAL_CAP:
        raise Refused(f"cot exceeds {COT_TOTAL_CAP} chars total ({total}) — a trace "
                      "that cannot be read after a wipe is a narrative, not a trace")
    return cot


def cot_canonical(cot):
    """Single-line canonical form the ledger digest prefixes. Whitespace is
    collapsed so a digest survives ledger round-trips through channels that
    wrap or normalize spaces (gists, forum posts, mail)."""
    can = f"t={cot.get('t', '')}|b={cot.get('b', '')}|r={cot.get('r', '')}|f={cot.get('f', '')}"
    return re.sub(r"\s+", " ", can).strip()


def cot_digest(cot):
    """Space-free prefix digest for the ledger line: ledger fields are
    space-separated and every consumer (ours and foreign) keys fields by
    whitespace, so a digest carrying spaces would silently truncate on the
    first word. Whitespace becomes '_' here and in the comparison — the
    manifest keeps the true text; only the ledger copy is normalized."""
    return re.sub(r"\s+", "_", cot_canonical(cot))[:COT_DIGEST_LEN]


def cot_secret_scan(cot):
    blob = " ".join(str(v) for v in (cot or {}).values()).lower()
    return [h for h in SECRET_HINTS if h in blob]


# ------------------------------------------------- ledger command adapter ----
# The command adapter is deliberate, opt-in functionality — config-as-code of
# the git-hook trust class (SECURITY.md). Two audit rounds shaped it:
#   1.0.3 — every execution warns once per command per process, on stderr only
#           (stdout stays clean for JSON consumers and ledger parsing).
#   1.0.4 (audit T09, round 3) — a warning is not consent, and a
#           workspace-contributed config must not fire just because a routine
#           subcommand ran. Execution now requires an explicit per-invocation
#           --allow-cmd-ledger, and commands run as argv vectors (shlex-split,
#           shell=False) — never through a shell. Shell features exist only if
#           the config names `sh -c '…'` itself, in plain sight.
#   1.0.5 (audit T09, round 4) — the same trust boundary moves from WHAT RUNS
#           to WHAT IS READ: a workspace-contributed config could redefine the
#           backup root and collect files far outside the selected project,
#           with output_dir/chain_name steering where the archive lands.
#           load_config now pins the stored root to the canonical invocation
#           root (realpath equality, refuse on mismatch) and re-validates
#           every path the config controls (members, chain_name, output_dir).
#           Config proposes; the invocation root and the operator dispose.
#   1.0.6 (audit T09, round 5) — the boundary closes over the last unvalidated
#           config sink: ledger.file. An append-only ledger is still a write
#           primitive when its destination is attacker-chosen, and a path that
#           resolves outside the workspace (absolute, traversing, or through a
#           planted symlink) now requires the same per-invocation consent class
#           as the command adapter: --allow-external-ledger. In-root ledgers —
#           including symlinked in-root targets — are unaffected; the documented
#           wipe-safety setup (init --ledger-file /external/path) survives, with
#           the operator opting in once per invocation. Resolution is realpath-
#           based at every use, so a symlink swap after approval still fails
#           closed if it leaves the boundary.
_CMD_ADAPTER_WARNED = set()
CMD_LEDGER_ALLOWED = False
EXTERNAL_LEDGER_ALLOWED = False
_EXTERNAL_LEDGER_WARNED = False


def require_cmd_ledger_opt_in():
    """Audit T09 (round 3): refuse to execute config-supplied commands unless
    this process was explicitly launched with --allow-cmd-ledger."""
    if CMD_LEDGER_ALLOWED:
        return
    raise GateError("ledger adapter 'command' refuses to execute without "
                    "explicit per-invocation opt-in — inspect "
                    ".vault/config.json (config is code; see SECURITY.md) "
                    "and re-run with --allow-cmd-ledger")


def warn_cmd_adapter(action, cmd):
    if action in _CMD_ADAPTER_WARNED:
        return
    _CMD_ADAPTER_WARNED.add(action)
    preview = " ".join(str(cmd).split())
    if len(preview) > 100:
        preview = preview[:97] + "…"
    print(f"WARN  ledger command adapter: executing {action} — "
          f"\"{preview}\" (from .vault/config.json; config is code — "
          f"see SECURITY.md)", file=sys.stderr)


def require_external_ledger_opt_in():
    """Audit T09 (round 5): refuse a file-ledger destination that resolves
    outside the workspace unless this process was explicitly launched with
    --allow-external-ledger. Same consent class as the command adapter:
    a warning is not consent, and the config may propose, the operator
    disposes."""
    if EXTERNAL_LEDGER_ALLOWED:
        return
    raise GateError("file ledger resolves outside the workspace — a "
                    "workspace-contributed config may not point ledger "
                    "appends across the boundary; re-run with "
                    "--allow-external-ledger if this destination is "
                    "deliberate (config is code; see SECURITY.md)")


def ledger_file_path(cfg):
    """Resolve the file-ledger destination (audit T09, round 5).

    Returns (path, resolved_realpath, inside_root). The containment verdict
    is REALPATH-based at every use — not cached from load time — so a symlink
    planted (or swapped) after approval still fails closed if it leaves the
    workspace. A relative path is joined to the pinned config root; the
    default destination (<root>/.vault/ledger.log) is in-root by
    construction."""
    led = cfg.get("ledger") or {}
    p = led.get("file") or os.path.join(VAULT, LEDGER_FILE)
    if not isinstance(p, str) or not p.strip() or "\x00" in p:
        raise GateError("ledger.file is not a usable path — edit "
                        ".vault/config.json or re-init")
    p = p if os.path.isabs(p) else os.path.join(cfg.get("root") or ".", p)
    rp = os.path.realpath(p)
    root_rp = os.path.realpath(cfg.get("root") or ".")
    inside = (rp == root_rp or rp.startswith(root_rp + os.sep))
    return p, rp, inside


def warn_external_ledger(rp):
    """Opted-in external ledger use still warns once per process, on stderr
    only — same transparency rule as the command adapter (stdout stays clean
    for JSON consumers and ledger parsing)."""
    global _EXTERNAL_LEDGER_WARNED
    if _EXTERNAL_LEDGER_WARNED:
        return
    _EXTERNAL_LEDGER_WARNED = True
    print(f"WARN  file ledger: destination resolves outside the workspace "
          f"({rp}) — proceeding under --allow-external-ledger",
          file=sys.stderr)


def ledger_state(cfg):
    """Return {reachable, max_gen, entries, note}. Never raises."""
    led = (cfg or {}).get("ledger") or {"adapter": "none"}
    adapter = led.get("adapter", "none")
    note = ""
    try:
        if adapter == "none":
            return {"reachable": False, "max_gen": None, "entries": [],
                    "acks": [],
                    "note": "no ledger configured (adapter 'none') — local-chain fencing only"}
        if adapter == "file":
            p, rp, inside = ledger_file_path(cfg)
            if not inside:
                require_external_ledger_opt_in()
                warn_external_ledger(rp)
            if not os.path.exists(p):
                return {"reachable": True, "max_gen": 0, "entries": [], "acks": [],
                        "note": f"file ledger empty at {p}"}
            with open(p, errors="replace") as f:
                text = f.read()
            entries = parse_entries(text)
            mx = max((e["gen"] for e in entries), default=0)
            return {"reachable": True, "max_gen": mx, "entries": entries,
                    "acks": parse_acks(text),
                    "note": f"file ledger at {p}"}
        if adapter == "command":
            require_cmd_ledger_opt_in()
            warn_cmd_adapter("read_cmd", led["read_cmd"])
            try:
                argv = shlex.split(str(led["read_cmd"]))
            except ValueError as e:
                raise GateError(f"read_cmd is not a valid command line "
                                f"(shlex parse failed): {e}")
            r = subprocess.run(argv, shell=False, capture_output=True,
                               text=True, timeout=120)
            if r.returncode != 0:
                note = f"ledger read command failed (rc={r.returncode}): {r.stderr.strip()[:200]}"
                return {"reachable": False, "max_gen": None, "entries": [],
                        "acks": [], "note": note}
            entries = parse_entries(r.stdout)
            mx = max((e["gen"] for e in entries), default=0)
            return {"reachable": True, "max_gen": mx, "entries": entries,
                    "acks": parse_acks(r.stdout),
                    "note": "command-adapter ledger"}
    except subprocess.TimeoutExpired:
        note = "ledger read command timed out"
    except Exception as e:  # adapter misconfig, shell missing, permissions…
        note = f"ledger unreachable: {e}"
    return {"reachable": False, "max_gen": None, "entries": [], "acks": [], "note": note}


def ledger_append(cfg, line):
    led = cfg.get("ledger") or {"adapter": "none"}
    adapter = led.get("adapter", "none")
    if adapter == "none":
        raise GateError("cannot register: ledger adapter is 'none'")
    if adapter == "file":
        p, rp, inside = ledger_file_path(cfg)
        if not inside:
            require_external_ledger_opt_in()
            warn_external_ledger(rp)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "a") as f:
            f.write(line.rstrip("\n") + "\n")
            f.flush()
            os.fsync(f.fileno())
        return p
    if adapter == "command":
        require_cmd_ledger_opt_in()
        warn_cmd_adapter("append_cmd", led["append_cmd"])
        try:
            argv = shlex.split(str(led["append_cmd"]))
        except ValueError as e:
            raise GateError(f"append_cmd is not a valid command line "
                            f"(shlex parse failed): {e}")
        r = subprocess.run(argv, shell=False, input=line.rstrip("\n") + "\n",
                           capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            raise GateError(f"ledger append command failed (rc={r.returncode}): "
                            f"{r.stderr.strip()[:300]}")
        return led["append_cmd"]
    raise GateError(f"unknown ledger adapter: {adapter}")


def ledger_entry_for(lstate, gen):
    best = None
    for e in lstate.get("entries", []):
        if e["gen"] == gen:
            best = e  # last one wins in an append-only ledger
    return best


def ledger_event(cfg, kind, gen, extra=""):
    """Record a witness event line (`event=<kind> gen=N ts=… …`). Best-effort
    by design: a custody act that already succeeded must not be marked failed
    because its witness hiccuped — the heal-note build covers the gap. Returns
    True when recorded. Events are appended through the SAME adapter path as
    build registrations, so every audit consent boundary (rounds 3–5) applies
    unchanged: a command adapter still needs --allow-cmd-ledger, an external
    file ledger still needs --allow-external-ledger."""
    try:
        led = (cfg or {}).get("ledger") or {}
        if led.get("adapter", "none") == "none":
            return False
        line = f"event={kind} gen={gen} ts={now_iso()}"
        if extra:
            line += f" {extra}"
        ledger_append(cfg, line)
        return True
    except Exception as e:
        print(f"WARN  event not recorded ({kind} gen={gen}): {e}", file=sys.stderr)
        return False


# ------------------------------------------------------------ chain scan ----

def read_manifest(tarball):
    """Read + validate the manifest inside a tarball. None if absent."""
    try:
        with tarfile.open(tarball, "r:gz") as tf:
            names = tf.getnames()
            validate_archive_names(names)
            if MANIFEST_NAME not in names:
                return None
            f = tf.extractfile(MANIFEST_NAME)
            if f is None:
                return None
            m = json.loads(f.read().decode("utf-8"))
    except GateError:
        raise
    except Exception as e:
        raise GateError(f"cannot read archive {tarball}: {e}")
    if not isinstance(m, dict) or not isinstance(m.get("generation"), int):
        raise GateError(f"manifest in {tarball} is malformed (no integer generation)")
    return m


def local_archives(cfg):
    out = []
    for fn in archive_names_for(cfg):
        p = os.path.join(output_abs(cfg), fn)
        try:
            m = read_manifest(p)
        except GateError:
            m = None
        out.append({"path": p, "name": fn, "gen": (m or {}).get("generation")})
    return out


def local_max_gen(cfg, exclude_path=None):
    gens = [a["gen"] for a in local_archives(cfg)
            if a["gen"] is not None
            and (exclude_path is None or os.path.abspath(a["path"]) != os.path.abspath(exclude_path))]
    return max(gens, default=0)


def next_generation(cfg):
    ls = ledger_state(cfg)
    base = local_max_gen(cfg)
    if ls["reachable"] and ls["max_gen"] is not None:
        base = max(base, ls["max_gen"])
        src = "ledger" if ls["max_gen"] >= local_max_gen(cfg) else "local chain"
    else:
        src = "local chain (no ledger)"
    return base + 1, src, ls


def resolve_parent(cfg, gen, lstate):
    """Parent sha for gen-1: ledger first, local manifest second, never filenames."""
    if lstate["reachable"]:
        e = ledger_entry_for(lstate, gen - 1)
        if e and e.get("sha256"):
            return e["sha256"], f"ledger gen={gen - 1} entry"
    for a in sorted(local_archives(cfg), key=lambda x: x["gen"] or -1, reverse=True):
        if a["gen"] == gen - 1:
            return sha256_file(a["path"]), f"local archive {a['name']} (embedded manifest)"
    return None, "NO PARENT RESOLVED (chain head broken — line will omit parent)"


# ---------------------------------------------------------------- members ----

def collect_members(cfg):
    """Expand configured members to {rel: abspath} files + dir list.

    Critical members missing on disk are fatal; non-critical missing members
    warn and are skipped (an archive should still be possible).
    """
    files, dirs, missing = {}, [], []
    # Read boundary (audit T05): nested symlinks are dereferenced ONLY when
    # their resolved target stays inside the project root. The root is
    # canonicalized once; containment is checked with commonpath, never with
    # string prefixes (sibling dirs like /ws vs /ws-alt must not pass).
    root_rp = os.path.realpath(cfg["root"])
    for mem in cfg["members"]:
        rel = mem["path"]
        ab = os.path.join(cfg["root"], rel)
        if not os.path.lexists(ab):
            missing.append(rel)
            if mem.get("critical"):
                raise GateError(f"CRITICAL member missing on disk: {rel} — refusing "
                                "to build an incomplete backup")
            continue
        if os.path.isfile(ab) and not os.path.islink(ab):
            if not is_excluded(cfg, rel):
                files[rel] = ab
            continue
        if os.path.islink(ab):
            print(f"WARN  skipping symlink member: {rel}", file=sys.stderr)
            continue
        for dirpath, dirnames, filenames in os.walk(ab):
            dirnames.sort()
            for d in dirnames:
                dfull = os.path.join(dirpath, d)
                drel = normalize_member(os.path.relpath(dfull, cfg["root"]))
                if is_excluded(cfg, drel):
                    continue
                # Same containment rule as symlinked files just below: os.walk
                # (followlinks=False) never recurses into a symlinked
                # subdirectory either way, so an out-of-root dir-symlink was
                # already contributing no file content — but leaving its NAME
                # as an empty directory placeholder in the archive still
                # contradicts "skipped ... never part of what you selected."
                # Applying the identical realpath+commonpath check here closes
                # that gap; in-root symlinked directories are unaffected.
                if os.path.islink(dfull):
                    rp = os.path.realpath(dfull)
                    try:
                        inside = os.path.commonpath([rp, root_rp]) == root_rp
                    except ValueError:  # different drive (Windows)
                        inside = False
                    if not inside:
                        print(f"WARN  skipping symlinked directory escaping "
                              f"project root: {drel} -> {rp}", file=sys.stderr)
                        continue
                dirs.append(drel)
            for fn in sorted(filenames):
                full = os.path.join(dirpath, fn)
                frel = normalize_member(os.path.relpath(full, cfg["root"]))
                if is_excluded(cfg, frel):
                    continue
                if os.path.islink(full) and not os.path.exists(full):
                    print(f"WARN  skipping broken symlink: {frel}", file=sys.stderr)
                    continue
                # Non-regular files (FIFOs, sockets, devices — including
                # symlinks pointing at them) would hang or crash the hashing
                # step; skip with a warning like any other unrepresentable
                # member. os.path.isfile follows symlinks, so regular files
                # and valid file symlinks (dereferenced at build) pass.
                if not os.path.isfile(full):
                    print(f"WARN  skipping non-regular file: {frel}", file=sys.stderr)
                    continue
                # A nested symlink that resolves outside the project root must
                # not silently pull external bytes into the archive: whatever
                # is backing that link was not part of what the user selected,
                # and an innocuous link name (cache.txt, notes.txt) would carry
                # it past secret_warnings too. Skipped loudly, like any other
                # unrepresentable member. In-root links still dereference.
                if os.path.islink(full):
                    rp = os.path.realpath(full)
                    try:
                        inside = os.path.commonpath([rp, root_rp]) == root_rp
                    except ValueError:  # different drive (Windows)
                        inside = False
                    if not inside:
                        print(f"WARN  skipping symlink escaping project root: "
                              f"{frel} -> {rp}", file=sys.stderr)
                        continue
                files[frel] = full
    return files, dirs, missing


def secret_warnings(files):
    hits = []
    for rel in files:
        base = os.path.basename(rel).lower()
        if any(h in base for h in SECRET_HINTS):
            hits.append(rel)
    return hits


def ledger_line(gen, tarball, parent, member_count, cot_dig=None):
    return (f"gen={gen} sha256={sha256_file(tarball)} "
            f"{f'parent={parent} ' if parent else ''}"
            f"built={now_iso()} file={os.path.basename(tarball)} entries={member_count}"
            f"{f' cot={cot_dig}' if cot_dig else ''}")


# ------------------------------------------------------------------ drill ----

def run_drill(tarball, stage_dir):
    """Extract every manifest member to stage_dir, verify sha256 per member."""
    m = read_manifest(tarball)
    members = (m or {}).get("members") or {}
    if not members:
        raise GateError(f"{tarball}: manifest carries no member map — drill cannot verify")
    shutil.rmtree(stage_dir, ignore_errors=True)
    os.makedirs(stage_dir, exist_ok=True)
    ok = True
    with tarfile.open(tarball, "r:gz") as tf:
        for rel in sorted(members):
            expected = members[rel]
            try:
                f = tf.extractfile(rel)
            except KeyError:
                f = None
            if f is None:
                print(f"FAIL  {rel}: missing from archive")
                ok = False
                continue
            h = hashlib.sha256()
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
            same = h.hexdigest() == expected
            print(f"{'PASS' if same else 'FAIL'}  {rel}: {h.hexdigest()[:16]}…")
            ok = ok and same
    if not ok:
        raise GateError(f"restore drill FAILED — {tarball} is NOT verified recoverable")
    return len(members)


# ------------------------------------------------------------------ build ----

def cmd_build(args, root):
    cfg = load_config(root)
    if not cfg["members"]:
        raise Refused("no members configured — add members before building "
                      "(a chain of empty archives is theatre, not backup)")
    cot = validate_cot(args)  # refuses overflow; never truncates
    outdir = output_abs(cfg)
    os.makedirs(outdir, exist_ok=True)

    # G1: member presence (critical fatal, others warn)
    files, dirs, missing = collect_members(cfg)
    for rel in missing:
        print(f"WARN  non-critical member missing, excluded from build: {rel}",
              file=sys.stderr)
    if not files and not dirs:
        raise GateError("no members resolved on disk — refusing to build an empty archive")

    # G2/G3: generation via fencing (ledger-aware)
    gen, gen_src, lstate = next_generation(cfg)
    parent, parent_src = resolve_parent(cfg, gen, lstate)
    print(f"generation: {gen} (from {gen_src})")
    print(f"parent:     {parent_src}")

    # G4: manifest inside the archive
    manifest = {
        "kind": "backup-chain workspace snapshot",
        "protocol": "backup-chain/1",
        "chain_name": cfg["chain_name"],
        "generation": gen,
        "built_at": now_iso(),
        "parent_sha256": parent,
        "parent_source": parent_src,
        "carries": args.carries or "",
        "member_count": len(files),
        "dir_count": len(dirs),
        "members": {rel: sha256_file(files[rel]) for rel in sorted(files)},
    }
    if cot:
        manifest["cot"] = cot  # decision trace, written at decision time
    if args.output:
        out = args.output
    else:
        # Audit T09 (round 4): a symlinked output_dir would carry the archive
        # bytes outside the workspace even though the configured path looks
        # contained — the same realpath containment the member reader applies.
        out_rp = os.path.realpath(outdir)
        try:
            inside = os.path.commonpath([out_rp, cfg["root"]]) == cfg["root"]
        except ValueError:  # different drives (Windows)
            inside = False
        if not inside:
            raise GateError(f"output_dir resolves outside the project root "
                            f"({outdir} -> {out_rp}) — keep output_dir inside "
                            f"the workspace, or pass --output <path> for this "
                            f"invocation")
        label = args.label or ""
        if label and not re.fullmatch(r"[A-Za-z0-9._-]+", label):
            raise Refused(f"label may only contain [A-Za-z0-9._-]: {label!r}")
        fname = f"{cfg['chain_name']}-g{gen}" + (f"-{label}" if label else "") + ".tar.gz"
        out = os.path.join(outdir, fname)
    out = os.path.abspath(out)
    os.makedirs(os.path.dirname(out), exist_ok=True)

    tmp_out = out + ".part"
    # dereference=True: nested symlinked files WITHIN the project root are
    # hashed by resolved content (see collect_members / SECURITY.md); the
    # archive must store that same resolved content, not a bare symlink
    # entry, or the manifest hash and the archived bytes would refer to two
    # different things and the G8 restore drill would fail on every such
    # member. Out-of-root links never reach this point (containment gate in
    # collect_members).
    with tarfile.open(tmp_out, "w:gz", format=tarfile.GNU_FORMAT, dereference=True) as tf:
        mb = json.dumps(manifest, indent=2, sort_keys=True).encode("utf-8")
        ti = tarfile.TarInfo(MANIFEST_NAME)
        ti.size = len(mb)
        ti.mode = 0o644
        ti.mtime = int(time.time())
        tf.addfile(ti, io.BytesIO(mb))
        for d in sorted(dirs):
            ti = tarfile.TarInfo(d)
            ti.type = tarfile.DIRTYPE
            ti.mode = 0o755
            ti.mtime = int(time.time())
            tf.addfile(ti)
        for rel in sorted(files):
            tf.add(files[rel], arcname=rel, recursive=False)
    os.replace(tmp_out, out)

    # G5/G6: listing + manifest roundtrip
    with tarfile.open(out, "r:gz") as tf:
        names = tf.getnames()
    validate_archive_names(names)
    if MANIFEST_NAME not in names:
        raise GateError("G5 FAIL: manifest missing from archive listing")
    absent = [rel for rel in manifest["members"] if rel not in set(names)]
    if absent:
        raise GateError(f"G5 FAIL: {len(absent)} members missing from archive "
                        f"(first: {absent[0]})")
    rt = read_manifest(out)
    if rt["generation"] != gen or set(rt.get("members") or {}) != set(manifest["members"]):
        raise GateError("G6 FAIL: manifest roundtrip mismatch")
    print(f"G5/G6    listing + manifest roundtrip: OK ({len(names)} entries)")

    # G7: sha256 receipt
    digest = sha256_file(out)
    atomic_write(out + ".sha256", f"{digest}  {os.path.basename(out)}\n")
    print(f"G7       receipt: {digest[:16]}…  ({os.path.basename(out)}.sha256)")

    # G8: restore drill
    stage = os.path.join(vault_dir(cfg["root"]), DRILL_DIR)
    n = run_drill(out, stage)
    print(f"G8       restore drill: PASS ({n} members verified in {stage})")

    atomic_write(os.path.join(vault_dir(cfg["root"]), LAST_BUILD),
                 json.dumps({"generation": gen, "sha256": digest, "path": out,
                             "built_at": manifest["built_at"], "carries": manifest["carries"],
                             "cot": cot, "members": n, "drill": "PASS", "gates": "G1-G8"},
                            indent=2, sort_keys=True) + "\n")

    for rel in secret_warnings(files):
        print(f"SECRET-WARN member looks credential-like: {rel} — archive "
              "distribution is your responsibility (see references/SECURITY.md)",
              file=sys.stderr)
    for hint in cot_secret_scan(cot):
        print(f"SECRET-WARN decision trace mentions {hint!r} — traces are "
              "hashed into manifests and digested into ledgers; keep secrets "
              "out of the trace (see references/SECURITY.md)", file=sys.stderr)

    line = ledger_line(gen, out, parent, len(files),
                       cot_digest(cot) if cot else None)
    print("\n--- LEDGER ENTRY ---")
    print(line)
    if args.register:
        where = ledger_append(cfg, line)
        print(f"registered: {where}")
    else:
        print("(not registered — pass --register or append manually)")
    print(f"\nOK: gen {gen} built and verified recoverable: {out}")
    return 0


# ----------------------------------------------------------------- verify ----

def cmd_verify(args, root):
    cfg = load_config(root)
    tb = os.path.abspath(args.tarball)
    if not os.path.exists(tb):
        raise GateError(f"no such archive: {tb}")
    digest = sha256_file(tb)
    fail = False
    print(f"archive: {os.path.basename(tb)}  sha256={digest[:16]}…")

    rcpt = tb + ".sha256"
    if os.path.exists(rcpt):
        with open(rcpt) as f:
            want = f.read().split()[0]
        same = want == digest
        print(f"receipt: {'MATCH' if same else 'MISMATCH'} ({os.path.basename(rcpt)})")
        fail = fail or not same
    else:
        print("receipt: UNKNOWN (no .sha256 sidecar)")

    m = read_manifest(tb)
    if m is None:
        print("manifest: ABSENT (unversioned archive — legacy or foreign)")
    else:
        print(f"manifest: gen={m['generation']} parent="
              f"{(m.get('parent_sha256') or 'none')[:16]}… members={m.get('member_count')}")
        cot = m.get("cot")
        if cot:
            print(f"trace:   {cot_canonical(cot)}")
        else:
            print("trace:   none recorded (pre-v1.1 generation)")

    ls = ledger_state(cfg)
    print(f"ledger:  {ls['note']}")
    if ls["reachable"] and m is not None:
        e = ledger_entry_for(ls, m["generation"])
        if e is None:
            print(f"ledger:  UNKNOWN (gen {m['generation']} not registered)")
        elif e.get("sha256") is None:
            print("ledger:  UNKNOWN (entry carries no sha256)")
        else:
            same = e["sha256"] == digest
            print(f"ledger:  {'MATCH' if same else 'MISMATCH'} "
                  f"(gen {m['generation']} entry)")
            fail = fail or not same
        # --- witness layer (v1.1): agreement between the two trace copies is
        # evidence; disagreement is an ALARM, not a gate. Refusing here would
        # teach users to fix the alarm instead of investigating it.
        cot = m.get("cot")
        if e is not None and e.get("cot"):
            can_norm = re.sub(r"\s+", "_", cot_canonical(cot)) if cot else ""
            if can_norm.startswith(e["cot"]):
                print("trace:   ledger digest MATCH")
            else:
                print("trace:   ledger digest MISMATCH — manifest trace and "
                      "ledger digest disagree (witness disagreement is an "
                      "alarm; investigate, do not explain away)")
                print("WARN  trace digest mismatch between archive manifest and "
                      "ledger entry — one of them was rewritten", file=sys.stderr)
        acks = [a for a in (ls.get("acks") or []) if a.get("gen") == m["generation"]]
        if acks:
            for a in acks[-3:]:
                print(f"witness:  op=ack ts={a.get('ts', '')}"
                      f"{f' note={a["note"]}' if a.get('note') else ''}")
        else:
            print("witness:  no operator ack on record for this generation")
    elif not ls["reachable"]:
        print("ledger:  SKIPPED (unreachable) — verification is INCOMPLETE, marked")
    if fail:
        raise GateError("verification FAILED — do not trust this archive")
    print("verify: OK (see per-source lines above)")
    return 0


# ------------------------------------------------------------ fencing gates ----

def fencing_check(cfg, tb, lstate=None):
    """The pre-restore gate. Returns the decision dict; never raises for
    decision outcomes (only for unreadable archives).

    lstate may be passed in by a caller that already has a fresh ledger_state
    (e.g. cmd_restore), so a 'command' ledger adapter's read command is not
    invoked twice per restore."""
    try:
        m = read_manifest(tb)
    except GateError:
        raise
    agen = m.get("generation") if m else None
    if lstate is None:
        lstate = ledger_state(cfg) if cfg else {
            "reachable": False, "max_gen": None, "entries": [],
            "note": "no config available (vault absent?) — fencing degraded to local heuristic"}
    lmax = lstate["max_gen"]
    local_head = local_max_gen(cfg) if cfg else 0

    if agen is None:
        if lstate["reachable"]:
            return {"decision": "refuse", "archive_gen": None, "ledger_gen": lmax,
                    "reason": "unversioned archive (no manifest) while the ledger is live "
                              "— provenance unknown"}
        return {"decision": "restore", "archive_gen": None, "ledger_gen": lmax,
                "marked": True,
                "reason": "unversioned archive and no live ledger — mtime heuristic, "
                          "marked (last of the old protocol)"}
    if not lstate["reachable"]:
        if local_head and agen < local_head:
            return {"decision": "refuse", "archive_gen": agen, "ledger_gen": None,
                    "local_head": local_head,
                    "reason": f"stale vs local chain: archive gen {agen} < local head "
                              f"{local_head}; ledger unavailable so this refusal is "
                              "assertable locally"}
        return {"decision": "skip", "archive_gen": agen, "ledger_gen": None,
                "marked": True, "reason": f"ledger unreachable ({lstate['note']}) — "
                f"fencing SKIPPED (marked); archive gen {agen} vs local head {local_head}"}
    if lmax and agen < lmax:
        return {"decision": "refuse", "archive_gen": agen, "ledger_gen": lmax,
                "reason": f"stale handoff: archive gen {agen} < ledger head {lmax}; "
                          "a newer backup existed — heroic retry refused"}
    if agen < local_head:
        return {"decision": "refuse", "archive_gen": agen, "ledger_gen": lmax,
                "local_head": local_head,
                "reason": f"stale vs local chain: archive gen {agen} < local head "
                          f"{local_head} — a newer archive exists locally; refusing "
                          "regardless of ledger state"}
    note = ""
    if lmax and agen > lmax:
        note = " (archive is AHEAD of ledger head — unregistered build?)"
    return {"decision": "restore", "archive_gen": agen, "ledger_gen": lmax,
            "reason": "archive generation is current (>= ledger head)" + note}


def cmd_check(args, root):
    cfg = load_config(root) if os.path.exists(config_path(root)) else None
    tb = os.path.abspath(args.tarball)
    if not os.path.exists(tb):
        raise GateError(f"no such archive: {tb}")
    lstate = ledger_state(cfg) if cfg else None
    d = fencing_check(cfg, tb, lstate)
    print(json.dumps(d, indent=2))
    return 0 if d["decision"] != "refuse" else 2


def cmd_recheck(args, root):
    cfg = load_config(root) if os.path.exists(config_path(root)) else None
    try:
        gen = int(args.gen)
    except ValueError:
        raise Refused(f"GEN must be an integer, got: {args.gen!r}")
    lstate = ledger_state(cfg) if cfg else {"reachable": False, "max_gen": None,
                                            "entries": [], "note": "no config"}
    local_head = local_max_gen(cfg) if cfg else 0
    if lstate["reachable"]:
        if lstate["max_gen"] and gen < lstate["max_gen"]:
            d = {"decision": "stale", "restored_gen": gen, "ledger_gen": lstate["max_gen"],
                 "reason": f"CLEAN-COMPLETING STALE RESTORE: workspace restored to gen "
                           f"{gen} but the ledger remembers {lstate['max_gen']} — bytes "
                           "landed, precondition did not hold"}
        else:
            d = {"decision": "ok", "restored_gen": gen, "ledger_gen": lstate["max_gen"],
                 "reason": "precondition held after apply"}
    else:
        if local_head and gen < local_head:
            d = {"decision": "stale", "restored_gen": gen, "ledger_gen": None,
                 "local_head": local_head,
                 "reason": f"stale vs local chain ({gen} < {local_head})"}
        else:
            d = {"decision": "ok", "restored_gen": gen, "ledger_gen": None,
                 "marked": True,
                 "reason": f"no live ledger ({lstate['note']}) — local-chain check only"}
    print(json.dumps(d, indent=2))
    return 0 if d["decision"] == "ok" else 1


# ----------------------------------------------------------------- restore ----

def cmd_restore(args, root):
    cfg = load_config(root) if os.path.exists(config_path(root)) else None
    tb = os.path.abspath(args.tarball)
    if not os.path.exists(tb):
        raise GateError(f"no such archive: {tb}")
    target = os.path.abspath(args.target)
    if target in ("/", os.path.expanduser("~"), os.path.expanduser("~/")):
        raise Refused(f"refusing dangerous restore target: {target}")
    m = read_manifest(tb)
    members = (m or {}).get("members") or {}
    if not members:
        raise GateError(f"{tb}: no member map in manifest — nothing verifiable to restore")

    # --- fencing gate (skip = loud; refuse = honored unless --force)
    # ledger_state is fetched once here and reused below for the authenticity
    # check, so a 'command' ledger adapter's read command runs only once per
    # restore instead of twice.
    ls = ledger_state(cfg) if cfg else None
    d = fencing_check(cfg, tb, ls)
    print(json.dumps(d, indent=2))
    if d["decision"] == "refuse" and not args.force:
        raise Refused("fencing refused this restore — pass --force only if you have "
                      "independently established that refusing is wrong")
    if d["decision"] == "skip":
        print("!! FENCING SKIPPED (unverified precondition) — proceeding, loudly marked !!",
              file=sys.stderr)
    if d["decision"] == "refuse" and args.force:
        print("!! FENCING OVERRIDE — gate said refuse, proceeding on explicit --force !!",
              file=sys.stderr)

    # --- archive authenticity vs ledger (when the ledger knows this gen)
    if cfg and m is not None and ls is not None:
        e = ledger_entry_for(ls, m["generation"]) if ls["reachable"] else None
        if e and e.get("sha256"):
            same = e["sha256"] == sha256_file(tb)
            print(f"ledger authenticity: {'MATCH' if same else 'MISMATCH'}")
            if not same and not args.force:
                raise Refused("archive sha256 does not match its ledger entry — "
                              "do not restore unauthenticated bytes")

    # --- witness narrative (v1.1): the 3 a.m. operator reads why before
    # healing with it. Context, never a gate — a stale trace is a thing to
    # know, not a thing that blocks a heal.
    if m is not None:
        cot = m.get("cot")
        if cot:
            print(f"trace:    built as: t={cot.get('t')} b={cot.get('b')}")
            if cot.get("r"):
                print(f"trace:    risk consciously accepted: {cot['r']}")
            if cot.get("f"):
                print(f"trace:    falsifier: {cot['f']}")
        else:
            print("trace:    none recorded for this generation (pre-v1.1 archive)")
        if ls is not None and ls.get("reachable"):
            acks = [a for a in (ls.get("acks") or [])
                    if a.get("gen") == m.get("generation")]
            if acks:
                for a in acks[-3:]:
                    print(f"witness:   op=ack ts={a.get('ts', '')}"
                          f"{f' note={a["note"]}' if a.get('note') else ''}")
            else:
                print("witness:   no operator ack on record for this generation")

    # --- target boundary (audit T09): a pre-existing symlinked directory
    # component beneath --target would redirect restore writes outside the
    # selected target (open/os.replace follow directory symlinks). Member
    # name validation cannot see this — the names are clean, the FILESYSTEM
    # is not. Refused unconditionally, like the dangerous-target gate above:
    # --force is a fencing override, not a target-safety override. The fix is
    # manual and deliberate: remove or replace the symlink, or pick another
    # target. The target path itself may be a symlink — the user chose it.
    def _link_component(tpath):
        top = os.path.abspath(target)
        cur = os.path.dirname(os.path.abspath(tpath))
        while cur.startswith(top + os.sep):
            if os.path.islink(cur):
                return cur
            cur = os.path.dirname(cur)
        return None

    checked, escapes = {}, []
    for rel in sorted(members):
        dest = os.path.join(target, rel)
        parent = os.path.dirname(dest)
        if parent not in checked:
            # _link_component examines every component BELOW target and above
            # the final one — i.e. exactly the directories that would carry
            # the write. Passing the parent itself would skip it (dirname
            # strips it first), which is why this takes dest, not parent.
            checked[parent] = _link_component(dest)
        if checked[parent] and checked[parent] not in escapes:
            escapes.append(checked[parent])
    if escapes:
        if args.dry_run:
            for e in escapes[:5]:
                print(f"  WOULD REFUSE: symlinked path component beneath target: {e}")
            print("dry-run: no changes made")
            return 0
        raise Refused(
            f"refusing restore: {len(escapes)} symlinked path component(s) "
            f"beneath --target would redirect writes outside it "
            f"(first: {escapes[0]}) — remove or replace the symlink(s), "
            "or choose another target")

    # --- plan
    restore, already, conflicts = [], [], []
    for rel in sorted(members):
        tpath = os.path.join(target, rel)
        if os.path.islink(tpath):
            # An existing symlink at the final component counts as differing
            # no matter what it currently points at: restore never follows it
            # and never silently replaces it. With --overwrite, os.replace
            # swaps the link itself, not the link target.
            conflicts.append(rel)
        elif os.path.exists(tpath):
            cur = sha256_file(tpath)
            if cur == members[rel]:
                already.append(rel)
            else:
                conflicts.append(rel)
        else:
            restore.append(rel)
    print(f"plan: restore={len(restore)} already-current={len(already)} "
          f"conflicts={len(conflicts)}")
    if args.dry_run:
        # A dry run previews the plan, including conflicts that would need
        # --overwrite for a real restore — it must never itself require
        # --overwrite, or there is no way to preview conflicts before opting in.
        for rel in restore[:20]:
            print(f"  would restore: {rel}")
        if len(restore) > 20:
            print(f"  … and {len(restore) - 20} more")
        for rel in conflicts[:20]:
            print(f"  would need --overwrite (differs locally): {rel}")
        if len(conflicts) > 20:
            print(f"  … and {len(conflicts) - 20} more conflicts")
        print("dry-run: no changes made")
        return 0
    if conflicts and not args.overwrite:
        raise Refused(f"{len(conflicts)} existing files differ from the archive "
                      f"(first: {conflicts[0]}) — pass --overwrite to replace them")
    if conflicts and args.overwrite:
        restore = sorted(set(restore) | set(conflicts))

    # --- per-member, verified (NEVER bulk extraction)
    ok = failed = 0
    with tarfile.open(tb, "r:gz") as tf:
        for rel in restore:
            tpath = os.path.join(target, rel)
            os.makedirs(os.path.dirname(tpath) or target, exist_ok=True)
            try:
                f = tf.extractfile(rel)
            except KeyError:
                f = None
            if f is None:
                print(f"FAIL  {rel}: missing from archive")
                failed += 1
                continue
            tmp = tpath + ".restore-part"
            h = hashlib.sha256()
            with open(tmp, "wb") as w:
                for chunk in iter(lambda: f.read(1 << 20), b""):
                    h.update(chunk)
                    w.write(chunk)
                w.flush()
                os.fsync(w.fileno())
            if h.hexdigest() != members[rel]:
                print(f"FAIL  {rel}: sha256 mismatch after extraction")
                os.unlink(tmp)
                failed += 1
                continue
            os.replace(tmp, tpath)
            ok += 1
    for rel in already:
        print(f"SKIP  {rel}: already current")
    if conflicts:
        print(f"OVERWRITE: {len(conflicts)} conflicting files replaced")
    print(f"restored: {ok} verified · {failed} failed · {len(already)} already-current")
    if failed:
        raise GateError(f"restore INCOMPLETE: {failed} members failed verification — "
                        "workspace is NOT fully healed; investigate before proceeding")

    gen = m["generation"] if m else None
    if gen is not None:
        if cfg is not None and ledger_event(
                cfg, "restore", gen,
                extra=f"target={os.path.basename(os.path.normpath(target))}"):
            print("event:    restore recorded in ledger")
        rc = cmd_recheck(argparse.Namespace(gen=str(gen)), root)
        return rc
    print("recheck: SKIPPED (unversioned archive)")
    return 0


def cmd_drill(args, root):
    """Standalone drill + witness event. (The build-time G8 drill does not
    append an event: the build's own ledger line and last_build receipt are
    already witnesses of it, and a second line would be ceremony.)"""
    tb = os.path.abspath(args.tarball)
    m = read_manifest(tb)
    gen = m.get("generation") if m else None
    n = run_drill(tb, os.path.join(vault_dir(root), DRILL_DIR))
    cfg = load_config(root)
    if gen is not None and ledger_event(cfg, "drill", gen):
        print(f"event:    drill recorded in ledger (gen {gen})")
    return 0


# ------------------------------------------------------------------ status ----

def cmd_status(args, root):
    cfg = load_config(root)
    print(f"chain:    {cfg['chain_name']}  (root: {cfg['root']})")
    print(f"output:   {output_abs(cfg)}")
    ls = ledger_state(cfg)
    print(f"ledger:   {ls['note']}"
          + (f"  head={ls['max_gen']}" if ls["reachable"] and ls["max_gen"] else ""))
    acks = ls.get("acks") or []
    if acks:
        print(f"acks:     {len(acks)} operator acknowledgment(s) on record")
        for a in acks[-5:]:
            print(f"  op=ack gen={a['gen']} ts={a.get('ts', '')}"
                  f"{f' note={a["note"]}' if a.get('note') else ''}")
    print(f"members:  {len(cfg['members'])} configured")
    for mem in cfg["members"]:
        exists = os.path.exists(os.path.join(cfg["root"], mem["path"]))
        print(f"  {'x' if not exists else ' '} {'[critical]' if mem.get('critical') else '          '} {mem['path']}")
    files, _, _ = collect_members(cfg)
    for rel in secret_warnings(files):
        print(f"  SECRET-WARN {rel}")
    archs = local_archives(cfg)
    if archs:
        print("local chain (embedded manifest gens; filename is a label):")
        for a in sorted(archs, key=lambda x: x["gen"] if x["gen"] is not None else -1):
            print(f"  gen={a['gen'] if a['gen'] is not None else '??':>4}  {a['name']}")
        head = max((a["gen"] for a in archs if a["gen"] is not None), default=None)
        print(f"local head: gen {head}")
    else:
        print("local chain: empty")
    lb = os.path.join(vault_dir(root), LAST_BUILD)
    if os.path.exists(lb):
        with open(lb) as f:
            b = json.load(f)
        print(f"last build: gen {b.get('generation')} drill={b.get('drill')} "
              f"members={b.get('members')} carries={b.get('carries', '')[:60]}")
        cot = b.get("cot")
        if cot:
            print(f"  trace: {cot_canonical(cot)}")
    return 0


# ------------------------------------------------------------- init/members ----

def cmd_init(args, root):
    if os.path.exists(config_path(root)) and not args.force:
        raise Refused(f"config already exists at {config_path(root)} — "
                      "pass --force to overwrite deliberately")
    cfg = default_config(root, args.name, args.output_dir, args.ledger,
                         args.ledger_file, args.read_cmd, args.append_cmd)
    os.makedirs(vault_dir(root), exist_ok=True)
    if (cfg["ledger"]["adapter"] == "file"):
        lp = cfg["ledger"]["file"]
        if not os.path.isabs(lp):
            lp = os.path.join(root, lp)
        os.makedirs(os.path.dirname(lp), exist_ok=True)
        if not os.path.exists(lp):
            atomic_write(lp, "")
    save_config(root, cfg)
    print(f"initialized chain '{cfg['chain_name']}' at {root}")
    print(f"ledger:   {cfg['ledger']['adapter']}"
          + (f" ({cfg['ledger'].get('file')})" if cfg["ledger"]["adapter"] == "file" else ""))
    if cfg["ledger"]["adapter"] == "file":
        print("NOTE: a file ledger inside the workspace is NOT wipe-safe — for real "
              "protection use --ledger-file pointing outside this machine, or a "
              "command adapter over any append-only channel you have.")
    print("next:")
    print("  member add <path> [--critical]   # repeat for everything whose loss hurts")
    print("  build --carries \"what this generation holds\" --register")
    return 0


def cmd_member(args, root):
    cfg = load_config(root)
    if args.action == "list":
        for mem in cfg["members"]:
            print(f"{'[critical] ' if mem.get('critical') else '           '}{mem['path']}")
        return 0
    if not args.path:
        raise Refused(f"'member {args.action}' needs a PATH argument")
    rel = normalize_member(args.path)
    if args.action == "add":
        if not os.path.exists(os.path.join(root, rel)):
            raise GateError(f"path does not exist (add members that exist so --critical "
                            f"means something): {rel}")
        for mem in cfg["members"]:
            if mem["path"] == rel:
                print(f"already a member: {rel}")
                return 0
        cfg["members"].append({"path": rel, "critical": bool(args.critical)})
        cfg["members"].sort(key=lambda m: m["path"])
        print(f"member added: {rel}" + ("  [critical]" if args.critical else ""))
    elif args.action == "remove":
        before = len(cfg["members"])
        cfg["members"] = [m for m in cfg["members"] if m["path"] != rel]
        if len(cfg["members"]) == before:
            print(f"not a member: {rel}")
            return 0
        print(f"member removed: {rel}")
    save_config(root, cfg)
    return 0


def cmd_next_gen(args, root):
    cfg = load_config(root)
    gen, src, _ = next_generation(cfg)
    print(f"{gen}  # from {src}")
    return 0


def cmd_ledger_line(args, root):
    cfg = load_config(root)
    tb = os.path.abspath(args.tarball)
    m = read_manifest(tb)
    gen = m.get("generation") if m else None
    if gen is None:
        raise GateError("archive has no manifest — cannot compose a ledger line")
    parent, psrc = resolve_parent(cfg, gen, ledger_state(cfg))
    if m.get("parent_sha256") and not parent:
        parent = m["parent_sha256"]
        psrc = "archive manifest (fallback)"
    if m.get("parent_sha256") and parent and parent != m["parent_sha256"]:
        print(f"WARN  resolved parent differs from manifest parent "
              f"({parent[:12]}… vs {m['parent_sha256'][:12]}…)", file=sys.stderr)
    cot = m.get("cot")
    line = ledger_line(gen, tb, parent, len(m.get("members") or {}),
                       cot_digest(cot) if cot else None)
    print(line)
    print(f"parent source: {psrc}")
    if args.append:
        where = ledger_append(cfg, line)
        print(f"appended: {where}")
    return 0


def cmd_ack(args, root):
    """Operator acknowledgment — the human witness. Written when the operator
    actually looks, never on a schedule; attests the looking, not the
    believing. A witness, not a gate: nothing is refused for lack of an ack."""
    cfg = load_config(root)
    try:
        gen = int(args.gen)
    except ValueError:
        raise Refused(f"GEN must be an integer, got: {args.gen!r}")
    if gen <= 0:
        raise Refused(f"GEN must be a positive integer, got: {gen}")
    note = args.note or ""
    if "\n" in note or "\r" in note or "\x00" in note:
        raise Refused("ack note must be a single line")
    if len(note) > ACK_NOTE_CAP:
        raise Refused(f"ack note exceeds {ACK_NOTE_CAP} chars ({len(note)}) — "
                      "witnesses stay small")
    if (cfg.get("ledger") or {}).get("adapter", "none") == "none":
        raise Refused("no ledger configured — an ack needs a witness layer to "
                      "live in (adapter 'none' has none)")
    ls = ledger_state(cfg)
    if not ls["reachable"]:
        raise GateError(f"ledger unreachable — cannot ack what cannot be seen "
                        f"({ls['note']})")
    known = ledger_entry_for(ls, gen) is not None or any(
        a.get("gen") == gen for a in local_archives(cfg))
    if not known:
        raise Refused(f"gen {gen} is unknown to the ledger and the local chain — "
                      "an ack witnesses something; there is nothing here to witness")
    line = f"op=ack gen={gen} ts={now_iso()}" + (f" note={note}" if note else "")
    where = ledger_append(cfg, line)
    print(line)
    print(f"acknowledged: gen {gen} ({where})")
    print("witness, not gate: future commands do not require this ack")
    return 0


# -------------------------------------------------------------------- main ----

def main(argv=None):
    global CMD_LEDGER_ALLOWED, EXTERNAL_LEDGER_ALLOWED
    ap = argparse.ArgumentParser(
        prog="backup_chain",
        description="Fenced, hash-chained workspace backups (protocol invariants in "
                    "references/PROTOCOL.md). No network; off-site distribution is yours.")
    ap.add_argument("--root", default=".",
                    help="project root (default: cwd; config at <root>/.vault/config.json)")
    ap.add_argument("--version", action="version", version=f"backup-chain {VERSION}")
    # Shared guard (audit T09, round 3): every subcommand accepts the explicit
    # per-invocation opt-in that the command-ledger adapter requires to run.
    guard = argparse.ArgumentParser(add_help=False)
    guard.add_argument("--allow-cmd-ledger", action="store_true",
                       help="opt in to executing the command-ledger adapter from "
                            ".vault/config.json for THIS invocation (refused "
                            "without it; file/none ledgers unaffected)")
    # Shared guard (audit T09, round 5): same consent class for a file-ledger
    # destination that resolves outside the workspace (absolute, traversing,
    # or through a planted symlink). In-root ledgers never consult it.
    guard.add_argument("--allow-external-ledger", action="store_true",
                       help="opt in to a file-ledger destination outside the "
                            "workspace for THIS invocation (refused without it; "
                            "in-root ledgers unaffected)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="initialize a chain in the project root",
                       parents=[guard])
    p.add_argument("--name"); p.add_argument("--output-dir")
    p.add_argument("--ledger", choices=["none", "file", "command"], default="file")
    p.add_argument("--ledger-file"); p.add_argument("--read-cmd"); p.add_argument("--append-cmd")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_init)

    p = sub.add_parser("member", help="add/remove/list chain members",
                       parents=[guard])
    p.add_argument("action", choices=["add", "remove", "list"])
    p.add_argument("path", nargs="?")
    p.add_argument("--critical", action="store_true")
    p.set_defaults(fn=cmd_member)

    p = sub.add_parser("next-gen", help="print next generation (max(local, ledger)+1)",
                       parents=[guard])
    p.set_defaults(fn=cmd_next_gen)

    p = sub.add_parser("build", help="gated build: presence → manifest → roundtrip → "
                                     "receipt → drill", parents=[guard])
    p.add_argument("--carries", help="free-text note on what this generation holds")
    p.add_argument("--cot-trigger", help="decision trace trigger (v1.1): one of "
                                         + ", ".join(COT_TRIGGERS))
    p.add_argument("--cot-belief", help="decision trace: what was believed about "
                                         "workspace state at build time (≤140 chars)")
    p.add_argument("--cot-risk", help="decision trace: risk consciously accepted "
                                       "(≤80 chars)")
    p.add_argument("--cot-falsifier", help="decision trace: one checkable claim that, "
                                           "if false, indicts this generation's "
                                           "reasoning (≤80 chars)")
    p.add_argument("--label", help="optional filename label: <name>-g<GEN>-<label>.tar.gz")
    p.add_argument("--register", action="store_true", help="append the ledger line")
    p.add_argument("--output", help="override output path")
    p.set_defaults(fn=cmd_build)

    p = sub.add_parser("ledger-line", help="print (or append) the ledger entry",
                       parents=[guard])
    p.add_argument("tarball"); p.add_argument("--append", action="store_true")
    p.set_defaults(fn=cmd_ledger_line)

    p = sub.add_parser("verify", help="sha256 vs receipt and ledger entry",
                       parents=[guard])
    p.add_argument("tarball")
    p.set_defaults(fn=cmd_verify)

    p = sub.add_parser("drill", help="standalone restore drill (extract + hash-verify; "
                                     "records a witness event)",
                       parents=[guard])
    p.add_argument("tarball")
    p.set_defaults(fn=cmd_drill)

    p = sub.add_parser("ack", help="operator acknowledgment appended to the ledger "
                                   "(v1.1 witness — never a gate)", parents=[guard])
    p.add_argument("gen", help="generation being acknowledged (must be known to "
                               "ledger or local chain)")
    p.add_argument("note", nargs="?", help=f"optional single-line note (≤{ACK_NOTE_CAP} chars)")
    p.set_defaults(fn=cmd_ack)

    p = sub.add_parser("check", help="pre-restore fencing gate → JSON",
                       parents=[guard])
    p.add_argument("tarball")
    p.set_defaults(fn=cmd_check)

    p = sub.add_parser("restore", help="per-member verified restore into --target",
                       parents=[guard])
    p.add_argument("tarball")
    p.add_argument("--target", required=True)
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_restore)

    p = sub.add_parser("recheck", help="post-apply receipt → JSON",
                       parents=[guard])
    p.add_argument("gen")
    p.set_defaults(fn=cmd_recheck)

    p = sub.add_parser("status", help="chain state: members, local head, ledger head",
                       parents=[guard])
    p.set_defaults(fn=cmd_status)

    args = ap.parse_args(argv)
    CMD_LEDGER_ALLOWED = bool(getattr(args, "allow_cmd_ledger", False))
    EXTERNAL_LEDGER_ALLOWED = bool(getattr(args, "allow_external_ledger", False))
    root = os.path.abspath(args.root)
    try:
        return args.fn(args, root)
    except Refused as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        return 2
    except GateError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
