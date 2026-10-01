## Description:

Guides agents in managing Stripe customers, subscriptions, invoices, products, prices, and payments through a managed OAuth connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and administer a connected Stripe account, including billing resources and payment operations. It also documents optional hosted functions and event-triggered automation that require separate approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to live Stripe billing or payments can have significant or irreversible financial effects.

Mitigation: Default to read-only requests; verify the target account, object IDs, amounts, and test/live mode, then obtain explicit approval for every write, refund, payment, or deletion.

Risk: Broad connections or unattended automations can access customer and financial data beyond the intended task.

Mitigation: Use the least-privileged account and scopes; approve each connection, trigger, destination, and hosted function separately, and remove unused access.

Risk: A raw-HTTP write may use the wrong request encoding.

Mitigation: Prefer the Maton CLI and avoid raw-HTTP writes until the documented JSON/form-encoding inconsistency is corrected.

## Reference(s):

- [ClawHub Stripe skill release](https://clawhub.ai/byungkyu/skills/stripe-api)
- [Maton homepage](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Stripe API reference](https://docs.stripe.com/api)
- [Stripe event triggers](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit approval for changes.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
