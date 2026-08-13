## Description:

Integrates SanctifAI Trust Proof-of-Human attestations for apps that need cryptographic proof a human performed a task or completed human-in-the-loop verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sanctifai](https://clawhub.ai/user/sanctifai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate SanctifAI Trust into applications that need verifiable proof of human review, approval, signoff, or other human-in-the-loop work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tenant credentials could be exposed if copied into browser code or shared logs.

Mitigation: Store tenant credentials only on the backend or in a secret manager, and keep the Trust API key out of client-side JavaScript and agent chat logs.

Risk: Public certificate URLs and selected metadata can expose sensitive user or task information.

Mitigation: Treat certificate URLs as public, use opaque IDs, and avoid PII in certificate-visible fields.

Risk: Integrating a third-party proof-of-human attestation service may introduce external dependency and data-handling obligations.

Mitigation: Confirm organizational approval for SanctifAI Trust before installation and review the skill's security guidance before deployment.

## Reference(s):

- [SanctifAI Trust](https://trust.sanctifai.com)
- [ClawHub Skill Page](https://clawhub.ai/sanctifai/skills/sanctifai-trust)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with inline code blocks and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce integration steps, API usage, browser and backend code, environment-variable guidance, and verification checks.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
