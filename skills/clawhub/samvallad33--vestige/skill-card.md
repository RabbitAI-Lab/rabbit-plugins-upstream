## Description:

Local-first Rust MCP memory. Causal Backfill answers "what caused this?" using shared entities as the join key, with similarity excluded from ranking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samvallad33](https://clawhub.ai/user/samvallad33)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and call Vestige as a local MCP memory helper for recall, durable fact ingestion, and backward causal Backfill from later failures or symptoms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retain user-provided content in a local memory store.

Mitigation: Use a per-project --data-dir for containment and avoid storing secrets, credentials, regulated data, or confidential information unless deliberate local retention is intended.

Risk: Using Vestige as OpenClaw's default memory could create an unsupported configuration.

Mitigation: Configure Vestige as an additional MCP server only, and do not set plugins.slots.memory to Vestige unless a real OpenClaw memory plugin exists.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/samvallad33/skills/vestige)
- [Vestige repository](https://github.com/samvallad33/vestige)
- [Backfill tool schema](https://github.com/samvallad33/vestige/blob/main/crates/vestige-mcp/src/tools/backfill.rs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call local MCP tools through vestige-mcp; memory is retained in a local OS data directory unless --data-dir is configured.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
