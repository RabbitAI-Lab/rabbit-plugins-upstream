## Description:

Vestige is a local-first Rust MCP memory skill for recall, smart_ingest, and backward-only causal Backfill that answers "what caused this?" without serving as OpenClaw default memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samvallad33](https://clawhub.ai/user/samvallad33)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate Vestige as a local MCP memory server for recall, durable fact storage, and backward causal Backfill from later failures or symptoms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local persistent memory may retain sensitive work context or private material across sessions.

Mitigation: Use a per-project data directory for sensitive work, review what is saved, and avoid storing API keys, passwords, secrets, or private material that should not persist.

Risk: Preference trigger phrases could cause casual statements to be stored if an agent applies them too broadly.

Mitigation: Use smart_ingest only for explicit durable facts or preferences, and confirm ambiguous statements before saving them.

Risk: Misconfiguring Vestige as OpenClaw's default memory could create an unsupported setup.

Mitigation: Configure Vestige as an MCP server only, and do not set plugins.slots.memory to Vestige unless a real OpenClaw plugin exists.

Risk: The documented current npm package may not start on Ubuntu 22.04 or Debian 12 because of older glibc versions.

Mitigation: Avoid upgrading system glibc for this skill; use a supported platform or wait for a compatible Vestige release.

## Reference(s):

- [ClawHub Vestige skill page](https://clawhub.ai/samvallad33/skills/vestige)
- [Vestige MCP project](https://github.com/samvallad33/vestige)
- [Backfill tool schema](https://github.com/samvallad33/vestige/blob/main/crates/vestige-mcp/src/tools/backfill.rs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs describe local MCP memory setup and helper command usage; the skill itself can save and retrieve persistent local memory through Vestige.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
