## Description:

Checks transaction records for simple anti-money-laundering risk patterns, including structuring, rapid movement of funds, missing counterparty KYC, and unreported large transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theoretical text: All rights reserved

## Use Case:

Developers and compliance teams can use the local transaction checker to flag records for further human AML review; its heuristic results are not a regulatory or professional determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Simple heuristics and broad compliance claims may lead users to treat results as definitive AML or suspicious-activity determinations.

Mitigation: Review flagged and unflagged transactions with qualified personnel against current official requirements; do not rely on this skill for a final compliance decision.

Risk: Transaction data may be sensitive, and Chinese-language output may be misunderstood by other users.

Mitigation: Process transaction data locally with appropriate access controls and ensure reviewers understand the output before acting on it.

## Reference(s):

- [AML Sentinel on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/aml-sentinel)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Chinese-language text or JSON risk-check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports flagged patterns, a heuristic risk score and level, and whether any transaction is high risk.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
