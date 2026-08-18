## Description:

Integrate SanctifAI Trust Proof-of-Human attestations. Use when an app needs cryptographic proof a human performed a task or human-in-the-loop verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sanctifai](https://clawhub.ai/user/sanctifai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate SanctifAI Trust attestations into applications that need proof a human approved, reviewed, signed off, or completed a task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can send attestation metadata and hashes to SanctifAI Trust and may create public certificates or on-chain records.

Mitigation: Confirm the data-sharing posture before use, keep raw task and result data client-side, and avoid personal or sensitive details in certificate-visible fields.

Risk: Tenant API keys could be exposed if embedded integration is implemented in client-side code.

Mitigation: Store API keys only on the backend or in the worker extension path, and mint presence sessions server-side for embedded integrations.

Risk: Incorrect taxonomy codes, origin allowlists, or local API targets can cause integration failures.

Mitigation: Use the fixed three-letter taxonomy codes, register production origins and RP IDs with the tenant, target https://trust.sanctifai.com unless explicitly confirmed otherwise, and run the documented smoke tests before user testing.

## Reference(s):

- [SanctifAI Trust documentation](https://trust.sanctifai.com)
- [SanctifAI Trust pricing](https://sanctifai.com/trust/pricing)
- [ClawHub skill page](https://clawhub.ai/sanctifai/skills/sanctifai-trust)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces integration guidance for REST API calls, hosted script usage, WebAuthn flows, credential handling, taxonomy codes, and smoke tests.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; artifact frontmatter: 1.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
