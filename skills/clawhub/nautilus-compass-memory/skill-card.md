## Description:

Local-first long-term memory for AI agents via MCP, with zero LLM calls at write time, typed retrieval at read time, and drift detection for repeated mistakes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chunxiaoxx](https://clawhub.ai/user/chunxiaoxx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add persistent memory, shared filesystem context, semantic recall, and drift checks across sessions and MCP-compatible clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation asks users to run remote code that modifies Claude Code hooks and multiple MCP client configurations.

Mitigation: Inspect the cloned repository, verify the exact checked-out commit, and review configuration changes before applying them.

Risk: Using the hosted gateway sends memory content and recall queries off-machine.

Mitigation: Use the local daemon when memory data should stay on the user's machine.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chunxiaoxx/skills/nautilus-compass-memory)
- [Compass hosted MCP endpoint](https://compass.nautilus.social/mcp/)
- [Compass signup](https://compass.nautilus.social/signup)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local daemon and hosted gateway setup paths; no structured machine output.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
