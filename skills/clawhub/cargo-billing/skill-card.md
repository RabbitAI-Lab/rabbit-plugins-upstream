## Description:

Helps users review Cargo credit balances, usage, subscriptions, invoices, and payment methods.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators use this skill to check Cargo spending and remaining credits, investigate usage by resource, review subscription and invoice information, and manage a payment method.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A mutable latest-version CLI has admin access to billing and payment settings.

Mitigation: Install only from a trusted Cargo CLI package source and pin a reviewed version before using billing commands.

Risk: Entering payment-card details as command-line flags may expose them in shell history or process listings.

Mitigation: Prefer the hosted payment form or the CLI's standard-input option; do not place card details in command-line arguments.

## Reference(s):

- [Cargo Billing on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-billing)
- [Cargo skill homepage (declared in metadata)](https://github.com/getcargohq/cargo-skills)
- [Usage metrics examples](references/examples/usage-metrics.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Billing answers depend on the selected workspace and the data returned by the Cargo CLI.]

## Skill Version(s):

2.0.1 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
