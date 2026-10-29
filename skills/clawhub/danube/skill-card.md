## Description:

Governed tool access for your agent — one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services. Search, inspect, and execute tools over native MCP or plain curl, with explicit confirmation before anything that writes, sends, spends, or deletes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Danube to discover available organizational and catalog tools, inspect their schemas, and carry out requested operations through MCP or REST/curl. It supports permission-aware access, spending limits, and an audit trail for connected services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that settings may be saved without permission.

Mitigation: Get approval before saving defaults, and confirm their scope and complete replacement values.

Risk: The security review reports scheduled actions that may exceed API-key restrictions.

Mitigation: Use a restricted API key and organization policies; avoid scheduling sensitive actions until execution permissions and input changes are verified.

Risk: Credentials or other unnecessary sensitive data could be exposed while using connected services.

Mitigation: Provide only credentials and data needed for the task.

## Reference(s):

- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API Reference](references/rest-api.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Organization Internal Tools Guide](https://docs.danubeai.com/organizations/internal-tools)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration]

**Output Format:** [Markdown guidance with MCP tool calls and shell/curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by requested service and operation; state-changing actions require explicit user confirmation.]

## Skill Version(s):

8.1.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
