## Description:

Checks share-based payment detail tables for row-level arithmetic, totals, duplicate rows, blanks, and balance roll-forwards, with each finding tied to source values.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting teams use this skill before monthly, quarterly, or audit workpaper review to reconcile exported share-based payment amortization tables. It helps identify arithmetic and completeness issues, but it does not replace accounting judgment, valuation work, tax analysis, audit procedures, or assurance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privacy and telemetry wording is inconsistent, which may cause users to misunderstand whether any usage statistics are sent.

Mitigation: Confirm the publisher's current telemetry behavior before making privacy claims, and treat the checker as local-only for table contents but not as fully clarified on telemetry wording until corrected.

Risk: The free edition intentionally omits several checks, including straight-line amortization variance, excess amortization, and vesting-period completion checks.

Mitigation: Use this release only for the listed free checks, and perform manual review or use a complete checker when omitted controls are required.

Risk: The checker performs arithmetic reconciliation and completeness checks, not accounting, valuation, tax, audit, or assurance judgments.

Mitigation: Route accounting policy, fair-value, vesting-condition, tax, and audit conclusions through qualified review.

Risk: Incomplete or unrecognized table headers result in no conclusion rather than a clean result.

Mitigation: Provide exported table text with recognizable headers and required columns, and treat insufficient-input output as a request for more data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/share-based-payment-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Artifact skill instructions](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON or text checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source values; insufficient input returns missing requirements instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.16 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
