## Description:

Cargo Billing helps agents answer Cargo credit, usage, subscription, invoice, and payment-method questions using the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and Cargo workspace admins use this skill to inspect spend, remaining credits, usage breakdowns, subscription state, invoices, and payment-method status. It is intended for users who can grant an agent admin-level Cargo billing access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Admin billing access can expose workspace spend, subscription, invoice, and payment-method information.

Mitigation: Install only for billing work that requires admin access, use an admin Cargo token intentionally, and confirm the active workspace before payment or sample-run commands.

Risk: Passing real card details as command-line flags can expose them through shell history or process listings.

Mitigation: Prefer the Stripe hosted form or --card-stdin for card updates, and avoid passing real card details as command-line flags.

Risk: Cost estimates can be misleading when mixed usage units or execution charges are interpreted as the same quantity.

Mitigation: Use explicit --unit values for billing.credits, orchestration.executions, and storage.records, and include the execution charge when estimating batch costs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-billing)
- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Response shapes](artifact/references/response-shapes.md)
- [Usage metrics examples](artifact/references/examples/usage-metrics.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON response interpretation]

**Output Format:** [Markdown guidance with inline shell commands and JSON field references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and an admin Cargo token; billing commands return JSON.]

## Skill Version(s):

2.0.0 (source: frontmatter, release evidence, skill-metadata.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
