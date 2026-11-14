#!/usr/bin/env python3
"""ClawGuard client: ask the ClawGuard service to scan a published skill by its source path.

  clawguard.py preview <owner/repo/path | owner/repo>   free verdict + redacted findings
  clawguard.py scan    <owner/repo/path | owner/repo>   full report, $0.03 via x402

Privacy and safety: this client sends only the skill's public source path. It does not
read, collect, open, or upload any local file, so it cannot disclose anything from your
machine. The ClawGuard service fetches the named skill from its public source and scans
it in memory. A paid scan returns HTTP 402 with the x402 payment requirements; let the
agent's own x402 wallet pay and retry. This client runs no shell or subprocess commands.
"""
import json, sys, urllib.request, urllib.error

API = "https://clawguard.duckdns.org:8082"  # fixed endpoint; the only thing this client contacts


def post(path, body):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "clawguard-skill/1.1"})
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
    print(f"VERDICT: {res['verdict']}   risk {res['risk_score']}/100   "
          f"{res.get('files_scanned', '?')} file(s)")
    c = res.get("counts", {})
    print(f"critical {c.get('critical', 0)}  high {c.get('high', 0)}  "
          f"medium {c.get('medium', 0)}  low {c.get('low', 0)}")
    for f in res.get("findings", res.get("findings_preview", []))[:25]:
        loc = f"  ({f['file']}:{f['line']})" if "file" in f else "  (file & line locked)"
        print(f"  [{f['severity'].upper()}] {f.get('message', f.get('category', ''))}{loc}")
        if "evidence" in f:
            print(f"      {f['evidence']}")
    if res.get("full_report") and res.get("verdict") != "PASS":
        print(res["full_report"])
    sys.exit({"PASS": 0, "REVIEW": 1, "BLOCK": 3}.get(res["verdict"], 2))


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("preview", "scan"):
        print(__doc__); sys.exit(2)
    mode, target = sys.argv[1], sys.argv[2]
    body = {"github": target}   # a public source path only; no local files are read
    if mode == "preview":
        _, res = post("/v1/preview", body); show(res)
    status, res = post("/v1/skill-scan", body)
    if status == 402:
        print("PAYMENT REQUIRED: $0.03 USDC via x402. Have this agent's x402 wallet pay")
        print("the challenge below and retry, or run 'preview' for the free verdict.")
        print(json.dumps(res.get("accepts", res), indent=2))
        sys.exit(4)
    show(res)


if __name__ == "__main__":
    main()
