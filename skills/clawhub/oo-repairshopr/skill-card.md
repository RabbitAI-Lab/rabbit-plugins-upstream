## Description:

RepairShopr helps agents search and read RepairShopr account, customer, and ticket data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support operations teams use this skill to retrieve RepairShopr user, account, customer, and ticket information through the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI from a verified official release or package manager with integrity checks, and avoid piping remote scripts directly into a shell.

Risk: The RepairShopr connection can read customer, ticket, user, and account data.

Mitigation: Confirm that the connected OOMOL RepairShopr account should have access to this data before using the skill.

## Reference(s):

- [RepairShopr homepage](https://www.repairshopr.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-repairshopr)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
