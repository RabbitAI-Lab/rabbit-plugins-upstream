## Description:

提供行为树、有限状态机、寻路算法和决策系统的游戏AI开发指南，支持多语言及主流游戏引擎集成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers and engineers use this skill to design, implement, and troubleshoot game AI systems such as behavior trees, finite state machines, pathfinding, decision logic, and group behavior across common game engines and languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests shell and broad file authority for coding, deployment, file writes, and credential-adjacent workflows.

Mitigation: Review before installing, keep access limited to the intended game-AI project, and approve shell commands only when the purpose and target path are clear.

Risk: Generated code or configuration could change project behavior or game balance in unintended ways.

Mitigation: Review generated changes, run them in a sandbox or development branch, and test AI behavior before integrating into production builds.

Risk: Credential or sensitive project data may be exposed if commands or logs include secrets.

Mitigation: Avoid sharing secrets with the skill, redact logs before reuse, and only allow credential use for explicit, necessary tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/game-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with code examples and command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include game AI architecture notes, behavior tree, state machine, pathfinding, and decision-system examples.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
