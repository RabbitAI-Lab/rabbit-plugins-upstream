## Description:

Governed tool access for your agent - one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover, inspect, and execute Danube-hosted tools over MCP or REST while preserving confirmation gates for actions that write, send, spend, delete, store credentials, or run batches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill brokers access to services connected to a user's Danube account or organization, including actions that may write, send, spend, delete, or store credentials.

Mitigation: Use the narrowest Danube API key and service permissions available, inspect the exact tool and parameters, and require explicit user confirmation before high-impact or batch execution.

Risk: Credential values may be pasted by the user or returned unmasked by tools whose purpose is to create or hand off credentials.

Mitigation: Prefer dashboard or OAuth setup where possible, treat any unmasked credential as a live secret, avoid echoing it back, and rotate it if exposed.

Risk: External tool output can be truncated, redacted, or projected through a path that matched nothing, which can make results look incomplete or empty.

Mitigation: Check truncation, redaction, and path-match metadata before acting on results; fetch stored results or adjust requested fields instead of assuming the upstream tool failed.

## Reference(s):

- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube API Reference](https://docs.danubeai.com/api-reference/introduction)
- [Danube over plain HTTP](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)
- [ClawHub Danube Skill](https://clawhub.ai/preston-thiele/skills/danube)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DANUBE_API_KEY and curl; recommends explicit user confirmation before high-impact actions.]

## Skill Version(s):

8.1.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
