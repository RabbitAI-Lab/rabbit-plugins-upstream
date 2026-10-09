# Changelog — backup-chain

## 1.2.1 — 2026-10-09

Security hardening: unpredictable staging for every temporary write. No
option, gate, format, or default changed; with no flags passed, every
command behaves exactly as 1.2.0 (the full pre-existing suite passes
unchanged; the suite grows from 271 to 291 assertions, all green).

ClawHub's audit re-scan of 1.2.0 returned the T09 label for a third,
different root cause — and the same scan's own excerpts confirm the
round-3/4/5 consent-gate fixes (command adapter, config path boundary,
external ledger) are intact and remain the design. The new finding,
"Predictable Temporary Files Permit Symlink-Based Writes Outside
Authorized Boundaries" (Warning), is real in our own sink map: temporary
files were created at predictable names beside their destinations —
`.<name>.tmp` for config/marker/receipt/state writes, `<archive>.part`
for build and eviction, `<member>.restore-part` for restore — and the
writes went through path-reopening `open()` calls that follow symlinks.
Anyone who could write to a destination directory (operator-set
`--output`, external ledger path, restore `--target`) could pre-plant
the staging path as a symlink and have the bytes land outside the
boundary the operator chose. v1.2.0's own side-bucket and custody options
made the class worth taking seriously: the number of operator-chosen
destination directories had just grown.

Adopted remediation, per the auditor's suggestions: `tempfile.mkstemp`
in the destination directory (random, `O_CREAT|O_EXCL` — nothing can be
pre-planted at the name), writes through the returned fd (never by
reopening the pathname), fstat regular-file assertion, fsync and
`os.replace` preserved, umask-parity fchmod where the platform allows.
The staging suffix family stays `*.part`, so the self-exclusion default
excludes still shields crash leftovers from re-collection by the next
build (regression-tested both for the new naming and the legacy one).
Regression tests plant symlink decoys at every old predictable staging
name and verify: the decoy target is never written, the decoy itself is
never consumed, the operation succeeds, and no staging leftovers remain.

The standing rule is paid in RESIDUAL_RISK item 12: unpredictable staging
removes an observability signal (watching for predictable staging files
no longer works), and the honest residual stands — an attacker who
controls a destination directory still controls that directory; this
closes the out-of-boundary write primitive, not the trustworthiness of a
hostile directory.

## 1.2.0 — 2026-10-09

The curation layer. Second minor release: no invariant changed, no gate
added, no format broken — everything is additive, and with none of the new
flags passed, every command behaves byte-for-byte like 1.1.1 (asserted by
T31's "default build stays silent about stow" and by the whole pre-existing
suite passing unchanged). Born from a dead-weight audit of the production
chain this skill was distilled from: the chain was quietly creeping toward
its size ceiling, and the audit that slimmed it produced three
generalizations, submitted to the operator with implementation proposals.
The operator's decisions are on the record and shaped everything below:

1. *"We can't expect that an agent using skill would have some storage
   outside of own, so features about side buckets should be under options,
   not default behavior."* — adopted verbatim. There is still no upload
   code; `evict --stow-to|--stow-cmd` and `build --stow-to|--stow-cmd` are
   per-invocation opt-ins, and a build without them prints nothing about
   stow at all. This is the same ruling that shaped the skill at birth
   (PROVENANCE.md: "local-only by default with off-site distribution handled
   by the user") — re-applied to the new surface without amendment.
2. *"Same goes for exclusion of some paths/elements — we can't know for sure
   what structure would other agents have and exclusion shouldn't be on by
   default, but having such option is useful not only for us, so it should
   be there."* — adopted verbatim. Per-member `--exclude` added; the ONLY
   built-in patterns remain the self-exclusion class; no structural defaults
   were added.
3. *"Proposed detections seem like nice failsafes to have."* — implemented
   as advisory warnings that never gate and never change an exit code.
4. *"Make our choice of no user acks a formal option; the option to disable
   acks shouldn't be traceless — no ack should be mentioned as much as ack,
   for honesty."* — adopted as `ack-policy`. The ruling has production
   parentage: the deployment this skill was distilled from went ackless by
   a recorded disposition in September (chat-only operator, no shell; an
   agent-typed relay ack would be self-certification borrowing the
   operator's voice), and until now that choice lived only in that
   deployment's status docs, invisible to every other user of the skill.

- **Added: per-member excludes** — `member add PATH --exclude PATTERN`
  (repeatable), stored on the member, honored while walking that member
  (fnmatch on the root-relative path and the basename, same dual-match
  discipline as the global list). Patterns of the wrong shape are refused at
  config load (the global `exclude` list, previously unvalidated, is
  shape-checked too — additive, since any working config already holds valid
  patterns).
- **Changed: excluded directories prune the walk.** Previously only the
  directory *entry* was dropped and the descent continued, so one pattern
  excluded the entry but not the files under it — the documented
  two-pattern gotcha, now closed: one pattern means the subtree. Configs
  that already listed both forms behave identically (strictly less work);
  no bundled test asserted the leaky behavior.
- **Added: `evict PATH --stow-to DIR|--stow-cmd CMD [--note NOTE]`** —
  custody-preserving member removal. Packages the member's current content
  (own excludes honored) with a per-member hash map and an
  `evict-manifest.json` into `<chain>-evict-g<HEAD>-<ts>-<name>.tar.gz` +
  receipt, hands the package to the destination, and only then untracks the
  member and appends an `event=evict` witness line (through the same
  adapter/consent path as every event). Refuses without a destination
  (silent custody loss is the failure it exists to prevent; `member remove`
  stays the deliberate silent drop), refuses non-members, and **refuses to
  untrack when the hand-off fails** — custody is established before
  tracking stops, never after. `--stow-to` hash-verifies the copy at the
  destination (the roundtrip pattern); a mismatched copy is deleted, not
  left to impersonate custody. Files on disk are never touched.
- **Added: `build --stow-to DIR / --stow-cmd CMD`** — the same hand-off for
  a finished, drill-passed archive. `--stow-to` copies archive + receipt and
  hash-roundtrips the copy; `--stow-cmd` pipes the bytes to the operator's
  own command on stdin (exit code = its claim of success; reported as
  "claimed, not verified"). Failures warn and never gate: the archive
  already exists. Successes append `event=stow` witness lines. The stow
  command is **never read from config** — the planted-config attack class
  has no surface (SECURITY.md § Custody hand-off and eviction).
- **Added: detections** — advisory `DETECT` warnings on build (stderr; never
  stdout, never gates): archive growth vs the parent generation (parent
  archive locally resolved; silently skipped when it is not — a skipped
  advisory is documented, not a fencing claim), duplicate content across
  member paths, largest members entering the chain; `status` now prints raw
  member totals and archive totals, plus the custody-op trail
  (`event=evict|stow|ack-off|ack-on`). Config `detect` object:
  `growth_pct` (50), `growth_mb` (4), `archive_mb` (32), `enabled` (true);
  shape-validated at load.
- **Added: `ack-policy [off|on] [--note NOTE]`** — the ack policy, with the
  rule that a policy change is itself witnessed. Acks are witnesses, not
  gates, so disabling them is legitimate; what it may never be is
  traceless: `off`/`on` append `event=ack-off` / `event=ack-on` through the
  same adapter path and consent boundaries as acks themselves, and both
  REFUSE without a reachable ledger (adapter `none` included) — an
  un-witnessable policy change is refused, not made, and the config is
  left untouched by the refusal. While off: `ack GEN` refuses, naming the
  recorded decision and the re-enable path; `status` shows the policy;
  `verify`'s empty-witness note attributes the absence to the policy
  ("absence is policy, not neglect") instead of reading as perpetual debt.
  Historical acks remain on record and are still shown. Config
  `ack_policy` is operational state only (shape-validated at load; mode
  `off` with string `ts`/`note` and integer `gen`); the ledger line is the
  durable record. Default (key absent) is byte-identical to prior
  behavior, and policy lines are invisible to the build-entry parser by
  the same line-start anchor as every other witness class.
- **Added: ledger `event=evict|stow|ack-off|ack-on` witness lines** —
  invisible to the build-entry parser by the same line-start anchor as
  acks/events;
  `next-gen` untouched; adapter `none` and unreachable ledgers degrade to
  the documented best-effort behavior (the eviction package manifest is the
  durable record).
- **Compatibility:** no manifest/ledger format change, no exit-code change,
  no default-behavior change; `is_excluded` gained an optional parameter;
  `ledger_state` gained an `ops` key (additive). 184 assertions from 1.1.1
  pass unchanged.

RESIDUAL_RISK standing-rule payment (three questions, per feature):

- **Per-member excludes.** New failure it introduces: *the silent hole* — a
  mistyped pattern removes paths from every future archive with no warning
  at all (the one risk class in this skill that produces no signal at build
  time). Duplicates no existing witness; it is a negative capability.
  Failure mode is silent-by-nature, so the compensating controls are human:
  `member list` displays patterns, `status` prints raw weight so missing
  weight is noticeable, wrong shapes refuse at load. Recorded as
  RESIDUAL_RISK item 8.
- **Evict + stow.** New failure: a side-bucket copy that *claims* success
  (stow-cmd exit 0) without the skill being able to check the bytes —
  custody theater one flag away. Named on the output line itself
  ("claimed, not verified"), and `--stow-to` remains the only
  hash-verified path. A failed eviction now keeps the member — the
  control's own failure mode fails loud and refused. Duplicate cost: it
  re-witnesses what the package receipt already proves, buying an
  off-workspace record of the *act* (which the receipt cannot do — it dies
  with the workspace). RESIDUAL_RISK item 9.
- **Detections.** New failure: habituation (a detector that cries wolf
  trains its reader) and false precision (raw bytes ≠ compressed weight;
  duplicate detection sees only members collected this build). Named in
  output ("advisory, never gates") and in RESIDUAL_RISK item 10; the
  never-gate rule is the mitigation for both. Duplicates the size
  information `status` always had implicitly — deliberately: the audit's
  lesson was that implicit is invisible. RESIDUAL_RISK item 10.
- **Ack policy.** New failure: *ackless legitimacy* — the only thing
  distinguishing "disabled by decision" from "nobody watching" is one
  authored, forgeable ledger line, and the record dies with the ledger (a
  wipe that takes both collapses the distinction back to reader judgment).
  Named in the annex as item 11. Compensations are placement and refusal,
  not strength: the line lives where an ack would have lived (same
  adapter, same consent boundaries), no reachable ledger means no policy
  change and a config untouched by the refusal, and read-side honesty
  comes from attribution (`status`/`verify` name the policy) rather than
  from any new gate. Duplicates no witness — it is a policy over an
  existing one; the cost is one more line class in the ledger parser, under
  the same trust model as the others. Failure mode: fails loud at change
  time (refusals); at read time it is attribution, not enforcement.

Tests: 184 → 271 (T29–T33): per-member excludes end to end + walk pruning +
shape refusals; evict refusals, stow roundtrip MATCH, custody-failure member
retention, evict-manifest contents, witness lines; build stow happy/failed
paths + default silence; detections armed/disabled/tuned + status surfaces;
ack policy: off/on witnessed, ack refusal under policy with the re-enable
path named, status/verify attribution, parser discipline (policy lines never
advance next-gen), adapter-none refusal with config untouched, corrupt
`ack_policy` refused at load.

## 1.1.1 — 2026-09-26

Independent review pass (not a ClawHub round — no new scanner finding named
this). One real gap found by adversarial testing rather than by static
scanning: `collect_members`'s out-of-root symlink containment check
(1.0.5/T05) was applied to symlinked *files* found while walking a directory
member, but not to symlinked *sub-directories* found the same walk — a
different code path (`os.walk`'s `dirnames`, not `filenames`). Practical
impact was narrow: `os.walk(followlinks=False)` never descends into a
directory symlink either way, so no file *content* from outside the root was
ever reachable through this gap — confirmed by building an out-of-root
symlinked directory and inspecting the resulting tarball before the fix. What
did leak was the *name*: an out-of-root directory symlink still landed in the
archive as an empty directory placeholder, contradicting SECURITY.md's "skipped
… never part of what you selected." Fixed by applying the identical
`realpath` + `commonpath` check already used for files to each directory name
before it is added; in-root symlinked directories are unaffected (still
preserved as empty placeholders, as before). SECURITY.md corrected to say so
precisely — "neither the manifest nor the archive," not just "never enters
the manifest."

Also independently re-verified from scratch (not reused from the bundled
suite) against the current ClawHub audit (v1.1.0, "Pass", 25 findings):
command-adapter opt-in refusal and `shell=False` (semicolon in `read_cmd` is
inert, not a shell separator), external-ledger-file opt-in refusal, and the
restore `--target` symlinked-path-component refusal. All four held under
fresh adversarial reproduction outside the test harness. The `cot`
secret-scan warning (audited as "missing" — the changelog text didn't
describe it) was confirmed to already fire correctly at build time; no code
change needed there, only that the changelog prose undersold what the code
does.

RESIDUAL_RISK.md's "Language discipline" section extended on review feedback:
the four-word forbidden list is an example set, not the whole discipline — a
synonym that imports the same certainty a banned word carried ("ensures
integrity" for "tamper-proof") is equally forbidden, and future edits are
checked against the *claim*, not the string list. Proposed automated
detection of this (scoring an agent's reasoning trace for semantic drift
against the banned terms) was evaluated and declined in the same entry: this
codebase has no embedding model and no access to any calling process's
reasoning, so a "detector" built from what's actually available would be a
keyword list wearing a rigor it doesn't have — the exact control-inflation
the standing rule refuses. Recorded as a documentation-only change; no code
added.

Tests: 178 → 184 (T28): out-of-root directory symlink leaves no archive
trace, sibling real file in the same directory is unaffected, in-root
directory symlink placeholder is unaffected.

## 1.1.0 — 2026-09-26

The witness layer. First minor release: no invariant changed, no gate added,
no format broken — everything is additive, and every piece is a *witness*
(evidence at rest), never a *guard* (a check at invocation), because the
adversary attends the invocation. Framing adopted from the operator's
standing rebuttal of guarantee-seeking controls: we operate with
probabilities; the work is drawing the acceptable-risk line before
control-striving ruins everything. That line now exists as a first-class
document — `references/RESIDUAL_RISK.md` — with the standing rule: **every
future control addition must name, in the same version, the blind spot it
creates, or it is refused as control-inflation.**

- **Added: decision traces (`cot`)** — the operator's "very compressed chain
  of thoughts record," implemented as a bounded per-generation schema:
  `--cot-trigger` (enum: schedule | pre-migration | pre-risky-op | post-heal |
  manual | anomaly), `--cot-belief` (≤140), `--cot-risk` (≤80),
  `--cot-falsifier` (≤80; one checkable claim that indicts the reasoning if
  false). Written at decision time, stored in the manifest (hash-protected,
  rollback-proof), prefix-digested into the ledger line (`cot=`, space-free)
  so the why survives archive loss. Overflow **refuses** the build — traces
  are never truncated, because truncation silently edits reasoning.
  `verify`/`restore` print the trace; `verify` compares manifest trace vs
  ledger digest — agreement is evidence, disagreement is a loud WARN alarm,
  never a refusal. Convergent motivation on record: doctor_memory's
  "preserve inference steps, not identity" and katarina_martinity's "the
  receipt is written at decision time."
- **Added: operator acks** — `ack GEN [NOTE]` appends `op=ack gen=N ts=…
  note=…` to the ledger: the human witness, written when the operator
  actually looks, never on a schedule. Refuses unknown generations,
  unreachable ledgers, notes over 120 chars, and adapter `none`. The ack plus
  the chain form two independent witnesses: silent forgery now requires
  subverting both in coordination — a probability shift, stated as such
  everywhere. Mandatory signing, external-model attestation, and a
  hypothetical G9 "cot validity" gate were considered and **rejected** as
  control-inflation (RESIDUAL_RISK.md records the reasons).
- **Added: custody event lines** — `event=restore gen=N ts=… target=…` after
  a successful restore, `event=drill gen=N ts=…` after a standalone drill;
  best-effort (a WARN on failure, never a custody failure), inherited through
  the same adapter consent boundaries (rounds 3–5). Verifies deliberately not
  recorded: a verify is a read, repeatable at zero cost.
- **Added: witness surfaces in output** — `status` shows the ack trail and
  last-build trace; `verify` shows trace, digest agreement, and per-generation
  acks; `restore` shows the decision narrative (trace + acks) before healing.
- **Added: `references/RESIDUAL_RISK.md`** — the acceptable-risk line:
  eight enumerated non-protections, the standing rule, the language
  discipline (*witness / raises cost / probability shift / detects* allowed;
  *guarantee / tamper-proof / secure against* forbidden), versioned-movement
  rule.
- **Compatibility:** `op=ack`/`event=` lines are invisible to the build-entry
  parser by line-start anchoring; witness traffic never moves `next-gen`;
  pre-v1.1 manifests and ledgers read as honest gaps ("no trace recorded"),
  not errors. Manifest/ledger formats remain additive-compatible in both
  directions.
- **Tests:** 151 → 178 assertions (T27): trigger/without-trigger/overflow
  refusals, cot build + digest in ledger line, manifest trace roundtrip,
  verify digest MATCH, tampered-digest alarm (rc stays 0), ack happy path /
  unknown gen / note cap / adapter-none, status ack summary, restore
  narrative + event line, drill event, next-gen immunity to witness traffic,
  legacy-archive gap reporting.

## 1.0.6 — 2026-09-25

Fifth ClawHub audit round (against 1.0.5). The T09 slot persisted, downgraded
**Error → Warning (High → Medium)** and narrowed to a single function:
*"Workspace-Controlled File Ledger Can Append Outside the Selected Workspace"*
(`scripts/backup_chain.py` `ledger_append`/`ledger_state`, the `file` adapter
branch). The scanner's own analysis explicitly credits the 1.0.5 boundary —
root pin, member re-validation, `chain_name`/`output_dir` containment — and
points at the one sink it does not cover: `ledger.file`. That was the
"deliberate exception" 1.0.5 kept, and the scanner's rebuttal is correct under
this project's own trust model: an append-only ledger is still a *write
primitive* when its destination is attacker-chosen, and `.vault/config.json`
is adversarial input. A planted config could aim ledger appends at
`~/.bashrc`, a cron file, or any writable path outside the workspace — with
partially attacker-controlled line content (`chain_name` legally contains
backticks, `$`, spaces). Round 3 built the consent mechanism for *what runs*;
round 4 for *what is read and where archives land*; round 5 closes the last
unvalidated sink: *where the ledger appends*.

Adopted (T09, round 5) — same consent class as the command adapter:

- **`--allow-external-ledger`** (shared guard parent, all subcommands): a
  file-ledger destination that *resolves* outside the workspace — absolute,
  traversing relative, or through a planted symlink — refuses to append
  without it (`build --register` fails rc 1 naming the flag) and the read
  path reports unreachable-with-guidance (status/check proceed marked, not
  fatal — the round-3 semantics). In-root ledgers never consult the flag.
- **Realpath containment at every use.** `ledger_file_path()` resolves the
  destination through `os.path.realpath` on each read/append, so a symlink
  planted — or swapped — after approval still fails closed when it leaves
  the boundary. In-root symlinked targets keep working without any flag.
- **Shape validation at load.** `load_config` now validates the `ledger`
  object (must be an object; `ledger.file` must be a non-empty,
  NUL-free string). Containment stays a *use-time* decision because the
  verdict depends on a per-invocation flag, not on the config alone.
- **Wipe-safety preserved, now honestly priced.** `init --ledger-file
  /external/path` still works — the operator chooses the destination in
  their own voice — and init warns that every runtime invocation touching
  the ledger will need the flag. Opted-in external appends print a stderr
  `WARN` (once per process); stdout stays byte-clean for parsers.
- **Boundary separation held:** `--allow-external-ledger` does not enable
  the command adapter, and `--allow-cmd-ledger` does not enable external
  ledger paths — two flags, two distinct consent decisions.

One honest defect admitted in the same pass: the round-4 suite's "absolute
ledger file path still accepted" assertion set a bogus `ledger.ledger`
config subkey and never actually exercised an external path. The 1.0.6
suite repairs it and adds T26 (30 assertions): planted external config
refused with nothing written outside, traversing relative refused, planted
symlink refused (then allowed with the flag, landing in the target),
in-root symlink unaffected, malformed ledger shapes refused at load,
boundary separation, and the full wipe-safety workflow end to end.
Suite: 119 → 151, first-run green after the two test-authoring fixes
above; the production code itself needed none.

## 1.0.5 — 2026-09-25

Fourth ClawHub audit round (against 1.0.4). The T09 slot returned — but with a
**different finding behind the label**: *"Untrusted workspace configuration can
redefine the backup root and collect files outside the selected project"*
(Error/High, `scripts/backup_chain.py` `load_config`/`output_abs`/
`collect_members`/`cmd_build`). Round 3's T09 (ledger shell execution) is
confirmed fixed by the scanner's own excerpts: the 1.0.4 code shown cites
`shlex.split` + `shell=False` + refuse-by-default, and the audit overview now
names `--allow-cmd-ledger` as the intended opt-in. What "returned" is the
*reading-side twin* of the same trust boundary — and it was real:

- The stored `root` was validated only at `init` time and trusted forever
  after; `collect_members` derived its containment boundary from
  `realpath(cfg["root"])`. A planted `.vault/config.json` could point the
  boundary anywhere readable and collect those files into the archive.
- Config `members` were never re-validated at load — `normalize_member` rules
  (`..`, `~`, absolute refusal) applied only to the `member add` CLI, so a
  hand-edited config could smuggle traversing paths past the gate.
- `output_dir` accepted absolute/traversing values and `chain_name` was
  spliced into archive filenames unvalidated — the config could also steer
  where the (externally collected) archive landed, including filename
  traversal out of the output dir.

Adopted (T09, round 4) — "config proposes; the invocation root and the
operator dispose":

- **Root pin.** `load_config` now requires `realpath(cfg["root"])` to equal
  the canonical invocation root and pins `cfg["root"]` to it; mismatch is a
  refusal with recovery guidance (fix `root` in the config, or `init
  --force`). A moved workspace must now *say so* instead of silently
  re-targeting — which also fixes a latent pre-1.0.5 bug where a moved
  workspace kept backing up the old path. Symlinked paths to the same
  workspace pass (realpath equality).
- **Member re-validation at load.** Every configured member path goes through
  `normalize_member` on every command; config-sourced refusals surface as
  GateError with the reason, not silent collection.
- **`chain_name` containment.** A shared validator (used at `init` and at
  load) refuses empty, oversized, separator-bearing, or `..`-token names —
  while keeping spaces/unicode legal so basename-derived names keep working.
  `init --name "../evil"` is now refused outright (rc 2).
- **`output_dir` containment.** Config values must be relative and resolve
  inside the workspace; a symlinked output directory resolving outside is
  refused at build time (realpath + commonpath — same containment the member
  reader applies). External destinations stay available per invocation via
  `build --output` (operator voice, same trust class as `--allow-cmd-ledger`).
- **Docstring divergence fixed (SkillSpector rider).** Invariant 3 said
  "user-supplied shell commands … no platform code" — a contradiction the
  scanner flagged at 96% confidence. Reworded to state the 1.0.4 reality
  (opt-in argv execution); the file header version, stale since 1.0.1, is
  synced too.

Triage of the remaining round-4 items:

- **Absolute `--ledger-file` kept.** The audit asks that external paths
  require "a dedicated command-line option and an explicit confirmation" —
  for the ledger that option exists (`init --ledger-file`), is the documented
  wipe-safety feature (a ledger inside the workspace dies with it), and only
  aims reads/appends of one log file, not execution. Declined to gate;
  noted so the next reader doesn't mistake it for an oversight.
- **"Store the authoritative root outside the workspace / authenticate the
  config"** declined: heavyweight forms of the same boundary the root pin
  already enforces, and out of proportion for a no-network, no-daemon CLI.
- **SkillSpector (15 findings) re-triaged** along round-2 lines: 4× Tool
  Parameter Abuse and 3× Skill Enumeration cite `tests/test_backup_chain.sh`
  fixtures (fake `skills/sk1/SKILL.md`, symlink drills) — test evidence, not
  runtime behavior; 2× subprocess Medium acknowledge the residual design
  risk of the opt-in command adapter ("shell=False, shlex.split, and
  --allow-cmd-ledger reduce risk") — accepted, documented, operator-gated;
  Vague Triggers is the activation breadth that makes the skill findable
  (declined in round 2 for the same reason); Undeclared Tool Scope assumes an
  MCP permission manifest this skill does not have; the two Autonomous
  Decision Making excerpts quote our own CHANGELOG triage prose — the scanner
  flagging the security discussion as a finding.

Behavior changes for legitimate setups: a workspace that *moved* since init
refuses until `root` in `.vault/config.json` is fixed or the chain is
re-initialized (`init --force`); a pre-1.0.5 config with an absolute
`output_dir` is refused (use `--output` per invocation); `--name` values that
could not be honest filename components are refused at `init`.

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
