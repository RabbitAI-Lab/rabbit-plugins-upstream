## Description:

Checks waybill POD and COD reconciliation tables by recalculating row values, totals, duplicate rows, blanks, and negative amounts, with source-cited findings for the free tier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, logistics, and settlement staff use this skill during monthly close, reconciliation, or inventory checks to verify waybill proof-of-delivery and cash-on-delivery settlement tables. It helps identify arithmetic mismatches, duplicate same-period waybills, blank placeholders, and negative values while avoiding conclusions when required table material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes business and financial reconciliation records.

Mitigation: Provide only files intended for local review and treat the output as a reconciliation aid rather than accounting, tax, legal, or contract advice.

Risk: The free tier omits some checks that are listed as not included.

Mitigation: Review the executed and withheld check lists in the output before relying on the result for a settlement workflow.

Risk: Missing or unrecognized table material can lead to unsupported conclusions if interpreted casually.

Mitigation: Use the missing-material guidance returned by the skill and do not treat insufficient-input runs as a clean reconciliation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/waybill-pod-cod-check-free)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown-style terminal text or JSON when run with --json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows and locations; input is limited to 4 MB and insufficient material returns no reconciliation conclusion.]

## Skill Version(s):

1.0.46 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
