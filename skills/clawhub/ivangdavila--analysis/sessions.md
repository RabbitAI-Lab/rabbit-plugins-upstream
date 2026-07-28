# Live Activity — Loops, Zombies, And Two Writers On One File

This is the only phase where the problem is still happening while you read about it. Everything here is time-sensitive: a looping session spends money per minute, and two concurrent writers destroy data on every save.

**Before this pass**, read `## Open Findings` in `~/Clawic/data/analysis/memory.md` for sessions already known to be stuck, so a second run does not re-open the same finding under a new id.

**Contents:** [What To Enumerate](#what-to-enumerate) · [The Loop Signature](#the-loop-signature) · [Zombies](#zombies) · [Concurrent Writers](#concurrent-writers) · [Stale Locks](#stale-locks) · [Orphan Processes](#orphan-processes) · [Evidence Before Killing](#evidence-before-killing) · [Kill Order](#kill-order) · [Prevention](#prevention) · [Write It Down](#write-it-down)

## What To Enumerate

Cheapest evidence first (SKILL.md Rule 2): process list, then working directories, then transcripts, then any platform session listing.

| Item | Field that matters | How it goes wrong |
|---|---|---|
| Running agent processes | start time, working directory, parent pid | An hours-old process nobody remembers starting |
| Spawned subagents | spawn time, parent, completion state | Spawned with no completion path |
| Sessions with an open transcript | last write time | Writing for hours with no human turn |
| Working directories in use | duplicates across sessions | Two writers, below |
| Lock files under the data root | age, owner pid | Stale locks that block real work |
| Detached shells and watch loops | command line | A `while true` from a debugging session three days ago |

## The Loop Signature

A stuck agent does not look stuck. It looks busy. Three signals, any two of which together are conclusive:

1. **Repetition** — the same tool call with byte-identical arguments three or more times in a session. Once is a retry, twice is a bad retry policy, three times is a loop.
2. **No new artifacts** — token count rising while the set of files created or modified stays constant. Cost accrues, nothing is produced.
3. **Oscillation** — a file written back and forth between two states (A → B → A), typically two rules disagreeing about the same line.

Reportable threshold for an unattended session: cost or duration since the last new artifact exceeding one interval of ordinary work — a session that has produced nothing new in 15 minutes while still calling tools is a WARNING; one that has produced nothing in an hour is CRITICAL, because the only thing it is reliably doing is spending.

Related fan-out check: if each stuck session spawns children, growth is exponential, not linear. Count depth as well as breadth (`permissions.md`).

## Zombies

A subagent that was spawned, never completed, and has not written anything in 24 hours. Two causes, and the fix differs:

- **No completion path** — the parent never defined what "done" is, so the child waits. Fix at the spawn site: a completion condition and a timeout, always both.
- **Waiting on something that will never arrive** — a prompt on a TTY that does not exist, a lock, a network call with no timeout. Fix at the dependency; the same missing timeout will do it again next week.

Zombies are usually cheap (idle, not looping) and therefore ignored for months. They matter for two reasons: they hold locks, and they make the session list unreadable, which is how a real loop hides.

## Concurrent Writers

Two sessions with the same working directory, both able to write the agent's memory or notes, is silent data loss: whole-file writes mean last-writer-wins, and the loss is invisible because both writes succeeded.

Detection: group running sessions by working directory; any group larger than one is a finding. Severity CRITICAL when both sessions are actively writing (compare file mtimes against session start times), WARNING when one is idle.

Fix, in order: end the one that is not doing the work; where both are needed, give the second a different working directory, or serialize writes behind a lock with a max age. Append-only files tolerate concurrency far better than rewritten ones — this is a real argument for the log-shaped boxes in `memory-template.md`.

## Stale Locks

A lock without a max age converts one crash into a permanently blocked job. Every lock file should carry the owner pid and its start time; a lock whose pid is not running is stale by definition and safe to break after recording who held it and when.

Detection: for each lock file under the data root, is the pid alive, and is the lock older than the operation it guards should take? Report age and owner. Breaking a lock is a `safe-only` fix — reversible, verifiable, and its inverse is trivial — but record it in the fix row regardless (`remediation.md`).

## Orphan Processes

Processes whose parent has exited: watchers, headless browsers, language servers, tunnels, dev servers. They hold ports, memory, and sometimes credentials. Signals worth a finding: a port that a new run cannot bind, memory pressure with nothing obviously running, a browser process older than any session.

Check bound ports against the inventory of what should be listening. An unexplained listener is also a `permissions.md` question, not just a hygiene one.

## Evidence Before Killing

Killing first destroys the only record of why it happened, and guarantees the same loop next week. Before any kill, capture, in this order:

1. The repeated call — tool name and arguments, once, not the whole loop.
2. The last few exchanges before the repetition started; the cause is nearly always visible there.
3. Cost and duration since the session's last new artifact.
4. What the session was asked to do, in one line.

That is four lines in the fix row and it is the difference between a cleanup and a fix.

## Kill Order

1. Snapshot the evidence above.
2. Stop the spawner before the spawned, or the children keep coming.
3. Terminate gracefully first; escalate to a forced kill only after the grace period, and note that you did in the fix row of `runs/<year>.md`.
4. Release what it held: locks, ports, temporary files.
5. Verify: the process is gone, the lock is gone, and the cost meter stopped moving (`cost.md`).
6. Fix the generator — the missing timeout, the missing completion condition, the retry without a cap — or this recurs, and by SKILL.md Rule 6 that makes it a more severe finding next run.

Killing sessions is never a `safe-only` auto-fix: it is destructive and its inverse does not exist. Propose it with the evidence attached.

## Prevention

| Guard | Value that works |
|---|---|
| Wall-clock timeout on every unattended run | Longer than p95 runtime, shorter than the interval it runs on |
| Completion condition on every spawn | Stated at the spawn site, testable without a human |
| Max spawn depth | 2 unless there is a reason on record |
| Repetition circuit breaker | Stop after the same call with identical arguments three times |
| Cost ceiling per unattended run | Derived from the schedule: monthly budget ÷ runs per month (`cost.md`) |
| No interactive prompts in unattended paths | Any prompt is a hang, not a question |

## Write It Down

Same turn as the pass:

- Concurrency posture, timeout and depth limits, ports expected to be listening → `## System Baseline` in `memory.md`.
- Each stuck, zombie, or duplicated session with its evidence lines and what was done → `## Open Findings` while unresolved, and a fix row in `runs/<year>.md` when handled.
- A long-lived session the user runs on purpose → `## Accepted`, identified by working directory or job name, with a review date.
- The cause of a loop and how it was broken → `~/Clawic/data/analysis/artifacts/loop-<kebab>.md`, plus its `## Boxes` line. Loops recur by family; the write-up is what makes the second one a five-minute fix.
