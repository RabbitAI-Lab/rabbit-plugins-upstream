## Description:

Helps an AI agent discover and pay for external x402 or MPP services through the Nevermined Router using a capped delegation, funded wallet, routed paid calls, ledger review, and spending guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous agent operators use this skill when an agent needs to buy a metered call from an external x402 or MPP service without holding a direct account with that service. It covers catalog discovery, delegation setup, wallet funding, paid request routing, ledger review, and stop conditions for budget or payment failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to spend from a user-funded Nevermined delegation.

Mitigation: Use small spending limits, prefer sandbox for testing, and set recipient restrictions when practical.

Risk: An autonomous buyer could respond to budget, expiry, or wallet refusals by creating more spend authority.

Mitigation: Treat budget and wallet refusals as stop conditions and ask a human instead of widening or replacing the delegation.

Risk: Retries with a fresh requestId can purchase the same resource more than once.

Mitigation: Use one stable requestId per logical purchase and reuse it across retries.

Risk: Forwarding the Nevermined API key to a merchant would expose account-level payment authority.

Mitigation: Send NVM_API_KEY only to Nevermined APIs and pass merchant credentials separately when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined app](https://nevermined.app)
- [Nevermined Router documentation](https://nevermined.ai/docs/products/router/overview)
- [Nevermined Exa integration](https://nevermined.ai/docs/integrations/exa)
- [Bootstrap](references/bootstrap.md)
- [Discovery](references/discovery.md)
- [Paying](references/paying.md)
- [Ledger](references/ledger.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash, JSON, and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Nevermined API key in NVM_API_KEY and a capped, funded delegation before paid routing.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
