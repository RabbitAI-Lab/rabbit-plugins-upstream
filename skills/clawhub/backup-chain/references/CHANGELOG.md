# Changelog — backup-chain

## 1.0.4 — 2026-09-25

Third ClawHub audit round (against 1.0.3). One A.I.G-level finding — **T09,
"Workspace-Controlled Ledger Configuration Enables Arbitrary Shell Command
Execution" (High, `scripts/backup_chain.py`)** — the command adapter elevated
from round 2's mid-severity SkillSpector note to a full finding. Its argument
is fair and specific: the 1.0.3 runtime warning fires *before* execution but
requires no consent, so a planted `.vault/config.json` still executed on
routine `status`/`check`/`verify`/`restore`/`build`; the finding explicitly
acknowledges the feature itself ("commands deliberately configured by the
current user remain authorized functionality"). Warning ≠ consent — adopted.

Adopted (T09), mapping the audit's remediation list onto a no-network CLI:

- **Refuse-by-default execution.** Every command-adapter execution now
  requires an explicit per-invocation `--allow-cmd-ledger`. Without it, the
  read path reports unreachable with guidance (status/check degrade to the
  existing marked-skip fencing semantics, never fatal, never silent) and
  `build --register` fails loudly (rc 1). Implements "do not automatically
  execute command adapters loaded from an existing workspace", "explicit
  per-invocation command-line opt-in", and "safe default mode in which
  status, verification, and restore operations refuse command adapters".
- **argv execution, no shell.** Both call sites run `shlex.split(cmd)` with
  `shell=False`. Shell metacharacters are inert — `;`, `|`, `>` become literal
  arguments — and shell features exist only if the config names `sh -c '…'`
  itself, in plain sight in the WARN preview. Unparseable command lines are a
  clean refusal, not a traceback. Implements "prefer argument-array execution
  with shell=False".
- **Triage of the remaining remediation suggestions.** Interactive
  confirmation, approved-config digests, and an identity-bound trust store are
  heavyweight forms of the same consent gate; for a no-network, no-daemon CLI
  the per-invocation flag is the non-interactive equivalent — automation passes
  it only inside operator-reviewed scripts (our own chain builder does exactly
  that). "Store trusted configuration outside the workspace" is declined for
  the same reason `init` writes `.vault/` in the first place: the config is the
  deployment, and the flag now gates whether it can run at all. "Separate
  read-only inspection from adapter-authorized operations" was already the
  fence design; the refusal keeps file/none ledgers untouched.
- The 13 SkillSpector pattern findings repeat round 2's classes and keep that
  round's triage: two adapter excerpts (moot — the flagged `shell=True` is
  gone), four test-fixture false positives (the suite's own symlink/`ln`
  fixtures read as runtime behavior), two behavioral `subprocess` notes
  (inherent to a command-adapter feature), three skill-enumeration hits on the
  suite's fake `SKILL.md` fixture, and undeclared-scope/vague-trigger notes
  (trigger breadth is the feature).

Also fixed: `VERSION` in `backup_chain.py` had lagged at 1.0.1 through the
doc-bumped 1.0.2/1.0.3 releases — `--version` and fresh configs now record the
real release number.

Tests: T12/T23 fixtures moved to argv-form (`false`, `tee -a`) and given the
opt-in flag; new T24 (12 assertions): status proceeds marked without opt-in,
read/append never execute without it (canary + side-effect checks), register
fails loudly naming the flag, opted-in read parses, `;` stays literal under
argv execution, opted-in append lands through `tee`, unparseable command line
is a clean shlex refusal. Suite: 85 → 97, all green on first full run.

## 1.0.3 — 2026-09-25

Second ClawHub audit round (against 1.0.2, published same day). The audit's
two 1.0.1-era findings — nested-symlink read escape (T05) and restore write
escape through symlinked target components (T09) — no longer appear: both
fixes verified out. The new scan returned 14 findings; one was adopted, the
other thirteen triaged as duplicates, test-fixture false positives, or
deliberate design. No archive-format, manifest, or CLI changes — drop-in
compatible with 1.0.x chains.

- **Added (audit: Missing User Warnings, medium — the one adopted finding):**
  the command ledger adapter executed user-configured shell commands
  silently. Every adapter execution now prints a `WARN` line to stderr at
  the point of execution, naming the command key (`read_cmd` / `append_cmd`)
  with a truncated preview and pointing at `.vault/config.json` — once per
  command per process, stderr only, so stdout (JSON `check` output, ledger
  parsing) stays byte-clean. The capability is unchanged by design; the
  silence was the defect. T23 covers it: warnings fire on `status`, `build
  --register`, and `check`; the ledger still parses through the warned read
  path; the adapter still appends; stdout stays clean. Suite: 77 → 85.
- **Not adopted — command adapter shell execution (5 findings, variously
  high/medium, all circular):** `read_cmd`/`append_cmd` via `shell=True` is
  the documented, opt-in core of the `command` adapter — config-as-code of
  the git-hook trust class, flagged as such in the audit's own Overview
  ("review .vault/config.json as executable code"), SECURITY.md, and
  SKILL.md Permissions. Removing it would delete functionality the adapter
  exists to provide; the audit's own install guidance is "prefer the default
  file ledger or ledger none". With 1.0.3 the executions are loud as well as
  documented.
- **False positives — test fixtures scanned as runtime code (6 findings):**
  four "Tool Parameter Abuse" (high) hits on `tests/test_backup_chain.sh`
  are the suite's own symlink fixtures (`ln -s` into throwaway workspaces)
  exercising the 1.0.2 guards, and two "Skill Enumeration" (medium) hits are
  the same fixture creating a dummy `skills/sk1/SKILL.md` to back up. The
  runtime tool enumerates nothing it was not told to back up; "fixing"
  these would mean deleting test coverage.
- **Not applicable — Undeclared Tool Scope (medium, no source excerpt):**
  ClawHub skills carry no MCP permission-manifest format; the declaration
  this finding asks for does not exist to write.
- **Not adopted — Vague Triggers (medium):** the description deliberately
  triggers on backup-adjacent intent and already enumerates its exclusions
  (single-file copies, git, cloud-sync). Trigger breadth is the
  functionality, not a defect; tightening it would make the skill miss the
  wipes it was built for.

## 1.0.2 — 2026-09-25

Security-boundary pass from the ClawHub automated audit (two findings, both
real, both fixed; attribution to the audit). No archive-format, manifest, or
CLI changes — drop-in compatible with 1.0.x chains. Two remediation
suggestions from the audit were deliberately NOT adopted, with reasons:
removing `dereference=True` (would resurrect the 1.0.1 manifest/archive
mismatch and break G8 drills on every legit in-root link) and
O_NOFOLLOW/openat descriptor-relative I/O (defends a local TOCTOU race
attacker, which is outside the stated threat model — documented as a known
limitation instead).

- **Fixed (audit T05, high):** a symlinked *file* nested inside a directory
  member was dereferenced with no containment check, so a link pointing
  outside the project root silently pulled external bytes into the archive —
  an innocuous link name (`cache.txt`) could carry arbitrary readable files
  past the declared read boundary (SKILL.md Permissions) and past
  `secret_warnings`. Nested symlinks are now dereferenced ONLY when their
  resolved target stays inside the project root (`realpath` + `commonpath`,
  never string prefixes); out-of-root links are skipped loudly. In-root links
  (venvs, dotfile mirrors) keep dereferencing — T15 covers this explicitly.
- **Fixed (audit T09, medium):** a pre-existing symlinked directory component
  beneath `restore --target` redirected restore writes outside the selected
  target — member-name validation cannot see the filesystem, only the names.
  Restore now refuses (exit 2, unconditional — `--force` remains a fencing
  override, not a target-safety override) when any destination path component
  under the target is a symlink, naming the offending component; `--dry-run`
  previews the refusal instead of failing. A symlink at the final component
  counts as a conflict and is replaced only via `--overwrite`, which swaps
  the link itself (`os.replace` does not follow it).
- **Tests:** 61 → 77 assertions. T15 rewritten to prove in-root dereferencing
  survives; T20 proves out-of-root links never reach the manifest; T21 proves
  the symlinked-component refusal (dry-run preview, real refusal, nothing
  written outside the target); T22 proves final-component links are
  conflicts, `--overwrite` replaces the link itself, and the link target is
  never touched. T21 initially caught the fix's own first implementation
  passing the parent dir instead of the destination path — the guard
  examined every component *above* the parent and none of the parent; the
  suite went red exactly as designed.

## 1.0.1 — 2026-09-25

Bug-fix review pass — no protocol/invariant changes, no CLI/manifest format
changes. All four fixes are things the 1.0.0 SKILL.md/SECURITY.md already
claimed as the intended behavior; 1.0.1 makes the code match the docs.

- **Fixed:** a member directory containing a symlinked *file* (a real backup
  target: venvs, node_modules, dotfile symlinks, …) made every build fail its
  G8 restore drill. The manifest hashed the dereferenced content but the
  archive stored a bare symlink entry with no bytes, so drill/restore could
  never resolve it. `tarfile.open(..., dereference=True)` on the build path
  makes the archived bytes match the manifest hash, as SECURITY.md always
  claimed.
- **Fixed:** a *broken* symlink nested inside a directory member crashed the
  whole build with an unhandled `FileNotFoundError` traceback instead of
  being excluded with a warning (SECURITY.md's documented behavior).
  `collect_members` now checks for this case and skips it cleanly.
- **Fixed:** `member add` / `member remove` with no PATH argument crashed
  with an unhandled `AttributeError` instead of a clean refusal.
- **Fixed:** `restore --dry-run` against a target with conflicting files
  refused (exit 2, demanding `--overwrite`) before it ever reached the
  dry-run branch — so a dry run could not be used to discover conflicts,
  which is exactly what a dry run is for. Conflicts are now included in the
  dry-run preview; `--overwrite` is only required for a real restore.
- **Hardened:** `validate_archive_names` now also rejects Windows
  drive-letter member paths (`C:/x`), matching the check `normalize_member`
  already applied on the `member add` side. `os.path.join` treats such a
  path as absolute on Windows, silently ignoring `--target`; POSIX hosts
  were never affected.
- **Improved:** `restore` previously called the ledger adapter's read step
  twice per invocation (once inside the fencing gate, once for the
  authenticity check) — meaningful for the `command` adapter, whose read
  step is an arbitrary user shell command. It now reads once and reuses the
  result.
- Added T15–T18 to the test suite covering all four fixes (47 → 57
  assertions); none of the four were previously exercised.

### 1.0.1 final-version pass (same day, adopting the external review)

All fixes above were contributed by an external reviewer, verified against the
existing 47-assertion suite, and adopted in full. The final pass added one
guard from the same defect family the review had missed, plus its regression
test:

- **Hardened:** non-regular files (FIFOs, sockets, devices — including
  symlinks pointing at them) inside member directories are skipped with a
  warning. Previously they reached the hashing step, where a FIFO would hang
  the build indefinitely. T19 exercises this under a hard `timeout` (57 → 61
  assertions total; T17 also gained a `recheck` bad-input case).
- **Packaging:** final `.skill` rebuild confirmed against the tree after an
  independent re-download of the reviewer's submission (sha 862a8c14…, byte-
  identical to the reviewed copy); the first final rebuild had dropped
  `evals/evals.json` from the archive — the release package now carries all
  eight files, and package, tree, and `.moltbot` mirror verify byte-identical.

## 1.0.0 — 2026-09-25

Initial release. Distilled from a production chain that survived 14 wipes over
nine days (gens 1–59); every rule below has a named incident behind it.

- Fencing generations: monotonic `generation` inside each archive's manifest;
  `next-gen = max(local, ledger) + 1`; stale handoffs refused by `check`.
- Hash-linked chain: `parent_sha256` per manifest; parent resolution ledger →
  local manifest → omitted-with-warning; filename guessing removed (it bit us).
- Manifest member map (`path → sha256` per file): archives carry their own
  proof, so restores verify with no surviving source.
- Ledger adapters: `none` / `file` (wipe-safe only outside the machine) /
  `command` (user-supplied read+append shell snippets; no platform code).
- Gated builds G1–G8: member presence (critical-fatal) → generation fencing →
  parent resolution → manifest inside → listing check → manifest roundtrip →
  sha256 receipt → restore drill.
- Restore drill: extract every member to staging, hash-compare against the
  member map; the archive is not "verified recoverable" until it passes.
- Per-member verified restore (never bulk extraction — silent zero-write
  extraction observed twice in production); overwrite and fencing refusals are
  separate explicit flags; post-apply `recheck` receipt.
- Ledger line format `gen=N sha256=… parent=… built=… file=… entries=…`,
  append-only; manual posting supported (challenge-gated channels).
- `verify`: receipt + ledger authenticity, with loud UNKNOWN/SKIPPED marking.
- Stdlib-only, Python 3.8+, no network, no content parsing, path-traversal
  defences on every archive read, dangerous restore targets refused.
