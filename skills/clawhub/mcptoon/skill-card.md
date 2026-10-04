## Description:

Helps agents discover and call MCP tools through a compact catalog, manage shared skill catalogs, and configure a gateway across supported agent clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to navigate large MCP tool catalogs, call the tools they need, and manage tool and skill availability across agent clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gateway setup can change agent configurations and route existing MCP servers through mcptoon.

Mitigation: Preview configuration changes with dry-run options, confirm the package publisher, and keep the documented restore command available.

Risk: Compact exposure hides upstream tools from some agent tool lists, and result compression may obscure details.

Mitigation: Use the manifest to find callable tools, switch to full exposure if a visible tool list is needed, and retrieve the original result or disable compression when details matter.

## Reference(s):

- [mcptoon on ClawHub](https://clawhub.ai/activeing123/skills/mcptoon)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides users to inspect tools before calling them and retrieve original results when compression obscures details.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
