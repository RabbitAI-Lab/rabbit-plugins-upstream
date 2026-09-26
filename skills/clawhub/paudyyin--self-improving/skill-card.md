## Description:

Self-reflect, self-critique, self-learn, and organize memory with structured logging

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure persistent self-improvement memory, correction tracking, reflection logs, and structured error or feature-request capture for coding-agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory can retain sensitive or unwanted user, project, or operational context.

Mitigation: Use the skill only when persistent memory is intended; redact secrets and sensitive data, keep entries concise, and periodically audit or delete stored memory.

Risk: Agent-control changes such as hooks, cron jobs, or workspace steering files can alter future agent behavior beyond the current task.

Mitigation: Require explicit confirmation before enabling hooks, cron jobs, exports, deletions, cross-session sharing, or changes to AGENTS.md, SOUL.md, or TOOLS.md.

Risk: Automatically captured learnings may overgeneralize from narrow corrections or outdated context.

Mitigation: Treat inferred patterns as tentative, ask for confirmation before promoting them, and preserve source tracking so users can inspect why a behavior changed.

## Reference(s):

- [Entry Examples](references/examples.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [OpenClaw Integration](references/openclaw-integration.md)
- [Rule Categories](references/rule_categories.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and optional hook code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local memory and learning files when the user enables the workflow.]

## Skill Version(s):

2.6.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
