## Description:

A cross-session and cross-project workflow standard that directs agents to read project state on start, persist progress in nearby `.workflow` Markdown files, and leave a handoff anchor on finish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to maintain durable project state across sessions and across different AI agents. It is most useful for multi-step project work where progress, tasks, decisions, logs, and handoff notes need to survive context loss.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent project state files may capture sensitive project details if users or agents write secrets into `.workflow`.

Mitigation: Keep secrets out of `.workflow` files and review those files before sharing, committing, or handing a project to another agent.

Risk: The installer can copy the skill into user-level, global, or explicitly supplied agent skill directories.

Mitigation: Review or pin the npm package version in controlled environments and use `--dir` or global install options only for intended skill directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-workflow)
- [Agent Skills standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown state files, handoff text, and installation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates project-local `.workflow` files when used for project work; one-off read-only questions do not require initialization.]

## Skill Version(s):

0.2.7 (source: ClawHub release evidence; artifact SKILL.md, package.json, and CHANGELOG list 0.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
