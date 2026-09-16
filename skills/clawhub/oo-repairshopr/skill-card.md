## Description:

RepairShopr connector for reading RepairShopr user, account, customer, and ticket data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect RepairShopr account, customer, and ticket records through an OOMOL-connected RepairShopr account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Review the installer path first and prefer a version-pinned, verifiable oo CLI release or a trusted package manager; do not let an agent run the remote installer automatically.

Risk: RepairShopr customer, ticket, user, and account data may be routed through OOMOL-connected tooling.

Mitigation: Confirm that this data flow matches account policy and data-handling expectations before using the connector.

## Reference(s):

- [ClawHub RepairShopr skill page](https://clawhub.ai/oomol/skills/oo-repairshopr)
- [RepairShopr homepage](https://www.repairshopr.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented RepairShopr connector actions with paginated list support]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
