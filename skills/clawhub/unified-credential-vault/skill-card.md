## Description:

A documentation-only skill describing a unified credential vault concept for cross-ecosystem credential management, including zero-knowledge self-hosting, anti-phishing posture, AI-agent authorization, recovery, revocation, and auditability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and security reviewers can use this skill to understand a proposed credential-vault architecture and its claimed controls for personal, enterprise, and AI-agent credential authorization scenarios. It does not provide an executable vault implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Readers may mistake the package's credential-vault claims for a working password manager or verified secret-management implementation.

Mitigation: Treat the release as documentation-only until an implementation, threat model, and independent security review are available.

Risk: The artifact describes credential handling and AI-agent authorization but contains no executable controls that protect, store, or broker real secrets.

Mitigation: Do not use the skill itself to store credentials or grant access to real accounts; require a separate production system with tested access controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/unified-credential-vault)
- [MedXpert site](https://medxpert.cn)
- [Capabilities panorama](references/panorama-capabilities.svg)
- [Comparison radar](references/panorama-radar.svg)
- [Security radar](references/panorama-security-radar.svg)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown prose with linked SVG reference assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; no scripts, commands, dependency installation, automatic network access, or credential-handling implementation.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, manifest.json, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
