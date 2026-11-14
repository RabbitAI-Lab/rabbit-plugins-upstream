#!/usr/bin/env python3
"""
engram-sleep.py — Nightly "sleep" consolidation pipeline for Engram (Phase 4B).

Design follows research/cogsci-memory-2026.md, research/memory-systems-2026.md,
and research/engram-research-synthesis-jul05.md:
  - Sleep-time consolidation: replay recent episodic memory, distil the durable
    gist, forget the rest — done offline, not on the hot recall path.
  - Event segmentation: cut the episodic stream at topic-shift boundaries
    (embedding-similarity drops), so each segment is one "episode".
  - Predict-calibrate distillation: only what is SURPRISING or durably useful
    given what the engram already knows becomes new semantic memory.
  - Adaptive forgetting: age-decay × reinforcement strength; weak, old episodics
    are compressed into monthly digests, never hard-deleted.

SAFETY MODEL
  * Defaults to --dry-run: reads only, mutates NOTHING, prints what it WOULD do.
  * Mutations happen ONLY with --apply, which first takes a full DB backup via
    scripts/engram-backup.py.
  * NOTHING is ever hard-deleted. Pruned/merged nodes are snapshotted into a
    `sleep_archive` table and marked with an `archived|<type>` type prefix —
    fully reversible.
  * engram/engram.db is a LIVE WAL SQLite DB. We use short read-only connections
    (mode=ro) for reads, PRAGMA busy_timeout=5000, and never hold long
    transactions. sqlite3 CLI is not required — pure python3 sqlite3 module.
  * All summarization uses the LOCAL ollama model glm-5.1:cloud via the HTTP API
    at localhost:11434. If ollama is unavailable, LLM stages are skipped
    gracefully and the arithmetic stages still run. Zero paid-API calls.

STAGES (each independently runnable; all respect --dry-run):
  1. SEGMENT  — segment last N days of episodic nodes at topic-shift boundaries.
  2. DISTIL   — predict-calibrate: surprising/durable gist → candidate knowledge
                nodes (stored via engram store so supersede/dedup applies).
  3. MERGE    — near-duplicate knowledge nodes (cosine>0.93 + name fuzzy) → merge
                proposals; --apply archives the loser, re-points its associations.
  4. PRUNE    — age-decay × reinforcement strength; old weak episodics compressed
                into monthly digests, originals archived. Never touches protected
                types / trauma tier / useful_count>0.
  5. REPORT   — run summary to logs/engram-sleep.log (counts, changes, timing).

USAGE
  python3 scripts/engram-sleep.py --dry-run --days 2          # safe preview (default)
  python3 scripts/engram-sleep.py --dry-run --segment --distil
  python3 scripts/engram-sleep.py --apply                     # supervisor-gated

This script NEVER edits engram/engram.py or any existing system file. It is not
wired into cron — scheduling is the supervisor's separate decision.
"""

import argparse
import json
import os
import re
import struct
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from difflib import SequenceMatcher

# ── Paths ───────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Engram: load paths from config
try:
    import bpconfig
    _cfg = bpconfig.load_config()
    WORKSPACE = _cfg["workspace"]
    DB_PATH = _cfg["db_path"]
    ENGRAM_CLI = os.path.join(_cfg["engram_dir"], "engram.py")
    BQ_CLI = os.path.join(_cfg["engram_dir"], "bq.py")
    BACKUP_CLI = os.path.join(_cfg["scripts_dir"], "engram-backup.py")
    LOG_PATH = os.path.join(_cfg["logs_dir"], "engram-sleep.log")
except Exception:
    WORKSPACE = os.path.dirname(SCRIPT_DIR)
    DB_PATH = os.path.join(WORKSPACE, "engram", "engram.db")
    ENGRAM_CLI = os.path.join(WORKSPACE, "engram", "engram.py")
    BQ_CLI = os.path.join(WORKSPACE, "engram", "bq.py")
    BACKUP_CLI = os.path.join(SCRIPT_DIR, "engram-backup.py")
    LOG_PATH = os.path.join(WORKSPACE, "logs", "engram-sleep.log")

# ── Domain constants (mirrored READ-ONLY from engram/engram.py — not imported
#    to avoid triggering its on-open side effects against the live DB) ─────────
# EPISODIC_NODE_TYPES in engram.py + the email/event kinds named in the spec.
EPISODIC_TYPES = {
    "message_sent", "message_received", "heartbeat_log", "project_action",
    "session_summary", "email_event", "event",
}
# Types produced by distillation (semantic memory). knowledge is the default so
# _SUPERSEDE_ELIGIBLE_TYPES machinery in engram.py kicks in on store.
SEMANTIC_OUTPUT_TYPE = "knowledge"
# Near-duplicate merge operates over truth-maintained semantic types ONLY.
# 'lesson' is deliberately EXCLUDED: lessons are trauma-tier protected memory
# and their formulaic "Reflection YYYY-MM-DD: ..." names produce dangerous
# transitive over-merges (distinct daily reflections look near-duplicate).
MERGE_TYPES = {"knowledge", "fact", "concept"}
# Never prune / never archive during decay (spec + engram trauma/important tiers).
PROTECTED_TYPES = {
    "rule", "decision", "method", "person", "organization", "project",
    "credential", "config", "lesson", "troubleshooting", "fact", "knowledge",
    "policy", "mission_active", "mission_step",
}
# Trauma-tier tags — a node carrying any of these never ages out.
TRAUMA_TAGS = {"fix", "workaround", "solution", "bug", "troubleshooting",
               "lesson", "gotcha", "critical"}

OLLAMA_URL = "http://localhost:11434/api/generate"
# Model policy: recurring pipelines run on genuinely LOCAL
# models only. ":cloud" names are ollama's remote relay and are refused outright.
OLLAMA_MODEL = os.environ.get("SLEEP_MODEL", "qwen2.5:3b-instruct")
if ":cloud" in OLLAMA_MODEL:
    sys.exit(f"refusing model '{OLLAMA_MODEL}': cloud relay models are banned "
             f"in recurring pipelines (set SLEEP_MODEL to a local model)")

# ── Tunables (all overridable via CLI) ──────────────────────────────────────
DEFAULT_DAYS = 1
SEGMENT_SIM_THRESHOLD = 0.45   # cosine drop below this => topic-shift boundary
SEGMENT_MAX_ITEMS = 12         # hard cap on items per segment
MERGE_COSINE = 0.95            # spec floor is 0.93; raised to curb sibling merges
MERGE_NAME_FUZZ = 0.72         # SequenceMatcher ratio on names (belt & braces)
MERGE_MAX_CLUSTER = 5          # clusters larger than this are FLAGGED, never auto-applied
PRUNE_AGE_DAYS = 180           # spec: only episodics older than this
PRUNE_STRENGTH = 0.15          # strength below this => prune candidate
DECAY_TAU_DAYS = 60.0          # exponential recency decay constant
MAX_NEW_NODES = 10             # spec: cap new semantic nodes per run
OLLAMA_TIMEOUT = 120           # seconds per LLM call


# ── LLM token accounting (module-level, filled by ollama_generate) ──────────
_LLM_STATS = {"calls": 0, "prompt_tokens": 0, "eval_tokens": 0, "wall_s": 0.0,
              "available": None}


# ════════════════════════════════════════════════════════════════════════════
# DB helpers — short read-only connections
# ════════════════════════════════════════════════════════════════════════════
def ro_conn():
    """Read-only connection. Cannot mutate even if code tries to."""
    import sqlite3
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True, timeout=5.0)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA busy_timeout=5000")
    return con


def rw_conn():
    """Writable connection — used ONLY under --apply for archive bookkeeping."""
    import sqlite3
    con = sqlite3.connect(DB_PATH, timeout=10.0)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA busy_timeout=5000")
    return con


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def parse_ts(s):
    """Parse engram ISO timestamps (handles trailing Z and naive strings)."""
    if not s:
        return None
    s = s.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        # last resort: date only
        try:
            dt = datetime.fromisoformat(s[:19])
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def age_days(ts_str, ref=None):
    dt = parse_ts(ts_str)
    if dt is None:
        return 0.0
    ref = ref or datetime.now(timezone.utc)
    return max(0.0, (ref - dt).total_seconds() / 86400.0)


def unpack_vec(blob):
    import numpy as np
    n = len(blob) // 4
    return np.array(struct.unpack(f"{n}f", blob), dtype=np.float32)


def fetch_embeddings(con, node_ids):
    """{node_id: np.float32 vec} for the given ids (missing ids simply absent)."""
    if not node_ids:
        return {}
    out = {}
    ph = ",".join("?" * len(node_ids))
    for r in con.execute(
        f"SELECT node_id, embedding FROM embeddings WHERE node_id IN ({ph})",
        list(node_ids),
    ):
        try:
            out[r["node_id"]] = unpack_vec(r["embedding"])
        except Exception:
            pass
    return out


def cosine(a, b):
    import numpy as np
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na * nb))


def base_type(t):
    """Strip pipe-suffixes engram appends to types (e.g. 'task|done' -> 'task')."""
    return (t or "").split("|", 1)[0].lower()


def is_protected(con, row):
    """True if a node must never be archived/pruned: protected type, reinforced
    (useful_count>0), or carrying a trauma-tier tag."""
    if base_type(row["type"]) in PROTECTED_TYPES:
        return True
    if (row["useful_count"] or 0) > 0:
        return True
    if TRAUMA_TAGS & node_tags(con, row["id"]):
        return True
    return False


def node_tags(con, node_id):
    return {
        r["name"]
        for r in con.execute(
            "SELECT t.name FROM node_tags nt JOIN tags t ON t.id = nt.tag_id "
            "WHERE nt.node_id = ?",
            (node_id,),
        )
    }


# ════════════════════════════════════════════════════════════════════════════
# Ollama (local LLM) — graceful degradation
# ════════════════════════════════════════════════════════════════════════════
# --no-llm sets this. Every LLM path in this file goes through ollama_available(),
# and each one already has a deterministic fallback for an unreachable ollama, so
# one flag turns the whole pipeline arithmetic. Measured over 75 nights on a live
# graph: 314 of 340 segments distilled to nothing, at roughly 2.5 minutes of local
# GPU each. The deterministic run finishes in under a second. If your own log says
# otherwise, keep the LLM on — this is a switch, not a verdict.
LLM_DISABLED = False


def ollama_available():
    if LLM_DISABLED:
        return False
    if _LLM_STATS["available"] is not None:
        return _LLM_STATS["available"]
    try:
        req = urllib.request.Request("http://localhost:11434/api/tags")
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        names = {m.get("name", "") for m in data.get("models", [])}
        _LLM_STATS["available"] = OLLAMA_MODEL in names
    except Exception:
        _LLM_STATS["available"] = False
    return _LLM_STATS["available"]


def ollama_generate(prompt, system=None, temperature=0.2):
    """Call glm-5.1:cloud via HTTP. Returns clean text, or None on any failure.
    Thinking is disabled; if the model still emits <think> blocks they're stripped."""
    if not ollama_available():
        return None
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"temperature": temperature},
    }
    if system:
        payload["system"] = system
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=body, headers={"Content-Type": "application/json"}
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=OLLAMA_TIMEOUT) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        sys.stderr.write(f"[ollama] call failed: {e}\n")
        return None
    dt = time.time() - t0
    _LLM_STATS["calls"] += 1
    _LLM_STATS["wall_s"] += dt
    _LLM_STATS["prompt_tokens"] += int(data.get("prompt_eval_count", 0) or 0)
    _LLM_STATS["eval_tokens"] += int(data.get("eval_count", 0) or 0)
    text = data.get("response", "") or ""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    return text


def extract_json(text):
    """Pull the first JSON array/object out of an LLM reply. Returns obj or None."""
    if not text:
        return None
    # try fenced block first
    m = re.search(r"```(?:json)?\s*(.*?)```", text, flags=re.DOTALL)
    candidate = m.group(1).strip() if m else text.strip()
    for opener, closer in (("[", "]"), ("{", "}")):
        s = candidate.find(opener)
        e = candidate.rfind(closer)
        if s != -1 and e != -1 and e > s:
            try:
                return json.loads(candidate[s:e + 1])
            except json.JSONDecodeError:
                continue
    return None


# ════════════════════════════════════════════════════════════════════════════
# STAGE 1 — SEGMENT
# ════════════════════════════════════════════════════════════════════════════
def load_episodic(con, days):
    ph = ",".join("?" * len(EPISODIC_TYPES))
    rows = con.execute(
        f"""SELECT id, name, type, content, created_at, touch_count, useful_count
            FROM nodes
            WHERE type IN ({ph})
              AND created_at >= datetime('now', ?)
            ORDER BY created_at ASC""",
        (*EPISODIC_TYPES, f"-{days} days"),
    ).fetchall()
    return [dict(r) for r in rows]


def stage_segment(con, days, report):
    items = load_episodic(con, days)
    report["segment"]["episodic_nodes"] = len(items)
    if not items:
        report["segment"]["segments"] = []
        return []

    embs = fetch_embeddings(con, [it["id"] for it in items])
    segments = []
    current = [items[0]]
    boundaries = 0
    for prev, cur in zip(items, items[1:]):
        va, vb = embs.get(prev["id"]), embs.get(cur["id"])
        sim = cosine(va, vb) if (va is not None and vb is not None) else 0.0
        shift = sim < SEGMENT_SIM_THRESHOLD
        if shift or len(current) >= SEGMENT_MAX_ITEMS:
            segments.append(current)
            current = [cur]
            if shift:
                boundaries += 1
        else:
            current.append(cur)
    segments.append(current)

    report["segment"]["boundaries"] = boundaries
    report["segment"]["segments"] = [
        {
            "n": len(seg),
            "start": seg[0]["created_at"],
            "end": seg[-1]["created_at"],
            "sample": seg[0]["name"][:70],
        }
        for seg in segments
    ]
    return segments


# ════════════════════════════════════════════════════════════════════════════
# STAGE 2 — DISTIL (predict-calibrate)
# ════════════════════════════════════════════════════════════════════════════
def segment_text(seg):
    lines = []
    for it in seg:
        body = (it.get("content") or "").strip().replace("\n", " ")
        lines.append(f"- [{it['type']}] {it['name']}: {body[:240]}")
    return "\n".join(lines)


def related_knowledge(seg, limit=8):
    """Query existing knowledge for calibration context, via bq recall --compact."""
    seed = " ".join(it["name"] for it in seg[:3])[:120]
    if not seed.strip():
        return ""
    try:
        out = subprocess.run(
            [sys.executable, BQ_CLI, "recall", seed, "--compact",
             "--fast", "--limit", str(limit)],
            capture_output=True, text=True, timeout=30,
        )
        return out.stdout.strip()[:2000]
    except Exception as e:
        return f"(recall unavailable: {e})"


DISTIL_SYSTEM = (
    "You are the sleep-consolidation module of a personal memory system. "
    "You extract only durable, generalizable knowledge from a batch of raw "
    "episodic events. You are strict: most chatter is NOT worth remembering."
)


def distil_prompt(seg, known):
    return f"""Given what the memory system ALREADY KNOWS, decide what in the following
batch of recent episodic events is SURPRISING or DURABLY USEFUL enough to become
long-term semantic memory. Ignore routine chatter, acknowledgements, and things
already known.

ALREADY KNOWN (existing related knowledge):
{known or '(nothing closely related found)'}

RECENT EPISODIC EVENTS (one segment / topic):
{segment_text(seg)}

Return a JSON array (possibly empty) of at most 3 items. Each item:
{{"name": "<short unique title, <60 chars>",
  "content": "<one or two sentences of the durable fact/lesson>",
  "why_surprising": "<why this is new or non-obvious given what's known>"}}
Return ONLY the JSON array, nothing else. If nothing is worth keeping, return [].
"""


def stage_distil(con, segments, report, apply_changes):
    report["distil"]["segments_considered"] = len(segments)
    if not ollama_available():
        report["distil"]["skipped"] = ("--no-llm" if LLM_DISABLED
                                       else f"ollama/{OLLAMA_MODEL} unavailable")
        return []

    candidates = []
    for seg in segments:
        if len(candidates) >= MAX_NEW_NODES:
            break
        known = related_knowledge(seg)
        reply = ollama_generate(distil_prompt(seg, known), system=DISTIL_SYSTEM)
        parsed = extract_json(reply)
        if not isinstance(parsed, list):
            continue
        for item in parsed:
            if len(candidates) >= MAX_NEW_NODES:
                break
            name = (item.get("name") or "").strip()
            content = (item.get("content") or "").strip()
            if not name or not content:
                continue
            candidates.append({
                "name": name,
                "content": content,
                "why": (item.get("why_surprising") or "").strip(),
                "seg_start": seg[0]["created_at"],
            })

    report["distil"]["candidates"] = candidates
    report["distil"]["candidate_count"] = len(candidates)

    if apply_changes and candidates:
        stored = []
        for c in candidates:
            props = json.dumps({
                "source": "sleep-consolidation",
                "why_surprising": c["why"],
                "distilled_at": now_iso(),
            })
            try:
                r = subprocess.run(
                    [sys.executable, ENGRAM_CLI, "store",
                     "--name", c["name"], "--type", SEMANTIC_OUTPUT_TYPE,
                     "--content", c["content"], "--props", props,
                     "--tags", "sleep-consolidation,distilled"],
                    capture_output=True, text=True, timeout=60,
                )
                stored.append({"name": c["name"], "rc": r.returncode,
                               "out": r.stdout.strip()[:200]})
            except Exception as e:
                stored.append({"name": c["name"], "error": str(e)})
        report["distil"]["stored"] = stored
    return candidates


# ════════════════════════════════════════════════════════════════════════════
# STAGE 3 — MERGE (near-duplicate semantic nodes)
# ════════════════════════════════════════════════════════════════════════════
def stage_merge(con, report, apply_changes):
    ph = ",".join("?" * len(MERGE_TYPES))
    rows = con.execute(
        f"""SELECT id, name, type, content, created_at, updated_at,
                   touch_count, useful_count
            FROM nodes WHERE type IN ({ph})
            ORDER BY id ASC""",
        tuple(MERGE_TYPES),
    ).fetchall()
    rows = [dict(r) for r in rows]
    report["merge"]["candidate_pool"] = len(rows)
    if len(rows) < 2:
        report["merge"]["pairs"] = []
        return []

    embs = fetch_embeddings(con, [r["id"] for r in rows])
    have = [r for r in rows if r["id"] in embs]

    # Fewer than two vectors means there is no pair to compare. On a keyword-only
    # install, or on a database nobody has run `embed` against yet, this is the
    # normal case — it used to reach numpy and raise an AxisError on a 1-D array.
    if len(have) < 2:
        report["merge"]["pairs"] = []
        report["merge"]["skipped"] = (f"{len(have)} of {len(rows)} candidates are "
                                      f"embedded; need at least 2")
        return []

    import numpy as np
    ids = [r["id"] for r in have]
    mat = np.array([embs[i] for i in ids], dtype=np.float32)
    norms = np.linalg.norm(mat, axis=1, keepdims=True)
    norms[norms == 0] = 1e-9
    matn = mat / norms
    sims = matn @ matn.T

    by_id = {r["id"]: r for r in have}

    # --- Union-Find over qualifying edges, so a duplicate CLUSTER collapses to
    #     exactly one winner. This prevents the chaining bug where a node is the
    #     winner of one pair but the loser of another (archiving a node we just
    #     merged into). ---
    parent = {i: i for i in ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    edges = 0
    edge_meta = {}  # frozenset({a,b}) -> (cosine, fuzz) for reporting
    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            if sims[a, b] < MERGE_COSINE:
                continue
            ra, rb = by_id[ids[a]], by_id[ids[b]]
            fuzz = SequenceMatcher(None, ra["name"].lower(),
                                   rb["name"].lower()).ratio()
            if fuzz < MERGE_NAME_FUZZ:
                continue
            union(ids[a], ids[b])
            edges += 1
            edge_meta[frozenset((ids[a], ids[b]))] = (float(sims[a, b]), fuzz)

    # winner = most reinforced, then most touched, then newest
    def rank(r):
        return (r["useful_count"] or 0, r["touch_count"] or 0,
                r["updated_at"] or r["created_at"] or "")

    groups = {}
    for i in ids:
        groups.setdefault(find(i), []).append(i)

    clusters = []      # auto-safe merge proposals
    flagged = []       # too large to auto-collapse — human review only
    for root, members in groups.items():
        if len(members) < 2:
            continue
        recs = [by_id[m] for m in members]
        recs.sort(key=rank, reverse=True)
        winner = recs[0]
        # never archive a protected/reinforced/trauma node — it stays put
        losers = [l for l in recs[1:] if not is_protected(con, l)]
        if not losers:
            continue
        # strongest evidence edge anywhere inside the cluster (members may be
        # bridged loser<->loser, so don't restrict to winner<->loser edges)
        member_ids = {winner["id"]} | {l["id"] for l in losers}
        best_cos = max(
            (cos for key, (cos, _f) in edge_meta.items() if key <= member_ids),
            default=0.0)
        entry = {
            "size": len(members),
            "best_cosine": round(best_cos, 4),
            "winner": {"id": winner["id"], "name": winner["name"]},
            "losers": [{"id": l["id"], "name": l["name"]} for l in losers],
        }
        # Guard 1: oversized transitive clusters are almost always formulaic
        # near-duplicates bridged together, not one true duplicate set.
        # Guard 2: best_cos < threshold means the surviving members only cohered
        # THROUGH a member we excluded (protected) — no direct evidence remains,
        # so don't auto-archive on a broken bridge.
        # Either way: flag for human review instead of auto-collapsing.
        if len(members) > MERGE_MAX_CLUSTER or best_cos < MERGE_COSINE:
            flagged.append(entry)
        else:
            clusters.append(entry)
    clusters.sort(key=lambda c: -c["size"])
    flagged.sort(key=lambda c: -c["size"])

    report["merge"]["qualifying_edges"] = edges
    report["merge"]["clusters"] = clusters
    report["merge"]["cluster_count"] = len(clusters)
    report["merge"]["flagged_large"] = flagged
    report["merge"]["flagged_count"] = len(flagged)
    report["merge"]["nodes_to_archive"] = sum(len(c["losers"]) for c in clusters)

    if apply_changes and clusters:
        applied = []
        for c in clusters:
            for l in c["losers"]:
                applied.append(
                    archive_and_repoint(l["id"], c["winner"]["id"],
                                        reason="merge:near-duplicate"))
        report["merge"]["applied"] = applied
    return clusters


# ════════════════════════════════════════════════════════════════════════════
# STAGE 4 — DECAY / PRUNE
# ════════════════════════════════════════════════════════════════════════════
def strength(node, ref):
    """age-decay × reinforcement. Higher = keep."""
    import math
    a = age_days(node["created_at"], ref)
    recency = math.exp(-a / DECAY_TAU_DAYS)
    reinforce = 1.0 + math.log1p((node["touch_count"] or 0)
                                 + 2 * (node["useful_count"] or 0))
    return recency * reinforce


def stage_prune(con, report, apply_changes):
    ph = ",".join("?" * len(EPISODIC_TYPES))
    rows = con.execute(
        f"""SELECT id, name, type, content, created_at, touch_count, useful_count
            FROM nodes WHERE type IN ({ph})
              AND created_at < datetime('now', ?)
            ORDER BY created_at ASC""",
        (*EPISODIC_TYPES, f"-{PRUNE_AGE_DAYS} days"),
    ).fetchall()
    rows = [dict(r) for r in rows]
    report["prune"]["aged_episodic"] = len(rows)

    ref = datetime.now(timezone.utc)
    victims = []
    for r in rows:
        if is_protected(con, r):
            continue
        s = strength(r, ref)
        if s >= PRUNE_STRENGTH:
            continue
        victims.append({"id": r["id"], "name": r["name"], "type": r["type"],
                        "created_at": r["created_at"], "strength": round(s, 4)})

    # cluster victims by year-month => one digest node each
    clusters = {}
    for v in victims:
        dt = parse_ts(v["created_at"])
        key = dt.strftime("%Y-%m") if dt else "unknown"
        clusters.setdefault(key, []).append(v)

    report["prune"]["prune_candidates"] = len(victims)
    report["prune"]["digests"] = [
        {"month": k, "count": len(v), "example": v[0]["name"][:60]}
        for k, v in sorted(clusters.items())
    ]

    if apply_changes and clusters:
        applied = []
        for month, vs in sorted(clusters.items()):
            digest_name = f"Episodic digest {month}"
            summary = summarize_digest(month, vs)
            props = json.dumps({
                "source": "sleep-consolidation",
                "digest_month": month,
                "archived_ids": [v["id"] for v in vs],
                "created_at": now_iso(),
            })
            store_rc = None
            try:
                r = subprocess.run(
                    [sys.executable, ENGRAM_CLI, "store",
                     "--name", digest_name, "--type", "session_summary",
                     "--content", summary, "--props", props,
                     "--tags", "sleep-consolidation,digest"],
                    capture_output=True, text=True, timeout=60)
                store_rc = r.returncode
            except Exception as e:
                store_rc = f"error:{e}"
            arch = [archive_and_repoint(v["id"], None, reason=f"prune:digest:{month}")
                    for v in vs]
            applied.append({"month": month, "digest_rc": store_rc,
                            "archived": len(arch)})
        report["prune"]["applied"] = applied
    return victims


def summarize_digest(month, victims):
    names = "\n".join(f"- {v['name']}" for v in victims[:40])
    if ollama_available():
        reply = ollama_generate(
            f"Summarize this batch of {len(victims)} old low-value episodic memory "
            f"items from {month} into 2-3 sentences capturing anything worth "
            f"remembering. Items:\n{names}\n\nSummary:",
            temperature=0.3)
        if reply:
            return f"[{month}] {reply}"
    return f"[{month}] Digest of {len(victims)} archived episodic items:\n{names}"


# ════════════════════════════════════════════════════════════════════════════
# Archive machinery (mutating — only reached under --apply)
# ════════════════════════════════════════════════════════════════════════════
def ensure_archive_table(con):
    con.execute("""
        CREATE TABLE IF NOT EXISTS sleep_archive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            node_id INTEGER,
            name TEXT, type TEXT, content TEXT, props TEXT,
            created_at TEXT, updated_at TEXT,
            archived_at TEXT, reason TEXT, merged_into INTEGER
        )""")


def archive_and_repoint(loser_id, winner_id, reason):
    """Reversibly archive a node: snapshot into sleep_archive, prefix its type
    with 'archived|', and (for merges) re-point its associations to the winner.
    Returns a small dict describing what happened. Mutating — --apply only."""
    con = rw_conn()
    try:
        ensure_archive_table(con)
        row = con.execute("SELECT * FROM nodes WHERE id = ?", (loser_id,)).fetchone()
        if not row:
            return {"node_id": loser_id, "status": "missing"}
        keys = row.keys()
        con.execute(
            """INSERT INTO sleep_archive
               (node_id, name, type, content, props, created_at, updated_at,
                archived_at, reason, merged_into)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (row["id"], row["name"], row["type"], row["content"],
             row["props"] if "props" in keys else "{}",
             row["created_at"], row["updated_at"] if "updated_at" in keys else "",
             now_iso(), reason, winner_id))
        repointed = 0
        if winner_id:
            # re-point associations, skipping ones that would violate UNIQUE
            for rel in ("source_id", "target_id"):
                for a in con.execute(
                    f"SELECT id FROM associations WHERE {rel} = ?", (loser_id,)
                ).fetchall():
                    try:
                        con.execute(
                            f"UPDATE associations SET {rel} = ? WHERE id = ?",
                            (winner_id, a["id"]))
                        repointed += 1
                    except Exception:
                        pass  # duplicate edge — leave it; loser is archived anyway
        # mark node archived (reversible: original type kept in sleep_archive)
        cur_type = row["type"] or "concept"
        if not cur_type.startswith("archived|"):
            con.execute("UPDATE nodes SET type = ? WHERE id = ?",
                        (f"archived|{cur_type}", loser_id))
        con.commit()
        return {"node_id": loser_id, "status": "archived",
                "repointed_assocs": repointed, "merged_into": winner_id}
    finally:
        con.close()


# ════════════════════════════════════════════════════════════════════════════
# Reporting
# ════════════════════════════════════════════════════════════════════════════
def non_episodic_count(con):
    ph = ",".join("?" * len(EPISODIC_TYPES))
    return con.execute(
        f"SELECT COUNT(*) FROM nodes WHERE type NOT IN ({ph})",
        tuple(EPISODIC_TYPES),
    ).fetchone()[0]


def render_report(report, mode, wall_s):
    L = []
    L.append("=" * 72)
    L.append(f"Engram SLEEP run @ {report['started']}  mode={mode}")
    L.append(f"days={report['params']['days']}  stages={report['params']['stages']}")
    L.append("-" * 72)

    if "segment" in report["ran"]:
        s = report["segment"]
        L.append(f"[SEGMENT] episodic nodes={s.get('episodic_nodes',0)} "
                 f"segments={len(s.get('segments',[]))} "
                 f"boundaries={s.get('boundaries',0)}")
        for seg in s.get("segments", [])[:12]:
            L.append(f"   • {seg['n']:2d} items | {seg['start'][:19]} | {seg['sample']}")

    if "distil" in report["ran"]:
        d = report["distil"]
        if d.get("skipped"):
            L.append(f"[DISTIL]  SKIPPED — {d['skipped']}")
        else:
            L.append(f"[DISTIL]  segments={d.get('segments_considered',0)} "
                     f"candidate knowledge nodes={d.get('candidate_count',0)} "
                     f"(cap {MAX_NEW_NODES})")
            for c in d.get("candidates", []):
                L.append(f"   + {c['name']}")
                L.append(f"       {c['content'][:140]}")
            for st in d.get("stored", []):
                L.append(f"   STORED rc={st.get('rc')} {st.get('name')}")

    if "merge" in report["ran"]:
        m = report["merge"]
        L.append(f"[MERGE]   pool={m.get('candidate_pool',0)} "
                 f"edges={m.get('qualifying_edges',0)} "
                 f"auto_clusters={m.get('cluster_count',0)} "
                 f"→ nodes_to_archive={m.get('nodes_to_archive',0)} | "
                 f"flagged_large={m.get('flagged_count',0)} "
                 f"(cosine>{MERGE_COSINE}, fuzz>{MERGE_NAME_FUZZ}, max_cluster={MERGE_MAX_CLUSTER})")
        for c in m.get("clusters", [])[:25]:
            L.append(f"   * KEEP #{c['winner']['id']} '{c['winner']['name'][:44]}' "
                     f"(size {c['size']}, best_cos {c['best_cosine']})")
            for l in c["losers"]:
                L.append(f"        ⟵ archive #{l['id']} '{l['name'][:52]}'")
        for c in m.get("flagged_large", [])[:10]:
            L.append(f"   ⚠ REVIEW (size {c['size']}, not auto-applied) "
                     f"anchor #{c['winner']['id']} '{c['winner']['name'][:44]}'")
        for ap in m.get("applied", []):
            L.append(f"   APPLIED {ap}")

    if "prune" in report["ran"]:
        p = report["prune"]
        L.append(f"[PRUNE]   aged episodic (>{PRUNE_AGE_DAYS}d)={p.get('aged_episodic',0)} "
                 f"prune candidates={p.get('prune_candidates',0)}")
        for dg in p.get("digests", []):
            L.append(f"   ▸ {dg['month']}: {dg['count']} items → 1 digest "
                     f"(e.g. {dg['example']})")
        for ap in p.get("applied", []):
            L.append(f"   APPLIED {ap}")

    L.append("-" * 72)
    ls = _LLM_STATS
    L.append(f"[LLM] model={OLLAMA_MODEL} available={ls['available']} "
             f"calls={ls['calls']} prompt_tok={ls['prompt_tokens']} "
             f"eval_tok={ls['eval_tokens']} llm_wall={ls['wall_s']:.1f}s")
    L.append(f"[DB] non-episodic nodes before={report['db']['non_epis_before']} "
             f"after={report['db']['non_epis_after']} "
             f"(delta={report['db']['non_epis_after']-report['db']['non_epis_before']})")
    L.append(f"[TIME] total wall={wall_s:.1f}s")
    if mode == "dry-run":
        L.append("DRY-RUN: no mutations performed. Re-run with --apply to enact.")
    L.append("=" * 72)
    return "\n".join(L)


# ════════════════════════════════════════════════════════════════════════════
# Backup (apply only)
# ════════════════════════════════════════════════════════════════════════════
def take_backup():
    print("[apply] taking DB backup via scripts/engram-backup.py ...")
    r = subprocess.run([sys.executable, BACKUP_CLI],
                       capture_output=True, text=True, timeout=180)
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        raise SystemExit(f"[apply] backup FAILED rc={r.returncode} — aborting, "
                         "no mutations attempted.")
    print("[apply] backup OK.")


# ════════════════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════════════════
def main():
    global PRUNE_AGE_DAYS, LLM_DISABLED
    ap = argparse.ArgumentParser(
        description="Engram nightly sleep consolidation (dry-run by default).")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", default=True,
                      help="Preview only, mutate nothing (DEFAULT).")
    mode.add_argument("--apply", action="store_true",
                      help="Enact changes (takes a DB backup first).")
    ap.add_argument("--days", type=int, default=DEFAULT_DAYS,
                    help="Look-back window for SEGMENT/DISTIL (default 1).")
    ap.add_argument("--segment", action="store_true", help="Run SEGMENT stage.")
    ap.add_argument("--distil", action="store_true", help="Run DISTIL stage.")
    ap.add_argument("--merge", action="store_true", help="Run MERGE stage.")
    ap.add_argument("--prune", action="store_true", help="Run DECAY/PRUNE stage.")
    ap.add_argument("--prune-age-days", type=int, default=PRUNE_AGE_DAYS)
    ap.add_argument("--no-llm", action="store_true",
                    help="Skip every LLM call: no distillation, deterministic "
                         "digests only. Turns a ~7-minute night into under a second.")
    ap.add_argument("--no-log", action="store_true",
                    help="Don't append the report to logs/engram-sleep.log.")
    args = ap.parse_args()

    PRUNE_AGE_DAYS = args.prune_age_days
    LLM_DISABLED = bool(args.no_llm)
    if LLM_DISABLED:
        print("LLM stages disabled (--no-llm) — deterministic digests only")

    apply_changes = bool(args.apply)
    mode_str = "apply" if apply_changes else "dry-run"

    # default: run all stages if none explicitly named
    run_all = not any([args.segment, args.distil, args.merge, args.prune])
    do_segment = run_all or args.segment or args.distil  # distil needs segments
    do_distil = run_all or args.distil
    do_merge = run_all or args.merge
    do_prune = run_all or args.prune

    t0 = time.time()
    report = {
        "started": now_iso(),
        "params": {"days": args.days, "no_llm": LLM_DISABLED,
                   "stages": [s for s, on in
                              (("segment", do_segment), ("distil", do_distil),
                               ("merge", do_merge), ("prune", do_prune)) if on]},
        "ran": [],
        "segment": {}, "distil": {}, "merge": {}, "prune": {},
        "db": {},
    }

    if apply_changes:
        take_backup()

    con = ro_conn()
    report["db"]["non_epis_before"] = non_episodic_count(con)

    segments = []
    if do_segment:
        report["ran"].append("segment")
        segments = stage_segment(con, args.days, report)
    if do_distil:
        report["ran"].append("distil")
        stage_distil(con, segments, report, apply_changes)
    if do_merge:
        report["ran"].append("merge")
        stage_merge(con, report, apply_changes)
    if do_prune:
        report["ran"].append("prune")
        stage_prune(con, report, apply_changes)

    con.close()
    # fresh RO connection to observe post-run state
    con2 = ro_conn()
    report["db"]["non_epis_after"] = non_episodic_count(con2)
    con2.close()

    wall = time.time() - t0
    text = render_report(report, mode_str, wall)
    print(text)

    if not args.no_log:
        try:
            os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
            with open(LOG_PATH, "a") as f:
                f.write(text + "\n")
            print(f"\n[log] appended to {LOG_PATH}")
        except Exception as e:
            sys.stderr.write(f"[log] could not write log: {e}\n")


if __name__ == "__main__":
    main()
