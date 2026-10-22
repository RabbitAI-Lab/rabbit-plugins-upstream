## Description:

Governed tool access for your agent — one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services. Search, inspect, and execute tools over native MCP or plain curl, with explicit confirmation before anything that writes, sends, spends, or deletes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use Danube to discover and operate organization-connected services through MCP or HTTP API calls. The skill provides setup, tool-selection, and troubleshooting guidance for reading data and carrying out approved actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may save settings that affect future actions without obtaining approval first.

Mitigation: Require confirmation before saving defaults, review their exact scope, and preserve existing settings.

Risk: OAuth scope requests do not narrow access as the skill's guidance might suggest.

Mitigation: Do not rely on requested OAuth scopes to restrict access; use an API key restricted to the services needed.

Risk: Scheduled workflows may use the author's credentials beyond the scheduling key's restrictions.

Mitigation: Review which credentials scheduled workflows use and limit the services available to those credentials.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube API reference](https://docs.danubeai.com/api-reference/introduction)
- [REST API reference in skill package](references/rest-api.md)
- [Troubleshooting guide in skill package](references/troubleshooting.md)
- [Danube skill release](https://clawhub.ai/preston-thiele/skills/danube)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown guidance with inline shell examples, MCP configuration, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Danube API key supplied through DANUBE_API_KEY; examples support MCP and curl.]

## Skill Version(s):

8.1.41 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
