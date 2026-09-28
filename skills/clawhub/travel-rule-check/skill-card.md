## Description:

Checks whether a virtual-asset transfer includes required originator and beneficiary identity fields, including geographic details at the configured threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory: All rights reserved

## Use Case:

Developers and compliance teams can check transaction data for missing sender and recipient names, accounts or addresses, and geographic details before further review. This checklist is not a legal compliance determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer transaction and KYC details may remain in shell history or shared logs.

Mitigation: Enter sensitive details only through a private local workflow; avoid reusable shell history and shared logs.

Risk: A field-completeness check may be mistaken for a definitive regulatory assessment.

Mitigation: Verify applicable rules against current official guidance and seek qualified compliance review before making decisions.

## Reference(s):

- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/travel-rule-check)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text or JSON checklist result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports missing fields and a pass/fail result; exit codes distinguish passing checks, missing fields, and input errors.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
