## Description:

跨会话/跨项目通用工作流标准：让任何 AI 智能体活过会话——开工必读状态、状态就近存 .workflow、进行中自动记流水/任务/决策、收工必留交接锚点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to keep project state consistent across sessions and across different AI coding agents. It directs agents to read or initialize a local .workflow state directory, maintain progress, task, decision, roadmap, and log files, and produce a self-contained handoff anchor at session close.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project-local .workflow files can capture sensitive implementation notes, private customer data, credentials, or absolute paths if an agent records them without review.

Mitigation: Keep .workflow out of shared repositories unless reviewed, and instruct agents not to record secrets, credentials, private customer data, or sensitive absolute paths.

Risk: Because the skill asks agents to maintain status, task, decision, roadmap, and log files automatically, inaccurate agent-written state could mislead later sessions.

Mitigation: Review generated .workflow updates and handoff anchors before relying on them for project continuity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-workflow)
- [Agent Skills standard](https://agentskills.io/)
- [Project repository](https://github.com/YottaMeta/yotta-workflow)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance, Configuration]

**Output Format:** [Markdown instructions, local Markdown state files, and handoff text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains project-local .workflow files such as STATE.md, TASKS.md, DECISIONS.md, ROADMAP.md, and logs/YYYY-MM-DD.md when the host agent follows the skill.]

## Skill Version(s):

0.2.4 (source: frontmatter and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
