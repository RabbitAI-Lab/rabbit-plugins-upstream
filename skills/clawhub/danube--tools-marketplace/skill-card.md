## Description:

Helps agents discover, inspect, and run organization and catalog tools through Danube using MCP or curl, with confirmation for consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to find and run tools available to their organization, with permission checks and user confirmation before consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube API key can grant broad access to connected tools, credentials, workflows, skills, wallet actions, and organization context.

Mitigation: Install only when you trust Danube with the connected account; use an account and key with appropriate permissions.

Risk: Tool calls can write or delete data, spend funds, store credentials, or affect third-party services.

Mitigation: Review the exact tool and parameters and require explicit user consent before consequential actions; inspect each confirmation prompt before proceeding.

## Reference(s):

- [Danube OpenClaw documentation](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API reference](references/rest-api.md)
- [Danube troubleshooting](references/troubleshooting.md)
- [Danube skill on ClawHub](https://clawhub.ai/danube/skills/tools-marketplace)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Natural-language guidance with shell commands and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available tools and responses depend on the connected account and its permissions.]

## Skill Version(s):

8.1.24 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
