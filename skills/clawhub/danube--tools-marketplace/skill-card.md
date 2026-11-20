## Description:

Governed tool access for your agent — one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services. Search, inspect, and execute tools over native MCP or plain curl, with explicit confirmation before anything that writes, sends, spends, or deletes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use Danube to discover and call services connected to their organization through MCP or HTTP, while reviewing tool details and requiring explicit approval for consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports weak consent safeguards and potential permission-boundary issues, including concerns about confirmation, OAuth scope enforcement, and scheduled-run permissions.

Mitigation: Before connecting accounts or enabling scheduled runs, review granted scopes and permissions, and require explicit approval for consequential actions.

Risk: The security review is incomplete: obfuscated instruction text and unresolved references were not fully evaluated, and the binary image was outside analyzer scope.

Mitigation: Review unresolved references and unevaluated source content before installing or relying on the skill.

## Reference(s):

- [Danube OpenClaw documentation](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [Danube REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)
- [Danube ClawHub skill page](https://clawhub.ai/danube/skills/tools-marketplace)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration, Guidance, Text]

**Output Format:** [MCP tool calls or curl requests with structured service responses and concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available operations and response details depend on the connected services and the user's permissions.]

## Skill Version(s):

8.1.50 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
