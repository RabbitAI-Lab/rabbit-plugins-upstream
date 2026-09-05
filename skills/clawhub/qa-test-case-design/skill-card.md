## Description:

将需求解构、场景树、边界清单和组合矩阵等分析结果转化为 P0-P3 分级、可追溯的标准化测试用例。

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, testers, and product teams use this skill to turn completed requirement and scenario analysis into structured test-case reports, priority groups, coverage notes, and review-ready testing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may activate the skill for adjacent QA review requests.

Mitigation: Use it when the task is specifically test-case design, coverage improvement, or test-case review, and provide requirements or prior analysis outputs.

Risk: Test cases can become generic or misleading when requirement, scenario, boundary, or business-context inputs are incomplete.

Mitigation: Provide the source requirements and upstream analysis, mark missing coverage explicitly, and review generated cases before execution.

## Reference(s):

- [测试覆盖策略与质量标准](references/coverage-and-quality.md)
- [用例设计方法参考](references/design-methods.md)
- [测试用例字段模板与输出格式](references/output-template-full.md)
- [需求文档要求与用例评审标准](references/review-standards.md)
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-case-design)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown test-case reports, tables, coverage notes, and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses fixed test-case fields, P0-P3 priority labels, traceable TC identifiers, and blank test-step sections for user completion.]

## Skill Version(s):

1.7.6 (source: server release evidence; artifact frontmatter says 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
