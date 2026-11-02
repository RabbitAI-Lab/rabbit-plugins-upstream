## Description:

Helps Cargo workspace admins review credit balances, usage, subscriptions, invoices, and payment methods.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cargo workspace admins use this skill to understand credit consumption, inspect usage by workflow or connector, check subscription and invoice details, estimate costs, and manage payment methods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cost-estimation instructions start a real sample workflow that may consume credits and trigger downstream actions without separate approval.

Mitigation: Require separate approval for the sample workflow, its inputs, credit cost, and downstream actions; prefer historical usage for estimates.

Risk: Billing and payment operations use privileged workspace credentials and can involve sensitive payment details.

Mitigation: Limit reporting credentials to billing reads and use the hosted form for payment details.

Risk: The install metadata selects the latest CLI release, which may change over time.

Mitigation: Pin a reviewed CLI version.

## Reference(s):

- [Cargo Skills homepage](https://github.com/getcargohq/cargo-skills)
- [cargo-billing on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-billing)
- [Usage metrics examples](references/examples/usage-metrics.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown instructions with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.1.3 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
