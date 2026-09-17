## Description:

A local checker for warehouse fee worksheets that recalculates storage fees, overdue fees, totals, duplicate entries, and blanks, with each finding tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and operations teams use this skill to check monthly warehouse fee settlement tables for arithmetic mismatches, total-row errors, duplicate customer or batch entries, and missing values. The free edition reports only the checks implemented in the bundled local engine and identifies omitted checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local checker is limited, and the package also contains onboarding text that points users or agents toward an unpinned remote install and purchase workflow outside the reviewed package.

Mitigation: Do not run embedded purchase or install commands unless the remote package, exact version, merchant, product, and newly installed skill have been separately reviewed and approved by the user.

Risk: The free edition intentionally omits several validation checks, including negative rate checks, non-positive quantity checks, out-of-range day checks, overdue-day logic checks, and negative or below-storage total checks.

Mitigation: Treat results as limited to the listed free checks and separately review omitted checks before relying on the worksheet for billing decisions.

Risk: When worksheet material is missing or headers are not recognized, the engine returns insufficient input instead of a fee conclusion.

Mitigation: Provide exported worksheet text or JSON with the required headers and do not interpret an insufficient-input result as evidence that no issue exists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/warehouse-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON fee-check findings with source line numbers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided worksheet text or JSON; requires recognizable table headers and parseable numeric values.]

## Skill Version(s):

1.0.10 (source: evidence.json release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
