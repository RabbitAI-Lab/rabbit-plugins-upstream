# PROVENANCE — backup-chain

**Origin.** Distilled 2026-09-25 from a production backup chain that ran for
nine days across 14 workspace wipes (generations 1–59, ~1,300 files per
archive) in a sandboxed agent environment. Every rule in this skill has a
named incident behind it — the mtime trap, the stale handoff, the silent
zero-write bulk extraction (hit twice), the filename-collision parent, the
clean-completing stale restore.

**Design partners.** Co-developed by an AI agent (Super Z / GLM) and a human
operator. The human's contributions are structural: the demand that the skill
be **platform-agnostic** (no exact external services — users plug their own via
the command adapter), that it work **local-only by default** with off-site
distribution handled by the user, and that it contain **no personal data, no
credentials, and no platform identifiers** from the originating deployment.
The production system this was distilled from does use specific platforms; none
of them are named here, and nothing from their configurations survived the
abstraction.

**Dogfooding.** The skill was validated against a synthetic-workspace test
suite (14 scenarios, 47 assertions) before release; the suite caught two real
protocol bugs on its first run — a fencing gap (live-but-silent ledger skipped
the local-chain stale refusal) and an overwrite bug (`--overwrite` classified
conflicts but never restored them). Both fixes are argued in PROTOCOL.md.
The skill then went through an independent external review: six crash/UX
fixes (nested-symlink dereferencing, broken-symlink crash, drive-letter
hardening, single ledger read per restore, dry-run conflict preview, clean
refusals for missing arguments) were verified and adopted wholesale as
v1.0.1, with one further guard (non-regular-file hang protection) added in
the final pass because it belonged to the same defect family the review had
addressed. The ClawHub automated audit then found the two boundary escapes
that the dereferencing design had left open (reads out of the project root
through nested links; restore writes out of the target through symlinked
directories); 1.0.2 closes both with containment gates and the suite grew to
77 assertions — and immediately caught the first implementation of the
restore gate examining the wrong path components. Three defect classes,
three catches by the same drill-before-trust loop. The audit's second round
(against 1.0.2) returned 14 findings: the two 1.0.1-era escapes verified
gone, one finding (silent command-adapter execution) adopted as the 1.0.3
runtime warning, and thirteen triaged as duplicates, test-fixture false
positives (the scanner read the suite's own symlink fixtures as runtime
behavior), or deliberate documented design — every triage decision is
argued in the 1.0.3 CHANGELOG entry. The audit's third round (against 1.0.3)
elevated the command adapter to a full High finding (T09): the 1.0.3 warning
fires but does not ask consent, so a planted config still executed on routine
subcommands — the scanner itself noted the feature is legitimate for
deliberately configured commands. 1.0.4 answers with refuse-by-default
execution behind an explicit per-invocation `--allow-cmd-ledger` and
argv-only (`shell=False`) command execution; the warning stays, the silent
path is gone. One honest defect admitted in the same pass: the script's
`VERSION` constant had lagged at 1.0.1 through two doc-only releases.

**License of intent.** Copy it, fork it, port it. If it saves you one wipe, it
paid for itself.
