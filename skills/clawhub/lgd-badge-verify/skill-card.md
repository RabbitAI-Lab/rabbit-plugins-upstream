## Description:

Checks LGD badge certificate fields and fingerprint, with optional comparison against a supplied registry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and badge administrators use this skill to check a badge certificate's structure and fingerprint and, when a registry is supplied, compare its serial and fingerprint with that registry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A matching fingerprint can be mistaken for proof that a certificate was issued by a trusted authority.

Mitigation: Treat passing results as advisory; confirm issuance through a trusted registry or signature mechanism before relying on authenticity.

Risk: Registry comparison is optional and does not by itself establish current revocation status.

Mitigation: Use an authoritative, current registry with explicit revocation handling and review high-stakes decisions manually.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-badge-verify)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Human-readable verification results or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports per-check results and returns exit status 0 on pass, 1 on failed checks, or 2 on invalid certificate JSON.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
