## Description:

Provides a six-point, Chinese-first checklist for screening smart-contract interactions before proceeding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory: All rights reserved

## Use Case:

Developers and agents use this checklist to review contract audits, target addresses, token approvals, revocation, key handling, and small test transactions before a smart-contract interaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checklist results may be mistaken for a contract audit or legal, investment, or security advice.

Mitigation: Treat results as reminders only; independently verify the contract and seek qualified review for consequential decisions.

Risk: Broad WebFetch or Write permissions are unnecessary for the local checklist.

Mitigation: Do not grant WebFetch or Write unless a specific use requires them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/contract-interact-checklist)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Chinese-language checklist with PASS/FAIL results, optionally JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports missing checklist items and unlimited-approval warnings; exits 0 for pass and 1 for fail.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
