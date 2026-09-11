# Signal Dreaming — Version History

Each entry states what changed and why. Where a release fixed something that had
been running wrong, the entry says what the wrong behaviour cost, because that is
the part that stops it being reintroduced.

---

## 5.0.0

Makes the index a domain-level summary rather than a mirror of the L2 topic list,
and curates on every run rather than only when the index is over budget.

Both halves change what the protocol produces, so an existing workspace will see
its `MEMORY.md` restructured on the first run after upgrading. That restructuring
is backed up like any other write (Phase 3.1), but it is not something the human
asked for on that particular day — hence the major version.

**Curation stopped being conditional on size.** The protocol said that below its
target, size was "not a consideration at all", then asked — correctly — whether
each section still belonged at index level. In practice the first clause won: the
run reached the target, stopped, and never got to the question. Measured across
eight consecutive runs on a CJK workspace, the index finished between 92% and 100%
of a 16,000-character target every time, while five archived projects kept full
entries throughout. A target that is only ever consulted when exceeded is not a
ceiling; it is a floor, and the index grows until it finds it.

**The index stopped mirroring the topic directory.** Phase 1.5's topic identity
guard forbids merging L2 files that describe materially different things. That
guard is right, and it was being applied one layer too high: every new topic file
earned its own index entry, nothing ever merged, and eleven of thirty-one entries
in one workspace turned out to be facets of a single line of work. The guard now
says explicitly that it governs L2 files and not index structure, and Phase 3.2
groups index entries by the question a reader is asking.

**Phase 1 now reads L2 modification times.** Deciding whether an entry still
describes something live was unanswerable from the entry itself — an index says a
project is active in the same words the day the work stops. The modification time
of the file an entry points at is a fact produced by Phase 2 rather than a field
someone has to remember to maintain. A date stamped into the entry was the
obvious alternative and the weaker one: it survives only until the first run that
refreshes every line at once. mtime informs the judgement; it never retires
anything by itself.

**Entries are placed deliberately.** New entries were appended to the end of the
file, which is not a neutral position — it sits under whatever heading happens to
be last. An active project entry landed under a standing-rules heading in
production, where later runs would have read it as a permanent rule and never
considered it for consolidation again. Phase 3.2 now assigns a section before
writing, and Phase 3.6 checks that every entry sits under a heading matching what
it is.

**Individual entries are sized.** A total budget says nothing about one entry, so
a section can reach several times the length of its neighbours unnoticed. The
anchor is `maxPromotedSnippetTokens` — the cap `memory-core` puts on a single
promoted snippet — read from config rather than copied into this document. It is
used to find outliers only: entries already at or below it are left alone,
because a per-entry cap used as a target rebuilds the same attractor one level
down.

**Finished work keeps one line.** Closed and archived projects are reduced to a
line plus an L2 pointer. Nothing in the protocol asks about them again, so a full
entry is pure accumulation.

**Security: the audit helper no longer evaluates its numeric overrides.**
`references/dream-audit.sh` read `SD_BOOTSTRAP_MAX_CHARS`,
`SD_BOOTSTRAP_TOTAL_MAX_CHARS` and `SD_INDEX_TARGET_PCT` straight into `$(( ))`.
Bash evaluates an array subscript inside arithmetic expansion as a command, so
`SD_INDEX_TARGET_PCT='x[$(cmd)]'` executed cmd — confirmed by running it. The
three values are now accepted only as plain non-negative integers; anything else
falls back to the default and warns, since an override dropped in silence is its
own defect. Defaults and legitimate overrides behave exactly as before.

**Packaging: the audit helper is invoked through `bash`.** The protocol called
`references/dream-audit.sh` by path, which needs the executable bit. A ClawHub
archive does not preserve it, so the call worked on the publishing machine and
failed on every fresh install. Naming the interpreter removes the difference.

`SD_INDEX_TARGET_PCT` is unchanged at 80. Lowering it would have moved the
attractor rather than removing it.

One consequence is documented so it is not later mistaken for a regression: index
size no longer converges on a figure. Run-to-run variation means curation is
tracking content; a flat line means it has started tracking the target again.

Also includes the unreleased 4.0.4 fix below.

---

## 4.0.4 (unreleased)

Fixes a dream number that stops advancing once the diary reaches its trim cap.

Phase 3 derived the new number by counting `## 🌙 Dream #` headings, while Phase 5
deletes the oldest entry whenever the count exceeds 30. The two rules agree only
while the diary is still growing. Once it saturates, the count is permanently 30,
so every subsequent run writes `#31` — observed in production across four
consecutive runs after the cap was reached. The watermark is unaffected, since it
is read from `Consolidated through:`, so consolidation stays correct while the
diary quietly loses monotonic identity and the gap check that depends on it.

Phase 3 now reads the number out of the newest heading and adds 1, and Phase 5
states that trimming must never change the next number. Repairing an
already-frozen diary means renumbering the affected headings once, from the last
correct entry forward; nothing else in the log changes.

---

## 4.0.3

Restates the 4.0.2 scope without enumerating what falls outside it.

4.0.2 fixed the rule by naming categories of ordinary content as out of scope. The
rule was right; the enumeration was not. A list of what a memory system will
retain reads, to someone reviewing the skill rather than running it, as a
description of what it sets out to collect — and the three constraints that
actually do the work need no examples to be unambiguous: the list is exhaustive,
it is not to be extended, and nothing outside it raises the alert.

The scope is now stated as a limit on the guard rather than a judgement about
content. It covers authentication material and is not a privacy classifier;
anything else follows the workspace's own conventions. Behaviour is identical to
4.0.2.

---

## 4.0.2

Closes the secret guard's scope.

The list of what counts as a secret was introduced with *"treat these as sensitive
by default"* — wording that reads as a floor rather than a boundary, so a run could
classify ordinary log content as sensitive on its own judgement, withhold it from
L2, and ask for manual review of the daily log.

That alert has nowhere to go. This protocol never edits daily logs, so the value
stays exactly where it already was; the only durable effects are an index missing
an ordinary fact and a review request that cannot resolve. Repeated, it teaches
the human to skim past the alert that does matter.

The list is now stated as **exhaustive**, and nothing outside it raises the alert.

---

## 4.0.1

Fixes a guardian that could skip work it should have done, and sizes the batch cap
to the task timeout.

The guardian tested for daily logs dated strictly *after* the watermark, while
Phase 1 selects `>=` precisely because a watermark-dated log can be appended to
after the last run read it. Since the guardian runs first, that defence never
applied: inside the debounce window a run reported no-op while same-day additions
waited for a later pass. Session-reset hooks that write `YYYY-MM-DD-HHMM.md` files
make several logs share the watermark date every day, so this is now the normal
case rather than an edge one. The two log conditions are merged into one that
reuses Phase 1's `>=` and asks whether any selected log changed since the last
entry's heading timestamp.

The byte cap moves from `512 KB` to `192 KiB`. A cap means something only if the
batch it admits can finish before the scheduler kills the run: at a measured
`0.12-0.21 KiB/s`, an `1800 s` timeout admits roughly `216 KiB`, so the old number
was never reachable. **If your task timeout differs, recompute the cap from your
own slowest observed throughput.** The cap bounds accumulation across days and
cannot bound a single day — the date-boundary rule still processes an oversized
date whole, and such a run now records its actual input size and duration in the
dream-log.

---

## 4.0.0

Returns to the protocol-only design of the 1.x line and removes the 2.x/3.x script
layer entirely.

Those versions compiled the same rules into enforced JavaScript preconditions — a
transaction state machine, run manifests, lock files, staged candidate
directories. That layer added no new safety rules; it changed who enforced them,
and in production turned recoverable conditions into aborted runs: an over-limit
index refused to run the pass that shrinks it, and an optional audit's path error
cancelled an otherwise complete consolidation.

It also retires the byte-based index target inherited from 1.x. That `8 KB` was
written where a byte and a character were the same thing; the real limit is
`bootstrapMaxChars`, measured in **characters**. For a CJK workspace at ~1.7 bytes
per character it enforced about a quarter of the real budget — and 3.x then made
crossing it a hard error, so a healthy index could block its own consolidation
pass. 4.0.0 does not substitute another constant: headroom is derived from the
runtime's own caps, and the target is a configurable percentage of it (default
80%, leaving a growth band). A hard-coded threshold caused the original damage, so
the protocol no longer contains one.

Upgrading from 2.x or 3.x: delete any cron payload steps invoking `preflight`,
`begin`, `finalize`, `run-guard`, or `dream-audit.mjs` and use the template in
`SKILL.md`. There is no state to migrate. Existing `.backup/memory-dreams/`
directories can stay; nothing reads them. Your existing `dream-log.md` works
as-is — the watermark is found by scanning back for the newest entry that carries
a `Consolidated through:` field, and if none does, the newest entry's heading date
is used.
