## Description:

Integrate SanctifAI Trust Proof-of-Human attestations. Use when an app needs cryptographic proof a human performed a task or human-in-the-loop verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sanctifai](https://clawhub.ai/user/sanctifai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to integrate Proof-of-Human attestations into applications or chat-agent workflows that need human participation verification and a returned certificate URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The chat-agent path may send raw task and result data to a hosted bridge even though the skill also describes privacy-preserving hashed payloads.

Mitigation: For confidential, regulated, or customer data, prefer the embedded flow that hashes locally, or self-host/control the bridge and send only minimized, pseudonymous payloads.

Risk: Public certificate URLs can expose metadata that an integrator places in attestation fields.

Mitigation: Use opaque identifiers, avoid PII in certificate-visible fields and bridge payloads, and keep detailed records in the integrator's own system.

Risk: Tenant API keys could be exposed if integration guidance is copied into client code or shared chat logs.

Mitigation: Keep TRUST_API_KEY only in backend or controlled bridge environments, and never print or request it in agent-visible outputs.

## Reference(s):

- [SanctifAI Trust homepage](https://trust.sanctifai.com)
- [ClawHub skill page](https://clawhub.ai/sanctifai/skills/sanctifai-trust)
- [SanctifAI-hosted chat bridge](https://trust-agent-c94n.onrender.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with code blocks, REST API examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include environment variable guidance for tenant credentials and API integration paths.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; artifact frontmatter reports 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
