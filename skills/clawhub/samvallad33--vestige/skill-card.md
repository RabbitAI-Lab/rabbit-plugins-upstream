## Description:

Local-first Rust MCP memory for recall, smart_ingest, and backward-only Causal Backfill, not as OpenClaw default memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samvallad33](https://clawhub.ai/user/samvallad33)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Vestige as a local MCP memory helper for recalling session context, storing durable preferences or project facts, and tracing likely earlier operational records after a later failure. It sits beside OpenClaw memory-core and is not configured as OpenClaw's default memory plugin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local memory can capture broad preferences or sensitive facts if users ask the agent to remember them.

Mitigation: Avoid saving API keys, passwords, credentials, and other secrets; be explicit about what should or should not be remembered.

Risk: A shared local data store can mix memory across projects.

Mitigation: Use a per-project absolute data directory with the Vestige MCP server's --data-dir setting when separation matters.

Risk: Misconfiguring Vestige as OpenClaw's default memory slot can conflict with the documented memory-core behavior.

Mitigation: Configure Vestige as a separate MCP server only, and do not set plugins.slots.memory to vestige unless a real OpenClaw plugin exists.

Risk: Using an unpinned or incompatible server package can create platform or dependency issues.

Mitigation: Install the documented vestige-mcp-server@2.6.0 package, use an absolute command path in GUI MCP configuration, and follow the documented platform notes.

## Reference(s):

- [ClawHub Vestige skill page](https://clawhub.ai/samvallad33/skills/vestige)
- [Official Vestige server](https://github.com/samvallad33/vestige)
- [Backfill tool schema](https://github.com/samvallad33/vestige/blob/main/crates/vestige-mcp/src/tools/backfill.rs)
- [Vestige skill wrapper repository](https://github.com/Belkouche/vestige-skill.git)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing guidance for MCP memory tool use and a Bash helper that returns text from Vestige MCP calls.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
