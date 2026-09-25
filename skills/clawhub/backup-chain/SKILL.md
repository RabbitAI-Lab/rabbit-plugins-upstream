---
name: backup-chain
description: "Fenced, hash-chained workspace backups: tarball snapshots carrying a monotonic generation counter and parent sha256 inside each archive, an append-only external ledger (file or user-supplied command — no platform code), gated builds (member presence, manifest roundtrip, sha256 receipt, restore drill), and per-member verified restore. Use whenever the user wants to back up, snapshot, or checkpoint a workspace/project so a crash, wipe, sandbox reset, or rollback can be recovered from; to build or register a backup; to verify, drill, or restore/heal from an archive; or mentions backups, vault, chain head, generations, fencing, restore drill, stale handoff, or wipe recovery — even if none of those exact words are used. Do not use for single-file copies, git/version-control workflows, or cloud-sync setup: this skill is deliberately platform-agnostic and contains no upload code — off-site distribution belongs to the user."
---

# backup-chain v1.0.4

Crash- and wipe-resilient workspace backups built on six invariants learned the
hard way. A chain, not a pile of copies: every archive knows its generation and
its parent's hash, an append-only ledger outside the failure domain remembers
both, and no archive counts as "verified" until a restore drill has passed.

## Permissions

- **filesystem read**: the configured project root and the archive paths passed
  on the command line. Enforced, not assumed: a nested symlink whose resolved
  target leaves the project root is skipped with a warning, so archive
  content cannot escape the boundary through a link planted inside a member
  directory.
- **filesystem write**: `<root>/.vault/` (config, ledger file, drill staging),
  the configured output dir (tarballs + `.sha256` receipts), and
  `restore --target` — never without an explicit `--target`.
- **subprocess**: tarfile/sha256 are in-process; the ONLY external execution is
  the user-configured ledger command adapter (git-hook trust class) — and it is
  refuse-by-default: every invocation that would execute a configured command
  must pass `--allow-cmd-ledger`, and the command runs as an argv vector
  (shlex-split, `shell=False`), never through a shell — pipes/redirects/globs
  exist only if the config names `sh -c '…'` itself. Every execution also
  prints a `WARN` line to stderr naming the command; a workspace-contributed
  config cannot fire on a routine subcommand.
- **network: false** · **eval/exec: false**.
- **file content reading: hashing only** — member bytes are read to compute
  sha256 and streamed through archives; never parsed, logged, or transmitted.

## When to use

Use when **all** of these hold:

- the workspace contains files whose loss would be **costly or irreplaceable**
  (credentials, skills, long documents, derivation trails, worklogs), and
- the environment has a **real failure class beyond your control** — sandbox
  resets, dotdir rollbacks, storage rollbacks, platform-side wipes, and
- recovery must be possible **by a later session with no memory** of this one.

Do **not** use when any of these hold:

- **Version control suffices** — if the history lives in git and the remote is
  trusted, git already solves ordering and integrity
- **Single-file copies** — "copy this file somewhere safe" needs no protocol
- **Secrets without a plan** — archives may contain credential files; if the
  user has no private storage for them, read `references/SECURITY.md` first
- **The user just wants cloud sync** — this skill has no upload code by design

## The six invariants

1. **Ordering is asserted, never inferred.** "Newest" by mtime or filename is a
   claim by whatever last touched the inode. Each archive carries a monotonic
   `generation` integer inside a manifest that lives INSIDE the tarball. Stale
   restores are refused by comparison, not guessed away.
2. **The chain is hash-linked.** Each manifest records `parent_sha256` — the
   hash of the previous generation's archive. Parent resolution order: ledger
   entry first, local archive with matching embedded manifest second, filename
   guessing never.
3. **The ledger lives outside the blast radius.** An append-only record of
   `gen / sha256 / parent / built / file` lines. If the workspace and its
   archives can be destroyed together, the ledger must not be destroyable with
   them. The skill ships three adapters — `none`, `file`, `command` — and
   knows nothing about any platform: a `command` adapter is two user-supplied
   command lines (read / append, executed argv-style behind an explicit
   `--allow-cmd-ledger` opt-in), so any append-only channel the user has
   (a gist, a forum post, a git branch, a database row) works unchanged.
4. **A build is not done until a drill passed.** Member presence gate →
   manifest roundtrip → sha256 receipt → extract to staging → hash-compare
   against the manifest. An archive that was never extracted and re-hashed is
   a hope, not a backup.
5. **Restore is per-member, verified.** Bulk extraction has a documented
   failure class: exits 0, writes nothing (observed twice in production with
   patched sandbox environments). This skill never bulk-extracts. Every member
   is streamed out individually and its sha256 checked against the manifest's
   member map — so restores verify even when the source files are gone.
6. **Fencing failures are loud or refused, never silent.** Unreachable ledger
   → proceed marked `SKIP (unverified)`. Older archive than the ledger head →
   refuse (stale handoff). A clearly marked untested solution is more useful
   than a falsely verified one; a heroic retry that overwrites newer state is
   worse than either.

## Quickstart

```bash
BC="python3 <skill-dir>/scripts/backup_chain.py"

# one-time setup (from the project root)
$BC init --name myproject --ledger file
$BC member add worklog.md --critical
$BC member add skills/
$BC member add download/        # tarballs/receipts inside are auto-excluded
$BC status                      # review the member list

# every build
$BC build --carries "what changed this turn" --register   # --register appends to the ledger
# → prints the ledger line even without --register (for manual posting)

# recovery
$BC verify download/myproject-g12.tar.gz
$BC check download/myproject-g12.tar.gz       # pre-restore fencing gate → JSON
$BC restore download/myproject-g12.tar.gz --target /fresh/workspace
$BC recheck 12                                # post-apply receipt
```

The ledger is what makes a wipe survivable: after a total loss, `next-gen`
still respects the ledger's highest generation, `check` refuses stale archives
the ledger never registered, and `verify` can authenticate a pulled archive
against a ledger entry even when nothing local survives.

## Commands

`<BC>` = `python3 <skill-dir>/scripts/backup_chain.py [--root DIR]`.
Default root is the current working directory; config lives at `<root>/.vault/config.json`.

```bash
# setup
$BC init [--name NAME] [--output-dir DIR] [--ledger none|file|command]
         [--ledger-file PATH] [--read-cmd CMD] [--append-cmd CMD] [--force]
$BC member add PATH [--critical] | member remove PATH | member list

# build and register
$BC next-gen                       # print next generation: max(local, ledger)+1
$BC build [--carries NOTE] [--label LABEL] [--register] [--output PATH]
$BC ledger-line TARBALL [--append] # print (or append) the ledger entry

# inspect and verify
$BC status                         # local chain head, ledger head, members
$BC verify TARBALL                 # sha vs .sha256 receipt + ledger entry
$BC drill TARBALL                  # standalone restore drill

# fencing and restore
$BC check TARBALL                  # → {"decision": "restore"|"refuse"|"skip", ...}
$BC restore TARBALL --target DIR [--overwrite] [--dry-run] [--force]
$BC recheck GEN                    # → {"decision": "ok"|"stale"|"skip", ...}
```

### Exit codes

`0` success · `1` failure (gate, verification, drill, or restore mismatch —
the message says which) · `2` refused (fencing refuse, overwrite without
`--overwrite`, dangerous target). Refusals matter: `build && next_thing` must
not proceed on the assumption a backup exists.

### Ledger adapters

| adapter | read | append | notes |
|---|---|---|---|
| `none` | — | — | local-chain fencing only; every gate result says so |
| `file` (default) | read `.vault/ledger.log` | append + fsync | a ledger inside the workspace is NOT wipe-safe — use it for testing, or move it elsewhere via `--ledger-file` |
| `command` | `--read-cmd CMD` (stdout = ledger text) | `--append-cmd CMD` (entry on stdin) | your platform, your credentials, your identity filtering — the skill never learns any of it |

Command-adapter rules: the configured command is parsed with `shlex` and
executed as an argv vector — no shell — with the entry text piped to stdin for
appends. Shell features (pipes, redirects, globs) are inert unless you name a
shell yourself (`sh -c '…'`), in plain sight in the WARN preview. Execution is
refuse-by-default: pass `--allow-cmd-ledger` on any invocation that should run
the adapter. The flag is per-invocation, so a planted config cannot fire on a
routine `status`/`check`/`restore`; automation passes it only in scripts you
reviewed. Without the flag, the read path reports unreachable-with-guidance
and registration fails loudly. This is user-owned configuration in the
git-hook trust class — review it before `init`. If the channel is shared,
filter for identity **inside the command** (e.g. `grep` for your handle),
because the ledger parser accepts any line that looks like an entry.

## Workflow

### Steady state

1. `member add` every path whose loss would hurt; `--critical` ones fail the
   build if missing (others warn).
2. `build --carries "note"` each session (or each turn). Read the printed
   drill result — `drill: PASS` is the whole point.
3. `--register` (or post the printed line by hand) so the ledger head advances.
4. `status` occasionally; keep at least the newest receipt beside its archive.
5. Copy the newest tarball + `.sha256` off-site **yourself** (see
   `references/PROTOCOL.md` § Off-site distribution for the roundtrip
   verification pattern: upload → fetch back → hash-compare → only then call
   it MATCH).

### Wake after a wipe

1. `status` — inventory what survived. Missing `.vault/` is fine; rebuild with
   `init --force` and re-add members.
2. Find the newest archive (local or off-site pull). `sha256sum -c` its receipt.
3. `verify` against the ledger (authenticates even with an empty workspace).
4. `check` — refuse on stale handoff is the protocol working; investigate, do
   not override.
5. `restore --target .` — per-member, hash-verified.
6. `recheck <gen>` — `ok` closes the incident; `stale` means the ledger
   remembers more than you restored (bytes landed, precondition did not).
7. `build` a fresh generation carrying the heal note, so the chain records the
   incident and the cure.

## Session-tracker and content provenance

This skill pairs well with a checkpointing skill (e.g. session-tracker) but is
a different layer: the tracker checkpoints **task state** so work resumes; the
chain guarantees **artifact custody** so conclusions survive. Custody is not
validity — a sha256 proves a sentence survived a restore, not that it was ever
right. If your workspace records why conclusions were drawn (route files,
premises, falsifiers), put those route files in the member list so they hash
into the same chain as the artifacts they audit. See
`references/PROTOCOL.md` § Custody vs validity.

## What this skill does not do

- **No network** — no sockets, no HTTP, no upload. Off-site copies are made by
  you; the ledger `command` adapter touches whatever your commands touch.
- **No platform code** — no storage SDKs, no forum clients. Distribution is
  the user's job; verification is the skill's.
- **No secret management** — it will warn when member paths look secret-like
  (credentials, tokens, keys) and hash them like anything else. Whether that
  is safe depends entirely on where you send the archives. Read
  `references/SECURITY.md` before backing up secrets.
- **No content reading** — bytes are hashed and streamed, never parsed or logged.
- **No daemon, no scheduling** — a chain you forget to extend is a pile.
  Pair it with whatever scheduler you already have.

## Files

| Path | Purpose |
|---|---|
| `<root>/.vault/config.json` | Chain configuration (members, ledger, output dir) |
| `<root>/.vault/backup-chain-dir` | Ownership marker |
| `<root>/.vault/ledger.log` | Default file-ledger (append-only) |
| `<root>/.vault/drill/` | Restore-drill staging (self-excluded from archives) |
| `<root>/.vault/last_build.json` | Receipt of the last build (gen, sha, gates) |
| `<output-dir>/<name>-g<GEN>[-<label>].tar.gz` | Archives (generation in the NAME is a label; the manifest is authoritative) |
| `<output-dir>/<name>-g<GEN>[-<label>].tar.gz.sha256` | Hash receipts |

## Installation

```bash
cp -r backup-chain/ <your-skills-dir>/backup-chain/
python3 <your-skills-dir>/backup-chain/scripts/backup_chain.py --help
bash <your-skills-dir>/backup-chain/tests/test_backup_chain.sh
```

Python 3.8+, standard library only, no dependencies, no network.

## Further reading

- `references/PROTOCOL.md` — threat model, the six invariants argued properly,
  gate list, fencing state machine, off-site distribution patterns, and the
  incident classes behind each rule
- `references/SECURITY.md` — secrets in archives, ledger-adapter trust, restore
  overwrite discipline, audit notes
- `references/CHANGELOG.md` — version history
