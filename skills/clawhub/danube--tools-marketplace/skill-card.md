## Description:

Connects agents to an organization's tools and a catalog of services through Danube using MCP or curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can discover, inspect, and run organization-connected and catalog tools through Danube, with consent before consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad account access can enable changes to tools, credentials, organization settings, workflows, and wallets.

Mitigation: Use a restricted dashboard-created API key with allowed services and tools, and enable confirmation.

Risk: OAuth scopes, Personal workspace selection, and tool-list filters do not reliably limit permissions.

Mitigation: Do not treat these controls as permission boundaries; restrict the key and review requests before approving writes, spending, or other sensitive actions.

## Reference(s):

- [Danube skill on ClawHub](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API guide](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown and JSON tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Danube API key; available tools and results depend on account access.]

## Skill Version(s):

8.1.27 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
