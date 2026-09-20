## Description:

Checks wastewater treatment fee settlement tables locally by recomputing settled volume, service fees, quality-band unit prices, and excess-discharge deductions, then flags duplicate settlements and blanks with source-line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

Wastewater plant, industrial park water-operations, finance, and reconciliation teams use this skill during monthly settlement review to check table arithmetic and consistency before invoicing, payment, reporting, or follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input tables may contain business, operational, or financial settlement data.

Mitigation: Run the checker only on files the user intends the local agent and script to read, and avoid providing unrelated sensitive material.

Risk: Arithmetic and consistency findings could be mistaken for legal, environmental-compliance, audit, or payment authorization advice.

Mitigation: Treat the output as table checking only and have qualified reviewers validate decisions before billing, reporting, or enforcement action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/wastewater-fee-check-free)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Guidance]

**Output Format:** [Plain text or JSON reports with line-referenced findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns missing-field guidance instead of conclusions when the input table is insufficient.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
