#!/usr/bin/env python3
"""playbook_selftest.py — offline verification for arena-power-user-playbook.

10 groups, all offline, deterministic. Exit 0 only if ALL CHECKS PASSED.
"""

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLI = [sys.executable, str(ROOT / "scripts" / "arena_playbook.py")]
FAILS = []
PASSES = []


def check(name, cond, detail=""):
    if cond:
        PASSES.append(name)
        print(f"PASS: {name}")
    else:
        FAILS.append((name, detail))
        print(f"FAIL: {name} — {detail}")


def run(*args, cwd=None):
    proc = subprocess.run(CLI + list(args), capture_output=True, text=True, cwd=cwd)
    return proc


def out_json(out_file):
    with open(out_file, "r", encoding="utf-8") as fh:
        return json.load(fh)


def fm(path):
    text = Path(path).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    meta = {}
    for line in m.group(1).splitlines():
        if line.startswith("  ") or line.startswith("- "):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta


TMP = tempfile.mkdtemp(prefix="apselftest_")

# ── Group 1: consistency + phantom references ──────────────────────────────
f = fm(ROOT / "SKILL.md")
check("1a frontmatter name matches folder", f.get("name") == "arena-power-user-playbook", f.get("name", ""))
check("1b frontmatter version is 2.0.0", f.get("version") == "2.0.0", f.get("version", ""))
check("1c license MIT-0", f.get("license") == "MIT-0", f.get("license", ""))
desc = (ROOT / "SKILL.md").read_text(encoding="utf-8")
dsc = re.search(r"^description:\s*\n((?:\s+.+\n?)+)", desc, re.M)
desc_text = re.sub(r"\s+", " ", dsc.group(1)).strip() if dsc else f.get("description", "")
check("1d description <=1024 chars", 0 < len(desc_text) <= 1024, f"len={len(desc_text)}")
changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
check("1e CHANGELOG has v2.0.0", "## v2.0.0" in changelog)
phantoms = []
for doc in ("SKILL.md", "README.md", "AGENT_DISCOVERY.md"):
    text = (ROOT / doc).read_text(encoding="utf-8")
    for mref in re.finditer(r"(?:scripts|data|references|tools)/[A-Za-z0-9_\-./]+\.(?:py|json|md|sh)", text):
        if not (ROOT / mref.group(0)).exists():
            phantoms.append(f"{doc}: {mref.group(0)}")
check("1f no phantom file references in docs", not phantoms, "; ".join(phantoms))
for needed in ("scripts/arena_playbook.py", "data/model_snapshot_2026-09-05.json",
               "references/modes.md", "references/leaderboard.md", "references/fallback.md",
               "tools/playbook_selftest.py"):
    check(f"1g required file exists: {needed}", (ROOT / needed).exists())

# ── Group 2: mode advisor ───────────────────────────────────────────────────
r = run("mode", "--task", "what is a python list comprehension?")
check("2a simple Q&A -> direct", "mode=direct" in r.stdout, r.stdout)
check("2a exit 0", r.returncode == 0)
r = run("mode", "--task", "what is the average of column A in this csv", "--files", "1")
check("2b single-file question -> direct (spec regression)", "mode=direct" in r.stdout, r.stdout)
r = run("mode", "--task", "build a full dashboard from this dataset", "--files", "1", "--steps", "3", "--coding")
check("2c multi-step build -> agent", "mode=agent" in r.stdout, r.stdout)
r = run("mode", "--task", "compare gpt and claude on this prompt", "--compare")
check("2d compare -> side-by-side", "mode=side-by-side" in r.stdout, r.stdout)
r = run("mode", "--task", "blind test", "--blind")
check("2e blind -> battle", "mode=battle" in r.stdout, r.stdout)
r = run("mode", "--task", "search the web for recent reports and write a summary", "--steps", "2")
check("2f-pre tool-chain task -> agent", "mode=agent" in r.stdout, r.stdout)
r = run("mode", "--task", "search the web for recent reports and write a summary", "--steps", "2", "--budget-conscious")
check("2f budget-conscious downgrade works", "mode=direct" in r.stdout and "downgraded" in r.stdout, r.stdout)
tasks = os.path.join(TMP, "tasks.json")
with open(tasks, "w", encoding="utf-8") as fh:
    json.dump({"tasks": [
        {"task": "quick def", "files": 0, "steps": 1},
        {"task": "build an app that searches and writes a report", "files": 1, "steps": 4, "coding": True},
        {"task": "compare models", "compare": True},
    ]}, fh)
outf = os.path.join(TMP, "mode_out.json")
r = run("mode", "--tasks", tasks, "--out", outf)
d = out_json(outf)
check("2g tasks batch n=3", r.returncode == 0 and d.get("n") == 3, r.stdout)
check("2g batch counts", d.get("counts") == {"direct": 1, "agent": 1, "side-by-side": 1}, json.dumps(d.get("counts")))
r = run("mode")
check("2h no input -> exit 2", r.returncode == 2 and "no_data" in r.stdout, r.stdout)

# ── Group 3: weak-response screener ─────────────────────────────────────────
strong = ("Here is the answer you asked for. The list comprehension "
          "[x for x in range(10) if x % 2 == 0] evaluates to [0, 2, 4, 6, 8]. "
          "It iterates over the range, keeps even numbers, and builds the new list "
          "in a single expression. The time complexity is linear in the input size.")
r = run("weak", "--response", strong)
check("3a strong response -> strong band", "band=strong" in r.stdout and r.returncode == 0, r.stdout)
weakresp = "I'm sorry, I cannot help you with that task as an AI."
r = run("weak", "--response", weakresp)
check("3b refusal+short+apology -> weak", "band=weak" in r.stdout and r.returncode == 1, r.stdout)
longwithcaveat = strong + " That said, I can't guarantee the performance on every input, but in general the behavior is as described. " * 3
r = run("weak", "--response", longwithcaveat)
d = None
outf = os.path.join(TMP, "weak_out.json")
run("weak", "--response", longwithcaveat, "--out", outf)
d = out_json(outf)
check("3c 'I can't' in long response not refusal flag", "refusal_pattern" not in d.get("flags", []), json.dumps(d.get("flags")))
short_legit = "The answer is 42."
r = run("weak", "--response", short_legit)
check("3d short legit -> not weak band", "band=weak" not in r.stdout, r.stdout)
r = run("weak", "--response", short_legit, "--expect-short", "--out", os.path.join(TMP, "ws.json"))
check("3e expect-short disables word floor", "too_short" not in out_json(os.path.join(TMP, "ws.json")).get("flags", []))
r = run("weak")
check("3f no input -> exit 2", r.returncode == 2, r.stdout)
r1 = run("weak", "--response", weakresp, "--out", os.path.join(TMP, "w1.json"))
r2 = run("weak", "--response", weakresp, "--out", os.path.join(TMP, "w2.json"))
check("3g deterministic output", out_json(os.path.join(TMP, "w1.json")) == out_json(os.path.join(TMP, "w2.json")))
codepad = "```python\nx = 1\ny = 2\nz = x + y\nprint(z)\n```"
outf = os.path.join(TMP, "wpad.json")
run("weak", "--response", codepad, "--out", outf)
d = out_json(outf)
check("3h code stripped before word count", d["words_after_code_strip"] < 10, str(d["words_after_code_strip"]))

# ── Group 4: model-check ────────────────────────────────────────────────────
snap = out_json(str(ROOT / "data" / "model_snapshot_2026-09-05.json"))
top = snap["top"]
dump = {
    "dump_date": "2026-09-20", "total_models": 59,
    "top": [
        {"rank": 1, "model": "GPT 5.6 Sol (xHigh)"},
        {"rank": 2, "model": "Claude Fable 5.1 (Max)"},
        {"rank": 3, "model": "Some Brand New Model (High)"},
    ],
}
dumpf = os.path.join(TMP, "dump.json")
with open(dumpf, "w", encoding="utf-8") as fh:
    json.dump(dump, fh)
outf = os.path.join(TMP, "mc.json")
r = run("model-check", "--dump", dumpf, "--out", outf)
d = out_json(outf)
check("4a stale-rotation detected", r.returncode == 1 and d["status"] == "findings", r.stdout)
drift_models = {x["model"] for x in d["rank_drift"]}
check("4b rank drift computed (Sol 5->1, Fable 1->2)",
      "GPT 5.6 Sol (xHigh)" in drift_models and "Claude Fable 5.1 (Max)" in drift_models,
      json.dumps(d["rank_drift"]))
check("4c rotated-out includes Opus 5 (High)", any(x["model"] == "Claude Opus 5 (High)" for x in d["rotated_out"]),
      json.dumps([x["model"] for x in d["rotated_out"]]))
check("4d new model flagged for verification", any("Some Brand New Model" in x["model"] for x in d["rotated_in"]),
      json.dumps(d["rotated_in"]))
dump_old = dict(dump); dump_old["dump_date"] = "2026-08-01"
dumpf2 = os.path.join(TMP, "dump_old.json")
with open(dumpf2, "w", encoding="utf-8") as fh:
    json.dump(dump_old, fh)
outf2 = os.path.join(TMP, "mc_old.json")
r = run("model-check", "--dump", dumpf2, "--out", outf2)
d = out_json(outf2)
check("4e stale dump warns, still computes",
      any("OLDER" in w for w in d["warnings"]) and d["status"] == "findings", json.dumps(d["warnings"]))
r = run("model-check", "--dump", os.path.join(TMP, "missing.json"))
check("4f missing dump -> exit 2", r.returncode == 2, r.stdout)

# ── Group 5: snapshot writer ────────────────────────────────────────────────
outf = os.path.join(TMP, "snap_new.json")
r = run("snapshot", "--dump", dumpf, "--out", outf)
check("5a snapshot written", r.returncode == 0 and os.path.exists(outf), r.stdout)
if os.path.exists(outf):
    d = out_json(outf)
    check("5b snapshot has date+source+rows",
          d.get("snapshot_date") == "2026-09-20" and d.get("source", "").startswith("https://") and len(d.get("top", [])) == 3,
          json.dumps({k: d.get(k) for k in ("snapshot_date", "source")}))
    check("5c tier extracted", d["top"][0]["tier"] == "xhigh", json.dumps(d["top"][0]))
bad_dump = os.path.join(TMP, "bad_dump.json")
with open(bad_dump, "w", encoding="utf-8") as fh:
    json.dump({"dump_date": "2026-09-20", "top": [{"rank": 1, "model": "A"}, {"rank": 3, "model": "B"}]}, fh)
r = run("snapshot", "--dump", bad_dump, "--out", os.path.join(TMP, "bad_out.json"))
check("5d non-contiguous ranks rejected", r.returncode == 2 and "contiguous" in r.stdout, r.stdout)
dump_nodate = os.path.join(TMP, "dump_nodate.json")
with open(dump_nodate, "w", encoding="utf-8") as fh:
    json.dump({"top": dump["top"]}, fh)  # no dump_date inside
r = run("snapshot", "--dump", dump_nodate)
check("5e missing date -> exit 2", r.returncode == 2 and "date" in r.stdout, r.stdout)

# ── Group 6: state manager ──────────────────────────────────────────────────
sf = os.path.join(TMP, "SESSION-STATE.md")
r = run("state", "--file", sf, "--action", "init", "--goal", "Ship the dashboard")
check("6a init creates file", r.returncode == 0 and os.path.exists(sf), r.stdout)
r = run("state", "--file", sf, "--action", "init", "--goal", "other")
check("6b init refuses overwrite", r.returncode == 2 and "overwrite" in r.stdout, r.stdout)
r = run("state", "--file", sf, "--action", "add", "--phase", "research",
        "--done", "collected data", "--done", "collected data", "--next", "write report")
d = None
outf = os.path.join(TMP, "st.json")
r = run("state", "--file", sf, "--action", "add", "--phase", "design", "--done", "chose layout", "--next", "build pages", "--out", outf)
d = out_json(outf)
check("6c add works with phase bump (two adds -> chunk 3)", r.returncode == 0 and d["chunk"] == "3", r.stdout)
st = open(sf, encoding="utf-8").read()
check("6d add dedupes", st.count("- collected data") == 1, st)
outf6 = os.path.join(TMP, "st2.json")
r = run("state", "--file", sf, "--action", "add", "--done", "regression check", "--out", outf6)
d = out_json(outf6)
check("6d2 placeholder not counted as item",
      d["done"] == 3 and d["next"] == 3, json.dumps({k: d.get(k) for k in ("done", "next")}))
r = run("state", "--file", sf, "--action", "summary")
check("6d3 summary carry has no phantom '(none yet)'", "(none yet)" not in r.stdout.split("done:")[1].split("\n")[0], r.stdout)
r = run("state", "--file", sf, "--action", "summary")
check("6e summary carry block", r.returncode == 0 and "[STATE-CARRY]" in r.stdout and "Ship the dashboard" in r.stdout, r.stdout)
r = run("state", "--file", sf, "--action", "next")
check("6f next message embeds state", r.returncode == 0 and "chunk 4" in r.stdout and "do not redo" in r.stdout.lower(), r.stdout)
bad_sf = os.path.join(TMP, "bad_state.md")
with open(bad_sf, "w", encoding="utf-8") as fh:
    fh.write("no frontmatter here\n")
r = run("state", "--file", bad_sf, "--action", "validate")
check("6g corrupted state -> exit 2", r.returncode == 2 and "frontmatter" in r.stdout, r.stdout)
r = run("state", "--file", sf, "--action", "validate")
check("6h valid state -> exit 0", r.returncode == 0, r.stdout)

# ── Group 7: stats loop ─────────────────────────────────────────────────────
logf = os.path.join(TMP, "log.jsonl")
r = run("stats", "--action", "log", "--event", "weak_response", "--model", "Model A", "--mode", "agent", "--log", logf)
check("7a log event", r.returncode == 0 and os.path.exists(logf), r.stdout)
run("stats", "--action", "log", "--event", "mode_pick", "--mode", "direct", "--log", logf)
run("stats", "--action", "log", "--event", "weak_response", "--model", "Model B", "--mode", "direct", "--log", logf)
outf = os.path.join(TMP, "stats.json")
r = run("stats", "--action", "report", "--log", logf, "--out", outf)
d = out_json(outf)
check("7b report counts", d.get("entries") == 3 and d.get("by_event", {}).get("weak_response") == 2
      and d.get("by_mode", {}).get("agent") == 1, json.dumps(d.get("by_event")))
r = run("stats", "--action", "log", "--event", "bogus_event", "--log", logf)
check("7c unknown event rejected", r.returncode == 2 and "allowed" in r.stdout, r.stdout)
r = run("stats", "--action", "report", "--log", os.path.join(TMP, "nope.jsonl"))
check("7d missing log -> no_data exit 2", r.returncode == 2 and "no_data" in r.stdout, r.stdout)

# ── Group 8: snapshot data integrity ────────────────────────────────────────
snapf = ROOT / "data" / "model_snapshot_2026-09-05.json"
check("8a snapshot file dated in name+content",
      snapf.stem.endswith("2026-09-05") and snap.get("snapshot_date") == "2026-09-05")
check("8b top-1 is Claude Fable 5.1 (Max)", top[0]["model"] == "Claude Fable 5.1 (Max)", top[0]["model"])
check("8c 30 rows ranks 1..30", len(top) == 30 and [r_["rank"] for r_ in top] == list(range(1, 31)))
check("8d board totals recorded", snap.get("total_models") == 59 and snap.get("total_sessions") == 2285256,
      json.dumps({k: snap.get(k) for k in ("total_models", "total_sessions")}))
check("8e all rows have lab+tier+net_improvement",
      all(r_.get("lab") and "net_improvement_pct" in r_ for r_ in top))
check("8f signal leaders recorded", "signal_leaders_2026_09_05" in snap)

# ── Group 9: CLI contract ───────────────────────────────────────────────────
r = run("--help")
check("9a --help exit 0", r.returncode == 0, r.stdout + r.stderr)
r = run("bogus-cmd")
check("9b unknown subcommand exit 2", r.returncode == 2, str(r.returncode))
r = run("weak", "--file", os.path.join(TMP, "missing_resp.txt"))
check("9c missing response file -> exit 2", r.returncode == 2, r.stdout)
r = run("mode", "--task", "hello")
line = r.stdout.strip().splitlines()[-1]
check("9d one-line machine summary starts with command=", line.startswith("command=mode "), line)
for sub in ("mode", "weak", "model-check", "snapshot", "state", "stats"):
    r = run(sub, "--help")
    check(f"9e {sub} --help works", r.returncode == 0)

# ── Group 10: honesty phrases in SKILL.md ───────────────────────────────────
skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
for phrase, label in [
    ("screening flags", "weak = screening not quality"),
    ("comparison baseline only", "snapshot = baseline only"),
    ("cloud-only", "cloud-only fallback rule"),
    ("No unverifiable numbers", "anti-fabrication rule"),
    ("never quality judgments", "explicit no-quality-claim"),
]:
    check(f"10 honesty phrase: {label}", phrase.lower() in skill_text.lower(), phrase)
fb = (ROOT / "references" / "fallback.md").read_text(encoding="utf-8")
check("10i fallback doc names the removed anti-pattern", "GGUF" in fb and "cloud-only" in fb.lower())

# ── result ──────────────────────────────────────────────────────────────────
print()
print(f"groups: 10 | passed: {len(PASSES)} | failed: {len(FAILS)}")
if FAILS:
    print("FAILED CHECKS:")
    for name, detail in FAILS:
        print(f"  - {name}: {detail}")
    sys.exit(1)
print("ALL CHECKS PASSED")
sys.exit(0)
