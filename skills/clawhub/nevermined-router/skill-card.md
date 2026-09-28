## Description:

Guides AI agents through discovering x402 or MPP services, budgeting and pricing purchases, making paid calls through Nevermined Router, and auditing spend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to find payable services, establish a capped spending Delegation, quote and purchase individual calls, and reconcile payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can spend funds authorized by a Delegation.

Mitigation: Use a capped Delegation, quote before purchase, and set maxTotalCents to limit the charged price.

Risk: Retrying a paid call with a new request ID can cause a second charge.

Mitigation: Reuse one stable request ID per purchase and inspect pending results or the ledger before retrying.

Risk: API credentials or merchant-supplied authorization may be exposed to the wrong recipient.

Mitigation: Keep NVM_API_KEY out of merchant headers and verify the destination before forwarding merchant credentials or using raw proxy targets.

Risk: A quote can trigger an unpaid request to a service, including actions with side effects.

Mitigation: Avoid quoting side-effectful actions and make one quote per purchase decision.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined API key setup](https://nevermined.app)
- [Service discovery guidance](references/discovery.md)
- [Payment and proxy guidance](references/paying.md)
- [Delegation and wallet setup](references/bootstrap.md)
- [Router errors and guardrails](references/errors.md)
- [Payment ledger guidance](references/ledger.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with example API calls and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides quote, payment, and ledger workflows; paid service responses depend on the merchant.]

## Skill Version(s):

0.1.28 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
