## Description:

Use this skill to discover external x402 or MPP services, quote and pay for calls through the Nevermined Router, manage a capped spending Delegation, and review the payment ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use the skill to let an agent discover, price, and pay eligible x402 or MPP services through the Nevermined Router while respecting a spending cap.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid calls and Delegation controls can spend real funds, and a payment may be marked settled.

Mitigation: Use sandbox credentials or a low spending cap when appropriate, review the quote and destination before paying, and verify the provider outcome before marking a payment settled.

Risk: Payment credentials and API keys grant access to paid services.

Mitigation: Keep NVM_API_KEY private, use only the required environment, and set a spending limit that matches the task.

## Reference(s):

- [Nevermined Router overview](https://nevermined.ai/docs/products/catalog/router/overview)
- [Buyer identity](https://nevermined.ai/docs/products/catalog/router/buyer-identity)
- [Nevermined API key portal](https://nevermined.app)
- [Bootstrap and spending Delegations](references/bootstrap.md)
- [Service discovery](references/discovery.md)
- [Payment and routing errors](references/errors.md)
- [Payment ledger](references/ledger.md)
- [Paying for services](references/paying.md)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration Instructions, JSON, Shell Commands]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
