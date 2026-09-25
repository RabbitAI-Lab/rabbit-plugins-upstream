## Description:

Overwing checks text for safety, personal data, confidential leaks, self-harm, sexual content, and severity, returning an API verdict and recommended action for moderation, screening, or draft review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frod27](https://clawhub.ai/user/frod27)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Overwing to screen model output, incoming messages, and drafts before sending, storing, or acting on them, especially when personal data or confidential content may be present.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checked text and optional context are sent to the Overwing remote service.

Mitigation: Use the skill only for content you are comfortable sending to Overwing, and avoid including unnecessary personal, confidential, or proprietary details in context.

Risk: The skill can create an account, handle an API key, or use an optional wallet-funded payment path.

Mitigation: Prefer a manually provisioned API key, never print the key into chat, and require explicit human limits before account creation or wallet spending.

Risk: Optional MCP usage through npx adds dependency and package supply-chain exposure.

Mitigation: Pin or review the MCP package before using the optional npx path.

## Reference(s):

- [Overwing homepage](https://overwing.ai)
- [Overwing agent guide](https://overwing.ai/llms.txt)
- [Overwing API reference](https://overwing.ai/docs)
- [Outbound message rule set example](https://overwing.ai/api/v1/rule-sets/outbound-message)
- [ClawHub skill listing](https://clawhub.ai/frod27/skills/overwing)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses with markdown usage guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and an OVERWING_API_KEY for authenticated API calls; optional x402 payment flow is available only with explicit wallet permission.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
