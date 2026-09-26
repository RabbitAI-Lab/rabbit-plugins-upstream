## Description:

Gives agents governed access to an organization's tools and connected services through Danube, with user confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Danube to discover and run organizational and connected-service tools over MCP or curl, subject to permissions, spending limits, and explicit consent for actions that change state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key can indirectly grant broad access to connected services, organizational tools, profiles, wallets, workflows, and credentials.

Mitigation: Use a Danube API key scoped to the agent's intended tasks and share only necessary task data.

Risk: Agent actions may write, send, spend, delete, store credentials, or change skills and workflows.

Mitigation: Show the exact tool and parameters and obtain explicit user approval before each consequential action.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)
- [ClawHub release](https://clawhub.ai/preston-thiele/skills/danube)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Tool results]

**Output Format:** [Markdown with inline shell commands and structured JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Danube API key; available tools and their responses depend on connected services.]

## Skill Version(s):

8.1.14 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
