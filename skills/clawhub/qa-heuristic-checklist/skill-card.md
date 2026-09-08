## Description:

提供面向登录、支付、搜索、购物车、导入导出、审批、消息通知和权限管理等功能类型的 QA 启发式测试清单，帮助测试人员生成测试要点、用例表格和探索测试指南。

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

测试人员、开发者和 QA 团队在面对新功能或不确定测试要点时使用此技能，按功能类型选择启发式清单并生成结构化测试用例、覆盖提示和探索测试指南。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checklist examples can include destructive target-application actions such as deleting cart items or changing roles.

Mitigation: Run generated QA scenarios only in safe test environments and avoid applying them to production data.

## Reference(s):

- [功能类型启发式检查清单](references/checklists.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a structured test-case table, heuristic checklist, coverage notes, and exploration guide]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed 9-column test case table and calls out covered and uncovered areas without claiming absolute coverage.]

## Skill Version(s):

1.7.6 (source: server release evidence; artifact frontmatter lists 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
