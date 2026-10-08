## Description:

Guides agents in using mcptoon to compact MCP tool discovery, manage shared skill catalogs, and find relevant documents without reading entire folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to navigate large MCP tool catalogs, manage skills across agents, and identify relevant documentation while conserving context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading an unexpected package could run untrusted code.

Mitigation: Verify the package publisher and source before installation; confirm upgrades before running them.

Risk: Quickstart or takeover can change agent MCP configuration and tool visibility.

Mitigation: Review configuration changes, preview with dry-run where available, and use restore to undo takeover or full exposure to show all tools.

Risk: Compressed tool results may omit details needed for an answer.

Mitigation: Retrieve the original result by handle or disable compression for the affected tool or session.

## Reference(s):

- [Mcptoon on ClawHub](https://clawhub.ai/activeing123/skills/mcptoon)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend MCP tool calls and document paths; does not itself create compressed tool results.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; artifact frontmatter lists 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
