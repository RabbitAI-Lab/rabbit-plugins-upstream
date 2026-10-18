## Description:

Guides agents in discovering and using an organization's tools and Danube's service catalog through MCP or HTTP, with consent before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to find, inspect, and call connected services and organization tools while managing access, credentials, and approvals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad tool access may expose connected services to unintended actions or data sharing.

Mitigation: Use a restricted API key with allowed services and tools; review connected-app access and share only task-required data.

Risk: Writes, spending, credential storage, and persistent or scheduled workflows can have lasting effects.

Mitigation: Require explicit user approval before these actions, and inspect saved defaults and workflow permissions in the Danube dashboard.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API reference](references/rest-api.md)
- [Danube troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool calls may require credentials and explicit user confirmation.]

## Skill Version(s):

8.1.37 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
