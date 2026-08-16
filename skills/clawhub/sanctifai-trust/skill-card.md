## Description:

Integrate SanctifAI Trust Proof-of-Human attestations. Use when an app needs cryptographic proof a human performed a task or human-in-the-loop verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sanctifai](https://clawhub.ai/user/sanctifai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add SanctifAI Trust Proof-of-Human attestations to applications that need a verifiable human approval, review, signoff, or task-completion record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tenant API key could be exposed if an embedded integration places it in client-side code.

Mitigation: Keep the tenant API key only on the backend and mint presence sessions server-side.

Risk: Public certificate fields may reveal personal or sensitive information if populated with direct identifiers or descriptive private data.

Mitigation: Use opaque internal identifiers and avoid personal or sensitive data in fields that may appear on public certificates.

Risk: Users may rely on an attestation provider or public proof flow without confirming it fits their trust and privacy requirements.

Mitigation: Confirm trust in SanctifAI Trust as the attestation provider before installation and review the public proof data model before deployment.

## Reference(s):

- [SanctifAI Trust homepage](https://trust.sanctifai.com)
- [ClawHub skill page](https://clawhub.ai/sanctifai/skills/sanctifai-trust)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces integration guidance for REST API calls, WebAuthn flows, environment variables, and operational checks.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
