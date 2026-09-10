#!/usr/bin/env python3
"""mirror.py — agent-grade HTTrack wrapper (ClawHub skill "httrack" v2.0.0).

Turns `httrack` invocations into safe recipes + a stable machine contract.

Subcommands
  doctor            environment check (JSON; rc 0 ok / 3 binary missing)
  snapshot URL      one page + its inline assets only (no link following)
  mirror URL        bounded mirror of a site (depth/sockets robots politeness)

Contract (stdout, --json — default for doctor; add --json to snapshot/mirror):
  {"schema": "httrack.report.v1", "request": {...}, "result": {...}}
Exit codes: 0 ok · 2 usage/policy rejection · 3 httrack missing · 4 run failed.
Evidence for every flag in docs/evidence.md. Never uses a shell; scheme
allowlist is http/https only; binary can be overridden with $HTTRACK_BIN.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.parse

DEFAULT_SOCKETS = 2        # polite by default (see docs/evidence.md)
DEFAULT_DEPTH = 2
DEFAULT_ROBOTS = 2         # 2 = always obey robots.txt (httrack default is 2)
SNAPSHOT_ASSETS = ["*.css", "*.js", "*.png", "*.jpg", "*.jpeg", "*.gif",
                   "*.svg", "*.webp", "*.ico", "*.woff", "*.woff2", "*.ttf"]


class UsageError(Exception):
    pass


def find_binary():
    over = os.environ.get("HTTRACK_BIN", "").strip()
    if over:
        return over if os.path.isfile(over) else None
    return shutil.which("httrack")


def check_url(u, allow_private=False):
    u = u.strip()
    if any(c.isspace() for c in u):
        raise UsageError("url contains whitespace")
    p = urllib.parse.urlparse(u)
    if p.scheme not in ("http", "https"):
        raise UsageError(f"scheme {p.scheme or '(none)'} refused — only http/https are mirrored")
    if not p.netloc:
        raise UsageError("url has no host")
    if "@" in p.netloc:
        raise UsageError("userinfo (user@host) in url refused — phishing-shaped hosts are refused")
    if not allow_private:
        host = p.hostname or ""
        if host.lower() == "localhost" or _is_private_ip(host):
            raise UsageError(
                f"host {host!r} is loopback/link-local/private — refused by default; "
                "pass --allow-private for authorized LAN mirrors")
    return u.split("#", 1)[0]


def _is_private_ip(host):
    import ipaddress
    h = host.strip("[]")
    try:
        ip = ipaddress.ip_address(h)
    except ValueError:
        return False                      # a DNS name — can't classify lexically
    return (ip.is_loopback or ip.is_link_local or ip.is_private
            or ip.is_multicast or ip.is_unspecified)


def check_filters(allows, denies):
    """Normalize scan rules into +/− prefixes ourselves: a stray leading sign
    is stripped (UX), anything with whitespace is refused (no shell-argument
    ambiguity can leak through the glob)."""
    out = []
    for sign, items in (("+", allows), ("-", denies)):
        for f in items:
            f = f.lstrip("+-").strip()
            if not f or " " in f:
                raise UsageError(f"scan pattern {f!r} refused — plain glob only, no spaces")
            out.append(sign + f)
    return out


def version_of(binary):
    try:
        p = subprocess.run([binary, "--version"], capture_output=True, timeout=15)
        blob = (p.stdout + p.stderr).decode("utf-8", errors="replace")
        line = blob.splitlines()
        return line[0].strip() if line else "unknown"
    except Exception:
        return "unknown"


def doctor(as_json=True):
    b = find_binary()
    rep = {"schema": "httrack.doctor.v1",
           "binary": {"found": bool(b), "path": b,
                      "source": "HTTRACK_BIN" if os.environ.get("HTTRACK_BIN") else "PATH",
                      "version": version_of(b) if b else None},
           "policy": {"schemes": ["http", "https"], "default_sockets": DEFAULT_SOCKETS,
                      "default_robots": DEFAULT_ROBOTS, "shell_used": False}}
    print(json.dumps(rep, indent=2))
    return 0 if b else 3


def run_httrack(argv_extra, timeout):
    b = find_binary()
    if not b:
        raise SystemExit(3)
    argv = [b] + argv_extra
    t0 = time.time()
    try:
        p = subprocess.run(argv, capture_output=True, timeout=timeout or None)
        rc = p.returncode
        out = p.stdout.decode("utf-8", errors="replace")
        err = p.stderr.decode("utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return None, 124, "", "timeout", time.time() - t0
    return argv, rc, out, err, time.time() - t0


def measure(outdir):
    files = hall = bytes_ = 0
    for root, _dirs, names in os.walk(outdir):
        for n in names:
            fp = os.path.join(root, n)
            if os.path.islink(fp):     # don't double-count symlinked payloads
                continue
            try:
                bytes_ += os.path.getsize(fp)
            except OSError:
                continue
            files += 1
            if n.lower().endswith((".html", ".htm")):
                hall += 1
    return {"files": files, "bytes": bytes_, "html_pages": hall}


def report(a, cmd, request, t0_args=None):
    argv, rc, out, err, dur = run_httrack(t0_args, a.timeout)
    res = {"exit_code": rc, "duration_s": round(dur, 2), **measure(a.out),
           "argv_len": len(argv) if argv else 0}
    warnings = []
    if rc == 124:
        warnings.append("mirror hit --max-time; re-run with --resume to continue")
    log_tail = (err or out).strip().splitlines()[-20:] if (err or out).strip() else []
    rep = {"schema": "httrack.report.v1", "command": cmd, "request": request,
           "result": {**res, "log_tail": log_tail}, "warnings": warnings}
    if a.json:
        print(json.dumps(rep, indent=2))
    else:
        print(f"{cmd}: {request['url']} -> {a.out}")
        print(f"  files={res['files']} bytes={res['bytes']} pages={res['html_pages']} "
              f"duration={res['duration_s']}s exit={rc}")
        for w in warnings:
            print(f"  [!] {w}")
    return 0 if rc == 0 else 4


def main():
    ap = argparse.ArgumentParser(prog="mirror.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("doctor", help="environment check (always JSON)")

    def base(name, helptext):
        sp = sub.add_parser(name, help=helptext)
        sp.add_argument("url")
        sp.add_argument("-o", "--out", required=True, help="output directory")
        sp.add_argument("--sockets", type=int, default=DEFAULT_SOCKETS,
                        help=f"parallel connections (default {DEFAULT_SOCKETS}; keep low)")
        sp.add_argument("--robots", type=int, choices=[0, 1, 2, 3], default=DEFAULT_ROBOTS,
                        help="robots.txt compliance 0=never 1=sometimes 2=always 3=strict (default 2)")
        sp.add_argument("--max-time", type=int, default=None, help="max mirror seconds (-E)")
        sp.add_argument("--timeout", type=int, default=0,
                        help="hard kill wrapper (seconds; 0=off — a killed run leaves a resumable cache)")
        sp.add_argument("--resume", action="store_true", help="continue/update existing mirror (-i)")
        sp.add_argument("--json", action="store_true", help="JSON machine report on stdout")
        sp.add_argument("--allow", action="append", default=[], metavar="GLOB",
                        help="scan-rule accept pattern (repeatable), e.g. --allow '*.pdf'")
        sp.add_argument("--deny", action="append", default=[], metavar="GLOB",
                        help="scan-rule reject pattern (repeatable), e.g. --deny '*/forums/*'")
        sp.add_argument("--allow-private", action="store_true",
                        help="permit loopback/link-local/private-LAN mirrors (authorized use only)")
        return sp

    snap = base("snapshot", "one page + inline assets only")
    mir = base("mirror", "bounded site mirror")
    mir.add_argument("--depth", type=int, default=DEFAULT_DEPTH,
                     help=f"link-following depth (default {DEFAULT_DEPTH})")
    mir.add_argument("--max-mb", type=int, default=None, help="overall size ceiling MB (-M)")

    # normalize `--allow VALUE` / `--deny VALUE` where VALUE starts with a
    # sign (would otherwise be parsed as a new option) into `--allow=VALUE`.
    argv = sys.argv[1:]
    fixed = []
    i = 0
    while i < len(argv):
        if argv[i] in ("--allow", "--deny") and i + 1 < len(argv) and argv[i + 1].startswith(("+", "-")):
            fixed.append(argv[i] + "=" + argv[i + 1])
            i += 2
        else:
            fixed.append(argv[i])
            i += 1
    a = ap.parse_args(fixed)
    try:
        if a.cmd == "doctor":
            return doctor()
        url = check_url(a.url, allow_private=a.allow_private)
        if ".." in a.out.split("/"):
            raise UsageError("relative '..' in -o refused — pass an explicit output directory")
        if a.sockets < 1:
            raise UsageError("--sockets must be >= 1")
        flts = check_filters(a.allow, a.deny)
        if a.cmd == "snapshot":
            if flts:
                raise UsageError("snapshot already pins asset scan rules; pass no --allow/--deny")
            argv = [url, "-O", a.out, "-r1", "-%e0", "-n", "-a",
                    f"-c{a.sockets}", f"-s{a.robots}",
                    "-*", *[f"+{p}" for p in SNAPSHOT_ASSETS]]
            if a.resume:
                argv.append("-i")
            if a.max_time:
                argv.append(f"-E{a.max_time}")
            req = {"url": url, "out": a.out, "sockets": a.sockets, "robots": a.robots,
                   "recipe": "snapshot(-r1 -%e0 -n -a +asset-rules)"}
        else:  # mirror
            if a.depth < 0:
                raise UsageError("--depth must be >= 0")
            argv = [url, "-O", a.out, f"-r{a.depth}", f"-c{a.sockets}",
                    f"-s{a.robots}", "-a"]
            if a.resume:
                argv.append("-i")
            if a.max_time:
                argv.append(f"-E{a.max_time}")
            if a.max_mb:
                argv.append(f"-M{a.max_mb * 1000000}")
            argv += flts
            req = {"url": url, "out": a.out, "depth": a.depth, "sockets": a.sockets,
                   "robots": a.robots, "resume": a.resume, "filters": flts}
        return report(a, a.cmd, req, argv)
    except UsageError as e:
        print(f"usage error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
