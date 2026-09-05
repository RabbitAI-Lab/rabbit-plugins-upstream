## Description:

Logs agent-infrastructure issues such as prompt drift, rule conflicts, hook failures, and context bloat while keeping the default workflow log-only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent-infrastructure maintainers use this skill to capture prompt-file ambiguity, rule conflicts, stale memory, hook failures, and missing skill capabilities as local learning, issue, and feature-request entries. It supports reviewed improvement workflows without silently changing shared prompt files, hooks, memory, or skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional PostToolUse error detection reads command output from the hook environment.

Mitigation: Enable it only in trusted projects and review .learnings entries for secrets or private details before committing them.

Risk: The skill can initialize or append local .learnings files and includes optional project-scoped reminders.

Mitigation: Decide before installation whether local learning files and reminders are desired; keep hooks opt-in and scoped to the current project.

Risk: Infrastructure learnings can lead to proposed changes in shared prompt files, hooks, memory policies, or skills.

Mitigation: Apply those changes only after an explicit user request and a reviewed diff in the current session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jose-compu/skills/self-improving-meta)
- [Hook setup guide](artifact/references/hooks-setup.md)
- [OpenClaw integration](artifact/references/openclaw-integration.md)
- [Entry examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or append local .learnings markdown files; optional hooks emit reminders only.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
