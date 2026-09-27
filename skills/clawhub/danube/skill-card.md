## Description:

Gives agents governed access to an organization's tools and a catalog of services through Danube, using MCP or curl to discover, inspect, and execute tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Danube to discover available organization and catalog tools, inspect their requirements, and execute authorized actions through MCP or REST with user confirmation for sensitive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may save reusable service defaults persistently without asking first.

Mitigation: Review the skill before installation and require user consent before persisting service defaults.

Risk: Broad API keys or disabled confirmation can expose sensitive tool actions.

Mitigation: Use narrowly scoped Danube keys and keep require_confirmation enabled where available.

Risk: Tool actions can store credentials, change spending, modify skills or workflows, or register organization services.

Mitigation: Show the exact action and parameters and obtain explicit user approval before proceeding.

## Reference(s):

- [Danube release on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

8.1.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
