# Repo Standardizer Vision

Repo Standardizer is the skill that turns any bare GitHub repository into a
professional one — without the wall of prompts.

It started as a practical annoyance: every new project needed the same
templates, labels, CI, rules, and docs, and pasting a giant prompt each time
was tedious. The skill exists so that "standardize this repo" is one sentence.

## Guiding principles

- **Idempotent by design.** Run it twice, get the same result. It fills gaps
  and reconciles drift; it never clobbers user content.
- **Safety first.** Auth is checked before anything happens. Destructive
  operations (rulesets, deletions) require a dry-run plan and confirmation.
- **Repo-aware.** Personal vs. organization, public vs. private, archived vs.
  active — behavior adapts to the repository's type and visibility.
- **Designed, not copied.** Label taxonomies are designed for each project's
  audience. Rating tiers need icons, gradients, and documented ordering —
  and must never be lifted verbatim from another repo.
- **Tested against the real API.** Every command in the skill is verified
  against the live GitHub API. Silent failure is the worst bug.

## Current state

- v0.1.x: core modules (labels, issue forms, PR template, CI, rulesets,
  docs, AI guides), bilingual README, automated release workflow.
- Live skill + templates are the source of truth; releases ship the skill
  zip automatically from `v*` tags.

## Direction

Priority:

- Reliability of the core modules across repo types
- Better drift detection (report what changed between runs)

Next:

- ClawHub / skills.sh publishing
- More CI templates (Java, C++, Docker-based projects)
- Org-level rulesets support
- Interactive dry-run reports (rendered plan before applying)

Contribution rules:

- One PR = one issue/topic.
- Commit style: `type(scope): description` (see CONTRIBUTING.md).
- `SKILL.md` commands must be tested against the real GitHub API before
  landing (see AGENTS.md "Verification").
