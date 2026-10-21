## Description:

Governed tool access for your agent — one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services. Search, inspect, and execute tools over native MCP or plain curl, with explicit confirmation before anything that writes, sends, spends, or deletes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use Danube to discover and inspect available services, then invoke organization-connected tools through MCP or curl. The skill guides agents through setup, API use, and confirmation before sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Settings may be saved or replaced without approval.

Mitigation: Require explicit approval before saving or replacing defaults.

Risk: Scheduled actions may recur and exceed the initiating API key's restrictions; authors and editors may affect their inputs.

Mitigation: Use a dedicated restricted API key and leave schedules disabled unless you accept the recurring actions, author-level access, and who can edit their inputs.

## Reference(s):

- [Danube OpenClaw documentation](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, configuration examples, and API request and response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

8.1.40 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
