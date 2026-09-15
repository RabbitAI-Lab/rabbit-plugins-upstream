## Description:

Operate SamCart through an OOMOL-connected account to retrieve and list customers, orders, products, and subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect SamCart connector schemas and run supported SamCart customer, order, product, and subscription actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute remote installer scripts directly.

Mitigation: Review the setup path before installing and prefer a verified, versioned, signed package or inspect the installer before execution.

Risk: The skill can access SamCart customer, order, product, and subscription data through the connected OOMOL account.

Mitigation: Confirm the account connection, requested action, and payload before exposing sensitive marketplace data.

Risk: Scope language is broader than the listed actions and future connector actions could become write-capable.

Mitigation: Inspect the live action schema and confirm any write-capable connector action with the user before use.

## Reference(s):

- [ClawHub SamCart skill page](https://clawhub.ai/oomol/skills/oo-samcart)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [SamCart homepage](https://www.samcart.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
