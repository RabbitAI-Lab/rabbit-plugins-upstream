## Description:

Collects marked shortcut comments across a repository into a one-shot technical-debt ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inventory deliberate shortcuts in repository comments, identify missing revisit triggers, and track technical debt without changing source files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning the current repository reads comment content throughout the project.

Mitigation: Confirm the intended repository scope before running the scan.

Risk: Persisting the ledger changes a file when the user only expects a report.

Mitigation: Keep the default report read-only; save a ledger only when explicitly requested.

## Reference(s):

- [Project homepage](https://github.com/DietrichGebert/ponytail)
- [ClawHub skill listing](https://clawhub.ai/dietrichgebert/skills/ponytail-debt)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown ledger grouped by file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entries include file and line, shortcut, ceiling, and revisit trigger; missing triggers are tagged and totals are reported. Saves to a file only on request.]

## Skill Version(s):

5.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
