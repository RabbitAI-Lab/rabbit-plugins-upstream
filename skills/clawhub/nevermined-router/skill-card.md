## Description:

Use when an agent must pay for a call to an external AI service (data, search, enrichment, inference, scraping) it has no account with. Finds the service in the Nevermined Agent Services Catalog, prices the call for free, pays per call through the Nevermined Router from a budget a human capped, and checks what was spent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover cataloged AI services, make paid calls within a human-approved spending limit, and review payment records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid call may spend more than the amount inspected in a quote while remaining within the delegation cap.

Mitigation: When a per-call ceiling is needed, use a route that supports maxTotalCents; keep the delegation cap appropriately small and verify recorded spend after calls.

## Reference(s):

- [Nevermined Router overview](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined Commerce MCP](https://nevermined.ai/docs/products/catalog/mcp)
- [Catalog service discovery](https://nevermined.app/catalog/llms.txt)
- [Paying and per-call limits](references/paying.md)
- [Delegation setup and funding](references/bootstrap.md)
- [Catalog discovery guidance](references/discovery.md)
- [Payment ledger](references/ledger.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a human-provided Nevermined API key or MCP sign-in and a human-capped spending delegation; paid calls may use real funds.]

## Skill Version(s):

0.1.52 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
