## Description:

Guides an AI agent through discovering, budgeting for, paying, and auditing x402 or MPP service calls through the Nevermined Router.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to buy single paid calls from x402 or MPP services through Nevermined Router when the agent lacks a direct account or billing relationship. The skill helps the agent apply budget caps, ledger checks, and retry guardrails before spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can spend through Nevermined Router if given an active NVM_API_KEY and Delegation.

Mitigation: Use sandbox first, set small Delegation caps and expirations, and require human review before increasing budgets or funding wallets.

Risk: Leaking NVM_API_KEY could expose payment-routing capability.

Mitigation: Keep NVM_API_KEY private and never send it to merchant services; pass merchant-specific credentials separately when needed.

Risk: Blind retries or fresh request IDs can cause duplicate purchases or bypass budget intent.

Mitigation: Reuse one stable requestId per logical purchase, stop on documented non-retryable failures, and do not widen or replace Delegations to get past refusals.

## Reference(s):

- [Bootstrap - API key, Delegation, funded wallet](references/bootstrap.md)
- [Discovery - finding something to buy](references/discovery.md)
- [Paying - mode B, streaming proxy, and mode A](references/paying.md)
- [Ledger - what you actually spent](references/ledger.md)
- [Errors and guardrails](references/errors.md)
- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined Exa integration](https://nevermined.ai/docs/integrations/exa)
- [Nevermined app API keys](https://nevermined.app)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY for authenticated Router operations; catalog discovery is public.]

## Skill Version(s):

0.1.7 (source: server release evidence; artifact frontmatter reports 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
