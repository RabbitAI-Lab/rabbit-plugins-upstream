## Description:

Danube helps agents discover and use an organization's connected tools and service catalog through MCP or HTTP, with consent before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to find, inspect, and run tools from their organization's connected services and Danube's catalog, subject to permissions and user approval for consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to save persistent parameter defaults without first asking, which can change later tool calls or replace existing defaults.

Mitigation: Require approval before saving defaults; show the full replacement object and review existing defaults first.

Risk: A Danube API key can grant access to connected services beyond the intended task.

Mitigation: Use a restricted API key scoped to the needed services; prefer it over OAuth when least privilege matters.

Risk: Tool calls can write, send, spend, delete, or store credentials.

Mitigation: Show the exact action and parameters and obtain explicit user approval before execution or credential storage.

## Reference(s):

- [Danube skill on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with API examples and summarized tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool access requires a Danube API key and curl or an MCP client.]

## Skill Version(s):

8.1.35 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
