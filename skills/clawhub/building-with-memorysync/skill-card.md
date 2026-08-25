## Description:

Building with MemorySync guides developers through designing, implementing, evaluating, and troubleshooting MemorySync integrations for long-term memory in agents, chatbots, and applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafay121](https://clawhub.ai/user/rafay121)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when adding MemorySync-backed long-term memory to agents, chatbots, or applications, including scoping users, ingesting facts or turns, retrieving memory, choosing adapters, and evaluating an integration before rollout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may contact MemorySync, mint evaluation credentials, or make memory calls without the user understanding destination, quota, or account effects.

Mitigation: Confirm the destination, credential creation, and quota or account effects before allowing evaluation key minting or MemorySync read/write operations.

Risk: Memory payloads can accidentally include secrets, tokens, passwords, API keys, or sensitive identifiers.

Mitigation: Review payloads before storage and refuse to store secrets, credentials, passwords, tokens, API keys, or sensitive identifiers as memory.

Risk: Retrieved memory can be mistaken for instructions when injected into a prompt.

Mitigation: Treat retrieved memory as background data only and add an explicit guard when using memory text in prompts.

Risk: Using broad account-level deletion could remove more data than intended.

Mitigation: Avoid account purge behavior and use documented per-memory deletion flows when removing stored memories.

## Reference(s):

- [MemorySync documentation MCP](https://docs.memorysync.io/mcp)
- [Building with MemorySync on ClawHub](https://clawhub.ai/rafay121/skills/building-with-memorysync)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, API examples, shell commands, and configuration recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs agents to verify exact endpoints, parameters, fields, and limits against the live MemorySync documentation before shipping.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
