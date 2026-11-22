## Description:

Use when an agent must pay for a call to an external AI service it has no account with by discovering the service, pricing the call, paying through the Nevermined Router within a human-capped budget, and checking what was spent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agent operators use this skill to discover and call paid external AI services through the Nevermined Router, while tracking spend against a budget set by a human.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live service calls can spend real money using the supplied Nevermined credentials; the security review also notes a possible autonomy concern and partial analysis.

Mitigation: Review proposed external calls and the skill's autonomous-action guidance, use a human-approved spending cap, and use the sandbox deployment for testing.

## Reference(s):

- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined Commerce MCP documentation](https://nevermined.ai/docs/products/catalog/mcp)
- [Nevermined Agent Services Catalog](https://nevermined.app/catalog/)
- [Authentication and API keys](https://nevermined.app/auth.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls]

**Output Format:** [Markdown instructions with shell command and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and examples for service discovery, quote, payment, and spend review]

## Skill Version(s):

0.1.49 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
