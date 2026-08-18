## Description:

Guides an AI agent through using the Nevermined Router to discover payable x402 or MPP services, create and fund a capped Delegation, make paid Router calls, read the payment ledger, and apply buyer guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous-agent operators use this skill when an agent needs to buy individual calls from external x402 or MPP services through Nevermined Router while staying within a human-approved budget, expiry, and payment ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through real-money Router purchases.

Mitigation: Use sandbox keys first, set small Delegation limits and short expiries, and require explicit human approval before funding live wallets.

Risk: An agent could exceed the user's intended spend by widening or replacing a Delegation after a refusal.

Mitigation: Treat exhausted, expired, revoked, or underfunded Delegations as stop conditions and do not raise budgets or create replacement Delegations without human approval.

Risk: Retries with a fresh request id can buy the same resource more than once.

Mitigation: Use one stable requestId per logical purchase and reuse it across retries.

Risk: Forwarding the Nevermined API key to a merchant would expose account credentials.

Mitigation: Use NVM_API_KEY only for Nevermined Router calls and pass merchant credentials separately when a service requires its own authentication.

Risk: An agent could accept updated legal terms on behalf of an account holder.

Mitigation: Report consent_required responses to the human and stop; do not use API credentials to accept legal terms for the account holder.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined API keys](https://nevermined.app)
- [Nevermined Router overview](https://nevermined.ai/docs/products/router/overview)
- [Nevermined Exa integration](https://nevermined.ai/docs/integrations/exa)
- [Bootstrap](references/bootstrap.md)
- [Discovery](references/discovery.md)
- [Paying](references/paying.md)
- [Ledger](references/ledger.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Configuration instructions, JSON examples]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only output; requires a Nevermined API key for live Router usage.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
