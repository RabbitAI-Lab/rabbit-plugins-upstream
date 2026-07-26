# Skill design mechanics reference

Loaded on demand from SKILL.md — the reasoning behind every rule in the main
build process. You don't need to read this top to bottom; jump to the
numbered section you need.

## 1. Progressive disclosure (3 levels)

- Level 1: metadata (`name` + `description`) — always in context.
- Level 2: `SKILL.md` body — loaded after the skill triggers (flow, routing).
- Level 3: `references/` + `scripts/` — loaded only on demand.

This is the single biggest token-cost lever a skill author has. A skill with
everything crammed into one huge SKILL.md pays that token cost on every
trigger, even for the 90% of invocations that never need the deep-dive
material.

## 2. Scripts that run without ever entering context

A script under `scripts/` should be invoked directly (e.g.
`python -m scripts.verify`) rather than pasted into the model's context. The
model reads the *result*, not the script source, so the cost is near zero
regardless of script size.

## 3. Domain organization through references

`SKILL.md` should hold the decision logic (which variant, which path). The
supporting detail belongs in `references/`, split by topic, so the model
loads only the one file it actually needs.

## 4. Table of contents for files over ~300 lines

Past that size, a table of contents lets the model jump straight to the
relevant section instead of reading the whole file into context.

## 5. Pushy descriptions — fighting under-triggering

The single most common skill-authoring failure is a description written in
natural, modest language that the model never matches against a real user
message. Write the description more aggressively than feels natural: list
synonyms, list the contexts where it applies, don't undersell it. Draft 2-3
candidate descriptions and pick the one that triggers most reliably against
your eval set.

## 6. Automatic trigger-tuning loop

Split your eval set 60/40 into train/test. Iterate the description against
the train split, up to ~5 rounds, then confirm against the held-out test
split. This keeps you from overfitting the description to the exact wording
of your training examples.

## 7. Eval sets need hard negatives

A good eval set isn't just "should trigger" examples — it needs near-miss
negatives: inputs that sound adjacent to the skill's domain but shouldn't
trigger it. Without hard negatives you can't tell a well-tuned description
from an over-eager one.

## 8. Lack of Surprise (security property)

The `description` is a contract with the user and the reviewing human: it
must not hide instructions that aren't disclosed there. A skill that says
"formats your code" and secretly also phones home or exfiltrates data
violates this property — and it's the first thing a skill-security-auditor
should catch.

## 9. Avoid rigid CAPS/MUST language — justify instead

Compare:

> ALWAYS use Kotlin.

vs.

> Kotlin by default. Rationale: null-safety, official support. Java also
> works if the project already standardized on it.

The second form generalizes better to edge cases the author didn't
anticipate, because the model has the reasoning, not just the verdict.

## 10. Conditional, per-environment instructions

One `SKILL.md` can hold clearly labeled sections for different runtimes —
e.g. "Claude.ai-specific," "OpenClaw-specific," "API-specific" — so the same
skill file works correctly across hosts instead of needing per-host forks.

## 11. Packaging into a `.skill` file (optional)

Use `package_skill.py` (or your host's equivalent) once the skill family is
stable, if you need a single-file distributable artifact rather than a
directory.

## 12. Directory name = frontmatter `name` (critical)

When updating an existing skill, keep the directory name and the
frontmatter `name` field exactly as they were. Changing either makes the
host treat it as a brand-new skill rather than a new version of the
existing one — you lose version history and any existing install
references break.

## 13. Selective triggering by task complexity

Models will often (correctly) skip loading a skill for a trivial,
one-step request, because they can just do it directly. Design for this:

- Eval queries need to be complex enough that the skill actually has a
  chance to trigger — trivial eval queries produce a false sense that the
  description "works."
- The description itself should hint at complexity ("multi-step process,"
  "step by step") so the model's own judgment about whether to load the
  skill lines up with when the skill is actually useful.
- Test with both simple and complex queries before shipping.

## 14. Explicit "why," not just "what"

Justify every instruction. This is what lets a model generalize the
intended behavior to an input the author never explicitly covered, instead
of following the letter of a rule into an obviously wrong edge case.
