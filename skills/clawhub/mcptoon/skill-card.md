## Description:

Guides agents in using the mcptoon CLI to find and call MCP tools efficiently, manage skill catalogs, and navigate large documentation folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to discover and call MCP tools with less catalog overhead, manage skills across agents, and locate relevant documentation without reading entire folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted package or changing MCP and skill configurations without review could affect the local agent setup.

Mitigation: Confirm the package source and approve installation and configuration changes; use a pinned version when reproducibility matters.

Risk: Routing servers through a gateway or syncing and removing skills may hide tools or change existing agent configuration.

Mitigation: Preview changes with dry-run or read-only checks, review removals, and use restore when undoing gateway takeover.

Risk: Compressed tool results may omit details needed for a task.

Mitigation: Retrieve the original result by its handle or turn off compression for the affected tool or session.

## Reference(s):

- [mcptoon on ClawHub](https://clawhub.ai/activeing123/skills/mcptoon)
- [Publisher profile](https://clawhub.ai/user/activeing123)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and tool availability depend on the installed CLI and local agent configuration.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; skill frontmatter states 1.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
