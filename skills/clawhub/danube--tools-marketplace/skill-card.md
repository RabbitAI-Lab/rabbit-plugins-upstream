## Description:

Helps agents discover, inspect, and use an organization's tools and Danube's service catalog through MCP or curl, with user confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use Danube to find and run connected services and organizational tools, while seeking approval before actions that change data or incur costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may use connected tools to write, send, spend, delete, or run batches without the user's intent.

Mitigation: Show the exact tool and inputs and obtain explicit user confirmation before each consequential action or batch.

Risk: Exposed credentials could allow unauthorized use of the Danube account or connected services.

Mitigation: Keep the Danube API key secret and use dashboard or OAuth connections for sensitive service credentials where available.

Risk: Saved defaults, context, wallet settings, or spending limits may change future agent behavior or costs.

Mitigation: Confirm changes before making them and review saved settings in the Danube dashboard.

## Reference(s):

- [Danube OpenClaw documentation](https://docs.danubeai.com/sdk/openclaw)
- [Danube skill release](https://clawhub.ai/danube/skills/tools-marketplace)
- [REST API reference](artifact/references/rest-api.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with commands and tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool availability and results depend on account permissions and connected services.]

## Skill Version(s):

8.1.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
