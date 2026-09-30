## Description:

Helps agents discover, inspect, and use an organization's connected tools and Danube's service catalog through MCP or REST with confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to find and run their organization's tools and third-party services through a governed Danube connection, while reviewing sensitive actions before approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key grants access to connected services and organization tools.

Mitigation: Install only if you trust Danube with that access, and use a scoped API key where possible.

Risk: Tool calls can write, send, spend, or delete data.

Mitigation: Review the exact proposed action and parameters before explicitly approving it.

Risk: Recurring non-secret defaults, such as team IDs, may be saved after successful calls.

Mitigation: Check proposed parameters and avoid including unnecessary personal or sensitive data.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [REST API reference](references/rest-api.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Conversational text and Markdown, including tool results and example commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results depend on the connected service; consequential actions require user confirmation.]

## Skill Version(s):

8.1.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
