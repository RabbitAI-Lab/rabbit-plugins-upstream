# Label taxonomy

Contents:

- the axes
- sized starter sets
- naming rules
- cleaning up an existing label mess
- tracker mechanics

## The axes

A queue is readable when each label belongs to one axis and an item carries at most one value per axis.

| Axis               | Answers                         | Applied by                                | Required                           |
| ------------------ | ------------------------------- | ----------------------------------------- | ---------------------------------- |
| Type               | What kind of work is this?      | Intake form, or triager                   | Always                             |
| State              | What is this waiting on?        | Triager, automation                       | Always                             |
| Priority           | What happens if nobody does it? | Triager or maintainer                     | Once the queue outgrows one person |
| Area               | Which part of the project?      | Automation from changed paths, or triager | Once there is more than one owner  |
| Contributor-facing | Is this open to outside help?   | Maintainer, deliberately                  | Only when the promise can be kept  |

Two labels from the same axis on one item means nobody decided - the single most useful invariant to enforce, by convention or by tooling.

A minimum viable state set:

- `needs-triage` - nobody looked
- `needs-info` - waiting on the reporter
- `accepted` - real, will be worked
- `needs-owner` - real, unstaffed
- `blocked` - waiting on something external

Kubernetes runs `needs-triage` → `/triage accepted`; mattpocock's triage skill runs five states ending in `ready-for-agent` / `ready-for-human` / `wontfix`. Both work: pick one vocabulary and write it down.

## Sized starter sets

The three reference points from step 3:

- **ten** default GitHub labels (`bug`, `documentation`, `duplicate`, `enhancement`, `good first issue`, `help wanted`, `invalid`, `question`, `wontfix`, `accessibility`)
- **five state roles plus two categories** in the most-installed triage skill on skills.sh
- **six prefixed families** at Kubernetes (`kind/`, `priority/`, `sig/`, `area/`, `triage/`, `lifecycle/`)

The mapping below is this skill's judgment, not a sourced rule.

**Solo maintainer, small queue.** Four labels, state only:

- `needs-triage`
- `needs-info`
- `accepted`
- `blocked`

Type comes from the intake form. Priority honestly lives in the maintainer's head, and pretending otherwise creates unused labels. This sits below the shipped default of ten - the right direction: delete the defaults you will not apply.

**Small team.** Add:

- type: `type/bug`, `type/feature`, `type/docs`, `type/support`
- a two-value priority: `priority/now`, `priority/later` (three is already a debate)
- a contributor-facing pair: `help wanted`, `good first issue`

Near the five-plus-two shape.

**Multi-owner project.**

- Add `area/*` per owning team or subsystem.
- Split priority into the four Kubernetes levels if release planning depends on it.
- Add `lifecycle/*` for staleness.

This is the six-family shape, and the point at which the taxonomy needs an owner, a written definition file and the validation below, or it decays.

## Naming rules

- Prefix every multi-value axis: `kind/bug`, `priority/now`, `area/parser` - the prefix makes the axis visible in an alphabetical label list.
- Write one sentence of definition per label, in the repository, not only in the tracker's description field.
- Name the state from the waiting party's perspective (`needs-info` says who owes what; `pending` says nothing).
- Reuse conventional names where they exist (`good first issue`, `help wanted`) - trackers and third-party indexes surface them algorithmically, and a custom synonym loses that reach.
- Colour by axis, not by mood: one hue per family reads at a glance.

## Cleaning up an existing set

1. Export the label usage counts (`triage-baseline.py` prints them, including labels used exactly once).
2. Sort into: keep, rename into an axis, merge into another label, delete.
3. Delete unused and single-use labels - a label nobody applies twice is a private note.
4. Rename before deleting: deleting erases the label from every past item and any saved view built on it.
5. Migrate in one pass, announce it in one place, updating every saved view, form and automation in the same pass. A half-migrated taxonomy is worse than either version.

## Keeping a taxonomy from decaying: the allowlist pattern

A taxonomy with many labels and any automation touching it needs an enforcement layer. PyTorch runs one in production on its main repository - the clearest worked pattern available.

- **Hold the triage-eligible label set as a separate, versioned, machine-readable artifact**, not "whatever the tracker currently contains". Theirs carries a name and description per entry and deliberately excludes CI triggers, release-note labels, deprecated labels and anything needing a human decision; keeping it smaller than the live label set is the point.
- **Validate every write against it**, stripping labels not in the allowlist - which rejects invented or guessed names outright.
- **Collapse redundant pairs** - drop the general area label when a more specific one from the same family is present.
- **Merge with existing labels, never replace.** Most "set labels" operations are a full overwrite, so a write without a merge step silently erases what a human applied. The single highest-consequence detail in the pattern.
- **Fall back to a review state rather than doing nothing** when validation filters everything out, so the item still carries a status.
- **Stamp mutations for auditability** with a marker label, so triage actions can be filtered and reviewed later independently of the decision logic.
- Step 3's two PyTorch rules - confidence-gated labelling, top priority never auto-applied - are part of this same pattern.

Without automation the same discipline applies: an undefined label is applied inconsistently within a week, and an unvalidated taxonomy drifts into synonyms.

## Tracker mechanics worth knowing

- **Mutual exclusion.** GitLab's scoped labels (`priority::high`) enforce one value per key - a second value of the same key removes the first. Without that feature the invariant is a convention the triager holds.
- **Types vs labels.** Where the tracker has a first-class issue type (Bug, Feature, Task, Epic), use it for the type axis rather than duplicating it as labels.
- **Triage permission.** GitHub's `Triage` role grants labelling, closing, reopening, assigning, marking duplicates and requesting reviews, with no push or merge access - how a triage team grows without commit rights. Check the equivalent role on other trackers.
- **Automation surfaces.** Path-based auto-labelling fills `area/*` from the diff; owner files route review requests; intake forms apply the type label at submission. Every axis filled by a machine is one the triager does not spend attention on.
