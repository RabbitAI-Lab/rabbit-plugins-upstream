---
name: "signal-dreaming"
description: "Consolidate daily session logs into L2 topic files and a compact MEMORY.md index, in three bounded phases with backups, lifecycle and secret guards."
---

# Signal Dreaming

Memory consolidation in three phases: **Sense → Consolidate → Settle**.

Daily session logs accumulate raw detail. This skill reads the ones written since the last run, promotes what matters into durable topic files, and keeps the top-level index worth reading at session start.

## Memory Architecture Assumed

A two-layer memory layout:

- **Daily logs** (`memory/YYYY-MM-DD*.md`) — raw session notes, read-only, never moved or deleted
- **L2 topic files** (`memory/<topic>.md`) — curated durable knowledge per subject (e.g. `memory/clash-verge.md`)
- **Index** (`MEMORY.md`) — high-level status with pointers down to L2

If you are starting fresh, create `MEMORY.md` and `memory/dream-log.md` before the first run. L2 files are created on demand.

`memory/dream-log.md` doubles as the only state this skill keeps: entries record a **`Consolidated through:`** date — the newest daily log already folded into memory. The next run scans back for the most recent entry carrying that field to know where to resume. There is no state file, no lock file, and nothing to migrate or repair.

## Quick Start

### Manual dream

Tell your agent:

> "Run a memory dream consolidation. Follow the protocol in `<SKILL_PATH>/references/dream-protocol.md`. Workspace root: `<YOUR_WORKSPACE_PATH>`."

Or just *"run a dream consolidation"* — if this skill is loaded, the agent will know what to do.

### Automated daily dream (cron)

```json
{
  "name": "daily-dream",
  "schedule": { "kind": "cron", "expr": "0 7 * * *", "tz": "<YOUR_TIMEZONE>" },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "timeoutSeconds": 900,
    "message": "Run a memory dream consolidation. Read <SKILL_PATH>/SKILL.md and <SKILL_PATH>/references/dream-protocol.md in full, then follow the protocol phases in order. Workspace root: <YOUR_WORKSPACE_PATH>. Do not modify cron jobs, agent config, the Gateway, any daily log, or memory/dreaming/**. End your final response with a one-line dream summary — the cron delivery mechanism will auto-announce it."
  },
  "delivery": { "mode": "announce", "channel": "<CHANNEL_TYPE>", "to": "<CHANNEL_ID>" }
}
```

Set `expr` and `tz` to when your human is asleep.

## Three-Phase Safety Model

| Phase | Writes | Purpose |
|-------|--------|---------|
| **Sense** | ❌ None | Select logs since the watermark, plan the work |
| **Consolidate** | ✅ L2 files only | Promote content into topic files |
| **Settle** | ✅ MEMORY.md + dream-log.md | Update index, write diary entry |

Phase 1 is always read-only. An error in Sense never corrupts files.

## Quality Gates

A read-only planning checkpoint runs before any write: **topic identity** (do not merge legacy and current projects on name similarity), **lifecycle** (closed work must not reappear as an active TODO), **secret propagation** (never promote credentials into curated memory; the credential list is exhaustive and the guard is not a privacy classifier), **backup** (existing L2 files and `MEMORY.md` are copied to `<WORKSPACE_ROOT>/.backup/memory-dreams/YYYYMMDD-HHMM/` with a `.bak` suffix first), and a **post-write audit** reporting size, structure, lifecycle separation, and credential patterns without gating the run. `references/dream-audit.sh` covers the common checks; it is not full DLP.

## Failure Philosophy

This protocol is written for an agent to follow, not for a program to enforce. It fails **soft**:

- Do the work you can do, then report what you skipped and why.
- Diagnostics inform the final summary. They never block consolidation.
- An oversized `MEMORY.md` is the reason to run, not a reason to abort.
- Limits are derived from the runtime, never hard-coded into the protocol.
- Never wait on an answer that cannot arrive. A scheduled run has nobody to ask, so out-of-bounds work is dropped and reported, not blocked on.

Exactly two conditions cancel writes: a **failed backup**, or a **write plan reaching outside the allowed paths** — and the second cancels only those targets, not the run.

The secret guard is the one hard block on content — and it blocks the offending value, not the run.

## Where this sits in OpenClaw's memory stack

Verified against OpenClaw **2026.7.1**. This skill operates entirely on the documented Markdown layer — `MEMORY.md` plus `memory/*.md` — which remains the durable memory model.

**Built-in memory-core Dreaming** is a separate system, opt-in and disabled by default:

| | memory-core built-in Dreaming | signal-dreaming (this skill) |
|---|---|---|
| Trigger | Managed cron when enabled | Cron agentTurn |
| Source | Short-term recall store under `memory/.dreams/` | Daily logs on disk |
| Output | `DREAMS.md` / `memory/dreaming/{phase}/` | `memory/dream-log.md` + L2 files |

The two are independent; run this skill with built-in Dreaming on or off. This protocol never reads or writes `memory/dreaming/**` or `memory/.dreams/**`, and skips `## Light Sleep` / `## REM Sleep` blocks if it finds them inside a daily log (older `inline` mode).

Adjacent components this protocol deliberately does not touch:

- **`memory-wiki`** — per the OpenClaw docs it "does not replace the active memory plugin"; its vault is its own layer, neither read nor written here.
- **Alternate backends** (QMD, Honcho, LanceDB) — they change how `memory_search` retrieves, not where durable notes live. This protocol reads and writes files, so it is backend-agnostic.
- **Database-first state** — the SQLite migration covers runtime state (sessions, transcripts, task ledgers). Workspace Markdown memory is out of scope.
- **Automatic memory flush** — the pre-compaction pass writes daily notes; this protocol consumes them. No conflict.

Tool names in the protocol (`exec`, `edit`) are OpenClaw's; on another harness use its equivalents.

## Key Rules

- **Never move or delete daily logs** — archiving breaks `memory_search` indexing
- **dream-log.md is Markdown** — append text directly, never write JSON
- **Never copy credentials into curated memory** — omit/redact and alert instead. The secret list is **exhaustive**: authentication material only. This guard is not a privacy classifier; anything outside the list follows the workspace's own conventions and never raises a secret alert
- **Keep lifecycle state sticky** — closed/archived/snowed lines stay non-active
- **Back up before rewriting** `MEMORY.md` and any existing L2 file
- **MEMORY.md budget is derived, never hard-coded** — headroom = `min(bootstrapMaxChars, bootstrapTotalMaxChars − other bootstrap files)`; target = **80%** of it (`SD_INDEX_TARGET_PCT`, a knob), the remaining 20% being growth slack. Count characters, not bytes. Crossing the target means sink detail into L2 — it never blocks and never justifies deleting facts
- **Batch limit**: 32 logs or 192 KiB per run, cut on date boundaries. Sized so one batch fits inside the task timeout; a single date that exceeds it on its own is still processed whole. When resuming after a gap it takes the oldest first so the watermark advances contiguously

## Full Protocol

See `references/dream-protocol.md` for the complete three-phase workflow, quality gates, dream-log format, and safety rules.

## Version Note

**4.0.3** restates the 4.0.2 scope without enumerating what falls outside it.

4.0.2 fixed the rule by naming categories of ordinary content as out of scope. The rule was right; the enumeration was not. A list of what a memory system will retain reads, to someone reviewing the skill rather than running it, as a description of what it sets out to collect — and the three constraints that actually do the work need no examples to be unambiguous: the list is exhaustive, it is not to be extended, and nothing outside it raises the alert.

The scope is now stated as a limit on the guard rather than a judgement about content. It covers authentication material and is not a privacy classifier; anything else follows the workspace's own conventions. Behaviour is identical to 4.0.2.

**4.0.2** closes the secret guard's scope.

The list of what counts as a secret was introduced with *"treat these as sensitive by default"* — wording that reads as a floor rather than a boundary, so a run could classify ordinary log content as sensitive on its own judgement, withhold it from L2, and ask for manual review of the daily log.

That alert has nowhere to go. This protocol never edits daily logs, so the value stays exactly where it already was; the only durable effects are an index missing an ordinary fact and a review request that cannot resolve. Repeated, it teaches the human to skim past the alert that does matter.

The list is now stated as **exhaustive**, and nothing outside it raises the alert.

**4.0.1** fixes a guardian that could skip work it should have done, and sizes the batch cap to the task timeout.

The guardian tested for daily logs dated strictly *after* the watermark, while Phase 1 selects `>=` precisely because a watermark-dated log can be appended to after the last run read it. Since the guardian runs first, that defence never applied: inside the debounce window a run reported no-op while same-day additions waited for a later pass. Session-reset hooks that write `YYYY-MM-DD-HHMM.md` files make several logs share the watermark date every day, so this is now the normal case rather than an edge one. The two log conditions are merged into one that reuses Phase 1's `>=` and asks whether any selected log changed since the last entry's heading timestamp.

The byte cap moves from `512 KB` to `192 KiB`. A cap means something only if the batch it admits can finish before the scheduler kills the run: at a measured `0.12-0.21 KiB/s`, an `1800 s` timeout admits roughly `216 KiB`, so the old number was never reachable. **If your task timeout differs, recompute the cap from your own slowest observed throughput.** The cap bounds accumulation across days and cannot bound a single day — the date-boundary rule still processes an oversized date whole, and such a run now records its actual input size and duration in the dream-log.

**4.0.0** returns to the protocol-only design of the 1.x line and removes the 2.x/3.x script layer entirely.

Those versions compiled the same rules into enforced JavaScript preconditions — a transaction state machine, run manifests, lock files, staged candidate directories. That layer added no new safety rules; it changed who enforced them, and in production turned recoverable conditions into aborted runs: an over-limit index refused to run the pass that shrinks it, and an optional audit's path error cancelled an otherwise complete consolidation.

It also retires the byte-based index target inherited from 1.x. That `8 KB` was written where a byte and a character were the same thing; the real limit is `bootstrapMaxChars`, measured in **characters**. For a CJK workspace at ~1.7 bytes per character it enforced about a quarter of the real budget — and 3.x then made crossing it a hard error, so a healthy index could block its own consolidation pass. 4.0.0 does not substitute another constant: headroom is derived from the runtime's own caps, and the target is a configurable percentage of it (default 80%, leaving a growth band). A hard-coded threshold caused the original damage, so the protocol no longer contains one.

Upgrading from 2.x or 3.x: delete any cron payload steps invoking `preflight`, `begin`, `finalize`, `run-guard`, or `dream-audit.mjs` and use the template above. There is no state to migrate. Existing `.backup/memory-dreams/` directories can stay; nothing reads them. Your existing `dream-log.md` works as-is — the watermark is found by scanning back for the newest entry that carries a `Consolidated through:` field, and if none does, the newest entry's heading date is used.
