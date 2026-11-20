## Description:

将重型开发的需求和方案拆成 Phase 及所属 Task，每个 Phase 可在独立上下文中实施、评审和测试。适用于跨模块大任务及剩余工作重排，沿用同一份任务清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-zh](https://clawhub.ai/user/peterflow-zh)

### License/Terms of Use:

MIT-0

## Use Case:

开发者可用它把跨模块开发需求和方案整理成按依赖衔接的 Phase 与 Task，并在同一份 tasks.md 中跟踪交接、验证证据和累计验收。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports file-reading capability without a declared tool scope.

Mitigation: Before use, confirm that file-reading access is appropriate and limit the agent to relevant project materials.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/peterflow-zh/skills/tasks-pro)
- [Publisher profile](https://clawhub.ai/user/peterflow-zh)
- [阶段任务模板](assets/tasks.md)
- [Dependency checker](scripts/check_dependencies.py)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown task plan with Phase and Task sections, dependencies, handoffs, and acceptance checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A single tasks.md checklist that carries task status and verification evidence.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
