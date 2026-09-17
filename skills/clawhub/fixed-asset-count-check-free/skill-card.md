## Description:

Checks fixed-asset inventory tables for row arithmetic, total reconciliation, duplicate asset IDs, blanks, and negative cost or depreciation values, with each finding tied to source evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and accounting users can run this skill during month-end close, reconciliation, or inventory review to check fixed-asset count sheets against ledger-style arithmetic and totals. It reports concrete inconsistencies and insufficient input rather than making unsupported conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill steers users or agents toward installing payment tooling and buying another skill.

Mitigation: Do not follow the paid-upgrade prompt or run the npm installer unless the payment package, merchant, and newly installed skill are independently trusted, preferably with pinned versions and explicit user approval at each step.

Risk: The free release omits several fixed-asset checks and may be mistaken for a complete accounting or tax review.

Mitigation: Review the reported check scope and checks_not_run list, and perform omitted accounting, tax, and internal-control judgments separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/fixed-asset-count-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Console text or JSON findings with cited source lines and check scope.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on supplied fixed-asset table text; reports missing required columns or insufficient input instead of fabricating conclusions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
