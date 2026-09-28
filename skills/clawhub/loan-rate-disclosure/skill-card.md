## Description:

Checks Chinese-language loan offers for annualized-rate disclosure and rates above four times a supplied reference rate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory: All rights reserved

## Use Case:

Agents and reviewers preparing Chinese-language loan promotions can use this skill to pre-screen annualized-rate wording and compare quoted rates with a supplied reference rate. Results require human review and are not legal or financial advice.

### Deployment Geography for Use:

China-focused (LPR-based checks; confirm applicable rules before use in any jurisdiction)

## Known Risks and Mitigations:

Risk: A rough disclosure screen may be mistaken for legal or financial clearance.

Mitigation: Have a qualified reviewer verify the current official rules and any material lending decision.

Risk: Remote install instructions point to a GitHub tag that has not been established as this release's server-resolved provenance.

Mitigation: Verify the referenced source and tag independently before using the remote install commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/loan-rate-disclosure)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable PASS/FAIL checks or JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports disclosure and rate checks with problems; command exits 0 on pass, 1 on fail, and 2 on usage error.]

## Skill Version(s):

1.0.2 (source: ClawHub release; packaged SKILL.md says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
