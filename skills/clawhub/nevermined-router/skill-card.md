## Description:

Guides an AI agent through discovering payable x402 or MPP services, creating a budget-capped Nevermined Delegation, funding the buyer wallet, routing paid calls, reading the payment ledger, and applying spending guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill when an autonomous agent needs to buy a single call from a payable x402 or MPP service without holding a direct account or long-lived merchant API key. The skill focuses on budget-capped payment delegation, routed paid calls, ledger review, and stop conditions for spending refusals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can spend from a Nevermined-funded wallet.

Mitigation: Install only for agents intended to make paid service calls, set small Delegation caps and expirations, and monitor the payment ledger.

Risk: An unrestricted Delegation can pay any reachable merchant supported by the Router.

Mitigation: Use recipient scoping when the merchant is known, and rely on the Delegation cap and expiry as hard spending limits.

Risk: Retrying non-retryable Router refusals can waste budget or bypass intended human controls.

Mitigation: Treat budget, wallet, legacy-key, 3-D Secure, and deterministic payment errors as stop conditions requiring human review.

Risk: Forwarding the Nevermined API key to a merchant would expose the buyer credential.

Mitigation: Use NVM_API_KEY only for Nevermined Router calls and pass any merchant-specific credential separately.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined Publisher Profile](https://clawhub.ai/user/nevermined-io)
- [Nevermined Router Overview](https://nevermined.ai/docs/products/router/overview)
- [Nevermined App API Keys](https://nevermined.app)
- [Nevermined Exa Integration](https://nevermined.ai/docs/integrations/exa)
- [Bootstrap](references/bootstrap.md)
- [Discovery](references/discovery.md)
- [Errors and Guardrails](references/errors.md)
- [Ledger](references/ledger.md)
- [Paying](references/paying.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, HTTP examples, JSON payloads, and decision rules]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY for Router calls; catalog discovery is public and unauthenticated.]

## Skill Version(s):

0.1.3 (source: release metadata; artifact frontmatter says 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
