# The Installed Set — Collisions, Dead Weight, And What It Costs Per Turn

Scope: operational health of the skills that are installed — do they fire when they should, do they cost more than they return, do their files exist. Whether a skill's *code* is safe to run is a different question with a different method (`skill-audit`).

**Before this pass**, read `## System Baseline` in `~/Clawic/data/analysis/memory.md` (or the file its `## Boxes` line names) for the last recorded installed set: what changed since then explains most new behavior.

**Contents:** [The Per-Turn Tax](#the-per-turn-tax) · [Trigger Collisions](#trigger-collisions) · [Skills That Never Fire](#skills-that-never-fire) · [Skills That Fire Too Often](#skills-that-fire-too-often) · [Broken References](#broken-references) · [Undeclared Requirements](#undeclared-requirements) · [Duplicates And Drift](#duplicates-and-drift) · [Local Edits](#local-edits) · [Sweep](#sweep) · [Write It Down](#write-it-down)

## The Per-Turn Tax

Every installed skill's name and description sit in context on every turn, whether or not it activates. The bodies do not — those load on activation — so the tax is computed on the catalog, not on the folder size.

```
always_on_tokens ≈ Σ (len(name) + len(description)) / 4
```

Worked example: 60 skills averaging 700 characters of name plus description is 42,000 characters, about 10.5k tokens, on every single turn. At 60 turns a day that is ~630k input tokens a day spent describing skills that mostly did not run. The same arithmetic in reverse is the argument for keeping a skill: one activation that saves a wrong architecture pays for a year of its own description.

Report the total, the count, and the three longest descriptions. The action is never "uninstall everything" — it is uninstall what has not activated (below) and shorten what is verbose without losing its trigger words.

## Trigger Collisions

A collision is two skills whose **first sentences** claim the same trigger words, because the first sentence is what carries activation: it is what an attention-limited reader keys on, and it is what survives when a catalog gets truncated under budget pressure.

Detection: extract each skill's name plus first description sentence; tokenize to content words (drop stopwords); report any pair sharing a distinctive domain noun or task verb. Distinctive means the word is not generic ("use", "help", "manage", "files") and appears in fewer than ~5 descriptions overall.

| Collision shape | Symptom the user reports | Fix |
|---|---|---|
| Same domain noun, different sub-job | "It always picks the wrong one" | Partition: each first sentence names its sub-job; the narrower skill gets an explicit "not for X" pointing at the other |
| One is a strict superset of the other | The general one always wins | Merge, or make the specific one's first sentence lead with the symptom only it handles |
| Both generic ("analysis", "helper", "assistant") | Neither fires reliably | Rewrite around the words a user actually types; a name is not a trigger |

Report the pair, the shared words, and which one should narrow. Two skills that legitimately overlap and the user wants both go to `## Accepted` with both slugs named.

## Skills That Never Fire

An installed skill with no activation in 60 days is either mis-triggered or unwanted, and the difference is decided by one question: has the user done work in that domain during the window?

- Yes, and the skill did not fire → trigger problem. The first sentence lacks the words the user actually used. Action: rewrite the description, not the body.
- No → dead weight. Action: uninstall, keeping the note in `## Accepted` if the user wants it kept for a season that has not arrived (tax filing, a yearly conference).

Where the platform keeps no activation record, the proxy is the user's answer to "when did this last help", plus the domain-activity test. Say which evidence was used; a guess presented as a measurement is worse than no finding.

## Skills That Fire Too Often

Over-activation costs more than a missing skill, because it loads a body every time and steers answers toward a domain that was not asked about. Signals: a skill's body appears in sessions whose subject it does not match; a description whose first sentence is a list of generic verbs; a description missing its "not for" clause where a neighbor exists.

Fix at the description, in this order: narrow the first sentence to the actual job, add the "not for X" clause naming the neighbor, and only then consider uninstalling.

## Broken References

| Break | Detection | Severity |
|---|---|---|
| A file named by the skill body does not exist | Extract referenced paths, test existence | WARNING — the depth the skill promises is not there |
| A file exists but is reachable only through another file | Two-level path from the entry point | INFO — it will rarely be read (`workspace.md`) |
| A dead external link in the body | Resolve on the cheapest rung, batched, never per check (SKILL.md Rule 2) | INFO |
| Frontmatter that does not parse | Load the frontmatter | WARNING — the skill may not register at all |
| Name, slug, and directory disagree | Compare the three | WARNING — installation and updates resolve by directory; a mismatch breaks updates silently |

## Undeclared Requirements

A skill that shells out to a binary, needs an environment variable, or writes to a path must declare it, or it fails at the moment it is needed instead of at install time.

Check each skill's declared requirements against what its body actually uses: binaries invoked, environment variables read, paths written. Two findings come out of this — declared but missing on this machine (WARNING, action: install or uninstall the skill), and used but undeclared (INFO here; if the undeclared thing is a network endpoint or a broad path, it is a `permissions.md` finding and a `skill-audit` question).

## Duplicates And Drift

- **Duplicates**: the same skill installed in two agent directories, or a scoped and an unscoped copy of the same slug. They diverge, and which one wins is undefined. Keep one, symlink or reinstall the rest.
- **Version drift**: an installed copy older than the published one. Report the delta as INFO with the version numbers; updating is `skill-manager`'s job, not this audit's.
- **Near-duplicates**: two different slugs covering the same job — the collision case above, and usually the result of installing before searching.

## Local Edits

A modified installed skill is a real decision and a real hazard: the next update overwrites it without warning. Detect by comparing against the source copy where one exists; where it does not, an mtime later than the install date is the signal.

Action is not "revert". It is: record what was changed and why in `~/Clawic/data/analysis/artifacts/skill-edits.md` with its `## Boxes` line, so the edit can be reapplied after an update, and flag the skill as pinned so an update is a decision rather than a surprise.

## Sweep

| Check | Passing looks like |
|---|---|
| Per-turn tax computed | A number, with the three biggest contributors named |
| No unresolved trigger collisions | Each pair either partitioned or in `## Accepted` |
| No skill unfired for 60 days with domain activity | Descriptions fixed or skills removed |
| Every referenced file exists | Zero dangling references |
| Frontmatter parses; name, slug, directory agree | All three identical |
| Declared requirements present on this machine | No skill that fails at first use |
| No duplicate installs of the same slug | One copy per slug |
| Local edits recorded | `artifacts/skill-edits.md` current |

## Write It Down

Same turn as the pass:

- Installed count, per-turn tax, agent directories in use, date of this inventory → `## System Baseline` in `memory.md`.
- Collisions, dangling references, missing binaries, drift → `## Open Findings`, each naming the slug.
- Overlaps and unused skills the user wants kept → `## Accepted`, by slug, with a review date.
- Local modifications → `~/Clawic/data/analysis/artifacts/skill-edits.md`, plus its `## Boxes` line.
