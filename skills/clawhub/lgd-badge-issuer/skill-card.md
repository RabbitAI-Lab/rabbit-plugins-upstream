## Description:

Issues an LGD badge certificate with SHA-256 evidence fingerprints and an issuance ledger only when all three required evidence categories are present; otherwise records a refusal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); All rights reserved (documentation and theoretical text)

## Use Case:

Developers and governance teams use this skill to record local badge issuance or refusal for an agent or asset based on evidence supplied for three LGD categories. The badge is a governance aid, not independent regulatory certification or professional advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evidence files may contain sensitive information that is read and hashed locally.

Mitigation: Supply only appropriate evidence files or non-sensitive values, and confirm local hashing is acceptable before use.

Risk: The helper writes a local registry and can write a certificate file.

Mitigation: Choose registry and certificate paths deliberately and review their contents and access permissions.

## Reference(s):

- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-badge-issuer)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Human-readable or JSON status; JSON certificate and local issuance/refusal registry]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issued certificates include SHA-256 evidence fingerprints; refusals are logged when a required evidence category is missing.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release; bundled frontmatter says 1.1.0 and manifest says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
