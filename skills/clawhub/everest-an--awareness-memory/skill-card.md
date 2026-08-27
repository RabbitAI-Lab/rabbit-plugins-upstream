## Description:

Provides setup guidance for adding the Awareness local-first memory layer to Claude Code, Cursor, Windsurf, and other MCP clients so agents can retain cross-session project context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[everest-an](https://clawhub.ai/user/everest-an)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to install and operate Awareness memory for Claude Code, Cursor, Windsurf, and other MCP clients when they need persistent project context across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can change agent rules and MCP configuration, which may alter agent behavior across sessions.

Mitigation: Review configuration and rule diffs after setup, prefer dry-run or manual setup where possible, and verify how to remove injected rules.

Risk: The memory layer may store cross-session project and conversation context and index local project documents.

Mitigation: Avoid recording secrets or regulated data, confirm deletion controls before use, and avoid sensitive projects until storage behavior is approved.

Risk: A local daemon and telemetry-related behavior may create operational or privacy concerns.

Mitigation: Verify how to stop the daemon, disable telemetry, and remove stored memory before installing in sensitive environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/everest-an/skills/awareness-memory)
- [Awareness Documentation](https://awareness.market/docs)
- [Awareness MCP Tools Reference](https://awareness.market/docs?doc=MCP_TOOLS_REFERENCE)
- [Awareness Benchmarks](https://awareness.market/benchmarks)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first setup guidance; no generated files are produced by the skill itself.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
