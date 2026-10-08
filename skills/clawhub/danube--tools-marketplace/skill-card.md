## Description:

Helps agents discover and use an organization's tools and Danube's service catalog through MCP or HTTP, with guidance to confirm consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use Danube to find available organizational or catalog tools, inspect their capabilities, and perform authorized tasks through MCP or HTTP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may gain broad authority over connected services, including writes and spending.

Mitigation: Use a restricted Danube API key where possible and obtain explicit user confirmation before writes, purchases, spending, credential changes, or batch execution.

Risk: Saved service defaults can persist or select the wrong team, organization, or app without a separate confirmation.

Mitigation: Review saved defaults in the Danube dashboard and remove or correct any unintended selection.

Risk: OAuth connections and tool visibility filters do not necessarily restrict the agent's underlying permissions.

Mitigation: Do not treat filtered tool lists as access controls; prefer keys restricted to the required services or tools.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube HTTP reference](references/rest-api.md)
- [Danube troubleshooting](references/troubleshooting.md)
- [ClawHub skill release](https://clawhub.ai/danube/skills/tools-marketplace)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls]

**Output Format:** [Markdown responses with tool results and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the user's available tools, credentials, and service permissions.]

## Skill Version(s):

8.1.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
