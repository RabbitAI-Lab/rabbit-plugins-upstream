## Description:

Guides an AI agent through discovering x402 or MPP services, creating and using a capped Nevermined Delegation, making paid routed calls, reading the payment ledger, and applying buyer guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill when an agent needs to buy a single call from an external x402 or MPP merchant without holding a direct account, API key, or billing relationship with that service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent activity can spend funds through Nevermined within the user's delegated budget.

Mitigation: Use sandbox keys for testing, set small Delegation caps and expirations, and review the payment ledger for unexpected request IDs or spend.

Risk: A Nevermined API key could be exposed to a merchant or other external service.

Mitigation: Keep NVM_API_KEY scoped to Nevermined requests and never provide it to merchants; use separate merchant authentication only when explicitly required.

Risk: An autonomous agent could try to bypass budget or consent boundaries to complete a purchase.

Mitigation: Do not allow the agent to raise budgets, create replacement Delegations to evade refusals, or accept legal terms on the user's behalf.

## Reference(s):

- [Nevermined Router skill on ClawHub](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined API key management](https://nevermined.app)
- [Nevermined Router overview](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined Exa integration](https://nevermined.ai/docs/integrations/exa)
- [Bootstrap - API key, Delegation, funded wallet](references/bootstrap.md)
- [Discovery - finding something to buy](references/discovery.md)
- [Errors and guardrails](references/errors.md)
- [Ledger - what you actually spent](references/ledger.md)
- [Paying - mode B, the streaming proxy, and mode A](references/paying.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and HTTP request patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Nevermined API key in NVM_API_KEY and uses a human-capped Delegation for paid calls.]

## Skill Version(s):

0.1.10 (source: ClawHub release evidence; artifact frontmatter reports 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
