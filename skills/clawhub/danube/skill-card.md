## Description:

Helps agents discover and use an organization's tools and Danube's service catalog through MCP or HTTP, with user confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can discover, inspect, and invoke connected organization tools and third-party services using a Danube API key. The skill guides agents to seek approval before actions that change data, spend funds, or manage credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube connection can expose broad account and organization tool access.

Mitigation: Install only when that access is intended; prefer API keys restricted by allowed_services and allowed_tools.

Risk: OAuth scopes and tool-list filters do not enforce least privilege.

Mitigation: Do not treat OAuth scopes or ?tools= as permission boundaries; use restricted keys and review tool access.

Risk: Tools may change data, spend funds, store credentials, or change skills and workflows.

Mitigation: Review exact actions and obtain user approval before writes, spending, credential storage, and skill, workflow, or context changes.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [REST API guide](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results and actions depend on the user's connected services and permissions.]

## Skill Version(s):

8.1.28 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
