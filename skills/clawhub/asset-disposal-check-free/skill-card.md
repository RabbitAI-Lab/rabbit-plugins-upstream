## Description:

Runs a local fixed-asset disposal table check that recalculates row values, totals, duplicates, and blank fields, then reports each finding with source evidence for the free check set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during fixed-asset disposal reconciliation to check table arithmetic, totals, repeated assets, and missing required values before close, audit, or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may assume the free version covers every fixed-asset disposal issue.

Mitigation: Review the omitted and out-of-scope checks before relying on the result, especially tax, impairment, and accounting-policy questions.

Risk: Input tables may contain sensitive accounting data.

Mitigation: Provide only the table data needed for the check and run the skill locally in an environment approved for that data.

Risk: Material gaps or unrecognized headers can make an apparent result misleading.

Mitigation: Use the insufficient-input response as a stop condition and add the required table columns before drawing conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/asset-disposal-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON with executed checks, omitted checks, summary status, and line-referenced findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on user-provided fixed-asset disposal table text; insufficient input returns missing requirements instead of a conclusion.]

## Skill Version(s):

1.0.54 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
