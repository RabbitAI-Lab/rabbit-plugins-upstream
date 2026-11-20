## Description:

按重型任务的执行单元组织独立上下文实现、内部评审和测试，核验结果后推进依赖与累计验收。可接续任何来源的合适单元清单，不依赖外部评审或测试 Skill。

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-zh](https://clawhub.ai/user/peterflow-zh)

### License/Terms of Use:

MIT-0

## Use Case:

面向开发者和工程团队，用于将复杂项目目标拆分为带有依赖关系和验收条件的执行单元，并组织独立实现、评审、测试和累计验收。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that local file-reading scope was not fully resolved.

Mitigation: Before use, confirm that the project, standards, task, and evidence paths the skill reads are within the intended scope.

## Reference(s):

- [角色协议](references/roles.md)
- [最小改动对照](references/minimal-change.md)
- [ClawHub release page](https://clawhub.ai/peterflow-zh/skills/implement-pro)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text, Files]

**Output Format:** [Markdown instructions, task records, review and test receipts, and final status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records retain unit status, decisions, verification evidence, and recovery details.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
