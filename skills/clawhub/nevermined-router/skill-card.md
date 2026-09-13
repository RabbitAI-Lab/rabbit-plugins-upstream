## Description:

Guides an AI agent through discovering and paying for x402 or MPP services with the Nevermined Router, including Delegation setup, wallet funding, routed calls, ledger review, and spend guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an autonomous agent needs to buy capped paid calls from external x402 or MPP merchants through Nevermined. It helps the agent discover services, create and use Delegations, avoid double-spend retry patterns, and reconcile spend through the Router ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can spend real funds through Nevermined Router calls.

Mitigation: Use sandbox first, set small Delegation caps and expiries, and stop on budget, expiry, or wallet-balance refusals instead of widening limits automatically.

Risk: Retrying paid calls with fresh request IDs can buy the same resource more than once.

Mitigation: Use one stable requestId per logical purchase and reuse it across retries.

Risk: Secrets or merchant credentials can be misrouted if the agent sends the wrong authorization header.

Mitigation: Keep NVM_API_KEY only for Nevermined API calls and pass merchant-specific credentials separately when required.

Risk: Spend accounting can be wrong if the agent sums merchant prices or stale response data.

Mitigation: Reconcile against Delegation state and ledger activity, including fee fields and unexpected request IDs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined app](https://nevermined.app)
- [Nevermined Router overview](https://nevermined.ai/docs/products/catalog/router/overview)
- [Exa integration](https://nevermined.ai/docs/integrations/exa)
- [Bootstrap](references/bootstrap.md)
- [Discovery](references/discovery.md)
- [Paying](references/paying.md)
- [Ledger](references/ledger.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY for authenticated Router operations; catalog discovery is public.]

## Skill Version(s):

0.1.13 (source: server release metadata; artifact frontmatter reports 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
