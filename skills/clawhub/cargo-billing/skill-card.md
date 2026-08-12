## Description:

Pull usage metrics, check subscription status, view invoices, and manage credits using the Cargo CLI. Use when the user wants billing analytics, usage reports, credit usage, cost analysis, subscription details, or invoice history for their Cargo workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and workspace administrators use this skill to analyze Cargo usage and credits, review subscriptions and invoices, and open billing self-service workflows through the Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing and usage commands require admin access and can reveal subscription, invoice, credit-card, usage, and portal-session information.

Mitigation: Install only for users who should administer Cargo billing, verify credentials with the Cargo CLI before use, and avoid portal or workflow-run commands unless the billing or usage impact is intended.

Risk: The skill depends on the external Cargo CLI package and its authentication state.

Mitigation: Review the Cargo CLI package source and trust posture separately when your environment requires pinned or pre-approved dependencies.

## Reference(s):

- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Usage metrics examples](references/examples/usage-metrics.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and admin workspace access; commands may return billing, usage, invoice, credit-card, and portal-session data.]

## Skill Version(s):

1.0.3 (source: frontmatter, skill-metadata.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
