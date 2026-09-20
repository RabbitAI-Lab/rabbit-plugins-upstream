## Description:

Performs local arithmetic and consistency checks on Chinese construction monthly settlement materials for subcontractor settlement, progress payments and retention, and project output/progress reconciliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and construction operations staff use this skill during monthly closing or reconciliation to check pasted construction settlement tables for arithmetic errors, totals, repeated rows, blanks, and missing required material. It reports cited findings for the free version's three supported check categories and identifies checks that were not run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat a clean result as accounting, legal, tax, or audit assurance.

Mitigation: Present results as arithmetic and consistency checks only, and require qualified review for accounting, legal, tax, audit, or assurance decisions.

Risk: Users may assume the free version performed the full set of construction monthly checks.

Mitigation: Call out the withheld full-version checks in outputs and avoid interpreting omitted checks as passed checks.

Risk: Incomplete or malformed pasted materials can produce an under-scoped review.

Mitigation: Require the expected section headers and table columns, and treat insufficient input as no conclusion rather than a clean result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chenqg618/skills/construction-monthly-selfcheck-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable command output or JSON containing check scope, findings, per-check status, missing-input guidance, and summary verdict.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill reports which checks ran, which full-version checks were withheld, and whether execution was local without network use.]

## Skill Version(s):

1.0.52 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
