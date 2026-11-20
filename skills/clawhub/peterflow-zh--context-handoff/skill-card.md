## Description:

上下文交接：用户显式调用时新建只接收交接的会话；主 Agent 可隐式使用来整理并向子 Agent 同步任务信息，不负责创建或调度代理。讨论、编写或评审本技能时不触发交接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-zh](https://clawhub.ai/user/peterflow-zh)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to prepare a handoff for a new session or synchronize context with an already assigned subagent, preserving the current authorization boundary and work state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Handoff notes may expose credentials or unrelated personal information if copied into the package.

Mitigation: Remove secrets and unrelated personal details before saving or sending the handoff.

Risk: A recipient could mistake pending work or historical authorization in a handoff for permission to act now.

Mitigation: State the recipient's current authorization separately from follow-up work, and make clear that historical instructions do not grant new authority.

## Reference(s):

- [新会话交接](artifact/references/new-chat.md)
- [子 Agent 同步](artifact/references/subagent.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown handoff notes and concise context messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves authorization, workspace state, sources, progress, and interruption point; excludes secrets and unrelated personal information.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
