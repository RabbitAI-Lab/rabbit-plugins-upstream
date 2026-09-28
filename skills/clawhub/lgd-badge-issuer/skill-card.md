## Description:

Issues an lgd-certified badge certificate with a SHA-256 fingerprint and issuance ledger when evidence covers all three LGD laws; otherwise records a refusal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and LGD theory: all rights reserved

## Use Case:

Developers and governance teams use this skill to check evidence for all three LGD laws before issuing a badge certificate and recording issuance or refusal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local issuer creates or updates JSON at the registry and optional certificate paths provided by the user.

Mitigation: Review destination paths before running and keep a backup of any existing registry.

Risk: The published license metadata and bundled terms differ, and the code license does not cover the documentation or LGD theory.

Mitigation: Confirm the applicable release terms before reuse or redistribution of code or documentation.

## Reference(s):

- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-badge-issuer)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON certificate and registry; text or JSON status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SHA-256 evidence fingerprints; optional certificate file; issuance and refusal records]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled skill frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
