## Description:

Transforms task-following agents into proactive partners with persistent memory, reverse prompting, security hardening, self-healing, verification, and alignment patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gasgangrene](https://clawhub.ai/user/gasgangrene)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to install a workspace-level operating pattern for proactive assistance, persistent memory, user onboarding, heartbeat checks, and safer background work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory files can retain personal and project details beyond the current chat session.

Mitigation: Install only when this workspace-level memory behavior is intended, and review what USER.md, MEMORY.md, SESSION-STATE.md, and daily notes may store.

Risk: The skill encourages background heartbeats, cron-driven work, cleanup, and self-modification patterns that can change workspace state.

Mitigation: Do not enable heartbeats, cron jobs, autonomous turns, cleanup, or policy-file edits until the exact actions are reviewed and approved.

Risk: Copying bundled assets over an existing workspace can overwrite local agent configuration and memory files.

Mitigation: Back up existing AGENTS.md, SOUL.md, USER.md, MEMORY.md, HEARTBEAT.md, and TOOLS.md, then use manual merge or no-overwrite copy behavior.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/gasgangrene/skills/proactive-agent)
- [Onboarding Flow Reference](references/onboarding-flow.md)
- [Security Patterns Reference](references/security-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with file templates and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes workspace asset files and a security audit shell script.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact SKILL.md frontmatter states 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
