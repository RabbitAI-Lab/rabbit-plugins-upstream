## Description:

Guides an AI agent through paying external x402 or MPP services with the Nevermined Router, including catalog discovery, capped Delegations, funded buyer wallets, routed paid calls, ledger review, and autonomous-buyer guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent builders use this skill when an agent needs to buy a single call from an external x402 or MPP service without holding a direct account or billing relationship with that merchant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can spend from a Nevermined-funded wallet when using Router payment routes.

Mitigation: Use sandbox keys for testing, set small Delegation caps and expiries, and consider recipient scoping when the intended merchant is known.

Risk: Credential exposure could let a merchant or unrelated service receive the Nevermined API key.

Mitigation: Keep NVM_API_KEY separate from merchant credentials and never forward it in routed request headers.

Risk: Incorrect retry behavior can double-spend or route around user budget decisions.

Mitigation: Reuse one stable requestId per logical purchase, stop on budget or wallet refusals, and reconcile spend against the Delegation and ledger.

## Reference(s):

- [Nevermined Router product documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined app API keys](https://nevermined.app)
- [Bootstrap - API key, Delegation, funded wallet](references/bootstrap.md)
- [Discovery - finding something to buy](references/discovery.md)
- [Paying - mode B, streaming proxy, and mode A](references/paying.md)
- [Ledger - what you actually spent](references/ledger.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY and a funded Nevermined Delegation for paid Router operations.]

## Skill Version(s):

0.1.16 (source: ClawHub release evidence; artifact frontmatter lists 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
