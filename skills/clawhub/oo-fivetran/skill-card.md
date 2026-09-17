## Description:

Use this skill to search and read Fivetran data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect live Fivetran action schemas and retrieve hybrid deployment agents, log services, and transformation projects from their connected Fivetran account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the required oo CLI.

Mitigation: Do not let the agent run installer commands automatically; install the CLI only from a trusted and verified source and version.

Risk: A Fivetran/OOMOL connection can expose account data if it is over-scoped.

Mitigation: Use a connection scoped to the minimum access needed and review requested actions before execution.

## Reference(s):

- [Fivetran homepage](https://fivetran.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Fivetran connection](https://console.oomol.com/app-connections?provider=fivetran)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit oo CLI commands and JSON connector responses; setup commands should only be suggested after CLI, authentication, connection, or billing errors.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
