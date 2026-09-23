## Description:

Find, connect, and use MCP tools and skills via the Smithery CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[javotillo](https://clawhub.ai/user/javotillo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to discover Smithery MCP servers, connect managed MCP sessions, scope service tokens, inspect tool schemas, and call external tools through the Smithery CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead agents toward external service installs, long-lived MCP connections, and tool calls without enough user intent confirmation.

Mitigation: Confirm the requested namespace, connection ID, token policy, permissions, and target tool before authorizing services or calling tools.

Risk: Connected tools may modify external data such as issues, messages, records, or cloud resources.

Mitigation: Inspect tool schemas and restrict tokens to the minimum required resources, operations, metadata, and time-to-live before execution.

## Reference(s):

- [Smithery homepage](https://smithery.ai)
- [Smithery namespaces documentation](https://smithery.ai/docs/concepts/namespaces.md)
- [Smithery Connect documentation](https://smithery.ai/docs/use/connect.md)
- [Smithery token scoping documentation](https://smithery.ai/docs/use/token-scoping.md)
- [ClawHub skill page](https://clawhub.ai/javotillo/skills/smithery-ai-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce JSONL when Smithery output is piped.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
