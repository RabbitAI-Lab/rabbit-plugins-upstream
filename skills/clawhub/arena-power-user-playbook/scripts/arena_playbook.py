#!/usr/bin/env python3
"""arena_playbook.py — executable companion for the arena-power-user-playbook skill.

Offline, python3-stdlib-only. Subcommands (machine-readable JSON out, one-line
summary on stdout):

  mode         recommend an arena.ai mode for a task (Direct/Agent/Side-by-Side/Battle)
  weak         screen a response text with heuristic weak-response flags (NOT a quality judge)
  model-check  compare a fresh leaderboard dump against the dated snapshot (rotation protocol)
  snapshot     write a new dated snapshot from a leaderboard dump
  state        manage SESSION-STATE.md for chunked multi-chat agent work
  stats        local feedback log (log/report) — the self-improvement loop
  selftest     run tools/playbook_selftest.py

Exit codes: 0 = ok/no findings, 1 = findings/changes present, 2 = usage or no data, 3 = internal error.

Grounding: arena.ai official docs and live leaderboard — see references/ for sources and dates.
This tool never judges response quality; it reports screening flags only.
"""

import argparse
import datetime as _dt
import json
import os
import re
import sys

SKILL_VERSION = "2.0.0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAPSHOT_DIR = os.path.join(ROOT, "data")


def _emit(out_path, payload, summary):
    payload["skill_version"] = SKILL_VERSION
    if out_path:
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, sort_keys=True)
            fh.write("\n")
    print(summary)
    return payload


def _exit_for(status):
    return {"ok": 0, "findings": 1, "no_data": 2, "error": 2}.get(status, 3)


def _finish(cmd, status, error, out_path=None):
    payload = {"command": cmd, "status": status, "error": error}
    if out_path:
        try:
            with open(out_path, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, indent=2, sort_keys=True)
                fh.write("\n")
        except OSError:
            pass
    print(f"command={cmd} status={status} error={error} exit={_exit_for(status)}")
    return _exit_for(status)


def _read_json_file(path, label):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh), None
    except FileNotFoundError:
        return None, f"{label} not found: {path}"
    except json.JSONDecodeError as exc:
        return None, f"{label} is not valid JSON: {path}: {exc}"
    except OSError as exc:
        return None, f"{label} unreadable: {path}: {exc}"


# ──────────────────────────────── mode advisor ──────────────────────────────

DELIVERABLE_KW = re.compile(
    r"\b(build|create|make|generate|implement|deploy|develop|write\s+(me\s+)?(a\s+)?"
    r"(app|website|site|script|dashboard|game|api|landing\s+page|crawler|bot))\b", re.I)
TOOLS_KW = re.compile(
    r"\b(web\s+search|search\s+the\s+web|research\s+and|look\s+(up|into).{0,30}(then|and)\s+(write|build|create)|"
    r"scrape|crawl|fetch.{0,30}(page|data|api))\b", re.I)


def _mode_for(task, files, steps, coding, compare, blind, budget):
    reasons = []
    if compare:
        reasons.append("compare flag: comparing two or more models on the same task")
        return "side-by-side", reasons, "high"
    if blind:
        reasons.append("blind flag: blind A/B evaluation with voting")
        return "battle", reasons, "high"
    agent = False
    if steps >= 3:
        agent = True
        reasons.append(f"steps={steps} (>=3): multi-step workflow")
    if files >= 2:
        agent = True
        reasons.append(f"files={files} (>=2): multi-file interaction")
    if files >= 1 and (coding or DELIVERABLE_KW.search(task or "") or steps >= 2):
        agent = True
        reasons.append("file present with coding/deliverable/multi-step signal")
    if coding and steps >= 2:
        agent = True
        reasons.append("coding with steps>=2: sandbox/bash iteration")
    if DELIVERABLE_KW.search(task or "") and (steps >= 2 or files >= 1):
        agent = True
        reasons.append("deliverable wording with multi-step or file input")
    if TOOLS_KW.search(task or ""):
        agent = True
        reasons.append("tool-chain wording (search/scrape/fetch + produce)")
    if agent:
        if budget and steps < 3 and files == 0:
            reasons.append("budget-conscious: downgraded to direct (low complexity)")
            return "direct", reasons, "medium"
        return "agent", reasons, "high" if len([r for r in reasons if "downgraded" not in r]) >= 1 else "medium"
    reasons.append("single-shot task: no multi-step, tool, or compare signal")
    return "direct", reasons, "high"


def cmd_mode(args):
    if args.tasks:
        data, err = _read_json_file(args.tasks, "tasks file")
        if data is None:
            _finish("mode", "error", err, args.out)
            return _exit_for("error")
        rows = data if isinstance(data, list) else data.get("tasks", [])
        if not isinstance(rows, list) or not rows:
            _finish("mode", "no_data", "tasks file has no task rows", args.out)
            return _exit_for("no_data")
        results = []
        for idx, row in enumerate(rows):
            if not isinstance(row, dict):
                continue
            task = str(row.get("task", ""))
            mode, reasons, conf = _mode_for(
                task, int(row.get("files", 0) or 0), int(row.get("steps", 1) or 1),
                bool(row.get("coding", False)), bool(row.get("compare", False)),
                bool(row.get("blind", False)), args.budget_conscious)
            results.append({"id": str(row.get("id", idx)), "mode": mode,
                            "confidence": conf, "reasons": reasons})
        counts = {}
        for r in results:
            counts[r["mode"]] = counts.get(r["mode"], 0) + 1
        _emit(args.out, {"command": "mode", "status": "ok", "n": len(results),
                         "counts": counts, "results": results},
              f"command=mode status=ok n={len(results)} counts={json.dumps(counts, sort_keys=True)} exit=0")
        return 0
    task = args.task or ""
    if not task and args.files == 0 and not (args.coding or args.compare or args.blind):
        _finish("mode", "no_data", "need --task text or at least one flag", args.out)
        return _exit_for("no_data")
    mode, reasons, conf = _mode_for(task, args.files, args.steps, args.coding,
                                    args.compare, args.blind, args.budget_conscious)
    payload = {"command": "mode", "status": "ok", "mode": mode,
               "confidence": conf, "reasons": reasons}
    headline = next((x for x in reasons if "downgraded" in x), reasons[0] if reasons else "")
    headline = re.sub(r"\s+", " ", headline)[:70]
    _emit(args.out, payload,
          f"command=mode status=ok mode={mode} confidence={conf} reason={headline} exit=0")
    return 0


# ─────────────────────────── weak-response screener ─────────────────────────

CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
REFUSAL_RE = re.compile(
    r"\bI\s+(?:can'?t|cannot|am\s+unable\s+to|do\s+not\s+have\s+(?:access|the\s+ability))\b"
    r"|\bas\s+an\s+AI\b|\bI'?m\s+(?:an\s+AI|a\s+language\s+model)\b", re.I)
APOLOGY_RE = re.compile(r"\b(sorry|apologiz\w*|my\s+apologies)\b", re.I)
VAGUE_RE = re.compile(
    r"\b(it\s+depends|generally\s+speaking|as\s+a\s+language\s+model|there\s+are\s+many\s+factors|"
    r"depends\s+on\s+the\s+context|it\s+really\s+depends|hard\s+to\s+says?\b)", re.I)
SENT_END = ".!?)"  # last-char check set


def _strip_code(text):
    text = CODE_FENCE_RE.sub(" ", text)
    text = INLINE_CODE_RE.sub(" ", text)
    return text


def screen_response(response, min_words=35, apology_rate=0.04,
                    repeat_frac=0.2, expect_short=False):
    plain = _strip_code(response)
    words = re.findall(r"\w+", plain, flags=re.UNICODE)
    n_words = len(words)
    score = 0
    flags = []
    # (a) refusal — a response that OPENS with a refusal is a refusal; a
    # refusal pattern buried in a short response (<80 words) also counts.
    # Longer responses may legitimately contain "I can't ..." mid-text.
    m = REFUSAL_RE.search(plain)
    sentences = re.split(r"(?<=[.!?])\s+", plain)
    early = m and any(REFUSAL_RE.search(s) for s in sentences[:2])
    if m and (early or n_words < 80):
        score += 30
        flags.append("refusal_pattern")
    # (b) word-count floor
    if not expect_short and n_words < min_words:
        score += 20
        flags.append(f"too_short({n_words}<{min_words})")
    # (c) apology density
    if n_words >= 5:
        apol = len(APOLOGY_RE.findall(plain))
        if apol and apol / n_words > apology_rate:
            score += 15
            flags.append(f"apology_density({apol}/{n_words})")
    # (d) vagueness fillers — the filler list is specific multi-word hedges, so
    # one occurrence in a SHORT response (<50 words) is the signal; one in a
    # long response is normal prose. Threshold 0.02 encodes exactly that.
    if n_words >= 5:
        vague = len(VAGUE_RE.findall(plain))
        if vague and vague / n_words > 0.02:
            score += 10
            flags.append(f"vagueness({vague}/{n_words})")
    # (e) repetition — repeated 5-word grams
    if n_words >= 12:
        grams = [tuple(words[i:i + 5]) for i in range(n_words - 4)]
        if grams:
            uniq = set(grams)
            top = max(grams, key=lambda g: grams.count(g))
            frac = (grams.count(top) - 1) * 5 / max(1, len(uniq) * 5)
            if frac > repeat_frac:
                score += 15
                flags.append(f"repetition(frac={round(frac, 3)})")
    # (f) truncated ending
    tail = plain.rstrip()
    if tail and tail[-1] not in SENT_END and not tail.endswith(("```", "}", "]", "|", "…")):
        score += 10
        flags.append("truncated_ending")
    score = min(100, score)
    band = "weak" if score >= 50 else "medium" if score >= 25 else "strong"
    return {"words_after_code_strip": n_words, "score": score, "band": band,
            "flags": flags,
            "note": "heuristic screening only — not a quality judgment"}


def cmd_weak(args):
    if args.response is None:
        if args.file:
            try:
                with open(args.file, "r", encoding="utf-8") as fh:
                    raw = fh.read()
            except OSError as exc:
                _finish("weak", "error", f"response file unreadable: {exc}", args.out)
                return _exit_for("error")
        else:
            _finish("weak", "no_data", "need --response TEXT or --file PATH", args.out)
            return _exit_for("no_data")
    else:
        raw = args.response
    if raw.strip() == "":
        _finish("weak", "no_data", "empty response text", args.out)
        return _exit_for("no_data")
    res = screen_response(raw, min_words=args.min_words, apology_rate=args.apology_rate,
                          repeat_frac=args.repeat_frac, expect_short=args.expect_short)
    status = "findings" if res["band"] != "strong" else "ok"
    payload = {"command": "weak", "status": status, **res,
               "thresholds": {"min_words": args.min_words, "apology_rate": args.apology_rate,
                              "repeat_frac": args.repeat_frac,
                              "bands": "weak>=50, medium>=25, strong<25"}}
    _emit(args.out, payload,
          f"command=weak status={status} band={res['band']} score={res['score']} "
          f"words={res['words_after_code_strip']} flags={','.join(res['flags']) or '-'} "
          f"exit={_exit_for(status)}")
    return _exit_for(status)


# ───────────────────────────── rotation / snapshot ──────────────────────────

TIER_WORDS = {"high", "max", "xhigh", "medium", "low"}


def _norm_entry(name):
    """Normalize a leaderboard model name -> (base, tier).
    'Claude Opus 5 (High)' -> ('claude opus 5', 'high'); 'Hy4 preview' -> ('hy4 preview', '').
    Only a TRAILING parenthetical holding a known tier word counts as a tier;
    other trailing parens (e.g. '(0813)' date suffixes) keep the full name,
    tier stays '' — matching stays consistent across snapshot and dump."""
    name = (name or "").strip()
    m = re.search(r"\s*\(([^)]*)\)\s*$", name)
    tier = ""
    base = name
    if m and m.group(1).strip().lower() in TIER_WORDS:
        tier = m.group(1).strip().lower()
        base = name[:m.start()].strip()
    base = re.sub(r"\s+", " ", base).lower()
    return base, tier


def _key(entry):
    base, tier = _norm_entry(entry)
    return f"{base}|{tier}" if tier else f"{base}|"


def _load_latest_snapshot():
    """Return ({file, data}, None) on success, (None, error) on failure."""
    cands = []
    if os.path.isdir(SNAPSHOT_DIR):
        for fn in os.listdir(SNAPSHOT_DIR):
            if fn.startswith("model_snapshot_") and fn.endswith(".json"):
                cands.append(fn)
    if not cands:
        return None, "no snapshot files in data/"
    fn = sorted(cands)[-1]
    data, err = _read_json_file(os.path.join(SNAPSHOT_DIR, fn), "snapshot")
    if data is None:
        return None, err
    return {"file": fn, "data": data}, None


def cmd_model_check(args):
    dump, err = _read_json_file(args.dump, "dump file")
    if dump is None:
        _finish("model-check", "error", err, args.out)
        return _exit_for("error")
    rows = dump if isinstance(dump, list) else dump.get("top", [])
    if not isinstance(rows, list) or not rows:
        _finish("model-check", "no_data", "dump has no model rows", args.out)
        return _exit_for("no_data")
    snap, err = _load_latest_snapshot()
    if snap is None:
        _finish("model-check", "no_data", f"no baseline snapshot: {err}", args.out)
        return _exit_for("no_data")
    snap_file, snap_data = snap["file"], snap["data"]
    snap_date = snap_data.get("snapshot_date", "")
    dump_date = (dump if isinstance(dump, dict) else {}).get("dump_date", args.date or "")
    warnings = []
    try:
        if dump_date and snap_date and dump_date < snap_date:
            warnings.append(f"dump date {dump_date} is OLDER than snapshot {snap_date} — delta is historical, not drift")
        if not dump_date:
            warnings.append("dump has no dump_date — drift direction unknown")
    except TypeError:
        warnings.append("dates not comparable")
    snap_map = {}
    for row in snap_data.get("top", []):
        snap_map[_key(row.get("model", ""))] = row
    dump_map = {}
    for row in rows:
        name = row.get("model", "")
        k = _key(name)
        if k in dump_map:
            continue
        dump_map[k] = row
    rank_drift, rotated_out, rotated_in = [], [], []
    for k, drow in dump_map.items():
        srow = snap_map.get(k)
        if srow is None:
            rotated_in.append({"model": drow.get("model"), "dump_rank": drow.get("rank"),
                               "note": "new or renamed entry — verify against live leaderboard before acting"})
        else:
            delta = srow.get("rank", 0) - drow.get("rank", 0)
            if delta != 0:
                rank_drift.append({"model": srow.get("model"), "snapshot_rank": srow.get("rank"),
                                   "dump_rank": drow.get("rank"), "delta": delta})
    for k, srow in snap_map.items():
        if k not in dump_map:
            rotated_out.append({"model": srow.get("model"), "snapshot_rank": srow.get("rank"),
                                "note": "absent from dump — rotated out, renamed, or dump covers fewer rows"})
    status = "findings" if (rank_drift or rotated_out or rotated_in) else "ok"
    payload = {"command": "model-check", "status": status,
               "snapshot_file": snap_file,
               "snapshot_date": snap_date, "dump_date": dump_date or None,
               "warnings": warnings,
               "matched": len(snap_map) - len(rotated_out),
               "rank_drift": rank_drift, "rotated_out": rotated_out, "rotated_in": rotated_in}
    _emit(args.out, payload,
          f"command=model-check status={status} matched={payload['matched']} "
          f"drift={len(rank_drift)} out={len(rotated_out)} new={len(rotated_in)} "
          f"warnings={len(warnings)} exit={_exit_for(status)}")
    return _exit_for(status)


def cmd_snapshot(args):
    dump, err = _read_json_file(args.dump, "dump file")
    if dump is None:
        _finish("snapshot", "error", err, args.out)
        return _exit_for("error")
    rows = dump if isinstance(dump, list) else dump.get("top", [])
    if not isinstance(rows, list) or not rows:
        _finish("snapshot", "no_data", "dump has no model rows", args.out)
        return _exit_for("no_data")
    top = []
    for row in rows:
        model = row.get("model")
        if not model or not isinstance(row.get("rank"), int):
            _finish("snapshot", "error",
                    f"row missing model or integer rank: {json.dumps(row)[:120]}", args.out)
            return _exit_for("error")
        top.append({
            "rank": row["rank"], "model": model, "lab": row.get("lab", ""),
            "tier": _norm_entry(model)[1],
            "net_improvement_pct": row.get("net_improvement_pct"),
            "confirmed_success_pct": row.get("confirmed_success_pct"),
            "sessions": row.get("sessions"), "cost_task_p50_usd": row.get("cost_task_p50_usd"),
        })
    ranks = [r["rank"] for r in top]
    if ranks != list(range(1, len(top) + 1)):
        _finish("snapshot", "error", "ranks must be a contiguous 1..N sequence", args.out)
        return _exit_for("error")
    date = args.date or (dump.get("dump_date") if isinstance(dump, dict) else "")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date or ""):
        _finish("snapshot", "error", "need --date YYYY-MM-DD (or dump_date in file)", args.out)
        return _exit_for("error")
    out_path = args.out or os.path.join(SNAPSHOT_DIR, f"model_snapshot_{date}.json")
    payload = {
        "snapshot_date": date,
        "source": "https://arena.ai/leaderboard/agent",
        "methodology": "causal tracing over in-the-wild Agent Mode sessions (arena.ai/blog/agent-arena-methodology)",
        "total_models": (dump.get("total_models") if isinstance(dump, dict) else args.total_models) or len(top),
        "total_sessions": (dump.get("total_sessions") if isinstance(dump, dict) else None),
        "top": top,
    }
    _emit(out_path, payload,
          f"command=snapshot status=ok date={date} rows={len(top)} out={out_path} exit=0")
    return 0


# ─────────────────────────────── state manager ──────────────────────────────

FRONT_KEYS = ("goal", "created", "updated", "phase", "chunk")


def _parse_state(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except FileNotFoundError:
        return None, "state file not found: " + path
    except OSError as exc:
        return None, f"state file unreadable: {exc}"
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not m:
        return None, "missing YAML frontmatter (expected leading --- block)"
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if ":" not in line:
            return None, f"malformed frontmatter line: {line!r}"
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"')
    for k in ("goal", "phase", "chunk"):
        if k not in meta:
            return None, f"frontmatter missing required key: {k}"
    done, nxt = [], []
    section = None
    for line in text[m.end():].splitlines():
        if line.startswith("## "):
            section = line[3:].strip().lower()
            continue
        if line.startswith("- ") and section in ("done", "next"):
            item = line[2:].strip()
            if item == "(none yet)":  # human-readable placeholder, not an item
                continue
            (done if section == "done" else nxt).append(item)
    return {"meta": meta, "done": done, "next": nxt, "path": path}, None


def _write_state(path, meta, done, nxt):
    lines = ["---"]
    for k in FRONT_KEYS:
        if k in meta:
            lines.append(f"{k}: {meta[k]}")
    lines += ["---", "", "## Done"]
    lines += [f"- {d}" for d in done] or ["- (none yet)"]
    lines += ["", "## Next"]
    lines += [f"- {n}" for n in nxt] or ["- (none yet)"]
    lines.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def cmd_state(args):
    st, err = _parse_state(args.file) if args.file else (None, None)
    if args.action == "init":
        if args.file and os.path.exists(args.file) and not args.force:
            _finish("state", "error", f"refusing to overwrite existing {args.file} (use --force)", args.out)
            return _exit_for("error")
        today = _dt.date.today().isoformat()
        meta = {"goal": args.goal, "created": today, "updated": today,
                "phase": args.phase or "start", "chunk": "1"}
        _write_state(args.file, meta, [], [args.goal])
        _emit(args.out, {"command": "state", "status": "ok", "action": "init",
                         "file": args.file, "meta": meta},
              f"command=state status=ok action=init file={args.file} exit=0")
        return 0
    if st is None:
        if err is None:
            err = "state file required: " + (args.file or "")
        _finish("state", "error", err, args.out)
        return _exit_for("error")
    meta, done, nxt = st["meta"], st["done"], st["next"]
    if args.action == "add":
        if args.done:
            for d in args.done:
                if d.lower() not in (x.lower() for x in done):
                    done.append(d)
        if args.next:
            for n in args.next:
                if n.lower() not in (x.lower() for x in nxt):
                    nxt.append(n)
        if args.phase:
            meta["phase"] = args.phase
            meta["chunk"] = str(int(meta["chunk"]) + 1)
        meta["updated"] = _dt.date.today().isoformat()
        _write_state(args.file, meta, done, nxt)
        _emit(args.out, {"command": "state", "status": "ok", "action": "add",
                         "file": args.file, "done": len(done), "next": len(nxt),
                         "phase": meta["phase"], "chunk": meta["chunk"]},
              f"command=state status=ok action=add done={len(done)} next={len(nxt)} "
              f"phase={meta['phase']} chunk={meta['chunk']} exit=0")
        return 0
    if args.action == "validate":
        ok = bool(meta.get("goal")) and (len(done) > 0 or len(nxt) > 0)
        _emit(args.out, {"command": "state", "status": "ok" if ok else "error",
                         "action": "validate", "file": args.file,
                         "done": len(done), "next": len(nxt)},
              f"command=state status={'ok' if ok else 'error'} action=validate exit={_exit_for('ok' if ok else 'error')}")
        return 0 if ok else _exit_for("error")
    if args.action == "summary":
        block = (f"[STATE-CARRY] goal: {meta['goal']} | phase: {meta['phase']} | chunk: {meta['chunk']}\n"
                 f"done: {'; '.join(done) if done else '(none)'}\n"
                 f"next: {'; '.join(nxt) if nxt else '(none)'}")
        print(block)
        return 0
    if args.action == "next":
        chunk = int(meta["chunk"]) + 1
        msg = (f"New chat, chunk {chunk}. Continue the same task — do NOT redo completed items.\n"
               f"Goal: {meta['goal']}\n"
               f"Completed so far: {'; '.join(done) if done else '(none)'}\n"
               f"Do next: {'; '.join(nxt) if nxt else '(none)'}\n"
               f"Constraints: stay within the stated goal; cite what you verify; stop and ask on blockers.")
        print(msg)
        return 0
    _finish("state", "error", f"unknown action: {args.action}", args.out)
    return _exit_for("error")


# ─────────────────────────────── stats / feedback ───────────────────────────

ALLOWED_EVENTS = ("weak_response", "mode_pick", "rotation_check",
                  "chunk_start", "chunk_end", "model_note")


def cmd_stats(args):
    log_path = args.log or os.path.join(os.getcwd(), "playbook_log.jsonl")
    if args.action == "log":
        if args.event not in ALLOWED_EVENTS:
            _finish("stats", "error",
                    f"unknown event {args.event!r}; allowed: {', '.join(ALLOWED_EVENTS)}", args.out)
            return _exit_for("error")
        entry = {"ts": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
                 "event": args.event, "model": args.model or "", "mode": args.mode or "",
                 "note": args.note or ""}
        try:
            with open(log_path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(entry, ensure_ascii=True) + "\n")
        except OSError as exc:
            _finish("stats", "error", f"cannot write log: {exc}", args.out)
            return _exit_for("error")
        _emit(args.out, {"command": "stats", "status": "ok", "action": "log",
                         "log": log_path, "entry": entry},
              f"command=stats status=ok action=log event={args.event} log={log_path} exit=0")
        return 0
    if args.action == "report":
        if not os.path.exists(log_path):
            _emit(args.out, {"command": "stats", "status": "no_data", "action": "report",
                             "log": log_path, "entries": 0},
                  f"command=stats status=no_data action=report log={log_path} entries=0 exit=2")
            return _exit_for("no_data")
        entries = []
        bad = 0
        with open(log_path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    bad += 1
        by_event, by_model, by_mode = {}, {}, {}
        dates = []
        for e in entries:
            by_event[e.get("event", "?")] = by_event.get(e.get("event", "?"), 0) + 1
            if e.get("model"):
                by_model[e["model"]] = by_model.get(e["model"], 0) + 1
            if e.get("mode"):
                by_mode[e["mode"]] = by_mode.get(e["mode"], 0) + 1
            if e.get("ts"):
                dates.append(e["ts"][:10])
        _emit(args.out, {"command": "stats", "status": "ok", "action": "report",
                         "log": log_path, "entries": len(entries), "malformed": bad,
                         "by_event": by_event, "by_model": by_model, "by_mode": by_mode,
                         "date_min": min(dates) if dates else None,
                         "date_max": max(dates) if dates else None},
              f"command=stats status=ok action=report entries={len(entries)} "
              f"events={json.dumps(by_event, sort_keys=True)} exit=0")
        return 0
    _finish("stats", "error", f"unknown action: {args.action}", args.out)
    return _exit_for("error")


def cmd_selftest(_args):
    import subprocess
    proc = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "playbook_selftest.py")])
    return proc.returncode


def main(argv=None):
    p = argparse.ArgumentParser(prog="arena_playbook.py",
                                description="Executable companion for the arena-power-user-playbook skill.")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_out(pp):
        pp.add_argument("--out", help="write full JSON result to this path")

    pp = sub.add_parser("mode", help="recommend arena.ai mode for a task")
    pp.add_argument("--task", help="task description text")
    pp.add_argument("--files", type=int, default=0)
    pp.add_argument("--steps", type=int, default=1)
    pp.add_argument("--coding", action="store_true")
    pp.add_argument("--compare", action="store_true")
    pp.add_argument("--blind", action="store_true")
    pp.add_argument("--budget-conscious", dest="budget_conscious", action="store_true")
    pp.add_argument("--tasks", help="JSON file with a list of {task,files,steps,coding,compare,blind}")
    add_out(pp)
    pp.set_defaults(fn=cmd_mode)

    pp = sub.add_parser("weak", help="heuristic weak-response screening (not a quality judge)")
    pp.add_argument("--response", help="response text to screen")
    pp.add_argument("--file", help="read response text from file")
    pp.add_argument("--min-words", type=int, default=35)
    pp.add_argument("--apology-rate", type=float, default=0.04)
    pp.add_argument("--repeat-frac", type=float, default=0.2)
    pp.add_argument("--expect-short", action="store_true", help="disable the word-count floor")
    add_out(pp)
    pp.set_defaults(fn=cmd_weak)

    pp = sub.add_parser("model-check", help="compare a fresh leaderboard dump vs the dated snapshot")
    pp.add_argument("--dump", required=True, help="dump JSON (list of {rank, model, ...} or {top:[...]})")
    pp.add_argument("--date", help="dump date YYYY-MM-DD (else uses dump_date in file)")
    add_out(pp)
    pp.set_defaults(fn=cmd_model_check)

    pp = sub.add_parser("snapshot", help="write a new dated snapshot from a dump")
    pp.add_argument("--dump", required=True)
    pp.add_argument("--date", help="snapshot date YYYY-MM-DD (else dump_date in file)")
    pp.add_argument("--total-models", type=int, default=0)
    pp.add_argument("--out", help="output path (default data/model_snapshot_DATE.json)")
    pp.set_defaults(fn=cmd_snapshot)

    pp = sub.add_parser("state", help="manage SESSION-STATE.md for chunked agent work")
    pp.add_argument("--file", required=True)
    pp.add_argument("--action", required=True, choices=["init", "add", "summary", "next", "validate"])
    pp.add_argument("--goal", help="task goal (init)")
    pp.add_argument("--phase", help="current phase (init/add)")
    pp.add_argument("--done", nargs="*", help="completed items (add)")
    pp.add_argument("--next", nargs="*", help="next items (add)")
    pp.add_argument("--force", action="store_true", help="allow overwrite on init")
    add_out(pp)
    pp.set_defaults(fn=cmd_state)

    pp = sub.add_parser("stats", help="local feedback log/report")
    pp.add_argument("--action", required=True, choices=["log", "report"])
    pp.add_argument("--event", help="one of: " + ", ".join(ALLOWED_EVENTS))
    pp.add_argument("--model", default="")
    pp.add_argument("--mode", default="")
    pp.add_argument("--note", default="")
    pp.add_argument("--log", help="log path (default ./playbook_log.jsonl)")
    add_out(pp)
    pp.set_defaults(fn=cmd_stats)

    pp = sub.add_parser("selftest", help="run the skill self-test")
    pp.set_defaults(fn=cmd_selftest)

    args = p.parse_args(argv)
    try:
        return args.fn(args)
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 — contract: never crash without exit 3
        print(f"command={args.cmd} status=error error=internal: {type(exc).__name__}: {exc} exit=3")
        return 3


if __name__ == "__main__":
    sys.exit(main())
