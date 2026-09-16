## Description:

Guides an AI agent through using the Nevermined Router to discover payable x402 or MPP services, create and fund a capped Delegation, make routed paid calls, read payment records, and follow autonomous-spend guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent builders use this skill when an agent needs to buy a single call from an external x402 or MPP service through Nevermined without holding a direct account with that merchant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid call without a per-call ceiling can consume the delegated budget if a merchant returns an unexpected quote.

Mitigation: Use sandbox keys for testing, keep Delegations small and short-lived, scope allowedRecipients and maxTransactions when practical, and set maxTotalCents on production paid calls.

Risk: Retries with a fresh requestId can buy the same resource more than once.

Mitigation: Use one stable requestId per logical purchase and reuse it across retries.

Risk: Live Router calls can spend real funds from the funded buyer wallet.

Mitigation: Confirm the environment, wallet address, Delegation status, and remaining budget before routing paid calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined Router Documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined App](https://nevermined.app)
- [Bootstrap](references/bootstrap.md)
- [Discovery](references/discovery.md)
- [Paying](references/paying.md)
- [Ledger](references/ledger.md)
- [Errors and Guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY for authenticated Nevermined Router calls.]

## Skill Version(s):

0.1.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
