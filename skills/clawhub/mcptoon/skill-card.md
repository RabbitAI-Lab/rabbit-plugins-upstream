## Description:

Helps agents discover and call MCP tools through a compact catalog and manage skill catalogs across agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use mcptoon to find and call MCP tools without loading an entire tool catalog, and to manage skills across agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can reroute existing MCP servers through a gateway and change agent configuration.

Mitigation: Review proposed configuration changes, use dry-run or backup-aware setup, and use mcptoon restore to reinstate previous server entries.

Risk: Compact tool exposure can make upstream tools appear missing from an agent's tool list.

Mitigation: Use the manifest to find callable tools, or switch exposure to full if the host needs to show the complete list.

Risk: Automatic result compression can omit details from the agent-visible response.

Mitigation: Retrieve the original result by its handle, set individual tools to raw, or disable compression when full results are needed.

## Reference(s):

- [mcptoon on ClawHub](https://clawhub.ai/activeing123/skills/mcptoon)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include steps for inspecting tools, retrieving original results, and restoring agent configuration.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata; artifact frontmatter states 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
