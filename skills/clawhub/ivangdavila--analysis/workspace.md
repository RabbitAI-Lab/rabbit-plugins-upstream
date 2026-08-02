# Workspace — Structure, Orphans, Repo State, And Getting It Back

**Before this pass**, read `## System Baseline` in `~/Clawic/data/analysis/memory.md` (or the file its `## Boxes` line names) for the recorded paths, the last measured sizes, and which directories are deliberately large. Growth is only a finding against a previous number.

**Contents:** [What Must Exist](#what-must-exist) · [Orphans And Dangling References](#orphans-and-dangling-references) · [Size Budgets With Formulas](#size-budgets-with-formulas) · [Staleness](#staleness) · [Duplication And Contradiction](#duplication-and-contradiction) · [Malformed Files](#malformed-files) · [Invisible Characters](#invisible-characters) · [Repository State](#repository-state) · [Retention](#retention) · [Backup And Restore](#backup-and-restore) · [Write It Down](#write-it-down)

## What Must Exist

Every agent setup has an instruction layer, a data layer, and an ignore layer. The audit checks that all three exist and that they agree, whatever they are called here.

| Layer | Present means | Missing produces |
|---|---|---|
| Instructions | The file(s) the agent loads on every run, discoverable from the project root | Behavior that changes with whoever last pasted context |
| Index | A file that lists what is stored and when to read it | Data that exists and is never read — the most expensive failure in this domain (`agent-memory.md`) |
| Ignore rules | `.gitignore` (or equivalent) covering data, env, cache, and credential paths | The exposure findings in `secrets.md` |
| Data root | One directory holding persistent state, not scattered per-tool folders | Backups that miss half the state |

Report a missing layer as WARNING with the one-line action, never as a lecture about structure.

## Orphans And Dangling References

Two different bugs, two different fixes, and conflating them is why "clean up the workspace" loops forever.

- **Orphan**: the file exists, nothing points to it. It will never be read. Fix: index it, or delete it after confirming its content is elsewhere.
- **Dangling reference**: something points to a file that does not exist. Every read of that pointer fails silently. Fix: repair the path or remove the pointer.

Detect both with one set difference in each direction: the set of `.md` files under the data and notes roots, versus the set of paths mentioned in the index and instruction files. Left-only entries are orphans, right-only entries are dangling. Report counts, then list the five largest orphans and every dangling reference — dangling ones are always listed in full because each is a broken promise.

Second-level references are a third case: a file reachable only through another file (`A → B → C`). `C` is read only if `B` was read first, which the audit cannot assume, so `C` behaves like an orphan in practice. Flatten to one level from the entry point.

## Size Budgets With Formulas

| Budget | Threshold | How to compute |
|---|---|---|
| Always-loaded set | any single file above ~10 KB, or ~25 KB total, deserves a line in the report | `tokens ≈ bytes / 4` (prose) or `bytes / 3` (code, JSON); `daily tax ≈ tokens × turns_per_day` (SKILL.md Rule 8) |
| Memory and notes tree | `memory_budget_mb` (default 5 MB) | `du -sm` on the tree; compare with the last baseline, not with zero |
| Any file the agent edits by rewriting whole | ~400 lines | Rewrite cost is the whole file every time, in and out |
| Single data file read in full on a common path | ~40 lines or ~15 entries of real content | The split threshold in `memory-template.md` |
| Repository working tree | any single tracked file above 5 MB | `git ls-files -z \| xargs -0 du -k \| sort -rn \| head` — large files bloat every clone forever |

A budget breach is a WARNING only when it is *growing*: 6 MB of notes that has been 6 MB for a year is a fact, not a problem. Compare against the baseline and report the delta and the rate.

## Staleness

| Signal | Threshold | Action |
|---|---|---|
| Task or board entry untouched | 30 days | Close, delegate, or move to a parked section — three states, no fourth |
| Date-named note file | older than 30 days and already summarized | Move to an archive directory; deletion is a user decision |
| Completed items still in an active list | any | Archive; a list that is 70% done items is a list nobody reads |
| A reference to a tool, host, or service that no longer exists | any | Dangling reference, above |
| A "temporary" file (`tmp`, `draft`, `wip`, `old`, `copy`) | 14 days | Name it or delete it; the name is the audit trail |

## Duplication And Contradiction

The same fact in three files means two of them will go stale, and the agent will read whichever it reaches first. Detection is cheap: for each key fact in the baseline (paths, endpoints, thresholds, names), grep for it and count files. More than one home is a finding; the action is to pick the canonical home and replace the others with a pointer to it.

Contradiction is the severe form — two files giving different values for the same key. Always WARNING or higher, because the agent will act on one of them and nobody can predict which. Resolve by timestamp, keep the newer, and note in the canonical file what was replaced.

## Malformed Files

- Frontmatter that does not parse: an unquoted colon inside a value, a tab where spaces are required, a missing closing `---`. The file loads as text or not at all, silently.
- Unbalanced code fences: everything after an unclosed fence renders as code, which usually means the rest of the file stops being instructions.
- Broken links between local files (relative path from the wrong directory is the common one).
- Mixed line endings (CRLF in a file the agent appends to with LF) — makes every diff useless and can break a shebang.
- Symlink loops and symlinks pointing outside the workspace root: the second is also a permissions finding (`permissions.md`).

## Invisible Characters

Zero-width space (U+200B), zero-width joiner, non-breaking space, bidirectional overrides (U+202E), and soft hyphens are three problems at once: they break greps, they make two identical-looking strings unequal, and in an instruction file they are a place to hide text a human reviewer cannot see. Any occurrence in an instruction file or a skill is a finding — WARNING for whitespace variants, CRITICAL for bidi overrides or hidden text in a file that steers behavior. Detect with a byte-class grep over instruction files; report the file, the line, and the codepoint, never a copy of the line.

## Repository State

| Check | Threshold | Why it matters |
|---|---|---|
| Uncommitted changes | older than 7 days | Work with no history; one bad edit and it is gone |
| Unpushed commits | any, on a machine with no backup | The only copy lives on one disk |
| Detached HEAD or a long-lived local-only branch | any | Commits nobody will find |
| `.gitignore` coverage | data root, `.env*`, caches, credential paths | Everything in `secrets.md` |
| Tracked files that should be ignored | any | `git ls-files -i -c --exclude-standard` lists them |
| Stash entries | older than 30 days | Hidden work, invisible to every other check |
| Repository size vs working tree | tree ≫ checkout | History carries something big (`git count-objects -vH`) |

## Retention

Anything that appends forever needs a stated limit, or the disk-full finding arrives during something else. Per class: session transcripts, job output, run history, caches, generated reports, archived notes. A retention rule is three numbers — how long, how big, and what happens at the boundary (delete, archive, compress). Missing retention on a growing directory is WARNING once the directory doubles between two runs.

## Backup And Restore

- **Coverage question**: if this disk died right now, what is gone? Enumerate against the data root, the repo remote, and the credential store. Anything only in the data root and not in a backup is the answer.
- **The drill is the check.** A backup that has never been restored is a hypothesis. Restore into a scratch directory, open two files that the agent needs, and time it. Record the measured time in `## System Baseline` in `memory.md`, with the drill's date on its `## Due` row — restore time is the number nobody knows until the bad day.
- Cadence: quarterly, as a `## Due` row. If the drill has never run, that is a WARNING regardless of how good the backup looks.
- Backups inherit the secrets rule: a backup of a workspace that contained a credential still contains it (`secrets.md`).

## Write It Down

Same turn as the pass:

- Paths, measured sizes, always-loaded set and its token estimate, repo remotes, backup target and last measured restore time → `## System Baseline` in `memory.md`.
- Orphans, dangling references, contradictions, retention gaps → `## Open Findings`.
- A deliberately large or unindexed directory the user defends → `## Accepted`, with the path glob and a review date.
- The restore drill's date and measured time → the `## Due` row plus a line in `runs/<year>.md`.
- A restore or migration procedure that worked → `~/Clawic/data/analysis/artifacts/restore-<kebab>.md` with its `## Boxes` line.
