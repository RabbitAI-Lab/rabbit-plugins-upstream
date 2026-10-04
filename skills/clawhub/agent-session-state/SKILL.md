---
name: agent-session-state
description: >-
  Per-channel session state files and a Write-Ahead Log (WAL) protocol.
  Prevents cross-session interference, captures decisions and facts
  reliably, and provides context recovery for long or complex sessions.
  Designed to work with hierarchical-agent-memory and agent-provenance.
license: MIT-0
compatibility: "OpenClaw 2026.4.x or later."
metadata:
  openclaw:
    requires:
      bins: ["openclaw"]
    paths:
      write: ["memory/sessions/", "memory/topics/", "memory/contacts/", "memory/daily/", "MEMORY.md"]
      read: ["memory/sessions/", "memory/topics/", "memory/contacts/", "memory/daily/", "MEMORY.md"]
  version: "2.3.1"
  clawhub: {"category": "memory", "tags": ["session", "isolation", "wal"]}
---

# Agent Session State v2.3.1

Agents that serve multiple channels need structured per-channel state beyond what gateway transcripts capture. This skill provides curated agent-authored session files, a Write-Ahead Log (WAL) protocol for reliable decision capture, and a distillation workflow that promotes session-level state into topic files over time.

## At a glance

OpenClaw already provides per-channel transcript isolation via `session.dmScope`, gateway-owned session history, automatic session maintenance and pruning, a silent memory flush before compaction, and `sessions_search` / `sessions_history` for finding and reading prior transcripts. If that covers your needs — "keep different users' conversations separate" and "save durable facts before compaction summarizes the chat" — you do not need this skill.

This skill operates at a different layer. It adds curated agent-authored state files per channel at `memory/sessions/<session-key>.md`, a Write-Ahead Log discipline that commits decisions and corrections to disk before the agent responds, and a distillation workflow that promotes session-level state into topic files over time. The files are notebooks the agent actively maintains, not transcripts of what was said. Transcripts tell you what was said; session state files tell you what was decided.

Install this skill if your agent needs structured, human-readable, long-lived notes about each channel's ongoing work; if you find yourself losing decisions mid-session because they are never committed anywhere durable; if you want continuity after compaction that goes beyond the memory flush's single-turn save; or if you need topic-aware recovery when working on projects that span multiple sessions. For multi-user agents, run it alongside `session.dmScope = "per-channel-peer"` — they are complementary, not redundant.

## Relationship to OpenClaw native sessions

OpenClaw core handles transcript routing and raw history. The gateway owns session transcripts in the agent's state store under `~/.openclaw/agents/<agentId>/`, isolates them via `session.dmScope`, prunes them via `session.maintenance`, and exposes `sessions_list`, `sessions_search`, `sessions_history`, and `session_status` as agent tools. This skill does not replace any of that. If you run multiple users or channels, enable `session.dmScope = "per-channel-peer"` regardless of whether this skill is installed — that is what stops Alice's DMs from leaking into Bob's session at the routing level.

This skill handles curated agent-authored state in the workspace. `memory/sessions/<session-key>.md` lives alongside topic files and daily notes in the agent workspace, is human-readable markdown, and is actively maintained by the agent with WAL entries and distillation rules. The paths do not collide with OpenClaw's transcript store. The two layers compose cleanly: transcripts are raw append-only history; session state files are curated decision logs the agent keeps on purpose.

OpenClaw's silent memory flush and this skill's WAL protocol also compose cleanly. Memory flush is reactive — a single turn that runs at the compaction boundary to save durable facts to MEMORY.md and daily notes. WAL is proactive — per-decision entries written throughout the session, before the agent responds. Different cadences, different granularities, no conflict. Run both.

## Filesystem Access

This skill writes to these locations within the workspace:

- `memory/sessions/` — one markdown file per OpenClaw session key (see Session identity below). This is where the agent writes during normal operation.
- `memory/topics/`, `memory/contacts/`, `memory/daily/`, and `MEMORY.md` — shared long-term memory that every session can read. The agent writes here only during distillation, and only entries the user has approved (see Distillation Targets).

It reads the same paths during startup and compaction recovery. All paths are declared in the metadata above.

Set appropriate permissions on the sessions directory: `chmod 700 memory/sessions`. Each session file is only read and written by the session whose key it carries, so there are no cross-session file conflicts.

## Architecture

### Per-Channel Session Files

Each conversation context (Discord channel, Slack channel, group chat, etc.) gets its own session state file under `memory/sessions/`. These files store recent context from that channel, WAL entries specific to that conversation, channel-specific preferences, and active topic references (pointers to topic files when using hierarchical-agent-memory).

### Session identity

Each session file belongs to exactly one OpenClaw session key. That is the routing key OpenClaw assigns to the conversation, such as `agent:main:main`, and `sessions_list` returns it. The key already reflects agent, channel, account, and sender according to `session.dmScope`, and it stays the same when a session is reset. Never derive the identity from a channel display name, and never change its case; some channel IDs are case-sensitive.

- Filename: the session key with every character other than letters, digits, `.`, `_`, and `-` replaced by `_`, plus `.md`. Case is preserved. For example, `agent:main:main` becomes `agent_main_main.md`.
- The first line of every session file is `<!-- session-key: <exact session key> -->`.
- Before reading or writing a session file, compare that line with the current session key. The comparison is exact and case-sensitive. If it does not match, the file belongs to a different conversation; do not read it or write to it. Use the first file named with a numeric suffix (`agent_main_main--2.md`, then `--3`, and so on) whose session-key line matches, or create the next free one.
- A file without a session-key line is never loaded automatically.

### Write-Ahead Log (WAL) Protocol

The WAL protocol ensures that important information is captured reliably, even in the face of concurrent writes or session restarts.

**When to log:** Use your judgment. If the user states a decision, correction, preference, constraint, or important fact — log it before responding. Don't rely on keyword matching as a mechanical trigger. Instead, ask yourself: if this session ended right now, would losing this information hurt? If yes, log it.

**The protocol:** Write to the session state file FIRST, then respond. The urge to respond is the enemy. Context vanishes. Write it down.

**What to log:**

- Decisions — "We're going with approach B", agreements, commitments
- Corrections — "It's actually X, not Y", factual corrections
- Constraints — "Never do X", hard stops, gated items
- Preferences — style choices, tool preferences, workflow preferences
- Specific values — version numbers, dates, IDs, URLs, config settings
- New proper nouns — people, companies, projects the agent hasn't seen before

**What NOT to log:**

- Secrets, passwords, API keys, tokens, or credentials — never write these to session files. If the user shares a secret in conversation, log the fact that a credential exists and where it is stored (e.g., "API key for service X is in the password manager"), not the value itself.
- Personally identifiable information (PII) beyond what is needed for the agent's work — phone numbers, SSNs, financial account numbers, and similar sensitive data should not appear in session files.
- Casual conversation, greetings, small talk
- Information already in topic files or MEMORY.md
- Transient task context that won't matter next session

### What gets stored, and user control

Session files hold curated notes — decisions, corrections, constraints, preferences — written in the agent's own words. They never hold verbatim message logs; the gateway transcript already has those. A session file is only read by the session whose key matches the file's session-key line.

The first time the agent creates a session file for a channel, it tells the user in one line that it keeps decision notes for this channel at `memory/sessions/<session-key>.md`. If the user asks the agent to stop taking notes in a channel, the agent stops writing to that channel's file and records only that preference. If the user asks to delete the notes, the agent deletes the file.

### Upgrading from earlier versions

Before v2.3, session files were named by lowercasing the channel name, which let different channels share one file. Those files have no session-key line, so v2.3 does not load them automatically. The agent does not read or show legacy files, because their content may come from another conversation. The workspace owner migrates them: for each file, add the session-key line for the conversation it belongs to and rename the file to match, or delete it.

Before v2.2, versions kept a shared `memory/working-buffer.md` that logged raw exchanges from every channel. v2.2 removes it: the shared buffer could carry one channel's content into another, and the gateway transcript (via `sessions_history`) already covers raw-exchange recovery. This skill no longer reads or writes that file. If it exists in your workspace, review it, copy anything worth keeping into the relevant topic file, and delete it.

## Session Startup

Before doing anything else in a new session:

1. Find the session file for the current session key, confirm its session-key line matches (see Session identity), and read it for recent context from this conversation

This ensures continuity without loading irrelevant history from other channels.

## WAL Protocol in Practice

When you receive a message that contains a decision, correction, preference, or important fact:

1. Write to session state file FIRST (before thinking about your response)
2. Include: timestamp, channel, decision/fact, reasoning if relevant
3. Then respond to the user

Example WAL entry:

```markdown
- [Time] — [Channel] — Decision: [Project] will be deployed with [feature]. Reasoning: [justification].
```

## Compaction Recovery

If a session starts mid-task or you should know something but don't:

1. Read your session state file
2. Check active topic references in the session state — if the session was working on a specific project, read the relevant topic file for authoritative project state
3. Read today's and yesterday's daily notes
4. If still missing context, use memory_search
5. Use `sessions_search` to find the relevant exchange in this channel's transcripts, then `sessions_history` to read the excerpt — this is heavier than the other recovery paths but will surface literal exchanges when structured notes are incomplete
6. Let the user know context was recovered and what you picked up — use natural phrasing, but make it clear you're working from reconstructed context, not continuous memory

Never ask "what were we discussing?" — the session file and transcript have it.

## Distillation Targets

Distillation copies content out of one conversation's session file into shared memory that every later session can read, including sessions in other channels. It therefore requires approval:

- Propose first. List each entry you want to promote and where it would go, and get the user's approval in the same conversation before writing anything to shared memory. Write only the entries the user approved.
- Only distill the current conversation's own session file, never another conversation's.
- If no one is there to approve, as in an unattended maintenance run, post the proposal and write nothing to shared memory.
- Entries the user declines, and anything the user said was private, stay in the session file and are pruned on the normal schedule.

Approved entries go to the appropriate long-term location:

- Project decisions and status changes go to the relevant topic file if using hierarchical-agent-memory v3+. Topic files are the authoritative source for project state.
- New contact information goes to the relevant contact file.
- General observations and events go to today's daily note.
- Durable constraints or pointers go to MEMORY.md as one-line entries only — MEMORY.md is a routing table, not a notebook.

Do NOT dump session state into MEMORY.md as paragraphs. If the information is project-specific, it belongs in a topic file.

## Maintenance and Retention

During a maintenance pass (when the user asks, or as part of a maintenance routine the user has already set up):

- Check WAL for completeness — flag entries that haven't been distilled
- Propose distillation (see Distillation Targets); once the user approves, write the approved entries and remove them from the session file
- Prune session state entries older than 7 days that were distilled or that the user declined to promote — session files are active working memory, not archives
- Verify session state file integrity

Session files should stay small. If a session file exceeds 5KB, it likely contains entries that should have been distilled to topic files or daily notes. Review and distill before the file grows further.

## Integration with Other Skills

**hierarchical-agent-memory** provides the memory structure this skill writes into. With v3+, topic files are the primary working memory layer — distill important session decisions into topic files, not just daily notes. Per-channel session files prevent concurrent writes to the same memory files. Session state files can reference active topics by path for faster context recovery.

**agent-provenance** tracks file authorship. Session state files are agent-authored; provenance headers track creation and review dates. Commit tags apply to session state changes as they do to any other agent-authored file.

**OpenClaw's silent memory flush** (see `docs/concepts/compaction.md`) complements the WAL protocol. Memory flush is reactive and runs a single turn at the compaction boundary to save durable facts to MEMORY.md and daily notes. WAL is proactive and writes per-decision entries throughout the session. Run both — they cover different cadences and do not conflict. Memory flush is OpenClaw's default behavior and does not require this skill to be installed.

## Best Practices

**For session state:** Treat this as active working memory, not long-term storage. With the user's approval, move important decisions to topic files or daily notes during distillation. Prune old entries during maintenance routines. Include pointers to active topic files for faster recovery.

**For topic files:** Keep channel-specific runtime context in the session state file. Distill project decisions and status changes into the relevant topic file during maintenance, after the user approves. Cross-reference between session state and topic files as needed.

**For daily notes:** General observations and events go to daily notes. Project-specific decisions go to topic files, not daily notes. Use the WAL protocol for important facts regardless of destination.

## Related Skills

- **hierarchical-agent-memory** — Hybrid topic-based working memory with optional time-based archival layers
- **agent-provenance** — File authorship, review tracking, and governance
