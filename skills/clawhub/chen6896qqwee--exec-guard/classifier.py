#!/usr/bin/env python3
"""Exec Guard - Command permission classifier."""
import re, json, sys, argparse, urllib.request

RULES = [
    (r"rm\s+-rf\s+/", "recursive_force_delete", 1.0),
    (r"rm\s+-rf", "file_destruction", 0.85),
    (r"dd\s+if=/dev/zero", "disk_wipe", 1.0),
    (r"mkfs\.", "disk_wipe", 1.0),
    (r"curl\s+.*\|\s*bash", "network_pipe_to_shell", 0.95),
    (r"wget\s+.*\|\s*sh", "network_pipe_to_shell", 0.95),
    (r"sudo\s+rm\s+-rf", "permission_escalation", 0.90),
    (r"chmod\s+777", "permission_escalation", 0.70),
    (r"DROP\s+TABLE", "database_destructive", 0.90),
    (r"DROP\s+DATABASE", "database_destructive", 0.95),
    (r"TRUNCATE\s+TABLE", "database_destructive", 0.80),
    (r"shutdown\s+-[rh]\s+now", "system_shutdown", 0.80),
    (r"reboot", "system_shutdown", 0.70),
    (r"nc\s+-[eE]", "reverse_shell", 1.0),
    (r"bash\s+-i", "reverse_shell", 0.90),
    (r"/dev/tcp/", "reverse_shell", 0.95),
    (r"xmrig", "crypto_mining", 0.80),
    (r"base64\s+-d\s+.*\|", "suspicious_encoding", 0.75),
    (r"find\s+/\s+-name.*-exec\s+rm", "mass_delete", 0.90),
    (r"curl\s+.*-F\s+.*@", "data_exfiltration", 0.85),
    (r"env\s+\|\s+curl", "env_leak", 0.60),
]

SAFE_OVERRIDES = [r"rm\s+-rf\s+/tmp/", r"rm\s+-rf\s+\.git/", r"rm\s+-rf\s+node_modules", r"rm\s+-rf\s+__pycache__", r"find\s+\.\s+-name"]

def classify(command: str) -> dict:
    cmd_lower = command.lower().strip()
    for pat in SAFE_OVERRIDES:
        if re.search(pat, cmd_lower): return {"command":command,"verdict":"allow","risk_level":"safe","matched_rules":[],"reason":"Safe override"}
    matched_rules = []; max_risk = 0.0
    for pattern, category, weight in RULES:
        if re.search(pattern, cmd_lower):
            matched_rules.append(category); max_risk = max(max_risk, weight)
    if not matched_rules: return {"command":command,"verdict":"allow","risk_level":"safe","matched_rules":[],"reason":"No dangerous patterns"}
    verdict, risk_level = ("deny","critical") if max_risk>=0.85 else ("ask","high") if max_risk>=0.60 else ("ask","medium")
    return {"command":command,"verdict":verdict,"risk_level":risk_level,"matched_rules":list(set(matched_rules)),"max_risk_score":round(max_risk,2),"reason":"Matched: "+", ".join(set(matched_rules))}

def llm_classify(command: str, llm_url: str = None) -> dict:
    if not llm_url: llm_url = "http://localhost:1234/v1/chat/completions"
    prompt = "Classify this shell command: "+command+". Return JSON verdict."
    payload = json.dumps({"model":"local-model","messages":[{"role":"user","content":prompt}],"temperature":0.1,"max_tokens":200}).encode("utf-8")
    try:
        req = urllib.request.Request(llm_url, data=payload, headers={"Content-Type":"application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            content = result["choices"][0]["message"]["content"]
            m = re.search(r"\{.*\}", content, re.DOTALL)
            if m: return json.loads(m.group())
            return {"verdict":"ask","risk_level":"unknown","reason":"LLM returned non-JSON"}
    except Exception as e: return {"verdict":"allow","risk_level":"unknown","reason":"LLM unavailable: "+str(e)}

def main():
    parser = argparse.ArgumentParser(description="Exec Guard")
    parser.add_argument("--command","-c",help="Single command")
    parser.add_argument("--file","-f",help="File with commands")
    parser.add_argument("--llm",action="store_true",help="Use LLM")
    parser.add_argument("--llm-url",default="http://localhost:1234/v1/chat/completions",help="LLM URL")
    parser.add_argument("--json",action="store_true",help="JSON output")
    args = parser.parse_args()
    commands = []
    if args.command: commands = [args.command]
    elif args.file:
        with open(args.file,"r",encoding="utf-8") as f: commands = [line.strip() for line in f if line.strip()]
    else: commands = [line.strip() for line in sys.stdin if line.strip()]
    results = []
    for cmd in commands:
        result = classify(cmd)
        if args.llm and result["verdict"]=="allow":
            llm_result = llm_classify(cmd, args.llm_url)
            if llm_result.get("verdict") in ("deny","ask"): result = llm_result
        results.append(result)
    if args.json:
        print(json.dumps(results if len(results)>1 else results[0], indent=2, ensure_ascii=False))
    else:
        for r in results:
            icon = {"allow":"[OK]","ask":"[?]","deny":"[X]"}.get(r["verdict"],"[?]")
            print(icon+" "+r["command"])
            print("  Verdict: "+r["verdict"]+" | Risk: "+r.get("risk_level","?"))
            print("  Reason: "+r.get("reason",""))
            if r.get("matched_rules"): print("  Matched: "+", ".join(set(r["matched_rules"])))
            print()
if __name__ == "__main__": main()