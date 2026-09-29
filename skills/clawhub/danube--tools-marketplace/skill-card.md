## Description:

Danube helps agents discover, inspect, and use an organization's tools and catalog services through MCP or curl with a Danube API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to find, inspect, and run available organization and catalog tools, with consent before actions that change data or spend funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube API key can authorize access to external tools and spending.

Mitigation: Scope the API key narrowly and review wallet balances and spending limits before use.

Risk: Tool actions can write, send, spend, delete, or change credentials, workflows, and skills.

Mitigation: Get explicit approval for each action after showing the exact tool and parameters, including batch actions.

Risk: Saving service defaults can persist settings without sufficient consent.

Mitigation: Do not save defaults until the user approves the exact value and persistence scope.

## Reference(s):

- [Danube ClawHub release](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube API keys](https://danubeai.com/dashboard/api-keys)
- [REST API recipes](artifact/references/rest-api.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples and tool execution summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Danube API key and curl or an MCP client for tool access.]

## Skill Version(s):

8.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
