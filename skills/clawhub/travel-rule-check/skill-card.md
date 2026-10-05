## Description:

Checks supplied VASP transfer details for sender and recipient identity fields and reports missing information against a fixed threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); All rights reserved (documentation and theory)

## Use Case:

Developers and compliance teams can use this local checklist to flag missing sender and recipient details in supplied VASP transfer data. It is not a legal determination of Travel Rule compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A lightweight field check could be mistaken for definitive legal compliance advice.

Mitigation: Treat results as a checklist and confirm decisions against current official requirements and qualified advice.

Risk: Transaction data entered on a command line may expose sensitive KYC details in shell history.

Mitigation: Avoid putting sensitive KYC data directly in shell commands; use non-sensitive test data or a safer input method.

Risk: Chinese-language messages may be misread by users who do not understand Chinese.

Mitigation: Use only where Chinese-language documentation and output can be reviewed reliably.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/travel-rule-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Chinese-language checklist result or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports missing fields and a pass/fail result.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
