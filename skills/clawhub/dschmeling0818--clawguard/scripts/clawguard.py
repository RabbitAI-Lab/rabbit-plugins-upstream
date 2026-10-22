#!/usr/bin/env python3
"""ClawGuard client: send a skill bundle to the ClawGuard API and print the verdict.

  clawguard.py preview <folder|owner/repo/path>   free, verdict only
  clawguard.py scan    <folder|owner/repo/path>   full report, $0.03 via x402

Paid scans need an x402-capable payer. If CLAWGUARD_PAYER is set to a command
(for example an x402 CLI), the 402 challenge is piped to it on stdin and its
stdout is sent back as the X-PAYMENT header. Otherwise the challenge is printed
so the agent's own wallet tooling can pay it.
"""
import json, os, subprocess, sys, urllib.request, urllib.error

API = os.environ.get("CLAWGUARD_API", "https://clawguard.duckdns.org:8082").rstrip("/")
SKIP = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".gz", ".woff", ".woff2", ".ttf", ".mp3", ".mp4", ".lock")


def bundle(target):
    if os.path.isdir(target):
        files = []
        for root, dirs, names in os.walk(target):
            dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__", ".venv")]
            for n in names:
                p = os.path.join(root, n)
                if n.lower().endswith(SKIP) or os.path.getsize(p) > 500_000:
                    continue
                try:
                    with open(p, encoding="utf-8", errors="replace") as f:
                        files.append({"path": os.path.relpath(p, target), "content": f.read()})
                except OSError:
                    pass
                if len(files) >= 200:
                    break
        return {"files": files}
    if os.path.isfile(target):
        with open(target, encoding="utf-8", errors="replace") as f:
            return {"path": os.path.basename(target), "content": f.read()}
    return {"github": target}


def post(path, body, payment=None):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "User-Agent": "clawguard-skill/1.0"})
    if payment:
        req.add_header("X-PAYMENT", payment)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read())
        except Exception:
            return e.code, {"error": str(e)}


def show(res):
    if "error" in res and "verdict" not in res:
        print("ERROR:", res["error"]); sys.exit(2)
    print(f"VERDICT: {res['verdict']}   risk {res['risk_score']}/100   {res.get('files_scanned', '?')} files")
    c = res.get("counts", {})
    print(f"critical {c.get('critical', 0)}  high {c.get('high', 0)}  medium {c.get('medium', 0)}  low {c.get('low', 0)}")
    for f in res.get("findings", [])[:25]:
        print(f"  [{f['severity'].upper()}] {f['message']}  ({f['file']}:{f['line']})")
        print(f"      {f['evidence']}")
    if "full_report" in res and res["verdict"] != "PASS":
        print("Full report:", res["full_report"])
    sys.exit({"PASS": 0, "REVIEW": 1, "BLOCK": 3}.get(res["verdict"], 2))


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("preview", "scan"):
        print(__doc__); sys.exit(2)
    mode, target = sys.argv[1], sys.argv[2]
    body = bundle(target)
    if mode == "preview":
        _, res = post("/v1/preview", body); show(res)
    status, res = post("/v1/scan", body)
    if status == 402:
        payer = os.environ.get("CLAWGUARD_PAYER")
        if not payer:
            print("PAYMENT REQUIRED: $0.03 USDC via x402. Challenge:")
            print(json.dumps(res.get("accepts", res), indent=2))
            print("Set CLAWGUARD_PAYER to an x402 payer command, or use 'preview' for the free verdict.")
            sys.exit(4)
        header = subprocess.run(payer, shell=True, input=json.dumps(res), capture_output=True, text=True).stdout.strip()
        status, res = post("/v1/scan", body, header)
    show(res)


if __name__ == "__main__":
    main()
