## Description:

Waffo Pancake helps agents read, create, and update Waffo Pancake data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to manage Waffo stores, products, checkout sessions, payments, refunds, subscriptions, orders, and analytics through a connected Waffo account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote installer scripts.

Mitigation: Use official signed or version-pinned installation instructions where possible, inspect installers before execution, and avoid elevated privileges.

Risk: Write actions can change real Waffo account state, including publishing products, creating refunds, creating checkout sessions, and canceling subscriptions.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any write action.

## Reference(s):

- [Waffo Pancake homepage](https://www.waffo.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-waffo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to inspect live connector schemas and execute read or write Waffo actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
