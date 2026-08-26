## Description:

Guides an AI agent through buying calls from external x402 or MPP services with the Nevermined Router, including service discovery, Delegation budgeting, wallet funding, paid request routing, ledger review, and spending guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill when an autonomous agent must buy a single paid service call from an external x402 or MPP merchant without a direct account. It helps them create capped Delegations, route paid requests, and audit spend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables agents to make paid calls through Nevermined within a user-capped budget.

Mitigation: Use sandbox keys for testing, set small Delegation limits and expirations, prefer recipient scoping when possible, and review ledger activity regularly.

Risk: A poorly designed retry loop can cause duplicate purchases or repeated payment attempts.

Mitigation: Reuse one stable requestId per logical purchase, retry only documented retryable conditions, and stop on budget, wallet, consent, or key-related refusals.

Risk: Secrets could be exposed if the Nevermined API key is forwarded to a merchant service.

Mitigation: Keep NVM_API_KEY only for Nevermined API calls and pass any merchant-specific authentication separately.

## Reference(s):

- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined app](https://nevermined.app)
- [Exa integration documentation](https://nevermined.ai/docs/integrations/exa)
- [Bootstrap reference](references/bootstrap.md)
- [Discovery reference](references/discovery.md)
- [Errors and guardrails reference](references/errors.md)
- [Ledger reference](references/ledger.md)
- [Paying reference](references/paying.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY and emphasizes capped spending, stable request IDs, and ledger review.]

## Skill Version(s):

0.1.6 (source: server release metadata; artifact frontmatter says 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
