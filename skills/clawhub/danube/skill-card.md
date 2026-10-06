## Description:

Gives agents governed access to an organization's tools and a service catalog through Danube, with tool discovery and execution over MCP or curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use Danube to find, inspect, and run connected organization and third-party tools, with confirmation before actions that change data or spend funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with a Danube key can access connected services more broadly than intended.

Mitigation: Use a restricted API key and confirm that its permissions are appropriate before enabling tool execution.

Risk: The skill automatically retrieves personal and organization context.

Mitigation: Review whether automatic context retrieval is acceptable for your organization before installation.

Risk: Service defaults may be saved without a separate prompt, and credential storage can grant further access.

Mitigation: Review saved service defaults and credential storage prompts before allowing broad tool execution.

## Reference(s):

- [Danube on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with curl commands and tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected tools and the API key's permissions.]

## Skill Version(s):

8.1.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
