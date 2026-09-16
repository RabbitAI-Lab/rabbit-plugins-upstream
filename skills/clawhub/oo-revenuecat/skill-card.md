## Description:

RevenueCat helps agents search and read RevenueCat customers, subscriptions, entitlements, offerings, products, projects, and revenue metrics through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve RevenueCat account, subscription, entitlement, offering, product, project, and revenue data through the OOMOL oo CLI after the account connection is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents mutable remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Install the oo CLI only from independently trusted OOMOL distribution channels, and prefer pinned releases, checksums, or signatures before executing installers.

Risk: Connector calls can expose RevenueCat account and revenue data through an OOMOL-connected account.

Mitigation: Use least-privilege RevenueCat credentials, inspect the live action schema before each payload, and confirm any action tagged write or destructive before execution.

## Reference(s):

- [RevenueCat homepage](https://www.revenuecat.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub RevenueCat skill](https://clawhub.ai/oomol/skills/oo-revenuecat)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
