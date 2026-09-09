---
name: tinker-orca
version: 1.2.1
description: "Stop editing files one at a time. ORCA drafts every change in parallel, then applies them per-file-serialized so disjoint files fly and shared files never collide. It SPAWNS SUBAGENTS on your own provider (one per unit, which costs money) and writes ONLY the repo-relative files you list — an allowlist enforced in code, not requested in a prompt, and since 1.2.1 backed by a realpath check on disk so a symlinked path component cannot carry a write outside the repository. Committing rewrites git history and needs commit AND confirmedCommit; it is OFF by default and never inferred. In its default mode it creates a git worktree and branch per unit-group and removes them afterwards. It runs an external program ONLY when you pass its absolute path IN THE CALL — no environment variable can name one. See Permissions, Data Flow and Consent."
metadata:
  openclaw:
    emoji: "🐋"
    os: ["linux", "darwin"]
    requires:
      capabilities: ["shell", "file_write", "file_delete", "subagents"]
    permissions:
      shell: "Runs git inside the repoRoot you name: status, log, rev-parse, add, commit, worktree add/remove/prune, merge --ff-only, cherry-pick, checkout of named paths, and `git stash create`. Also mktemp/cp for off-tree staging, and a POSIX shell function that resolves write targets with `cd -P`/`pwd -P` before anything is written. It runs an external program ONLY when you pass its absolute path as an ARGUMENT (spawnCliPath, conductorPath, ownershipScript); with none passed, no other command is executed. Since 1.2.1 the environment cannot supply one — ORCA_CONDUCTOR / ORCA_SPAWN_CLI / ORCA_OWNERSHIP_SCRIPT are no longer read, because a variable set by a shell profile, a CI job or a parent process is not a consent surface. Never push, force-push, amend, or --no-verify."
      file_write: "Only the repo-relative paths listed in each unit's `writes`. Two independent boundaries: (1) every drafted patch hunk is checked against that allowlist in code before it is applied, and a unit that reports writing elsewhere is failed and disables committing for the run; (2) since 1.2.1 each write target is resolved ON DISK before it is written — a target that is a symlink, or whose nearest existing parent resolves outside the repository (or outside the group's worktree, in worktree mode), is refused and the unit stops. The first check reads the path as text and cannot see a symlinked directory component; the second can. Plus one temporary directory created with `mktemp -d` at mode 0700."
      file_delete: "Three delete paths, all scoped: (1) the temporary staging directory this run created with mktemp; (2) `git worktree remove` on worktrees this run created, whose paths carry this run's unique id — never --force, never a worktree it did not create; (3) with allowForeignWip only, `git checkout -- <named files>` discards another session's uncommitted changes in specific files after snapshotting them to a dangling commit, then restores them. It deletes no branches."
      subagents: "Spawns one or more workers per edit-unit through YOUR configured provider, at your cost. Model choice is yours. Cross-provider critics and panels are off unless you supply spawnCliPath."
      network: "None of its own. Your spawned agents use whatever provider you already configured."
      credentials: "None. Reads no tokens, keys or auth files."
repository: https://github.com/globalcaos/tinkerclaw
homepage: https://github.com/globalcaos/tinkerclaw
---

# ORCA — parallel multi-agent coding

> One of dozens of skills and plugins in **[TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — a self-improving OpenClaw fork that's been running 24/7 for months.

Your agent edits twelve files. One. At. A. Time.

You watch it read, think, patch, verify — then start again on the next file as if the other eleven didn't exist. The work is embarrassingly parallel and it is running in single file.

The reason nobody parallelises it is the fear of two workers touching the same file. ORCA removes the fear instead of working around it: the only contended thing in a repo is a **shared file**, so it puts a short-lived lease on files and on nothing else. Disjoint files run at full concurrency. Shared files queue for a moment. A patch that goes stale while waiting is re-derived rather than clobbering someone.

"Did it merge cleanly?" stops being a question you ask.

**Part of [TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — real-time token tracking, self-improving crons, persistent cognitive memory. This is one piece of that stack; the repo has dozens more.

👉 **https://github.com/globalcaos/tinkerclaw**

_Clone it. Fork it. Break it. Make it yours._

## How it works — three phases

**Phase A — no lease, fully parallel.** Every unit reads, diagnoses and drafts its exact patch simultaneously. That is ~95% of the wall-clock, and none of it contends. Nothing is written in this phase.

**Phase B — brief per-file lease.** Acquire the lease, apply the prepared patch, verify that file, release. Disjoint units run concurrently; units sharing a file serialise; a staleness guard makes a worker re-derive a patch that no longer applies.

**Phase C — one commit per unit.** OFF by default; needs `commit` **and** `confirmedCommit`. Each unit stages only its own files — never a blanket stage — so a parallel session's unrelated work is never swept in.

By default each unit-group applies inside its **own git worktree** off clean HEAD (branch `orca/<group>-<runId>`), and Phase C merges those branches back. Pass `worktreePerAgent: false` to apply directly in your working tree instead.

## Requirements

- OpenClaw with a configured model provider.
- A git repository. ORCA works on the repo you name and nowhere else.
- Optional: a subagent-spawn CLI (`spawnCliPath`) if you want cross-provider critics or panels. There is no default path — without it, those features stay off.

## Usage

```js
Workflow({
  scriptPath: "<this skill>/scripts/parallel-implement.workflow.js",
  args: {
    repoRoot: "/absolute/path/to/your/repo",
    units: [
      { id: "u1", task: "what to change", writes: ["src/a.ts"], reads: ["src/x.ts"] },
      { id: "u2", task: "what to change", writes: ["src/b.ts"] }
    ],
    verifyPreset: "npm-test",   // named check, run after each unit applies
    commit: true,               // opt in...
    confirmedCommit: true       // ...and confirm. Both required, or nothing is committed.
  }
})
```

`units[].writes` are the lease keys **and** the enforced write allowlist. Keep them disjoint for maximum parallelism; overlapping writes are safe — they simply serialise.

### Arguments worth knowing

| arg | default | what it does |
| --- | --- | --- |
| `repoRoot` | — | **Required.** Absolute, canonical path. Rejected if relative, containing `..`, or carrying shell metacharacters. |
| `units[].id` | — | **Required.** Must match `^[A-Za-z0-9_-]{1,64}$` — it appears in branch names and commands. |
| `units[].writes` | — | **Required.** Repo-relative paths only. Absolute paths, `..`, globs, and option-looking names are rejected. |
| `commit` + `confirmedCommit` | both `false` | Both must be `true` before anything is committed. |
| `coAuthor` | none | No attribution trailer is added unless you supply one. |
| `verifyPreset` | none | A named check: `npm-test`, `pnpm-typecheck`, `cargo-check`, `go-test`, `pytest`, … |
| `verifyHint` / `integrationVerify` | none | Raw command strings. **Refused unless `allowRawCommands: true`**, and echoed to the log before any agent runs them. |
| `policyText` | none | Extra house policy for draft agents. Printed in full before it is used, and ranked below the task, the allowlist and the repo boundary. |
| `worktreePerAgent` | `true` | Apply in an isolated worktree per group; `false` applies in your working tree. |
| `allowForeignWip` | `false` | Required before ORCA will touch another session's uncommitted changes. |
| `hmrPaths` | `[]` (off) | Repo-relative prefixes a live dev server watches; those files are staged off-tree and landed in one burst. |
| `spawnCliPath` / `conductorPath` / `ownershipScript` | none | Absolute paths to programs you want ORCA to run. **Arguments only** — no environment variable is consulted, and unset means the dependent feature is off. There is no fallback path of any kind. |

## Permissions, Data Flow & Consent

**What it does.** Runs git inside the `repoRoot` you pass, applies patches to the files you listed, and spawns one or more subagents per unit through your own provider.

**Everything it can touch, named.** git worktree and branch creation and removal (paths and branches carrying this run's unique id); `git stash create` snapshots; commits, fast-forward merges and cherry-picks when you have opted in; one `mktemp -d` directory at mode 0700 for off-tree staging and inter-agent hand-off; and an external program only when you give its absolute path. If you configure a `conductorPath`, ORCA also writes routing outcomes — domain, model, pass/fail — to that script's ledger. No code, prompts or file contents are written there.

**What it does not do.** It makes no network calls of its own, reads no credentials, and never pushes, force-pushes, amends, or passes `--no-verify` — your hooks run.

**The write boundary is checked twice, and the second check is on disk.** The first boundary is
lexical: every drafted hunk is re-checked against the unit's `writes` list before it is applied, and
a unit whose patch escapes is blocked whole rather than trimmed. That check reads the path as text,
and text has a blind spot — a path component can be a **symlink**. If `docs/vendor` points at `/etc`,
then `docs/vendor/hosts` is a perfectly well-formed repo-relative path that passes every string check
and writes `/etc/hosts`. So since 1.2.1 every write target is also resolved **on the filesystem**
before it is touched: the nearest existing parent is resolved with `cd -P`/`pwd -P` and compared to
the repository root (or, in worktree mode, to the group's own worktree), and a target that is itself
a symlink is refused outright. A path that resolves outside the root stops the unit and is reported
as a finding — it is never "fixed" into a different path. The worktree gets the same treatment: the
apply agent confirms the worktree it created resolves to the path ORCA named, and a group that
reports having applied somewhere else disables committing for the whole run.

**No program can be named by the environment.** ORCA runs an external program only when you pass its
absolute path as an argument. Until 1.2.1 an unset argument fell back to `ORCA_CONDUCTOR`,
`ORCA_SPAWN_CLI` or `ORCA_OWNERSHIP_SCRIPT` in the environment — which is the same problem one level
down: you read your own invocation, see no external program, and a variable set by a shell profile, a
CI job, a parent process or an earlier agent supplies one anyway, and it is executed. Those variables
are no longer read. What runs is visible in the call that asked for it.

**The write boundary is code, not a request.** Phase A is *asked* to stay inside each unit's `writes`; that request is not a control, so every drafted hunk is re-checked against the allowlist before it is applied, and a unit whose patch escapes is blocked whole rather than trimmed. After applying, each unit's reported file list is checked again; a unit that reports writing outside its allowlist is failed and committing is disabled for the entire run.

**Committing is OFF unless you ask twice.** Phase C writes git history, so it needs BOTH `commit: true` and `confirmedCommit: true`. With anything less, ORCA applies and verifies the patches and leaves them for you to inspect. There is no flag, env var or heuristic that makes committing the default, and the confirmation is yours to give — an orchestrating agent should not supply it on your behalf.

**Another session's work is not ours to move.** If the pre-flight finds uncommitted changes belonging to someone else in files this run writes, ORCA refuses to commit and says which files caused it. Snapshotting and restoring that work across a merge happens only with `allowForeignWip: true`.

**Verify commands are named, not free text.** A verify string is handed to an agent with "run this" attached, so the default is a fixed table of presets. Raw command strings still work, but only behind `allowRawCommands: true`, and the exact text is printed before any agent sees it.

**It ships no policy of its own.** Draft agents receive the unit task, the allowlist, and generic verification discipline. Anything else is yours to pass via `policyText`, which is displayed in full before use and cannot widen the write allowlist or move the repository boundary.

**Temporary files are unpredictable by construction.** The staging directory is created with `mktemp -d` at mode 0700. No path is derived from a unit id, so concurrent runs cannot collide and nothing can pre-create a file a worker is about to trust.

**It costs money.** One or more subagents per unit, on your provider, at your rates. A 12-unit run is at least 12 agents. Start with two.

## When NOT to use it

- A single-file change — just edit it.
- Edits where unit B must read unit A's committed result — split into separate runs.

## Verifying this yourself

```bash
node scripts/selftest.mjs
```

Runs the real workflow against stubbed agents and asserts the properties above: hostile paths, unit
ids and command strings are refused before any agent starts; the double opt-in actually gates
committing; a patch or a report that leaves the allowlist blocks the unit and stops the commit; every
prompt that leads to a write carries the realpath containment check, rooted at the repo in-place and
at the worktree in worktree mode; an environment full of `ORCA_*` executable paths supplies nothing;
and no prompt carries policy you did not supply.

## Included Files

| File | Purpose |
| --- | --- |
| `scripts/parallel-implement.workflow.js` | The orchestrator. |
| `scripts/selftest.mjs` | Executable checks for the safety properties documented above. |
