## Description:

Checks supplier accounts payable reconciliation tables for row-level arithmetic, totals, duplicate or blank entries, and nonzero differences, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations teams use this skill to check supplier reconciliation tables before follow-up or payment workflows. It helps identify arithmetic mismatches, unmatched supplier balances, duplicate suppliers, incomplete fields, and total-row errors in copied tabular text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a local Node script with Bash permission on supplier reconciliation data.

Mitigation: Run it only in a trusted local environment and provide only the reconciliation table intended for checking.

Risk: The output can support reconciliation review but is not audit, tax, legal, or payment approval advice.

Mitigation: Use findings as arithmetic reconciliation support and keep final approval decisions in the existing finance review process.

Risk: Insufficient or malformed input can prevent reliable reconciliation conclusions.

Mitigation: Provide copied tabular text with a recognizable supplier header and relevant amount columns; treat insufficient-input responses as no conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ap-reconciliation-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON with findings, summaries, executed checks, omitted checks, and source-line evidence.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines; insufficient input returns missing requirements without issuing a reconciliation conclusion.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
