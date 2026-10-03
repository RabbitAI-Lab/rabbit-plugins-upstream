## Description:

Creates JSON boarding-pass records for AI agents with stated identity, evidence hashes, allowed actions, and expiry, then checks their fingerprint and expiry locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theory)

## Use Case:

Developers and teams use this skill to record an agent's stated identity, supporting evidence hashes, allowed actions, and expiry in a shareable local checklist or audit note. The pass is not proof of identity or permission to act.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification can accept forged identity and permission records, so a passing result does not establish issuer identity or authorization.

Mitigation: Treat the pass only as a local checklist or audit note; do not grant permissions or gate sensitive actions on its result without authenticated signatures or an external trust store.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-boarding-pass)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [JSON records, Text, Guidance]

**Output Format:** [JSON pass files or human-readable CLI status and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local fingerprint and expiry checks; not an authorization credential.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release; bundled files show different versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
