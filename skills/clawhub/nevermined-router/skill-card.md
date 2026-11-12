## Description:

Use when an AI agent needs to pay an external x402 or MPP service through the Nevermined Router, from discovering services and setting a spending budget to quoting calls, routing payments, and reading the ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to discover and pay eligible external services without holding an account with each provider. It guides the agent through setting a capped spending Delegation, checking the price, routing a call, and reviewing payment records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routing requests can spend from the buyer wallet, and the security review flags a ledger settlement action as outside the skill's stated scope.

Mitigation: Use a human-approved spending cap, quote before routing, and review settlement actions against the authoritative payment record before proceeding.

Risk: Search terms sent to the external service catalog may disclose sensitive information.

Mitigation: Keep secrets and sensitive search terms out of catalog queries.

Risk: Security analysis coverage is partial because some local references could not be resolved.

Mitigation: Review the referenced guidance and confirm relevant behavior against current Nevermined documentation before execution.

## Reference(s):

- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined API key portal](https://nevermined.app)
- [Agent Services Catalog](https://nevermined.app/catalog/ai-catalog.json)
- [Bootstrap and funding](references/bootstrap.md)
- [Service discovery](references/discovery.md)
- [Paid calls and streaming](references/paying.md)
- [Payment ledger](references/ledger.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown with inline HTTP and curl examples and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and examples for an agent; no executable package is included.]

## Skill Version(s):

0.1.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
