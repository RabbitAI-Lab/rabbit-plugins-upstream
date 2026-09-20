## Description:

发票领用存台账逐项核对，复算逐行算术、合计勾稽、重复月份和空缺字段，并为结论提供原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or inventory checks to validate invoice usage and stock ledgers. It reports arithmetic mismatches, overuse, negative closing stock, duplicate periods, blank placeholders, and insufficient input without inventing conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence notes inconsistent telemetry wording: help text mentions anonymous usage statistics and --no-stats, but the inspected code did not implement observed network reporting or that option.

Mitigation: Review the packaged code and help text before deployment, and treat telemetry wording as a documentation inconsistency unless a future scan observes network behavior.

Risk: The free edition intentionally omits checks such as cross-month continuity, void-rate anomaly detection, reversal-rate anomaly detection, non-integer count detection, and no-receipt issuance detection.

Mitigation: Use results only for the listed checks and route omitted controls to a fuller review process when they matter.

Risk: The checker depends on user-provided invoice ledger text with recognizable headers; incomplete or malformed input can prevent conclusions.

Mitigation: Provide complete tables with the required columns and review insufficient-input responses before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/invoice-usage-stock-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable text or JSON containing findings, source line references, executed checks, withheld checks, and insufficiency messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns insufficient-input messages instead of conclusions when required ledger columns or rows are missing.]

## Skill Version(s):

1.0.52 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
