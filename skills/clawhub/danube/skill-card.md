## Description:

Helps agents discover, inspect, and use an organization's connected tools and Danube's service catalog through MCP or HTTP, with confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to find and invoke connected organization tools and catalog services while checking permissions and seeking approval for actions that change data or spend funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connection may reach broad organization tools beyond the task at hand.

Mitigation: Use a deliberately scoped API key when least privilege matters and review connected account and organization access before use.

Risk: Tool access can change credentials, persist workflow or skill changes, or spend wallet funds.

Mitigation: Review credential storage, scheduling, funding, skill changes, and saved defaults; require explicit confirmation before writes, spending, sending, deletion, or long-running actions.

## Reference(s):

- [Danube OpenClaw documentation](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API reference](references/rest-api.md)
- [Danube troubleshooting guide](references/troubleshooting.md)
- [Danube skill release on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool invocations may return structured results; consequential actions require explicit user confirmation.]

## Skill Version(s):

8.1.39 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
