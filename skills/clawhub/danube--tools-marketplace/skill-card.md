## Description:

Guides agents to discover and use Danube's catalog and organization tools over MCP or curl, with user confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Danube to find, inspect, and run connected services and an organization's own tools, subject to user approval for actions that change data or spend funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saving service defaults without asking can make lasting account changes.

Mitigation: Require explicit user approval before saving defaults and periodically review saved defaults in the Danube dashboard.

Risk: Connected tools can store credentials, manage skills or workflows, and spend funds.

Mitigation: Use a restricted API key where possible, confirm each consequential action, and review connected services and account settings.

## Reference(s):

- [Danube skill release](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell examples and tool-result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connected tool results vary by service; seek user approval before state-changing actions.]

## Skill Version(s):

8.1.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
