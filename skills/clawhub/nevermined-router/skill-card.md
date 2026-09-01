## Description:

Guides agents through discovering x402 or MPP services, creating capped Nevermined Router delegations, making paid calls, and auditing spend through the Router ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to let agents buy one-off calls from x402 or MPP services through capped Nevermined Router delegations, then reconcile spend through the payment ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using this skill can spend through Nevermined Router within user-created delegation caps.

Mitigation: Use sandbox keys for testing, create small capped and expiring delegations, fund only the wallet and network needed, and review the ledger for unexpected spend.

Risk: Leaking NVM_API_KEY to a merchant would expose the user's Nevermined authentication credential.

Mitigation: Keep NVM_API_KEY only in the Nevermined Authorization header and pass any merchant credential separately through the documented merchant-auth fields.

Risk: Retries with fresh request identifiers can buy the same resource more than once.

Mitigation: Use one stable requestId per logical purchase, reuse it across retries, and do not create new delegations to bypass a refusal.

Risk: Incorrect wallet, network, or delegation state can cause payment failures or misleading spend accounting.

Mitigation: Read the live delegation before paying, verify status, expiry, remaining budget, and providerPaymentMethodId, then reconcile spend against the delegation and ledger.

## Reference(s):

- [Bootstrap - API key, Delegation, funded wallet](references/bootstrap.md)
- [Discovery - finding something to buy](references/discovery.md)
- [Paying - mode B, the streaming proxy, and mode A](references/paying.md)
- [Errors and guardrails](references/errors.md)
- [Ledger - what you actually spent](references/ledger.md)
- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined App](https://nevermined.app)
- [Nevermined Exa integration](https://nevermined.ai/docs/integrations/exa)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with HTTP examples, JSON payloads, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY for Router calls; catalog discovery is public and unauthenticated.]

## Skill Version(s):

0.1.9 (source: ClawHub release metadata; artifact frontmatter lists 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
