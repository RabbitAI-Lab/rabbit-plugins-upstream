## Description:

Integrate SanctifAI Trust Proof-of-Human attestations. Use when an app needs cryptographic proof a human performed a task or human-in-the-loop verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sanctifai](https://clawhub.ai/user/sanctifai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integrators use this skill to add Proof-of-Human attestations to applications, Chrome extension workflows, or AI-agent chat flows when they need evidence that a person approved, reviewed, signed off, or completed a task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hosted chat bridge can receive raw taskData and resultData despite privacy claims that emphasize client-side commitments.

Mitigation: Use opaque, non-sensitive values with the hosted chat bridge, or choose an embedded or self-hosted commitment-only design for confidential workflows.

Risk: Public certificate URLs and task fields can expose sensitive context if identifiers or task descriptions contain personal or confidential data.

Mitigation: Use opaque identifiers, keep human-readable details in the integrating system, and retain exact payloads separately when later content proof is required.

## Reference(s):

- [SanctifAI Trust homepage](https://trust.sanctifai.com)
- [ClawHub skill release page](https://clawhub.ai/sanctifai/skills/sanctifai-trust)
- [SanctifAI Trust chat bridge skill](https://bridge.trust.sanctifai.com/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides implementation guidance and examples for embedded, extension, and chat bridge attestation flows.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
