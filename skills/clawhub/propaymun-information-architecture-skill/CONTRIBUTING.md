# Contributing

Thanks for helping improve ProPaymun Information Architecture.

## Principles

- Preserve user intent and flexible output selection.
- Add rules only when they improve real decisions or prevent demonstrated failure.
- Separate evidence from heuristics and proposed conventions.
- Do not turn one product, language, user group, or test result into a universal IA rule.
- Keep `SKILL.md` concise; route conditional detail to focused references.
- Keep the generated Agent Skill Package, Workspace Kit, and compatibility aliases synchronized with canonical sources.
- Keep product-sitemap and user-flow companion contracts distinct from IA while preserving their source lock or versioned minimum semantic substrate.
- Treat critical behavioral clauses as individual release gates; an aggregate score cannot override a security, authority, semantic-drift, or user-control failure.
- Keep visual builders such as Figma Make and Lovable downstream; do not reintroduce them as IA reasoning runtimes.
- Treat language, locale, jurisdiction, culture, and operating model as separate signals.

## Workflow

Before editing, classify each proposed rule as a semantic invariant, safety or authorization requirement, external standard, heuristic, local preference, example, historical observation, duplicate, or unsupported claim. Keep decision-changing rules in the smallest coherent context and route conditional detail to the owning reference.

1. Create a focused branch.
2. Update canonical files in `SKILL.md`, `references/`, `schema/`, or `scripts/`.
3. Rebuild packages with `python scripts/build_packages.py`.
4. Run `python -m unittest discover -s tests -v`.
5. Run the Agent Skill quick validator.
6. Add or refine an eval case when behavior changes.
7. Explain the user-observable improvement in the pull request.

Avoid tests that require exact prose. Test decisions, evidence handling, output selection, schema validity, and artifact usability.

For behavior changes, preserve representative output from the latest stable release and compare it with the candidate using `evals/RUBRIC.md`. Deterministic tests and package parity are necessary, but they do not establish mentoring quality, cross-host consistency, visual quality, or immunity to every prompt injection.
