## Description:

Connects agents to an organization's tools and a catalog of services through Danube, with discovery and consent before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to discover and invoke approved organizational and catalog tools via MCP or curl, while seeking consent for writes and other consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single Danube key can expose broad access to remote tools, credentials, workflows, context, and spending functions.

Mitigation: Use a least-privilege key and grant access only to services and capabilities the agent needs.

Risk: Tool calls may write, send, spend, or delete data.

Mitigation: Keep confirmation enabled and review the exact tool and parameters before approving each consequential action.

Risk: The skill may save reusable service identifiers as defaults without asking first.

Mitigation: Review saved parameter defaults and remove identifiers that should not persist.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](artifact/references/rest-api.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses depend on the connected services and permissions.]

## Skill Version(s):

8.1.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
