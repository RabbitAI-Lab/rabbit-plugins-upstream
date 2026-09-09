#!/usr/bin/env python3
"""kaggle_dock.py — run the hPL docking stack on Kaggle's free CPU/GPU kernels.

Machine-readable contract (agents: read this, do not improvise):

  COMMANDS
    check    verify credentials + API reachability            exit 0 = usable
    push     upload a self-contained docking kernel and start it
    status   poll kernel run state                            exit 0 = complete
    fetch    download kernel output into a local directory
    run      push + poll to completion + fetch (one shot)

  EXIT CODES (stable, machine-checkable)
    0 ok · 2 bad-usage · 3 auth-failure · 4 kernel-error · 5 timeout · 6 quota

  Every command prints exactly one JSON object to stdout as its LAST line:
    {"ok": bool, "cmd": str, "exit": int, ...}
  Parse that line. Human-readable progress goes to stderr.

Credentials are resolved in this order (first hit wins) — this list matches the
code in resolve_credentials(); explicit input always beats an ambient file:
  1. --username/--key flags
  2. $KAGGLE_USERNAME + $KAGGLE_KEY
  3. --creds FILE pointing at a JSON with providers.kaggle
     {"providers":{"kaggle":{"username","api_key","accounts":[{...}]}}}
     With (3) the --account N flag selects a rotation slot (0 = primary).
  4. $KAGGLE_CONFIG_DIR/kaggle.json  or  ~/.kaggle/kaggle.json  {"username","key"}

Why this exists: Vina is CPU-bound. Kaggle gives 4 vCPU / ~30 GB RAM CPU kernels
with a 12 h ceiling and no weekly cap, which is the right free tier for docking.
GPU is NOT required and NOT recommended (Vina does not use CUDA); --gpu only
exists for users who add a GPU rescoring step of their own.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
import time
from pathlib import Path

EXIT_OK, EXIT_USAGE, EXIT_AUTH, EXIT_KERNEL, EXIT_TIMEOUT, EXIT_QUOTA = 0, 2, 3, 4, 5, 6


# Flags a caller may forward to multi_site_docking.py inside the kernel.
# An allow-list rather than a block-list: anything not named here is refused,
# so a future flag cannot silently become an injection vector.
ALLOWED_EXTRA_FLAGS = {
    "--receptor-model", "--exhaustiveness", "--n-seeds", "--n-poses", "--seed",
    "--cpu-per-dock", "--max-mw", "--max-rotb", "--protonation", "--limit",
    "--sites-file", "--receptor", "--debug",
}


def parse_extra_flags(raw: str) -> list:
    """Tokenise --extra safely and reject anything outside the allow-list.

    The kernel runs this list with shell=False, so shell metacharacters are
    already inert; this is the second layer. Without it, a caller could pass
    `; rm -rf / #` and — before the shell=False fix — have it executed in the
    Kaggle kernel. Rejecting loudly beats silently dropping tokens.
    """
    import shlex
    if not raw or not raw.strip():
        return []
    try:
        toks = shlex.split(raw)
    except ValueError as e:
        emit(False, "extra", EXIT_USAGE, error=f"could not parse --extra: {e}")
    for t in toks:
        if t.startswith("-") and t.split("=", 1)[0] not in ALLOWED_EXTRA_FLAGS:
            emit(False, "extra", EXIT_USAGE,
                 error=f"flag not permitted in --extra: {t}",
                 allowed=sorted(ALLOWED_EXTRA_FLAGS))
        if not t.startswith("-") and any(c in t for c in ";|&`$><\n"):
            emit(False, "extra", EXIT_USAGE,
                 error=f"illegal character in --extra value: {t!r}")
    return toks


def slugify(title: str) -> str:
    """Reproduce Kaggle's title->slug rule.

    GOTCHA (verified live, 2026-09): Kaggle derives the kernel slug from the
    TITLE, not from the `id` you put in kernel-metadata.json. Push
    id=".../hpl-dock-verify-v101" with title="hPL docking verify v101" and the
    kernel is actually created at ".../hpl-docking-verify-v101" — every later
    kernels_status(id) then fails with "Permission 'kernels.get' was denied",
    which looks like an auth error but is a slug mismatch. We therefore always
    derive the slug from the title and keep the two consistent.
    """
    s = "".join(c.lower() if c.isalnum() else "-" for c in title)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")[:50]


def emit(ok: bool, cmd: str, code: int, **kw):
    """Print the single machine-readable result line and exit."""
    payload = {"ok": ok, "cmd": cmd, "exit": code}
    payload.update(kw)
    print(json.dumps(payload, default=str))
    sys.exit(code)


def log(msg: str):
    print(f"[kaggle_dock] {msg}", file=sys.stderr, flush=True)


# ── credentials ──────────────────────────────────────────────────────────────
def resolve_credentials(args) -> tuple[str, str, str]:
    """Return (username, key, source). Never logs the key."""
    if args.username and args.key:
        return args.username, args.key, "flags"
    if os.environ.get("KAGGLE_USERNAME") and os.environ.get("KAGGLE_KEY"):
        return os.environ["KAGGLE_USERNAME"], os.environ["KAGGLE_KEY"], "env"
    if args.creds:
        p = Path(args.creds).expanduser()
        if not p.exists():
            emit(False, "creds", EXIT_AUTH, error=f"--creds file not found: {p}")
        blob = json.loads(p.read_text())
        kag = blob.get("providers", {}).get("kaggle", blob.get("kaggle", blob))
        pool = []
        if kag.get("username"):
            pool.append({"username": kag["username"],
                         "key": kag.get("api_key") or kag.get("key")})
        for a in kag.get("accounts", []):
            pool.append({"username": a.get("username"),
                         "key": a.get("api_key") or a.get("key")})
        pool = [a for a in pool if a["username"] and a["key"]]
        if not pool:
            emit(False, "creds", EXIT_AUTH, error="no usable kaggle accounts in --creds")
        idx = args.account % len(pool)
        return pool[idx]["username"], pool[idx]["key"], f"creds[{idx}]"
    for cand in (Path(os.environ.get("KAGGLE_CONFIG_DIR", "~/.kaggle")).expanduser() / "kaggle.json",
                 Path("~/.kaggle/kaggle.json").expanduser()):
        if cand.exists():
            blob = json.loads(cand.read_text())
            if blob.get("username") and blob.get("key"):
                return blob["username"], blob["key"], str(cand)
    emit(False, "creds", EXIT_AUTH,
         error="no credentials: pass --username/--key, set KAGGLE_USERNAME/KAGGLE_KEY, "
               "or provide --creds with providers.kaggle")


def kaggle_api(username: str, key: str):
    """Authenticate and return the Kaggle API client (import is deferred: the
    kaggle package reads env vars at import time)."""
    os.environ["KAGGLE_USERNAME"] = username
    os.environ["KAGGLE_KEY"] = key
    for mod in [m for m in list(sys.modules) if m.startswith("kaggle")]:
        del sys.modules[mod]
    try:
        import kaggle  # noqa: E402
    except ImportError:
        emit(False, "auth", EXIT_AUTH,
             error="kaggle package missing — run: pip install kaggle")
    try:
        kaggle.api.authenticate()
        return kaggle.api
    except Exception as e:  # noqa: BLE001
        emit(False, "auth", EXIT_AUTH, error=f"authenticate failed: {e}")


# ── the kernel script that actually runs on Kaggle ───────────────────────────
KERNEL_TEMPLATE = r'''#!/usr/bin/env python3
"""Auto-generated by kaggle_dock.py — hPL multi-site docking on a Kaggle kernel.

Runs entirely offline-capable except for the conda/pip install step, so the
kernel MUST be pushed with enable_internet=true.
"""
import base64, io, json, os, subprocess, sys, time, zipfile
from pathlib import Path

T0 = time.time()
WORK = Path("/kaggle/working")
STACK = WORK / "docking_professional_stack"

def sh(cmd, **kw):
    print(f"$ {cmd}", flush=True)
    return subprocess.run(cmd, shell=True, check=False,
                          capture_output=True, text=True, **kw)

# 1) unpack the stack shipped inside this script (no external dataset needed)
print("== unpacking docking stack ==", flush=True)
zipfile.ZipFile(io.BytesIO(base64.b64decode(STACK_B64))).extractall(WORK)
assert (STACK / "multi_site_docking.py").exists(), "stack unpack failed"

# 2) ligands shipped inline too
(WORK / "ligands.csv").write_text(base64.b64decode(LIGANDS_B64).decode())
print((WORK / "ligands.csv").read_text()[:500], flush=True)

# 3) toolchain. micromamba is the fastest reliable route to vina+rdkit+meeko.
print("== installing toolchain (micromamba) ==", flush=True)
r = sh("curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest "
       "| tar -xvj -C /kaggle/working bin/micromamba")
MM = "/kaggle/working/bin/micromamba"
if not Path(MM).exists():
    print("FATAL: micromamba download failed — is internet enabled on this kernel?")
    print(r.stdout[-2000:], r.stderr[-2000:])
    sys.exit(4)
env = "/kaggle/working/plenv"
r = sh(f"{MM} create -y -p {env} -c conda-forge python=3.11 "
       f"rdkit meeko vina gemmi openbabel numpy scipy pytest 2>&1 | tail -5")
print(r.stdout[-3000:], flush=True)
PY = f"{env}/bin/python"
if not Path(PY).exists():
    print("FATAL: env creation failed"); print(r.stdout[-4000:]); sys.exit(4)

# 4) preflight — never dock against a broken env
print("== preflight ==", flush=True)
r = sh(f"cd {STACK} && PATH={env}/bin:$PATH {PY} multi_site_docking.py --check")
print(r.stdout[-3000:], r.stderr[-1500:], flush=True)
if r.returncode != 0:
    print("FATAL: preflight failed"); sys.exit(4)

# 5) dock
print(f"== docking (precision={PRECISION}, workers={WORKERS}) ==", flush=True)
out = WORK / "dock_results"
# Argument list + shell=False: EXTRA_FLAGS is a pre-tokenised list, so nothing
# in it can be interpreted as shell syntax (no ;, &&, backticks, redirects).
cmd = [PY, "multi_site_docking.py",
       "--ligands", f"{WORK}/ligands.csv", "--precision", PRECISION,
       "--workers", str(WORKERS), "--outdir", str(out)] + list(EXTRA_FLAGS)
print("$ " + " ".join(cmd), flush=True)
_env = dict(os.environ, PATH=f"{env}/bin:" + os.environ.get("PATH", ""))
r = subprocess.run(cmd, cwd=str(STACK), env=_env, capture_output=True, text=True)
print(r.stdout[-6000:], flush=True)
print(r.stderr[-3000:], flush=True)
rc = r.returncode

# 6) validate + summarize
res = out / "results_all_sites.csv"
if res.exists():
    v = sh(f"cd {STACK} && PATH={env}/bin:$PATH {PY} validate_results.py --results {res}")
    print(v.stdout[-3000:], flush=True)
    import csv
    rows = list(csv.DictReader(open(res)))
    print(f"== {len(rows)} result rows ==", flush=True)
    for row in rows[:40]:
        print("  ", row.get("name"), row.get("site"), row.get("score"), flush=True)

summary = {
    "ok": rc == 0 and res.exists(),
    "returncode": rc,
    "elapsed_s": round(time.time() - T0, 1),
    "results_csv": str(res) if res.exists() else None,
    "n_rows": len(rows) if res.exists() else 0,
}
(WORK / "kaggle_dock_summary.json").write_text(json.dumps(summary, indent=2))
print("SUMMARY " + json.dumps(summary), flush=True)

# Keep outputs small. Everything below is either re-derivable or huge; leaving
# it in /kaggle/working made `fetch` download 100+ files (the entire stack came
# back with the results). Only the results, logs and summary are worth pulling.
sh(f"rm -rf {env} /kaggle/working/bin {out}/ligprep {out}/receptor "
   f"{STACK} /kaggle/working/ligands.csv")
sh("find /kaggle/working -name '__pycache__' -type d -prune -exec rm -rf {} +")
sys.exit(0 if summary["ok"] else 4)
'''


def build_kernel_script(stack_dir: Path, ligands: Path, precision: str,
                        workers: int, extra: list) -> str:
    """Embed the stack + ligands as base64 so the kernel is self-contained."""
    import base64 as _b64
    import io as _io
    import zipfile as _zip

    keep_suffix = {".py", ".sh", ".csv", ".json", ".pdb", ".pdbqt", ".yml", ".txt", ".md"}
    buf = _io.BytesIO()
    n = 0
    with _zip.ZipFile(buf, "w", _zip.ZIP_DEFLATED, compresslevel=9) as z:
        for f in sorted(stack_dir.rglob("*")):
            if not f.is_file():
                continue
            if f.suffix.lower() not in keep_suffix:
                continue
            # the demo dashboard and the huge cleaned receptor copy are dead weight
            if f.name in {"executive_dashboard_demo.html", "receptor_clean.pdb"}:
                continue
            z.write(f, f"docking_professional_stack/{f.relative_to(stack_dir)}")
            n += 1
    stack_b64 = _b64.b64encode(buf.getvalue()).decode()
    lig_b64 = _b64.b64encode(ligands.read_bytes()).decode()
    log(f"embedded {n} stack files ({len(stack_b64) // 1024} KB base64)")

    header = (
        f"STACK_B64 = {stack_b64!r}\n"
        f"LIGANDS_B64 = {lig_b64!r}\n"
        f"PRECISION = {precision!r}\n"
        f"WORKERS = {workers}\n"
        f"EXTRA_FLAGS = {extra!r}\n\n"
    )
    return header + KERNEL_TEMPLATE


# ── commands ─────────────────────────────────────────────────────────────────
def reconcile_slug_title(args) -> tuple[str, str]:
    """Return (slug, title) that Kaggle will agree on.

    If the caller gave a title we derive the slug from it; if the caller gave
    only a slug we use it as the title too. Either way slugify(title) == slug,
    so the kernel lands where we will later poll for it.
    """
    if args.title:
        slug = args.slug or slugify(args.title)
        if slugify(args.title) != slug:
            log(f"WARNING: --slug {slug!r} does not match slugify(--title) "
                f"{slugify(args.title)!r}; Kaggle uses the title. Using the latter.")
            slug = slugify(args.title)
        return slug, args.title
    slug = args.slug or f"hpl-dock-{int(time.time())}"
    return slugify(slug), slug


def cmd_check(args):
    user, key, src = resolve_credentials(args)
    api = kaggle_api(user, key)
    try:
        ks = api.kernels_list(user=user, page_size=5)
    except Exception as e:  # noqa: BLE001
        emit(False, "check", EXIT_AUTH, username=user, error=str(e)[:200])
    emit(True, "check", EXIT_OK, username=user, cred_source=src,
         kernels_visible=len(ks),
         note="credentials valid; CPU kernels have no weekly quota, 12 h max run")


def cmd_push(args):
    user, key, src = resolve_credentials(args)
    stack = Path(args.stack).expanduser().resolve()
    if not (stack / "multi_site_docking.py").exists():
        emit(False, "push", EXIT_USAGE,
             error=f"--stack does not look like the docking stack: {stack}")
    ligands = Path(args.ligands).expanduser().resolve()
    if not ligands.exists():
        emit(False, "push", EXIT_USAGE, error=f"--ligands not found: {ligands}")

    api = kaggle_api(user, key)
    slug, title = reconcile_slug_title(args)
    kid = f"{user}/{slug}"
    workdir = Path(tempfile.mkdtemp(prefix="kaggle_dock_"))
    try:
        script = build_kernel_script(stack, ligands, args.precision,
                                     args.workers, parse_extra_flags(args.extra))
        (workdir / "script.py").write_text(script)
        meta = {
            "id": kid,
            "title": title,
            "code_file": "script.py",
            "language": "python",
            "kernel_type": "script",
            "is_private": not args.public,
            "enable_gpu": bool(args.gpu),
            "enable_internet": True,      # REQUIRED: toolchain is installed at runtime
            "dataset_sources": [],
            "competition_sources": [],
            "kernel_sources": [],
        }
        (workdir / "kernel-metadata.json").write_text(json.dumps(meta, indent=2))
        log(f"pushing {kid} (private={not args.public}, gpu={bool(args.gpu)})")
        try:
            api.kernels_push(str(workdir))
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            code = EXIT_QUOTA if "quota" in msg.lower() or "429" in msg else EXIT_KERNEL
            emit(False, "push", code, kernel=kid, error=msg[:300])
        emit(True, "push", EXIT_OK, kernel=kid, username=user, cred_source=src,
             url=f"https://www.kaggle.com/code/{kid}",
             next=f"poll with: kaggle_dock.py status --slug {slug}")
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def _normalize_status(raw) -> str:
    """Return a bare lowercase state token.

    GOTCHA: the Kaggle SDK is inconsistent here. kernels_status() may return a
    dict {"status": "COMPLETE"} OR an object whose .status is the *enum*
    KernelWorkerStatus.COMPLETE, which str()s to "KernelWorkerStatus.COMPLETE".
    A naive `status.lower() == "complete"` is False for the enum form, so a
    finished kernel was reported as still running and `run` polled until it
    timed out. Take the text after the last dot and strip the enum prefix.
    """
    s = str(raw)
    if "." in s:
        s = s.rsplit(".", 1)[-1]
    return s.strip().lower()


def _status(api, kid: str) -> tuple[str, str]:
    r = api.kernels_status(kid)
    if isinstance(r, dict):
        raw, fail = r.get("status", "unknown"), r.get("failureMessage")
    else:
        raw, fail = getattr(r, "status", "unknown"), getattr(r, "failure_message", None)
    return _normalize_status(raw), str(fail or "")


def cmd_status(args):
    user, key, _ = resolve_credentials(args)
    api = kaggle_api(user, key)
    kid = args.kernel or f"{user}/{args.slug}"
    if not args.slug and not args.kernel:
        emit(False, "status", EXIT_USAGE, error="need --slug or --kernel")
    try:
        st, fail = _status(api, kid)
    except Exception as e:  # noqa: BLE001
        emit(False, "status", EXIT_KERNEL, kernel=kid, error=str(e)[:200])
    done = st.lower() in {"complete", "error", "cancelacknowledged", "cancelrequested"}
    ok = st.lower() == "complete"
    emit(ok, "status", EXIT_OK if ok else (EXIT_KERNEL if done else EXIT_TIMEOUT),
         kernel=kid, status=st, running=not done, failure=fail[:300])


def cmd_fetch(args):
    user, key, _ = resolve_credentials(args)
    api = kaggle_api(user, key)
    kid = args.kernel or f"{user}/{args.slug}"
    dest = Path(args.out).expanduser().resolve()
    dest.mkdir(parents=True, exist_ok=True)
    try:
        api.kernels_output(kid, path=str(dest), force=True, quiet=False)
    except Exception as e:  # noqa: BLE001
        emit(False, "fetch", EXIT_KERNEL, kernel=kid, error=str(e)[:300])
    files = sorted(p.name for p in dest.rglob("*") if p.is_file())
    summary = None
    sp = dest / "kaggle_dock_summary.json"
    if sp.exists():
        summary = json.loads(sp.read_text())
    emit(True, "fetch", EXIT_OK, kernel=kid, out=str(dest),
         n_files=len(files), files=files[:30], summary=summary)


def cmd_run(args):
    """push → poll → fetch, with a bounded wait. Prints one JSON line at the end."""
    user, key, src = resolve_credentials(args)
    stack = Path(args.stack).expanduser().resolve()
    ligands = Path(args.ligands).expanduser().resolve()
    if not (stack / "multi_site_docking.py").exists():
        emit(False, "run", EXIT_USAGE, error=f"bad --stack: {stack}")
    if not ligands.exists():
        emit(False, "run", EXIT_USAGE, error=f"bad --ligands: {ligands}")

    api = kaggle_api(user, key)
    slug, title = reconcile_slug_title(args)
    kid = f"{user}/{slug}"
    workdir = Path(tempfile.mkdtemp(prefix="kaggle_dock_"))
    try:
        (workdir / "script.py").write_text(
            build_kernel_script(stack, ligands, args.precision, args.workers,
                                parse_extra_flags(args.extra)))
        (workdir / "kernel-metadata.json").write_text(json.dumps({
            "id": kid, "title": title, "code_file": "script.py",
            "language": "python", "kernel_type": "script",
            "is_private": not args.public, "enable_gpu": bool(args.gpu),
            "enable_internet": True, "dataset_sources": [],
            "competition_sources": [], "kernel_sources": [],
        }, indent=2))
        log(f"pushing {kid}")
        try:
            api.kernels_push(str(workdir))
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            emit(False, "run", EXIT_QUOTA if "quota" in msg.lower() else EXIT_KERNEL,
                 kernel=kid, error=msg[:300])
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    deadline = time.time() + args.timeout
    last = ""
    while time.time() < deadline:
        time.sleep(args.poll)
        try:
            st, fail = _status(api, kid)
        except Exception as e:  # noqa: BLE001
            log(f"status error (retrying): {e}")
            continue
        if st != last:
            log(f"status={st}  t+{int(time.time() - deadline + args.timeout)}s")
            last = st
        low = st.lower()
        if low == "complete":
            dest = Path(args.out).expanduser().resolve()
            dest.mkdir(parents=True, exist_ok=True)
            try:
                api.kernels_output(kid, path=str(dest), force=True, quiet=True)
            except Exception as e:  # noqa: BLE001
                emit(False, "run", EXIT_KERNEL, kernel=kid,
                     error=f"complete but fetch failed: {e}"[:300])
            sp = dest / "kaggle_dock_summary.json"
            summary = json.loads(sp.read_text()) if sp.exists() else None
            ok = bool(summary and summary.get("ok"))
            emit(ok, "run", EXIT_OK if ok else EXIT_KERNEL, kernel=kid,
                 url=f"https://www.kaggle.com/code/{kid}", out=str(dest),
                 summary=summary, username=user, cred_source=src)
        if low in {"error", "cancelacknowledged"}:
            emit(False, "run", EXIT_KERNEL, kernel=kid, status=st,
                 failure=fail[:400], url=f"https://www.kaggle.com/code/{kid}",
                 hint="fetch the log: kaggle kernels output %s" % kid)
    emit(False, "run", EXIT_TIMEOUT, kernel=kid, status=last,
         url=f"https://www.kaggle.com/code/{kid}",
         hint=f"still running after {args.timeout}s; poll with `status --slug {slug}`")


def main():
    ap = argparse.ArgumentParser(
        description="Run hPL multi-site docking on Kaggle kernels.")
    ap.add_argument("command", choices=["check", "push", "status", "fetch", "run"])
    ap.add_argument("--username"); ap.add_argument("--key")
    ap.add_argument("--creds", help="JSON with providers.kaggle (multi-account pool)")
    ap.add_argument("--account", type=int, default=0,
                    help="rotation slot when --creds holds several accounts")
    ap.add_argument("--stack", default="docking_professional_stack")
    ap.add_argument("--ligands", default="ligands.csv")
    ap.add_argument("--slug"); ap.add_argument("--kernel"); ap.add_argument("--title")
    ap.add_argument("--precision", default="balanced",
                    choices=["fast", "balanced", "max"])
    ap.add_argument("--workers", type=int, default=4,
                    help="Kaggle CPU kernels give 4 vCPU; 4 is the sweet spot")
    ap.add_argument("--extra", default="", help="extra flags for multi_site_docking.py")
    ap.add_argument("--gpu", action="store_true",
                    help="NOT recommended: Vina is CPU-only and GPU kernels are quota-capped")
    ap.add_argument("--public", action="store_true")
    ap.add_argument("--out", default="kaggle_out")
    ap.add_argument("--timeout", type=int, default=3600)
    ap.add_argument("--poll", type=int, default=30)
    args = ap.parse_args()

    {"check": cmd_check, "push": cmd_push, "status": cmd_status,
     "fetch": cmd_fetch, "run": cmd_run}[args.command](args)


if __name__ == "__main__":
    main()
