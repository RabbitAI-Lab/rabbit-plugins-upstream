## Description:

Creates agent onboarding records with identity, evidence hashes, permitted actions and an expiry, then checks their checksum and expiry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and teams can record an agent's identity, supporting evidence hashes, allowed actions and expiry for local onboarding and review. A passing check does not establish that a trusted issuer approved the pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A passing checksum check can be forged and does not prove trusted approval of an agent's identity, evidence, permissions or expiry.

Mitigation: Use the pass only as a local record; require authenticated approval or trusted-key signatures before relying on it for access control.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-boarding-pass)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON boarding-pass file or human-readable issuance and verification result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records evidence hashes, allowed actions, expiry and a checksum; verification returns check results and an exit status.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
