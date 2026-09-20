## Description:

This skill locally checks Chinese employee welfare and education expense ledgers for row-level arithmetic, total-row consistency, duplicate entries, blanks, placeholders, and negative amounts, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and bookkeeping staff use this skill during monthly close, reconciliation, or review to check employee welfare and education expense ledgers before relying on the table. It is scoped to deterministic ledger consistency checks and does not replace tax or compliance advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is a narrow ledger arithmetic and table-consistency checker, not a complete tax or compliance review.

Mitigation: Use the output as a review aid and confirm tax treatment, wage-base composition, adjustment timing, and filing details with the relevant tax authority or qualified reviewer.

Risk: A clean result can omit checks that are outside the free version or unavailable when input is incomplete.

Mitigation: Review the reported executed checks, checks not run, and missing-input messages before relying on the result.

Risk: Release evidence and artifact frontmatter disagree on the license.

Mitigation: Confirm the authoritative license before publication or downstream redistribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/welfare-limit-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, findings, missing-input guidance, scope, and summary status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include line references; the free version lists checks not run and withholds conclusions when input is insufficient.]

## Skill Version(s):

1.0.42 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
