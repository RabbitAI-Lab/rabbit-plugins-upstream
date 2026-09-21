## Description:

mcptoon helps agents compress MCP tool discovery, inspect and call MCP tools, and manage skill catalogs with the mcptoon CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an MCP tool catalog is large, when they need efficient tool discovery and calls, or when they need to manage one skill catalog across multiple agent views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide users toward persistent actions such as syncing, removing, archiving, tombstoning, or staging skill files.

Mitigation: Use dry-run or sandbox views first, review the planned changes, and run persistent catalog commands deliberately.

Risk: Installing or upgrading the mcptoon CLI gives it a role in MCP tool discovery and skill catalog management.

Mitigation: Review the PyPI publisher or package index before installing, confirm upgrades manually, and uninstall the CLI or remove its config if it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/activeing123/skills/mcptoon)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and command tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend dry-run or sandbox execution before persistent catalog changes.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
