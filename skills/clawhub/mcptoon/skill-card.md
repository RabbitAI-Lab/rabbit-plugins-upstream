## Description:

Helps agents use mcptoon to browse and call MCP tools with a smaller tool catalog and manage shared skill catalogs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to discover and call MCP tools with less catalog overhead, troubleshoot compressed results, and synchronize skill catalogs across agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gateway setup can reroute existing MCP servers and change agent configuration.

Mitigation: Preview changes before takeover and use mcptoon restore to undo routing edits; uninstalling the CLI alone does not restore them.

Risk: Compact exposure hides upstream tools from the host's tool listing.

Mitigation: Use the manifest to find callable tools, or switch exposure to full when the host requires a populated tool panel.

Risk: Result compression may omit details needed to interpret a tool response.

Mitigation: Retrieve the original result by handle, or disable compression when full results are required.

Risk: Installing a CLI or plugin from an unexpected publisher or package index may be unsafe.

Mitigation: Verify the package or plugin publisher before installing.

## Reference(s):

- [mcptoon on ClawHub](https://clawhub.ai/activeing123/skills/mcptoon)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include steps to retrieve original tool results or restore agent configuration.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
