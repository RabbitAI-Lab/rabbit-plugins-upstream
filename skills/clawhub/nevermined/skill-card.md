## Description:

Guides agents and developers through Nevermined payment-plan purchases, spending delegations, credit and revenue checks, and x402 payment protection for AI services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Nevermined payment protection to AI agents and APIs. Agents can use its guidance to purchase access, manage payment delegations, and check buyer credits or seller revenue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live payment actions or card delegations can incur real charges.

Mitigation: Start in sandbox; enable live credentials or card delegations only with approval, tight spending limits, and short delegation durations.

Risk: Payment credentials and customer data can leak through logs or insecure storage.

Mitigation: Store API keys server-side in a secret manager; avoid logging callback URLs, payment tokens, delegation IDs, customer emails, or scoped customer keys.

## Reference(s):

- [Nevermined Payments on ClawHub](https://clawhub.ai/nevermined-io/skills/nevermined)
- [Nevermined skill documentation](https://nevermined.ai/docs/development-guide/build-using-nvm-skill)
- [Get a Nevermined API key](https://nevermined.ai/docs/agents-guide/get-api-key)
- [Nevermined app and API key management](https://nevermined.app)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
