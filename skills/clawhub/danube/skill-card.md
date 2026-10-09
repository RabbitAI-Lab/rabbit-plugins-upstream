## Description:

Helps agents discover, inspect, and use an organization's Danube tools and service catalog through MCP or HTTP, with confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can connect to Danube to find and run authorized organizational and catalog tools while reviewing actions that change data or spend funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A key may expose broad access to organizational and catalog tools.

Mitigation: Use a dashboard-created key limited to necessary services and tools, with confirmation requirements enabled.

Risk: Actions can write, send, spend, store credentials, or persist changes to workflows and settings.

Mitigation: Review the exact action and parameters and require explicit user confirmation, including for saved defaults.

Risk: A guessed tool name may run a different tool than intended.

Mitigation: Use exact tool UUIDs or verified slugs and check the executed tool identity before trusting results.

Risk: Discovery can reveal private context, internal skills, wallet metadata, and past examples.

Mitigation: Limit the key's access and avoid exposing discovery results beyond the intended user and organization.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API reference](references/rest-api.md)
- [Danube troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tool discovery results and suggested execution parameters.]

## Skill Version(s):

8.1.29 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
