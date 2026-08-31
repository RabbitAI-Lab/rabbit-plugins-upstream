## Description:

Governed tool access for your agent - one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover, inspect, and execute Danube-connected tools through MCP or REST while preserving explicit confirmation for actions that write, send, spend, delete, store credentials, or run batches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent use a Danube account to run connected tools that may change data, send messages, spend funds, or store credentials.

Mitigation: Review Danube permissions, spending limits, and connected services, and approve execution only after the agent shows the exact tool and parameters.

Risk: The visible tool catalog can change and may include private organizational tools, so cached assumptions or stale tool IDs can lead to incorrect execution attempts.

Mitigation: Search and inspect the current tool schema before execution, and pass only the parameters needed for the user's requested task.

## Reference(s):

- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube Documentation](https://docs.danubeai.com)
- [Danube REST API Reference](references/rest-api.md)
- [Danube Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with bash commands, JSON snippets, and API call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to search before execution and to request explicit confirmation before state-changing, spending, credential-storage, or batch actions.]

## Skill Version(s):

8.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
