## Description:

Governed tool access for your agent - one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services for search, inspection, and execution over MCP or curl, with explicit confirmation before anything that writes, sends, spends, or deletes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to let an AI agent discover, inspect, and call Danube-connected organization tools and catalog services through MCP or REST. It supports governed execution workflows that require confirmation before write, send, spend, delete, credential-storage, or batch actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad access to external and organization tools, including actions that can write, send, spend, delete, store credentials, or run batches.

Mitigation: Require explicit user confirmation with the exact tool and parameters before any high-impact action, and report the executed tool, inputs, and returned result afterward.

Risk: A Danube API key grants access to the user's configured Danube tools and should be treated as sensitive.

Mitigation: Keep DANUBE_API_KEY secret, store only credentials the user explicitly provides and confirms, and avoid exposing or validating key contents beyond checking that a key exists.

Risk: The available tool catalog can change and tool IDs can become stale, which may lead to incorrect assumptions about available capabilities.

Mitigation: Search and inspect current tool schemas before execution, ask for missing required parameters, and do not reuse tool IDs from memory.

Risk: Connected third-party services may receive unnecessary sensitive data if the agent forwards more context than the task requires.

Mitigation: Use least-data parameter construction and send only the fields required for the selected tool call.

## Reference(s):

- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube Documentation](https://docs.danubeai.com)
- [Danube REST API Reference](artifact/references/rest-api.md)
- [Danube Troubleshooting](artifact/references/troubleshooting.md)
- [Danube ClawHub Skill Page](https://clawhub.ai/danube/skills/tools-marketplace)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and REST or MCP call patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include tool discovery results, exact tool names and parameters for user approval, execution summaries, configuration snippets, and troubleshooting steps.]

## Skill Version(s):

8.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
