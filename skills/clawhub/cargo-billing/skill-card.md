## Description:

Helps agents inspect Cargo billing, credit usage, subscription status, invoice history, and payment-method workflows through the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cargo workspace administrators and operators use this skill to answer billing and budget questions, estimate run costs, review invoices, and manage the workspace payment method with admin credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates on Cargo workspace billing and requires admin-level billing authority.

Mitigation: Install only where the agent is intended to have admin billing access, and confirm the active workspace with `cargo-ai whoami` before making changes.

Risk: Payment card details may be exposed if passed directly as command-line flags.

Mitigation: Prefer the hosted Stripe portal or `--card-stdin`, and avoid passing real card numbers in shell command arguments.

Risk: Billing and usage decisions can affect workspace spend.

Mitigation: Check current credits and estimate usage from a sample run before triggering large batches.

## Reference(s):

- [Cargo skill page](https://clawhub.ai/cargo-ai/skills/cargo-billing)
- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Usage metrics examples](references/examples/usage-metrics.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Cargo CLI shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require the Cargo CLI and an admin-capable Cargo workspace token; payment-method updates should prefer the hosted Stripe portal or card data via stdin.]

## Skill Version(s):

1.1.0 (source: frontmatter, skill-metadata.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
