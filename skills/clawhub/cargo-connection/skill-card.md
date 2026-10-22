## Description:

Connect Cargo to external systems by authenticating connectors, browsing the integration catalog, and finding the connector and action identifiers needed for workflow nodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to authenticate and inspect Cargo connectors, discover supported integrations and actions, and configure workflow nodes with the required connector identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deletion guidance may affect dependent workflows, tools, or models without clearly requiring approval.

Mitigation: Require explicit authorization for each affected item, check dependencies first, and prefer migrating references or preserving recoverable configurations.

Risk: Connector setup and troubleshooting may involve credentials or sensitive connector output.

Mitigation: Use narrowly scoped credentials, protect connector output, and choose a reviewed CLI version.

## Reference(s):

- [Cargo Connection skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-connection)
- [Project homepage (skill metadata)](https://github.com/getcargohq/cargo-skills)
- [Connector examples](references/examples/connectors.md)
- [Integration examples](references/examples/integrations.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Configuration guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workspace-specific connector identifiers and configuration examples; never expose live secrets.]

## Skill Version(s):

1.6.1 (source: server-resolved release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
