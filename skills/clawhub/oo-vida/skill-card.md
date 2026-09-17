## Description:

Vida (vida.io) helps agents operate Vida through an OOMOL-connected account for searching and reading account, usage, task, and task-statistics data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Vida action schemas and run read-oriented Vida connector actions through the OOMOL oo CLI. It is intended for retrieving Vida account details, usage counts, tasks, task statistics, and filtered task lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes remote shell installer commands for the oo CLI.

Mitigation: Prefer official package-manager or signed-release installation steps, verify the installer before running it, and avoid executing remote installer scripts automatically or from an elevated shell.

Risk: Connector actions depend on the live Vida action schema and authenticated OOMOL account state.

Mitigation: Inspect the live schema before constructing requests and only use first-time setup or reconnection steps after a command fails with the matching authentication, connection, scope, or billing error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-vida)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Vida Homepage](https://vida.io/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch live action schemas before constructing connector requests.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
