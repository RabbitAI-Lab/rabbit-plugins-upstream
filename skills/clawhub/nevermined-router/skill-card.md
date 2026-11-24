## Description:

Use when an agent must pay for a call to an external AI service (data, search, enrichment, inference, scraping) it has no account with. Finds the service in the Nevermined Agent Services Catalog, prices the call for free, pays per call through the Nevermined Router from a budget a human capped, and checks what was spent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover external AI services and route paid calls through Nevermined within a human-capped budget, then review recorded spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live paid calls can spend real funds within the approved delegation cap, and the security assessment notes that some referenced paths could not be resolved.

Mitigation: Use a small human-set cap, price requests before paying, check the payment ledger, and review relevant references for the intended use.

## Reference(s):

- [Nevermined app and API keys](https://nevermined.app)
- [Authentication and API keys](https://nevermined.app/auth.md)
- [Router overview](https://nevermined.ai/docs/products/catalog/router/overview)
- [Commerce MCP](https://nevermined.ai/docs/products/catalog/mcp)
- [Bootstrap](references/bootstrap.md)
- [Discovery](references/discovery.md)
- [Paying](references/paying.md)
- [Ledger](references/ledger.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Nevermined API key or approved MCP sign-in and a human-set spending cap before paid use.]

## Skill Version(s):

0.1.53 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
