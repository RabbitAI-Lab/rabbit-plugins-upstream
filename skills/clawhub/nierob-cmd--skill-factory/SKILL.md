---
name: skill-factory
description: Scaffolds a router + 2-6 variant skills for a problem with several recognizable variants — eval-tuned triggers, progressive disclosure, build checklist.
version: 1.0.0
---

# Skill Factory — Router + Sub-Skills Builder

This skill activates when the user wants to build a **family of skills** that
handles several variants of the same underlying problem — not a single,
narrow skill.

It is a factory: it produces 1 router skill + N variant skills, all real and
independently invocable.

## When to use

Use this skill only when **all three** are true:

1. A bounded set of variants (2-6) — not one, not dozens.
2. The variants are distinguishable from the input/file/context up front.
3. The logic differs enough between variants that one shared prompt would be
   confusing or would force awkward branching inside a single SKILL.md.

## When NOT to use

- Testing an existing single skill → use a skill-tester/eval tool instead.
- Security-auditing a skill before install → use a skill-security-auditor.
- Building one simple skill with no variants → use a plain skill-creation
  flow, not a factory.

## Process

### Step 0 — Gather inputs (max 3-5 questions)

- Domain/topic
- List of variants
- The recognition rule (how to tell variants apart)
- Source of truth for the rules per variant
- Expected output format

### Step 1 — Design the architecture

```
[Skill: <name>-router] → [Skill: <name>-variant-{1..N}]
```

Each variant skill gets its own trigger, inputs, rules, and a self-check
checklist at the end.

Design rules:
- Routing must be deterministic — use hard signals, not vibes.
- Each variant skill is self-sufficient — duplicate shared rules into it
  rather than making it depend on the router at runtime.
- Don't hardcode example data into the rules; keep rules general.
- Decide per variant: "generate + warn" mode vs. "ask for clarification"
  mode.
- End every variant skill with a checklist.

### Step 2 — Show the plan to the user

Skip this only if the user explicitly said "just do it."

### Step 3 — Create the skills

**Router skill:** trigger phrases + a routing table → "once you recognize
the variant, load that variant skill's instructions."

**Variant skill:** its own keywords, so it can also be invoked directly
without going through the router.

⚠️ When updating an existing skill family: never change the directory name
or the frontmatter `name` field. Either one changing makes the system treat
it as a brand-new skill instead of a new version of the existing one.

### Step 4 — Summarize what was built

### Step 5 (optional) — Test and package

- Build an eval set: complex positives + hard-negative near-misses.
- Iterate the `description` field against the eval set (see
  `references/skill-mechanics.md#5-6-7` for the tuning method).
- Package into a `.skill` file if you're distributing it.

For the full design rationale (progressive disclosure, eval-set tuning,
"Lack of Surprise," per-environment sections, and 8 more mechanics), see
[`references/skill-mechanics.md`](references/skill-mechanics.md) — loaded
only when you need the reasoning behind a rule, not on every run.

## Pitfalls to avoid

- Don't build a router for a single variant.
- Don't build more than 6 variant skills in one factory run.
- Don't invent rules out of thin air — flag a gap instead (⚠️).
- Don't skip the end-of-skill checklist.
- Description is a contract — no hidden instructions inside a skill's body
  that the description doesn't disclose ("Lack of Surprise").
- Avoid ALWAYS/NEVER language — justify the "why" instead.
- Never rename the directory or the frontmatter `name` when updating an
  existing skill family.
- Eval queries that are too simple won't ever trigger the skill in
  practice — write eval queries at realistic complexity.
