## Description:

Governed tool access for your agent - one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover, inspect, and call Danube-hosted tools through MCP or REST while preserving user confirmation for writes, spending, credential storage, and other sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can reach tools connected to the user's Danube account, including tools that may write, send, spend, delete, or store credentials.

Mitigation: Keep confirmation enabled for destructive, paid, batch, credential-storage, and write actions, and review the exact tool and parameters before execution.

Risk: The skill requires a Danube API key and can access services available to that key.

Mitigation: Use a scoped Danube key where possible, store it securely, and install the skill only when the publisher and connected services are trusted.

Risk: Credentials or credential-like values may be handled during service setup or tool responses.

Mitigation: Prefer dashboard or OAuth setup, avoid giving raw credentials to the agent unless intentional, and do not echo unmasked secrets into later calls.

## Reference(s):

- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube Documentation](https://docs.danubeai.com)
- [Danube Dashboard](https://danubeai.com/dashboard)
- [Danube REST API Reference](references/rest-api.md)
- [Danube Troubleshooting](references/troubleshooting.md)
- [Danube ClawHub Listing](https://clawhub.ai/danube/skills/tools-marketplace)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON request or response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require DANUBE_API_KEY and curl; tool execution can return JSON, text, execution identifiers, redaction metadata, confirmation tokens, or error objects.]

## Skill Version(s):

8.1.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
