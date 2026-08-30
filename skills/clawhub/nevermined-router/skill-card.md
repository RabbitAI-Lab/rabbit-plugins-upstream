## Description:

Use when an AI agent needs to pay an external x402 or MPP service through the Nevermined Router, including service discovery, Delegation setup, funded-wallet checks, paid route/proxy calls, ledger review, and autonomous spending guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous-agent builders use this skill when an agent must buy a single paid request from an x402 or MPP merchant without holding that merchant's own account. It guides the agent through creating a capped Delegation, funding the buyer wallet, routing paid calls, and reconciling spend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can spend funds through Nevermined Router when given a valid API key and funded Delegation.

Mitigation: Use sandbox keys for testing, set small Delegation caps and short expirations, and treat budget or wallet refusals as stop conditions.

Risk: A leaked NVM_API_KEY could expose the account to unauthorized Router operations within the key's authority.

Mitigation: Keep NVM_API_KEY private, never forward it to merchants, and pass merchant-specific credentials separately when needed.

Risk: Incorrect retry or requestId handling can buy the same paid resource more than once.

Mitigation: Use one stable requestId per logical purchase and do not replace it to bypass duplicate-payment responses.

Risk: Unexpected or unrecognized spend may occur if an autonomous agent pays services without reconciliation.

Mitigation: Monitor the Router ledger and Delegation state for unrecognized request IDs, burn rate, remaining budget, and unexpected spend.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined app](https://nevermined.app)
- [Nevermined Router overview](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined Exa integration](https://nevermined.ai/docs/integrations/exa)
- [Bootstrap](references/bootstrap.md)
- [Discovery](references/discovery.md)
- [Errors](references/errors.md)
- [Ledger](references/ledger.md)
- [Paying](references/paying.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY for Router calls; catalog discovery is public.]

## Skill Version(s):

0.1.8 (source: release evidence; artifact frontmatter says 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
