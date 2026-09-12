## Description:

Local-first Rust MCP memory for recall, smart_ingest, and backward-only causal Backfill that answers what caused a later failure without replacing OpenClaw default memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samvallad33](https://clawhub.ai/user/samvallad33)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to configure Vestige as a local MCP memory helper for recall, durable fact storage, and causal backfill after failures. It sits beside OpenClaw memory-core and is not presented as the OpenClaw default memory plugin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local memory persistence can retain sensitive or unwanted project context.

Mitigation: Use a per-project --data-dir for sensitive projects and avoid saving API keys, passwords, or secrets.

Risk: The skill depends on running the pinned external Vestige npm MCP server locally.

Mitigation: Install the pinned vestige-mcp-server@2.8.0 package only after reviewing trust requirements and resolving the absolute binary path used by the MCP configuration.

Risk: Casual preference phrases may trigger storage through smart_ingest.

Mitigation: Review what the agent is about to store before accepting memory writes.

## Reference(s):

- [Vestige official repository](https://github.com/samvallad33/vestige)
- [Backfill tool schema source](https://github.com/samvallad33/vestige/blob/main/crates/vestige-mcp/src/tools/backfill.rs)
- [ClawHub skill page](https://clawhub.ai/samvallad33/skills/vestige)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance references pinned vestige-mcp-server@2.8.0 and local MCP tool usage.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
