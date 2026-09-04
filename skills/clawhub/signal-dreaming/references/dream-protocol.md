# Signal Dreaming — Full Protocol

Memory consolidation in three phases: **Sense → Consolidate → Settle**.

---

## Design Stance

This protocol is written **for an agent to follow**, not for a program to enforce.

That distinction is deliberate and load-bearing. Every rule below is a judgement an agent makes with the actual content in front of it. Do not translate these rules into blocking assertions in code — a rule that says *"tell the human"* must not become a rule that says *"abort the run"*.

Three consequences, in order of importance:

1. **Fail soft, report loudly.** If something is wrong but memory is not at risk, do the work you can do, then say plainly what you skipped and why. A dream that consolidates 3 of 4 topics and reports the fourth is a success. A dream that refuses to start is not.
2. **Never let a diagnostic block the main job.** Audits, size checks, and sanity scans exist to inform the final report. None of them is a precondition for consolidating memory.
3. **Only two things justify stopping before writing:** a failed backup (Phase 2.0 / Phase 3.1), or a write plan that reaches outside the allowed paths — and the second cancels only those targets, not the run. Everything else is a note in the summary.

The one hard stop that *is* real: **never write a secret into curated memory.** That guard blocks the specific value, not the run.

**Never wait on an answer that cannot arrive.** A scheduled run has no human to consult; blocking on one is indistinguishable from failing.

### Derive limits from the runtime; never hard-code them

Every threshold in this protocol must be **derived from a value the runtime actually reports**, never written as a standalone constant.

The distinction matters more than it looks:

- **A hard-coded absolute** (`8 KB`, `10,000 characters`) is frozen at the moment someone typed it. Change the language, the config, or the runtime version, and it silently means something entirely different — while still being enforced with full confidence.
- **A percentage of a runtime value** moves with what it measures. Raise `bootstrapMaxChars` and the target rises with it. Nothing has to be remembered, migrated, or re-derived by hand.

This protocol has been burned by the first form twice: an `8 KB` index target written when a byte and a character were the same thing cut CJK workspaces to a quarter of their real budget, and a later version promoted that constant to a hard error, so a healthy index could refuse to run the pass that maintains it. Both felt conservative. Both caused damage no real constraint would have.

So: name the runtime value, read its current setting, and express the target as a fraction of it. Where no runtime ceiling exists at all, use judgement about the content and state what you decided — do not manufacture a constant to make the decision feel objective.

---

## Prerequisites

- `MEMORY.md` exists at workspace root
- `memory/dream-log.md` exists (create an empty file if missing)

That is the whole list. This protocol needs no state file, no lock file, and no prior run to function.

---

## Before Starting: Guardian Check (automated runs only)

Read `memory/dream-log.md` to find the last dream timestamp by locating the most recent `## 🌙 Dream #` heading.

**First run** (no Dream entries found): bypass the guardian entirely and proceed to Phase 1.

**Skip condition**: the last run was `< 20 hours ago` AND Phase 1 would select nothing unread — no daily log dated **on or after** the **watermark** (Phase 1.1) has been modified since the last entry's heading timestamp.

Compare dates against the watermark, never against the heading date. They are the same number on an ordinary day and they diverge exactly when it matters: a backfill entry is stamped with today's heading but deliberately leaves the frontier where it was. Judging by the heading date would skip a run that still has real work waiting behind that frontier.

**Ask Phase 1's question, with Phase 1's `>=` — never a cheaper `>`.** A log dated *on* the watermark can still have been appended to after the last run read it; that is exactly why Phase 1.2 selects `>=` rather than `>`. A guardian that looks only for logs dated strictly *after* the watermark silently overrides that defence: the appended work is invisible to it and waits for whichever later run happens to clear the debounce. Once session-reset hooks are writing `YYYY-MM-DD-HHMM.md` files, several logs share the watermark date every day — same-day additions are the normal case, not an edge one.

**Anchor the modification test to the last Dream entry's heading timestamp, not to a `SKIP` comment.** Skips are not runs; anchoring to one would treat everything written before it as already consolidated, which is this same bug in a new place. The heading is the wrong thing for deciding *which* logs are unread and the right thing for deciding *when* they were last read — two different questions that happen to share one line. Because it records when the run *started*, a file that landed while that run was still working is correctly seen as unread.

Use mtime for the modification test: `find <WORKSPACE_ROOT>/memory -maxdepth 1 -name '????-??-??*.md' -newermt '<heading timestamp>'` lists the candidates; discard any dated before the watermark, and an empty result means there is nothing to do. mtime is not tamper-proof, but its failure directions are the right way round — a false positive costs one extra no-op run, while a false negative needs someone to deliberately restore an old timestamp. Content hashes would be exact, and would hand this protocol the state file it otherwise does not need.

**If the newest entry carries no `Consolidated through:` field, do not skip.** That means the last run was a backfill, which by design consolidated history rather than advancing the frontier — so ordinary work may still be outstanding.

The real condition is the material one — nothing new past the watermark means nothing to do. The 20 hours is debounce sized for a once-daily schedule: it lets a run that is merely early exit quietly, while still forcing a pass roughly once a day even when no log changed. On a different cadence, size it to just under your interval.

If skipping: use `exec` to append `<!-- SKIP · YYYY-MM-DD HH:MM · reason -->` to `<WORKSPACE_ROOT>/memory/dream-log.md` and stop. Always use absolute paths — never `~`.

Manual triggers always bypass the guardian.

---

## Phase 1 · Sense — Read Only, No Writes

**Goal**: build a priority list without touching any file.

**Distinguishing file types:**
- **Daily logs**: match `memory/YYYY-MM-DD*.md` (e.g. `2026-04-13.md`, `2026-04-13-clash-fix.md`)
- **L2 topic files**: `memory/<topic>.md` files that do NOT match a date pattern (e.g. `memory/clash-verge.md`, `memory/business.md`)
- **⛔ Not daily logs**: `memory/dreaming/**` and `memory/.dreams/**` (built-in memory-core Dreaming output and internal state) — do NOT process these as daily logs or L2 files; skip entirely

### 1. Find the watermark

Everything this protocol needs to remember between runs lives in one line of `memory/dream-log.md`.

Scan entries from newest to oldest and take the **first one that carries a `Consolidated through:` field**. That date is the **watermark** — the newest daily log already folded into memory.

- **Scan back, do not stop at the newest entry.** Backfill runs deliberately omit the field (see Phase 3.4), so the newest entry may not carry one. Skipping past those to the last real frontier is the whole reason the field is optional.
- If no entry anywhere in the log carries the field, this workspace predates the format: fall back to the date in the **newest** entry's `## 🌙 Dream #` heading.
- If dream-log.md is empty or has no Dream entries, there is **no watermark** — this is a first run, handled separately below.

Reading only the newest entry would break backfill: a backfill entry is stamped with today's heading date, so falling back to that heading would jump the frontier forward over every log the backfill never touched — silently, and permanently.

The watermark tracks **how far through the logs you have read**, not when you last ran. Those are different numbers whenever a run defers work, and conflating them is how logs get skipped forever.

**Sanity-check it before use**: if the watermark is later than the newest daily log on disk, a previous run recorded it wrong. Fall back to the newest log's date, proceed normally, and say so in the final summary — a bad watermark is the one failure mode here that would otherwise stay silent.

### 2. Select daily logs

- List all daily log files (`memory/YYYY-MM-DD*.md`) — **exclude** anything under `memory/dreaming/**`
- Select files with date-based names **on or after** the watermark (use `>=` not `>`)

The `>=` matters: a log for the watermark date may have been appended to *after* the last run read it. Re-reading one already-seen file is cheap; missing an afternoon's work is not.

If a daily log contains `## Light Sleep` or `## REM Sleep` blocks (built-in Dreaming `inline` mode output), **skip those sections** — they are not user session notes.

### 3. Apply the batch limit

Cap a single run at **32 daily logs** or **192 KiB of total input**, whichever comes first. These two numbers bound one agent turn, not the memory system.

**Size the byte cap against the task timeout, not against comfort.** A cap is only meaningful if the batch it admits can finish before the scheduler kills the run. Measured throughput for this protocol has ranged from `0.12` to `0.21 KiB/s` of input, so a `1800 s` timeout admits roughly `216 KiB` at the slower end; 192 KiB leaves a margin under that. If you change the timeout, recompute the cap from the slowest throughput you have actually observed — a cap chosen independently of the timeout is decoration, because the timeout binds first either way.

**Always take at least one log, even if that single file exceeds the byte cap.** A cap that can produce an empty batch is a deadlock: the watermark never advances, so that log — and every log behind it — is blocked forever. Read the oversized file, summarise what you can, and note its size in the dream-log.

**Cut the batch on a date boundary, never inside one.** The watermark records a date, so it cannot express "processed 32 of today's 40 files". If the cap falls mid-day, keep going until that date's logs are finished, even if it overruns the cap — then stop. Splitting a date leaves the watermark unable to advance past it: the next run reselects the same day, processes the same prefix, and the tail is never reached. Both caps are soft; the date boundary is not.

When the selection *does* exceed the cap, which end you take depends on why — but the question only arises when the selection spans more than one date. If a **single** date's logs alone exceed the cap, the boundary rule above has already decided it: process that whole date. There is no end to choose.

**One date can exceed the byte cap on its own, and the boundary rule means you process it anyway.** The cap bounds accumulation across days; nothing bounds a single day but the timeout. When a run overruns the cap for this reason, record the batch's actual input size and wall-clock duration in the dream-log entry. Those two numbers are the only evidence a later run has for whether the cap and the timeout are still sized for how much now gets written per day.

**Resuming after a gap** (a watermark exists): take the **oldest** logs in the selection, in date order. Set `Consolidated through:` to the newest date you actually processed — *not* today's date. The next run selects `>= that date` and continues exactly where this one stopped. Report how many logs remain.

Taking the oldest is what makes the watermark work. Taking the newest would advance it past everything you skipped, and those logs would never be selected again.

**First run** (no watermark): take the **newest** logs instead. A new install should surface recent context immediately, not start a year in the past. Set the watermark to the newest date processed, and state plainly in the dream-log and the final summary how many older logs were left outside the watermark — they will not be picked up automatically.

**Manual backfill**: a human can ask for a specific date range (e.g. *"consolidate 2026-01 through 2026-02"*). Process exactly that range and **leave the watermark unchanged** — backfill fills in history behind the frontier, it does not move it.

Never skip a run because there is too much to read.

### 4. Identify L2 update candidates

- Match the selected log content to existing L2 topic files
- Flag L2 files likely needing updates
- Note topics with no matching L2 file — these may need new ones

### 5. Check MEMORY.md size

Measure `MEMORY.md` in **characters** (`wc -m`), not bytes. Also read the workspace's `bootstrapMaxChars` / `bootstrapTotalMaxChars` and the sizes of the other bootstrap files, so Phase 3 can compute headroom and target. Hold all of it for Phase 3. Do not act on any of it yet, and **never treat any size as a reason to stop** — see Phase 3.2.

**Output (held in memory, nothing written)**: selected log list, the date that will become the new watermark, deferred count, L2 update list, current index size.

---

## Phase 1.5 · Plan Quality Gates — Read Only, No Writes

Before touching any memory file, make an explicit consolidation plan and check it against these guards:

### 1. Topic identity guard

Do **not** merge records just because names are similar. Split or preserve separate L2 files when any of these differ materially:

- owner / customer / friend group
- environment or host (IP, domain, machine, OS user, cloud account)
- project lifecycle (legacy vs current, prototype vs production)
- world / database / repo / app ID / claim ID / other durable identifier

If old and new material share a broad label, prefer:

- `memory/<topic-current>.md` for the active project
- `memory/<topic-legacy>.md` for historical material
- `memory/<topic>.md` as a short disambiguation index, if needed

### 2. Lifecycle state guard

Classify every candidate as one of: **active**, **waiting**, **done**, **archived**, **closed**, or **snowed/paused**.

- Closed / archived / snowed projects must not be reintroduced as active TODOs.
- If a daily log says the human closed a line of work, update L2 + MEMORY.md to reduce future resurfacing.
- Historical facts may remain, but phrase them as reference/archive, not action items.

### 3. Secret propagation guard

Never copy secrets from daily logs into L2, MEMORY.md, or dream-log.md. Treat these as sensitive by default:

- API keys, tokens, OAuth strings, cookies, private keys
- passwords, invite/player/server passwords, recovery codes
- signed URLs or URLs containing access tokens
- private SSH keys or full credential-bearing command lines

If a source log contains a suspected live secret, do **not** quote it. Record only: `sensitive value omitted; source file needs manual review` and alert in the final response / dream summary.

This is the one guard that blocks content outright. It blocks **that value**, not the run — consolidate everything else normally.

### 4. Write plan

List the exact files you expect to touch. Phase 2 may touch only L2 files plus backups under `<WORKSPACE_ROOT>/.backup/memory-dreams/`. Phase 3 may touch only `MEMORY.md`, backups under `<WORKSPACE_ROOT>/.backup/memory-dreams/`, and `memory/dream-log.md`.

If the plan requires editing daily logs, system config, or files outside the workspace, do not write those targets.

In an interactive run, ask the human for explicit approval. In a scheduled or isolated run **there is nobody to ask** — so drop the out-of-bounds targets from the plan, consolidate everything else normally, and list exactly what was dropped and why in the final summary. Waiting on an answer that cannot arrive is the same as failing the whole run.

---

## Phase 2 · Consolidate — Write L2 Files Only

Process the priority list from Phase 1. **Do not modify MEMORY.md, dream-log.md, or any daily log file in this phase.**

### 0. Back up touched L2 files first

Before modifying an existing L2 file, copy it to:

`<WORKSPACE_ROOT>/.backup/memory-dreams/YYYYMMDD-HHMM/<relative-path-from-workspace-root>.bak`

Example: `memory/clash-verge.md` → `.backup/memory-dreams/20260426-1100/memory/clash-verge.md.bak`.

Keep dream backups **outside `memory/`** and use a non-`.md` final suffix (`.bak`) so memory indexing does not recall stale states or old TODOs from backups.

Create parent directories as needed. **If backup creation fails, stop before writing** — this is one of the two real hard stops.

For a newly created L2 file, no pre-existing backup is required; include it in the dream-log as `created`.

### Log entries → L2 extraction

- Read the selected daily logs
- Extract decisions, config changes, resolved issues, new knowledge
- Write or update the appropriate `memory/<topic>.md`
- If no matching L2 file exists for a topic, create one (e.g. `memory/network-setup.md`)

### Relative time correction (conservative)

- Only correct clear expired expressions: "today"/"this week" in L2 files → absolute dates
- Do not guess at vague expressions

### L2 write quality rules

- Prefer small, source-grounded edits over broad rewrites.
- Keep active and legacy material clearly separated; add a one-line pointer instead of duplicating long history.
- Do not add TODOs unless the source explicitly implies continuing action.
- Preserve security posture: write `password not stored`, `token omitted`, or `credential managed in env` instead of values.
- If an `edit` attempt fails twice for the same block, stop trying that block; use a safer whole-file rewrite only after re-reading the file, or leave a blocker in the final summary.

---

## Phase 3 · Settle — Write Index + Diary

### 1. Back up MEMORY.md

Copy current MEMORY.md content → `<WORKSPACE_ROOT>/.backup/memory-dreams/YYYYMMDD-HHMM/MEMORY.md.bak`.

**⚠️ Path guidance**: Always use absolute paths derived from the workspace root (e.g. `/path/to/workspace/MEMORY.md`). Never use `~`-prefixed paths in tool calls — isolated sessions may not resolve them. Use the workspace root passed in the task message.

**If this backup fails, stop before rewriting** — the second real hard stop.

### 2. Rewrite/trim MEMORY.md

**The budget is derived from the runtime. This protocol does not hard-code one.**

#### Compute the headroom

OpenClaw truncates the *injected copy* of a bootstrap file at `agents.defaults.bootstrapMaxChars` (default **20,000 characters**), with a combined cap across all bootstrap files at `agents.defaults.bootstrapTotalMaxChars` (default **60,000**). Read both from the agent config — `~/.openclaw/openclaw.json`, under `agents.defaults` — rather than assuming the defaults. Reading it is allowed: the out-of-bounds rule in Phase 1.5 governs **writes**. If it is unreadable, use the documented defaults above and say so in the summary. Per the OpenClaw docs, *"truncation is not data loss: the file stays intact on disk."* Nothing is destroyed at any size.

`MEMORY.md` shares the total with the other bootstrap files, so its real ceiling is whichever limit binds first:

```
headroom = min(
    bootstrapMaxChars,
    bootstrapTotalMaxChars − (size of the other bootstrap files)
)
```

The other bootstrap files are `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`, and `BOOTSTRAP.md` where present. On a default install with modest instruction files the per-file cap binds and headroom is 20,000; on a workspace with large instruction files the total binds instead and headroom is smaller. Compute it — do not assume.

#### Target 80% of headroom

```
target = headroom × SD_INDEX_TARGET_PCT / 100     # default 80
```

The remaining 20% is a **growth band**, and it is the entire reason for a percentage rather than the raw ceiling. The index grows between runs; a target sitting exactly at the ceiling means any growth is silently truncated before the next consolidation gets a chance to look at it. Twenty percent of a 20,000-character headroom is 4,000 characters of slack — enough for many days of ordinary accumulation.

`SD_INDEX_TARGET_PCT` is a knob, not a constant. Raise it toward 100 to use more of the budget and accept a thinner margin; lower it for a more aggressively curated index. It is expressed as a percentage precisely so that it keeps meaning the same thing when `bootstrapMaxChars` changes.

**Count characters, not bytes.** A byte target silently shrinks the usable index for anyone writing in a non-Latin script — CJK text runs 1.7–3 bytes per character, so an "8 KB" rule cuts the real budget to about a quarter of what the runtime allows.

Use `wc -m`, but **`wc -m` only counts characters under a UTF-8 locale**. In a scheduled or isolated session `LANG` is often unset, and `wc -m` silently returns the byte count instead — reintroducing the very error it was meant to avoid. Force a locale (`LC_ALL=en_US.UTF-8 wc -m file`) and sanity-check that the result is not larger than `wc -c`. If no UTF-8 locale is available, report bytes and say the character count was unavailable; do not compare a byte count against a character target.

#### What the target means

Crossing it is a **prompt to sink detail into L2 during this run**, nothing more. It is not a gate, not an error, and not a reason to delete facts.

Below the target, size is not a consideration at all: judge sections on whether they still belong in an index a human skims at session start — is the project active, is the status current, does the detail belong in an L2 file. A tight 4,000-character index and a well-earned 15,000-character one are both correct.

An oversized index is a reason to *run*, not a reason to stop. Proceed normally and report the result.

If the workspace genuinely needs more room, raising `bootstrapMaxChars` is a legitimate answer — the docs list it alongside distilling and sinking to L2. Say so in the summary rather than deleting facts to fit.

When the index has outgrown its budget, or when sections no longer belong at index level, fix it by **moving detail down to L2**, not by deleting information:

1. Find the longest sections and check what belongs in an L2 topic file instead
2. Move that detail into the L2 file (creating it if needed), leaving a one-line pointer
3. Only then trim wording

Other index rules:

- Update project states from Phase 2 findings
- Sync TODO states: mark completed ✅ items as done, add newly discovered todos
- Preserve lifecycle state: closed / archived / snowed items belong in archive/reference wording, not active sections
- Each section: one-line status + 2–4 bullets + L2 pointer (e.g. `**Details**: memory/clash-verge.md`)
- Move fully completed/archived projects to a short footer section

If the index still exceeds the computed headroom after sinking detail to L2, say so in the dream-log and the final summary so the human can decide whether to cut further or raise `bootstrapMaxChars`. Then finish the run normally.

### 3. Determine dream number

Count the number of `## 🌙 Dream #` lines in dream-log.md. The new entry is N+1.

Keep the timezone abbreviation in the heading (`2026-08-24 11:27 CST`). The guardian compares that timestamp both against now (the debounce) and against daily-log mtimes (to find unread appends), so a bare local time is ambiguous the moment the agent runs under a different zone than the one that wrote it. Record the time the run **started**: the guardian relies on it to catch files that landed while the run was still working.

### 4. Append to dream-log.md (Markdown — not JSON)

**⚠️ Tool guidance**: Tool names here are OpenClaw's (`exec` to run a shell command, `edit` to patch a file); on another harness use its equivalents. Use `exec` with a heredoc to append — **never** use the `edit` tool for appending (it requires exact text replacement and will fail on append). Replace `<WORKSPACE_ROOT>` with the absolute path from the task message.

```bash
cat >> <WORKSPACE_ROOT>/memory/dream-log.md << 'DREAM_EOF'

## 🌙 Dream #<NUMBER> · YYYY-MM-DD HH:MM TZ

**Trigger**: <auto|manual>
**Duration**: ~<MINS> minutes
**Consolidated through**: YYYY-MM-DD

### Signal summary
- Logs consolidated: <LOG_COUNT> (<DEFERRED_COUNT> deferred to next run)

### What changed
- Updated L2: <filename> — <one-line description>
- Synced <TODO_COUNT> TODO items
- MEMORY.md: <BEFORE> → <AFTER> chars

### Note
(One honest sentence about what was found or how it felt)
DREAM_EOF
```

**`Consolidated through` is the watermark the next run reads.** Set it to the date of the newest daily log you actually processed this run:

- Normal run: the newest selected log — usually today
- Deferred run (batch limit hit while resuming): the newest log **in the batch you processed**, not today
- Manual backfill: omit the field entirely. The next run scans past this entry to the last one that has it, so the frontier stays exactly where it was

Getting this wrong is the one mistake in this protocol that silently loses memory rather than reporting a problem. If a run defers work, say so in the `Signal summary` line as well, so it is visible to a human skimming the diary.

### 5. Trim dream-log.md

If total `## 🌙 Dream #` entries exceed 30, delete the oldest entry.

**Never delete the last entry that still carries a `Consolidated through:` field.** If the oldest entry is the only one holding the watermark — which happens after a run of backfills, since those omit the field — skip it and delete the next-oldest instead. Trimming the diary must not delete the frontier along with it.

Boundary rule: delete from the start of the chosen `## 🌙 Dream #` heading up to (but not including) the start of the next `## 🌙 Dream #` heading. Do not use `---` as a boundary — it may appear inside dream content.

### 6. Post-write audit

Run a lightweight verification pass. **This is a reporting step, not a gate** — it runs after the work is committed, and its findings go into the final summary. A failure here never invalidates the dream.

Check:

- `MEMORY.md` size in characters, against the computed headroom and target — report the numbers, never treat either as a pass/fail verdict
- `memory/dream-log.md` is still Markdown with no malformed duplicate heading
- touched L2 files still separate current vs legacy/archived material correctly
- touched files contain no obvious credential-bearing values

Use filename-only scans so secrets are not echoed into chat/logs:

```bash
grep -IlrE '(github_pat_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|[0-9]{8,12}:AA[A-Za-z0-9_-]{30,}|mfa\.[A-Za-z0-9_-]{20,}|-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----)' <TOUCHED_FILES>
```

A helper script covers the common checks:

```bash
<SKILL_DIR>/references/dream-audit.sh <WORKSPACE_ROOT> [touched-file ...]
```

Pass relative or absolute paths for touched files. The helper reports suspected secret filenames only; it does not print matched values. It is intentionally conservative and lightweight, not a replacement for a dedicated secret-scanning/DLP tool. Its exit code is advisory — never gate a run on it.

If a possible secret is found after writing, restore from the relevant backup where possible, then report the file path without quoting the secret.

---

## Safety Rules

| Rule | Detail |
|------|--------|
| Guardian runs before Phase 1 | Skip check writes only to dream-log.md |
| Phase 1 is read-only | An error in Sense touches no files |
| Never archive daily logs | Moving `YYYY-MM-DD*.md` breaks memory_search indexing |
| Always back up before rewriting | `.backup/memory-dreams/YYYYMMDD-HHMM/` before touching MEMORY.md or any L2 file |
| Backup failure is a hard stop | The only infrastructure condition that cancels writes |
| Out-of-bounds targets drop, never block | Ask when interactive; when scheduled, drop them, finish the rest, report what was dropped |
| dream-log.md = Markdown | Append text; never parse or write as JSON |
| L2 files are permanent | Never delete or archive `memory/<topic>.md` |
| Phase 2 = L2 only | MEMORY.md changes happen in Phase 3 |
| No secret propagation | Redact and alert; never promote credentials |
| Lifecycle is sticky | Closed/archived/snowed stay non-active until the human reopens them |
| Index size never gates a run | An oversized index is the reason to run, not to abort |
| Measure the index in characters | Byte targets silently shrink the budget for non-Latin scripts |
| Never hard-code a limit | headroom = `min(bootstrapMaxChars, bootstrapTotalMaxChars − other bootstrap files)`; target = headroom × `SD_INDEX_TARGET_PCT` (default 80) |
| The target is a prompt, not a gate | Crossing it means sink detail into L2 this run |
| Audits report, never block | Post-write checks inform the summary only |
| Watermark tracks reading, not running | Never set it past deferred work |
| Watermark is found by scanning back | Take the newest entry that *has* the field; backfill omits it deliberately |
| Trimming never removes the watermark | If the oldest entry is the only field holder, delete the next-oldest |
| Batches cut on date boundaries | The watermark stores a date; splitting a date strands its tail |
| Deferred work resumes from the oldest | So the watermark advances contiguously |

---

*Older releases kept a recall-frequency index at `memory/.dreams/short-term-recall.json`; current ones have migrated it away. Date-based selection is the only path this protocol needs. Never read anything under `memory/.dreams/**`.*
