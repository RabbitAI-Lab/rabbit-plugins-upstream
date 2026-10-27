## Description:

Helps agents review Cargo credits, usage, subscriptions, invoices, and payment methods through the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to check credit balances, analyze usage and invoices, estimate costs, and manage billing settings with appropriate permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing commands require administrative access and can change a workspace's payment method.

Mitigation: Grant only necessary billing permissions and obtain explicit user approval before payment changes or billing-management sessions.

Risk: Installing the unpinned external CLI may execute an unreviewed version.

Mitigation: Use a pinned, reviewed Cargo CLI version from a trusted source.

Risk: Entering card details in command-line flags can expose them in shell history or process listings.

Mitigation: Prefer the hosted Stripe form or stdin flow for card entry; do not place card details in command-line arguments.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Billing response shapes](artifact/references/response-shapes.md)
- [Usage metrics examples](artifact/references/examples/usage-metrics.md)
- [Billing troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with Cargo CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Billing results depend on the active workspace and its permissions.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
