## Description:

Maintain a local, auditable user-preference memory shared across coding agents such as Codex and Claude Code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cutd](https://clawhub.ai/user/cutd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding-agent users use Dongwo to keep local, auditable preference memory across Codex and Claude Code sessions. It supports remembered style preferences, cross-agent continuity, manual inspection, and lifecycle-hook setup for automatic capture and context injection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dongwo automatically stores user prompts locally under .dongwo/memory and can reuse derived preference context in later agent sessions.

Mitigation: Enable the hooks only in projects where local prompt retention is acceptable, inspect or delete the memory files when needed, and avoid highly sensitive work unless permissions and retention expectations are clear.

Risk: Stored prompt text that looks like a durable preference can influence future sessions without a separate confirmation step.

Mitigation: Treat memory as lower priority than the current request and project instructions, review generated preferences and conflicts, and keep pending or conflicted entries out of execution context.

## Reference(s):

- [Dongwo memory policy](references/memory-policy.md)
- [ClawHub skill page](https://clawhub.ai/cutd/skills/dongwo)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON hook snippets, and generated local Markdown memory context]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; automatic hooks store redacted local prompt evidence and return a bounded context snapshot.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
