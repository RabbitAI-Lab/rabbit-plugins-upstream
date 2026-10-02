## Description:

Connects agents to an organization's tools and a catalog of services through Danube, with search, inspection, and execution over MCP or curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Danube to discover, inspect, and invoke approved services and organization-connected tools through one API key. Side-effecting actions require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key can grant access to high-impact external and organization-connected tools.

Mitigation: Use the narrowest suitable key and organization permissions, and require explicit approval before writes, sends, spending, deletions, or credential changes.

Risk: The skill advises saving reusable tool parameter defaults without asking first, creating a persistent change.

Mitigation: Review and approve saved defaults before they are stored, or disable that behavior operationally.

## Reference(s):

- [ClawHub release](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](artifact/references/rest-api.md)
- [Troubleshooting reference](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses can be truncated; inspect truncation indicators before interpreting results.]

## Skill Version(s):

8.1.22 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
